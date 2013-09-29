#!/usr/bin/env python

from random import randint
import re

def Roll(DieString):
    roller = DiceParse(DieString)
    return roller.Roll()

def sign(x):
    return 1 if x>=0 else -1

class DiceParse(object):
    """
    A dice-rolling class.
    Allows for notation of the form '2d4' as commonly used in RPGs.
    Also allows for addition, subtraction, multiplication, division, and exponentiation.
    Note: In cases of fractional values, the results are rounded down after each step.
    """
    digits = '0123456789'
    ops = {'+':0,'-':0, #Plus, Minus
           '*':1,'/':1, #Mul, Div
           '^':2,       #Exponentiaion
           '-u':3,      #Unary negation
           'd':4}       #Dice operator
    right = ['-u']      #Right-associative operators
    otherchar = '+-*/^d()V'
    def __init__(self,DieString):
        self.DieString = DieString
    def get_DieString(self):
        return self._DieString
    def set_DieString(self,val):
        self._shunting_yard(val) 
        self._DieString = val
    DieString = property(get_DieString,set_DieString)
    def _parse(self, inString):
        """Tokenizes the current value of self.DieString into numbers and operators."""
        number = ''
        infix = False
        #Tokenize the string.  All tokens are either numbers or single character.
        for char in inString:
            if char in self.otherchar:
                if number:
                    yield int(number)
                    number = ''
                    infix = True
                if not infix and char=='-':
                    yield '-u'
                elif not infix and char=='d':
                    yield 1
                    yield 'd'
                else:
                    yield char
                infix = (char in [')','V'])
            elif char in self.digits:
                number += char
        #Clear out any number that remains.
        if number:
            yield int(number)
    def _shunting_yard(self,inString):
        """Implements the shunting yard algorithm to convert to reverse polish notation"""
        stack = []
        queue = []
        for tok in self._parse(inString):
            if isinstance(tok,int) or tok=='V':
                queue.append(tok)
            elif tok in self.ops:
                while (stack and
                       stack[-1] in self.ops and
                       ((tok in self.right and self.ops[tok] < self.ops[stack[-1]]) or
                        (tok not in self.right and self.ops[tok] <= self.ops[stack[-1]]))):
                    queue.append(stack.pop())
                stack.append(tok)
            elif tok=='(':
                stack.append(tok)
            elif tok==')':
                while stack and stack[-1]!='(':
                    if stack[-1] in self.ops:
                        queue.append(stack.pop())
                    else:
                        raise Exception("Incorrect syntax, mismatched ()",inString)
                if not stack:
                    raise Exception("Incorrect syntax, mismatched ()",inString)
                stack.pop()
        while stack:
            tok = stack.pop()
            if tok=='(':
                raise Exception("Incorrect syntax, mismatched ()",inString)
            queue.append(tok)
        args = sum(isinstance(i,int) or i=='V' for i in queue)
        args_needed = sum(i in {'+','-','*','/','d','^'} for i in queue)+1
        if args != args_needed:
            raise Exception("Error, too many operators",inString)
        self._rpn = queue
    @staticmethod
    def _dice_roll(number,sides):
        """
        Rolls {number} dice, each with {sides} sides.
        If either argument is negative, the absolute value is used, and the result is multiplied by -1.
        """
        return (sign(number)*sign(sides)*sum(randint(1,abs(sides)) for i in range(abs(number)))
                if sides!=0 else 0)
    def Roll(self,val=None):
        """Performs the calculation/dice-rolling requested, as stored in self._rpn."""
        stack = []
        for tok in self._rpn:
            if isinstance(tok,int):
                stack.append(tok)
            elif tok=='V':
                if val is None:
                    raise Exception("Value must be passed if value is asked for.")
                else:
                    stack.append(val)
            else:
                last = stack.pop()
                if tok=='+':
                    stack.append(stack.pop() + last)
                elif tok=='-':
                    stack.append(stack.pop() - last)
                elif tok=='*':
                    stack.append(stack.pop() * last)
                elif tok=='/':
                    stack.append(stack.pop() / last)
                elif tok=='^':
                    stack.append(int(stack.pop() ** last))
                elif tok=='d':
                    stack.append(self._dice_roll(stack.pop(),last))
                elif tok=='-u':
                    stack.append(-1*last)
        return stack[0]
    def __call__(self,val=None):
        return self.Roll(val)
            
class Table(object):
    """
    Reads in a file containing a table.
    The table should be tab-delimited, containing only integers, 'd', 'V', and operations.
    The first entry of each line is the key.
    The key can also be a range (e.g. 5-10,-3-5,-10--6)
    """
    def __init__(self,filename):
        self.values = []
        allowed = {'0','1','2','3','4','5','6','7','8','9','0',
                   ' ','\t','d','V','^','*','/','+','-','(',')'}
        for line in open(filename):
            line = line.strip()
            #Skip line if any forbidden characters are found.
            if not set(line).issubset(allowed):
                continue
            entries = [s.strip() for s in line.split('\t')]
            diceList = [DiceParse(ent) for ent in entries[1:]]
            if '-' not in entries[0]:
                self.values.append([int(entries[0]),
                                    int(entries[0]),
                                    diceList])
            else:
                res = re.match(r"(-\d+|\d*)"
                               r"-"
                               r"(-\d+|\d*)\Z", #Match a positive or negative integer, or empty.
                               entries[0])
                if res:
                    low,high = res.group(1,2)
                    self.values.append([int(low) if low else -float('Inf'),
                                        int(high) if high else float('Inf'),
                                        diceList])

    def __call__(self,key,item=0):
        for low,high,vallist in self.values:
            if low <= key <= high:
                if item=='ALL':
                    return [val(key) for val in vallist]
                else:
                    return vallist[item](key)
        raise KeyError("Table value not found.",key)
        

if __name__=='__main__':
    while True:
        t = DiceParse(raw_input("> "))
        print t.Roll()
