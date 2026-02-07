nums = [23, 34 ,56]
try:
    print(nums[4])
except IndexError:
    print('Element does not exist in list.')