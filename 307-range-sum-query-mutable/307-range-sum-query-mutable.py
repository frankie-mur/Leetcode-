class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.N = len(self.nums)
        self.tree = [0] * (self.N + 1)
        ## optimize initiate BIT in O(n)
        for j in range(1, self.N+1):
            self.tree[j] += self.nums[j-1]
            if (j + (j & (-j))) <= self.N:
                self.tree[j + (j & (-j))] += self.tree[j]

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.N:
            self.tree[i] += diff
            i += (i & (-i))

    def sumRange(self, i, j):
        return self.getSum(j) - self.getSum(i - 1)
    
    def getSum(self, i):
        sm = 0
        i += 1
        while i > 0:
            sm += self.tree[i]
            i -= (i & (-i))
        return sm