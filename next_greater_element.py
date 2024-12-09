"""
Brute Force: traverse the array in circular way using modulus.
TC:O(n^2)
Optimal way using stack: [10,9,8,7,6,5] 10 cannot be resolved w/o resolving 9, 9 cannot be resolved w/o resolving 8,
and so on. So we can store the elements that can not be resolved in the stack and once we find top of stack can be
 resolved, it is possible the rest of the elements in the stack can be resolved.
 Queue can not be used since the resolving is done from the end.
 TC: O(2n) + O(n) filling array
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        ans = [-1 for _ in range(len(nums))]

        for curr_idx in range(len(nums)):  # 1
            # find the next index using modolus
            next_idx = (curr_idx + 1) % len(nums)

            # the loop will run until the starting element is not visited again
            while next_idx != curr_idx:
                # check if next element is greater
                if nums[next_idx] > nums[curr_idx]:
                    ans[curr_idx] = nums[next_idx]
                    break
                # move to next indx
                next_idx = (next_idx + 1) % len(nums)

        return ans
