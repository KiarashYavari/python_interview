heights = [2, 1, 5, 6, 2, 3]
def greatest_bar_area(heights: list[int]) -> int:
    stack = []
    max_area = 0

    for i in range(len(heights)):

        while stack and heights[stack[-1]] > heights[i]:
            height_index = stack.pop()

            # calculate width here

            # calculate area
            # update max_area

        stack.append(i)

    # process anything still left in stack

    return max_area

print(greatest_bar_area(heights=heights))
