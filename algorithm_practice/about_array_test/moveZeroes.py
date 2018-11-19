'''

'''


def moveZeroes0(nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		if n <= 1:
			return
		for i in range(n):
			if nums[i] != 0:
				for j in range(i-1, -1, -1):
					if nums[j] == 0:
						nums[j+1], nums[j] = nums[j], nums[j+1]


def moveZeroes1(nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		输入: [0,1,0,3,12]
		输出: [1,3,12,0,0]
		"""
		n = len(nums)
		if n <= 1:
			return
		# for i in range(n):
		# 	if 



if __name__ == '__main__':
	nums = [0, 0, 1]
	# nums = [0,1,0,3,12]
	moveZeroes0(nums)
	print(nums)