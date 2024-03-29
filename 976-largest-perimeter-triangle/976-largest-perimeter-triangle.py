class Solution:
    def largestPerimeter(self, A):
        A.sort()
        return ([0] + [a + b + c for a, b, c in zip(A, A[1:], A[2:]) if c < a + b])[-1]