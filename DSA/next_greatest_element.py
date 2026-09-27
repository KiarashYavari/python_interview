nums = [2, 1, 2, 4, 3]
def next_greater_elements(nums: list[int]) -> list[int]:
    # your code
  stack = []
  result = [-1] * len(nums)
  for i in range(len(nums) - 1, -1, -1):
  
      while stack and stack[-1] <= nums[i]:
          stack.pop()
  
      if stack:
          result[i] = stack[-1]
  
      stack.append(nums[i])
  return result
print(next_greater_elements(nums))
# This is called a monotonic decreasing stack because, conceptually, we keep useful candidates in decreasing order.
