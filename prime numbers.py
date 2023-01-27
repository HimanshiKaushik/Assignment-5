lower_limit=int(input("ENTER THE LOWER LIMIT OF RANGE : "))
upper_limit=int(input("ENTER THE UPPER LIMIT OF RANGE : "))
for num in range(lower_limit,upper_limit + 1):
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count = count + 1
            break

    if count == 0 and num != 1:
        print("%d" % num)
    else:
        pass