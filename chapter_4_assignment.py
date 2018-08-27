nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# TODO 1
# print each number on a new line
# your code here:
for num in nums:
    print(num)

# TODO 2
# print each number and its square on a new line
# so that each line reads, for example, like this: The square of 12 is 144
# your code here:
for num in nums:
    sqr_of_num = num ** 2
    print("The square of", num, "is", str(sqr_of_num))
