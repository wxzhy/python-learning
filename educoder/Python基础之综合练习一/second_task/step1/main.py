from lcm_stu import Solution

ls = list(map(lambda x:int(x), input().split(',')))

print(Solution().get_lcm(ls))