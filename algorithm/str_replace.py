class Solution:
    def replace(self, origin, str1, str2):
        """
        origin : str
        str1 : str
        str2 : str
        rtype: str
        """
        l = len(origin)
        l1 = len(str1)
        if l1==0 or l < l1:
            return origin

        next = self.makeNext(str1)
        #Replace the string one by one
        idx = self.KMP(origin, str1, next)
        left = ""
        right = origin
        while idx != -1:
            left += right[:idx]+str2
            right = right[idx+l1:]
            idx = self.KMP(right, str1, next)
        left += right
        return left

    #KMP algorithm
    def KMP(self, T, P, next):
        n = len(T)
        m = len(P)

        q = 0
        for i in range(n):
            while q>0 and P[q] != T[i]:
                q = next[q-1]
            if P[q] == T[i]:
                q = q+1
            if q==m:
                return i-m+1
        return -1

    def makeNext(self, P):
        l = len(P)
        next = [0] * l
        k = 0
        for q in range(1, l):
            while k>0 and P[k]!=P[q]:
                k = next[k-1]
            if P[k] == P[q]:
                k = k+1
            next[q] = k
        return next
        

if __name__ == '__main__':
    s = Solution()
    print s.replace("abcdbc", "bc", "bc")
    print s.replace("abcd", "", "12")
    print s.replace("", "ab", "12")
    print s.replace("abcdeyabcwiyiabcueiababc", "abc", "12")
