class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # helper
        def recurse(subSetSum, i):
            if subSetSum == 0:
                return True

            if subSetSum < 0:
                return False

            if i == len(nums):
                return False # -- NOTE [2]

            if (i, subSetSum) in memo:
                return memo[(i, subSetSum)]

            result = recurse(subSetSum-nums[i], i+1) or recurse(subSetSum, i+1)
            memo[(i, subSetSum)] = result
            return result

        # main
        numSum = sum(nums)
        if numSum % 2 != 0: # if sum is odd -> no way can be divded into 2 equal parts
            return False

        memo = {}
        targetSum = numSum//2 # --- NOTE [1] 
        return recurse(targetSum, 0) # ([1], i=0)

        # NOTE [1]
        # --------
        # prompt asks to identify if a list of nums can be partitioned into exactly 2 subsets
        # with equal sums. This makes the problem easier as the traget is fixed
        # If instead, the number of subsets with equal sum is left undefined (n inseatd of 2)
        # then the target is dynamic and we need to check at every node whether the subset we have
        # is equal to its complement (is sum(subset) == sum(nums) - sum(subset))

        # NOTE [2]
        # --------
        # we have reached the end of nums without finding a pair of subsets satisfying the cond
        # Had we found a pair a True would have been returned much ealrier before we hot the last index
        # This is what I'd like to call a boolean knapsack which is a little different form classical knapsack problem,
        # because it's not about optimization
        # but rather, whether we have a particualr scenario in our solution space.
        # This is why it makes sense to to return False if the last index is encountered

        # True or False -> True (scneario found in one branch)
        # True or True -> True (sceanrio found more than once)
        # False or Flase -> False (sceanrio not found -> keep looking)


        # f(i) -> f(i+1) -> f(i+2) ...... -> f(i=n)
        # False -> False -> ....
