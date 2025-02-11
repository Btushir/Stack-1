"""
Approach1: traverse the ch and check for each ch. TC: O(n) SC: O(n)
Approach2: create a mapping in hmap. THis reduces the number of if statements.
TC: O(n), SC:(n) + hmap O(3)
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:
            if ch == "(":
                stack.append(ch)

            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            elif ch == "{":
                stack.append(ch)


            elif ch == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

            elif ch == "[":
                stack.append(ch)


            elif ch == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hmap = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)

            elif ch in hmap:
                if stack and stack[-1] == hmap[ch]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
