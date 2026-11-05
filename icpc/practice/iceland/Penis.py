nums = input()

r = int(nums.split(" ")[1])
pubs = int(nums.split(" ")[0])

start = (r - 1) * pubs


for i in range(start, (r + 1) * pubs):
	if (i/pubs > r - 1) :
		print(i)
		break
