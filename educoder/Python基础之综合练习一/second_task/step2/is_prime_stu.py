from math import sqrt
class Solution():
    def solve(self, l, r):
        '''
        :type l, r: int
        :rtype : list
        '''
        lst=[]
        for i in range(l,r+1):
            if self.is_prime_1(i):
                lst.append(i)
        return lst
        # 请在此添加代码，实现求得[l, r]范围内的所有素数，并将其返回
        # ********** Begin *********#
    def is_prime_1(self,x):
        if x == 1:
            return False
        for i in range(2, int(sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    
