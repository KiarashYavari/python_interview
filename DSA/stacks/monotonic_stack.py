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

# For each day, return how many days until a warmer temperature.
temps = [73, 74, 75, 71, 69, 72, 76, 73]
# [1, 1, 4, 2, 1, 1, 0, 0]
def daily_temperatures(temps: list[int]) -> list[int]:
    result = [0] * len(temps)
    stack = []
    # your code
    for indx in range(len(temps)):
      stack.append(indx)
      while stack and temps[stack[-1]] < temps[indx]:
        stack.pop()
      if stack:
        print("inside if")
        result[stack[-1]] += indx - stack[-1]
        print(indx - stack[-1])
      print(f"stack: {stack}", f"temps: {temps[indx]}")
        
    
    return result
      
print(daily_temperatures(temps=temps))
