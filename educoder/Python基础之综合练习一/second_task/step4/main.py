from file_hb_stu import Solution

file_1 = input()
file_2 = input()
file_3 = input()

Solution().solve(file_1, file_2, file_3)

with open(file_3, "r") as f:
	print(f.read(), end='')