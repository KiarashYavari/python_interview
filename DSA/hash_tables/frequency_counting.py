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

print(frequency_counting(nums=nums))