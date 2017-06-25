class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = 0
        for i in range(1,32):
            if (x%2 + y%2) == 1:
                r = r + 1
            x = int(x/2)
            y = int(y/2)
        return r
