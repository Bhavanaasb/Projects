# Find the number is Even or Odd in Python | Python Interview Questions.
#A number is even if  divisible by 2 gives a reminder of 0.
#If the remainder is 1, it is an odd num.

num=int(input("Enter the number:"))
if num%2==0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))