# given this list:
nums = [1, 2, 2, 3, 3, 3, 4]
#Build a dictionary that stores how many times each number appears.

def frequency_counting(nums: list)-> dict:
    result_dict = {}
    for num in nums:
        if num in result_dict:
            result_dict[num] += 1
        else:
            result_dict[num] = 1
    return result_dict

# print(frequency_counting(nums=nums))

nums = [4, 5, 1, 2, 1, 4, 5]
# Return the first number that appears exactly once.
def none_repeating_num(nums: list)->int:
    frequency_counting = {}
    result = None
    for num in nums:
        if num in frequency_counting:
            frequency_counting[num] += 1
        else:
            frequency_counting[num] = 1
    
    for num in nums:
        if frequency_counting[num] == 1:
            result = num
            return result
    
    # result = next((key for key, value in frequency_counting.items() if value==1 ), None)
    return result

# print(none_repeating_num(nums))

nums = [1, 1, 1, 2, 2, 3]
k = 2
# Return the k=2 most frequent elements.
def k_most_frequent(nums:list, k)->dict:
  frequency_dict = {}
  # calculate frequency_dict
  for num in nums:
    if num in frequency_dict:
      frequency_dict[num] += 1
    else:
      frequency_dict[num] = 1
     
  frequencies = list(frequency_dict.items())
  n = len(frequencies)
  for i in range(0, n-1):
    for j in range(i+1, n):
      if frequencies[j][1] >= frequencies[i][1]:
          frequencies[i], frequencies[j] = frequencies[j], frequencies[i]
  sorted_frequency_dict = dict(frequencies[:k])

  return sorted_frequency_dict

# print(k_most_frequent(nums=nums, k=k))

# most efficient approach with bucket sort
def k_most_frequent(nums: list, k: int) -> dict:
    frequency = {}

    # Step 1: count frequencies
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Step 2: create buckets
    buckets = [[] for _ in range(len(nums) + 1)]

    # Step 3: place each number in its frequency bucket
    for num, freq in frequency.items():
        buckets[freq].append(num)

    # Step 4: scan from highest frequency to lowest
    result = {}
    # buckets indexes are freq and numbers inside are numbers 
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result[num] = freq

            if len(result) == k:
                return result

print(k_most_frequent(nums=nums, k=k))
