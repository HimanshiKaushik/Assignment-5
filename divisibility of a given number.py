lower_limit=int(input("ENTER LOWER RANGE LIMIT:"))
upper_limit=int(input("ENTER UPPER RANGE LIMIT:"))
n = int(input("ENTER THE NUMBER : "))
for i in range(lower_limit,upper_limit+1):
    if(i%n==0):
        print(i)