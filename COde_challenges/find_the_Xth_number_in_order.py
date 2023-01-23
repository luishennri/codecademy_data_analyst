def getX(x, nums):

  nums.sort()
  if x > len(nums) or x <= 0:
      return 0
  else:
      return nums[x-1]

print(getX(2, [6, 3, -1, 5]))
