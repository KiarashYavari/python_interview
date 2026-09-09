# If only existence → set.
# If extra information such as index/count/value → dict.
# Return the indices of two numbers that add up to target.
nums = [7, 11, 15, 2]
target = 9
def two_sum_lookup(nums:list, target:int)->list:
  seen = {}
  # {7:0, 11:1}
  result = []
  for index in range(len(nums)):
    needed = target - nums[index]
    if needed in seen:
      result.append(seen[needed])
      result.append(index)
    
    seen[nums[index]] = index
  return result

# print(two_sum_lookup(nums=nums, target=target))
# def two_sum_lookup(nums: list, target: int) -> list:
#     seen = {}

#     for index in range(len(nums)):
#         needed = target - nums[index]

#         if needed in seen:
#             return [seen[needed], index]

#         seen[nums[index]] = index

#     return []
