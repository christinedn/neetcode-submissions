class Solution:
    def isValid(self, s: str) -> bool:
        # create dict to map closing to opening
        # go through string, if c exist in dict, push to stack
        # if not, return false. (meaning it is not a bracket)
        # if it is not a closing bracket, it must be an opening one to match. check if stack is non-empty and if top of the stack matches the correct closing bracket
        # pop from stack. 
        # if stack is empty, you can return true meaning the opening matches all closing brackets 
        stk = []
        d = {"}" : "{", 
                "]" : "[", 
                ")" : "("}

        for c in s:
            if c in d:
                # reading a closing bracket
                if stk and stk[-1] == d[c]:
                    stk.pop()
                else:
                    return False
            else:
                # it must be an opening bracket
                stk.append(c)
        return True if not stk else False

