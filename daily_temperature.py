"""
Brute Force: traverse the array and find the next greatest number. TC: O(n^2). Gives TLE.
Optimal approach: use stack. Why?
For example, [75, 71,69,72, 76]
75 can only be resolved when 71 is resolved, 71 can be resolved when 69 is resolved. 72 > 69. It resolved 69
but it may or may not resolve the previous elements.
The 2nd for loop is used until the last element if not able to resolve the ith element. THus, until the ith
element is resolved, store the in-between element into a DS, stack.
This is increasing the stack pattern.
TC: O(2n) for first iteration all elements goes inside stack then in 2nd all are resolved.
SC: O(n)+filling array
Note: for the next colder day, stack will be increasing.
THIS IS a MNOTONOIC STACK PROBLEM.
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        ans = [-1 for _ in range(len(nums))]
        stack = []
        n = len(nums)
        stack.append(0)
        # how many times the loop will run. 2n times
        for curr_idx in range(1, 2 * n):

            # while stack is not empty, compar the stack top and incoming number
            while stack and nums[stack[-1]] < nums[curr_idx % n]:
                popped_idx = stack.pop()
                ans[popped_idx] = nums[curr_idx % n]

            if curr_idx < n:
                # push the elment to stack during first pass only
                stack.append(curr_idx % n)
            # if top of stack is equal to current idx
            elif stack[-1] == curr_idx:
                break

        return ans


class Solution_using_stack:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []
        # add the idx of first element, no need to append the value
        stack.append(0)
        for i in range(1, len(temperatures)):
            curr_idx = i
            prev_idx = stack[-1]
            # compare the first element and top element of stack
            # if can be resolved, then resolve and check if other elements in the stack can be resolved
            #using while loop
            while stack and temperatures[prev_idx] < temperatures[curr_idx]:
                stack.pop()
                ans[prev_idx] = curr_idx - prev_idx
                if stack:
                    prev_idx = stack[-1]

            # append the current idx into stack to check
            # if it can be resolved
            stack.append(curr_idx)

        return ans


class Solution_brute_force:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            num_day = 0
            flag = False
            for j in range(i + 1, len(temperatures)):
                num_day += 1
                if temperatures[j] > temperatures[i]:
                    flag = True
                    ans.append(num_day)
                    break
            if not flag:
                ans.append(0)

        return ans
