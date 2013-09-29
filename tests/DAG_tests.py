#!/usr/bin/env python

import unittest

from backend import DAG

class Node(object):
    def __init__(self,names,reqParents=None,reqChildren=None):
        self.Names = [names] if isinstance(names,str) else names
        self.requestedParents = reqParents if reqParents is not None else []
        self.requestedChildren = reqChildren if reqChildren is not None else []
    def Changed(self,*args,**kw):
        pass

class DAGTester(unittest.TestCase):
    def test_building(self):
        dag = DAG.DAG()
        node1 = Node('node1',[],['node3'])
        dag.Add(node1)
        node2 = Node('node2',['node1'])
        dag.Add(node2)
        self.assertEqual(len(dag),2)
        self.assertEqual(dag.Parents(node2),[node1])
        self.assertEqual(dag.Children(node1),[node2])
        node3 = Node('node3')
        dag.Add(node3)
        self.assertEqual(dag.Parents(node3),[node1])
        dag.Remove(node1)
        self.assertEqual(len(dag),2)
        self.assertEqual(dag.Parents(node2),[])
        self.assertEqual(dag.Parents(node3),[])
        dag.Add(node1)
        self.assertEqual(dag.Parents(node3),[node1])
        self.assertEqual(dag.Parents(node2),[node1])
        self.assertEqual(dag.Children(node1),[node3,node2])

        node4 = Node('node4',[node1])
        dag.Add(node4)
        self.assertEqual(dag.Parents(node4),[node1])



if __name__=='__main__':
    unittest.main()
