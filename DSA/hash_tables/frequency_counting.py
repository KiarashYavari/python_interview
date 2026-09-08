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

print(none_repeating_num(nums))