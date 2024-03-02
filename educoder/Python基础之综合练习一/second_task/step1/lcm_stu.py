class Solution():
    def gcd(self,x, y):
        return x if y == 0 else self.gcd(y, x%y)
    def lcm(self,x,y):
        return x*y/self.gcd(x,y)
    def get_lcm(self, x):
        #请在此添加代码，实现求出给定的所有正整数的最小公倍数，并将其返回
        #********** Begin *********#
        y=1
        for i in x:
            y=self.lcm(y,i)
        return int(y)
        #********** End **********#