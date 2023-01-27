a = int(input("ENTER 1st SIDE OF TRIANGLE = "))
b = int(input("ENTER 2nd SIDE OF TRIANGLE = "))
c = int(input("ENTER 3rd SIDE OF TRIANGLE = "))
s = (a + c + b) / 2

area=((s)*(s-a)*(s-b)*(s-c))**0.5
if (a>0 and b>0 and c>0):
    if ((a+b>=c) and (b+c>=a) and (a+c>=b) ):
      print("TRIANGLE IS VALID")
      print ("AREA BY HERON'S FORMULA = ",area)
    else:
      print("TRIANGLE IS NOT VALID")
else:
    print("TRIANGLE IS NOT VALID")