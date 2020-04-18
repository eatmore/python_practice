nums = input()
s = set(nums)
lst = list(s)
sum = 0
for i in lst:
    sum += eval(i)
print(sum)
