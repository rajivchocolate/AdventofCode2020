with open("expense_report.txt") as f:
    lines = f.readlines()
    nums = {int(line.strip()) for line in lines}
# O(n*n) efficiency since there is 2 for loops
"""
PART ONE:
nums = [int(line.strip()) for line in lines]
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        first_num = nums[i]
        second_num = nums[j]
        if first_num + second_num == 2020:
            answer = first_num * second_num

# O(n) efficiency
nums = {int(line.strip()) for line in lines}
for num in nums:
    difference = 2020 - num
    if difference in nums:
        answer = difference * num
"""
"""
PART TWO:
"""
nums = {int(line.strip()) for line in lines}
desired_sum = 2020
for first_val in nums:
    first_difference = 2020 - first_val
    for second_val in nums:
        second_difference = first_difference - second_val
        if second_difference in nums:
            third_value = second_difference
            answer = first_val * second_val * third_value

print()