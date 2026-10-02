heights = [2, 1, 5, 6, 2, 3]
 
def greatest_bar_area(heights: list[int]) -> int:
    stack = []
    max_area = 0

    for i in range(len(heights)):

        while stack and heights[stack[-1]] > heights[i]:
            height_index = stack.pop()
            if stack:
                width = i - stack[-1] -1
            else:
                width = i
            area = width * heights[height_index]
            max_area = max(area, max_area)
            # calculate width here

            # calculate area
            # update max_area

        stack.append(i)
        
    n = len(heights)    
    while stack:
        height_index = stack.pop()
        
        if stack:
            width = n - stack[-1] - 1
        else:
            width = n
        
        area = 1 * heights[height_index]
        max_area = max(area, max_area)
    # process anything still left in stack

    return max_area

print(greatest_bar_area(heights=heights))
