nums=(12,34,54,2,3,42,233,26)
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")