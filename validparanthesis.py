#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

#now take stack as an array, put if open bracket then check if top of array matches with closing bracket and stack has elements then pop array return true if empty.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        else:
            stack = []
            for i in s:
                if i == '(' or i== '{' or i =='[':
                    stack.append(i)
                elif stack and stack[-1]=='(' and i ==')':
                    stack.pop()
                elif stack and stack[-1]=='['and i ==']':
                    stack.pop()
                elif stack and stack[-1]=='{' and i =='}':
                    stack.pop()
                else:
                    return False
            if len(stack)>=1:
                return False
            return True
