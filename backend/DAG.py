#!/usr/bin/env python

from utils import listReplace
from collections import defaultdict

import Character

def _equals(node,other):
    return (node is other) or (other==node.Name)

class DAG(object):
    """
    Implements a Directed Acyclic Graph.
    Assumes that adding/removing nodes will be rare,
      lookups will be common.
    Expects each node to have attributes
        requestedChildren, a list of strings of children to find,
        requestedParents, a list of strings of parents to find
     and Name, the name of the node.
    """
    def __init__(self):
        self._parents = defaultdict(list)
        self._children = defaultdict(list)
        self.nodes = []
    def Add(self,node):
        self._link(node)
        if self._isValid():
            return
        else:
            self._unlink(node)
            raise ValueError("Made a loop as a result")
    def Remove(self,node):
        self._unlink(node)
    def __iter__(self):
        notYielded = self.nodes[:]
        while notYielded:
            path = [notYielded[0]]
            while path:
                toYield = path.pop()
                if isinstance(toYield,Character.Skill):
                    path.extend(reversed(self.Children(toYield)))
                notYielded.remove(toYield)
                yield toYield
    def __getitem__(self,key):
        for node in self:
            if _equals(node,key):
                return node
        raise KeyError("Not found", key)
    def _singleLink(self,(par,ch,owner,req)):
        parTup = (ch,par is owner,req)
        chTup = (par,ch is owner,req)
        if par is owner:
            listReplace(self._children[id(par)],req,parTup)
            self._parents[id(ch)].append(chTup)
        else:
            self._children[id(par)].append(parTup)
            listReplace(self._parents[id(ch)],req,chTup)
        ch.Changed()
    def _connections(self,node):
        """
        Finds the new connections necessary based on the new node.
        """
        parents = list(node.requestedParents)
        children = list(node.requestedChildren)
        for othernode in self.nodes:
            #Parents requested by the new node
            for par in self._parents[id(node)]:
                if _equals(othernode,par):
                    yield (othernode,node,node,par)

            #Children requested by the new node
            for ch in self._children[id(node)]:
                if _equals(othernode,ch):
                    yield (node,othernode,node,ch)

            #Standing requests for parents from other nodes
            for name in self._parents[id(othernode)]:
                if _equals(node,name):
                    yield (node,othernode,othernode,name)

            #Standing requests for children from other nodes
            for name in self._children[id(othernode)]:
                if _equals(node,name):
                    yield (othernode,node,othernode,name)
    def _link(self,node):
        """
        Adds the specified node, along with any connections necessary to it.
        Does not perform any checks for cycles created.
        """
        node.graph = self
        self._parents[id(node)] = list(node.requestedParents)
        self._children[id(node)] = list(node.requestedChildren)
        for conn in self._connections(node):
            self._singleLink(conn)
        self.nodes.append(node)
        node.Changed()
    def _unlink(self,node):
        """
        Removes the given node from the graph.
        Removes all connections to the given node, and resets the requests.
        """
        if node not in self.nodes:
            raise ValueError("Given node was not in the graph")
        for parNode in self.Parents(node):
            self._children[id(parNode)] = [req if (ch is node) else (ch,owned,req)
                                           for (ch,owned,req) in self._children[id(parNode)]
                                           if (ch is not node) or (owned)]
        del self._parents[id(node)]
        for chNode in self.Children(node):
            self._parents[id(chNode)] = [req if (par is node) else (par,owned,req)
                                         for (par,owned,req) in self._parents[id(chNode)]
                                         if (par is not node) or (owned)]
            chNode.Changed()
        del self._children[id(node)]
        self.nodes.remove(node)
        node.Changed()
    def _isValid(self):
        return True
    def __len__(self):
        return len(self.nodes)
    def Parents(self,node):
        try:
            return [par[0] for par in self._parents[id(node)]
                    if isinstance(par,tuple)]
        except KeyError:
            raise ValueError("Node not found.", node)
    def OwnedParents(self,node):
        try:
            return [par[0] for par in self._parents[id(node)]
                    if isinstance(par,tuple) and par[1]]
        except KeyError:
            raise ValueError("Node not found.", node)
    def Children(self,node):
        try:
            return [ch[0] for ch in self._children[id(node)]
                    if isinstance(ch,tuple)]
        except KeyError:
            raise ValueError("Node not found.", node)
    def OwnedChildren(self,node):
        try:
            return [ch[0] for ch in self._children[id(node)]
                    if isinstance(ch,tuple) and ch[1]]
        except KeyError:
            raise ValueError("Node not found.", node)
    def MoveTo(self,nodeA,nodeB,before=False):
        """
        Moves nodeA to the position just after nodeB, or just before, if before is True.
        Has no effect if nodeA and nodeB have different skills as parents.
        """
        before = bool(before)
        parA = [par for par in self.Parents(nodeA) if isinstance(par,Character.Skill)]
        parB = [par for par in self.Parents(nodeB) if isinstance(par,Character.Skill)]
        if len(parA)!=len(parB) or any(p not in parB for p in parA):
            return False
        self.nodes.remove(nodeA)
        self.nodes.insert(self.nodes.index(nodeB)+1-before,nodeA)
        for par in self.Parents(nodeA):
            childList = self._children[id(par)]
            try:
                indexA = next(i for i,tup in enumerate(childList) if tup[0] is nodeA)
                indexB = next(i for i,tup in enumerate(childList) if tup[0] is nodeB)
            except StopIteration:
                continue
            finalPos = indexB + 1 - before
            finalPos = finalPos if finalPos<indexA else finalPos-1
            childList.insert(finalPos,childList.pop(indexA))
        return True
