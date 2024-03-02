from is_prime_stu import Solution

n = int(input())
so = Solution()
for i in range(n):
	a,b = list(map(lambda x:int(x), input().split(',')))
	print(so.solve(a, b))