'''
https://leetcode.com/problems/valid-parentheses/submissions/1756170769/
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    ch = stack.pop()
                    if (i == ')' and ch == '(') or (i == ']' and ch == '[') or (i == '}' and ch == '{'):
                        continue
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False
        