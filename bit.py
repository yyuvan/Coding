# def checkIfSame(num1,num2):
#     if ((num1^num2) != 0):
#         print("Numbers are not equal")
#     else:
#         print("Numbers are equal")
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# checkIfSame(num1,num2)

# def OddOccuring(num):
#     res = 0
#     for i in num:
#         res = res ^ i
#     return res
# num=[]
# n=int(input("Enter array size: "))
# while (n):
#     number=int(input("Enter element: "))
#     num.append(number)
#     n-=1
# print("\n \n Odd occurring number is: ", OddOccuring(num))

# def printTwoOdd(arr,size):
#     xorof2=arr[0]
#     x=0
#     y=0
#     set_bit =0
#     for i in range(1,size):
#         xorof2 = xorof2 ^ arr[i]
#     set_bit = xorof2 & ~(xorof2-1)
#     for i in range(size):
#         if (arr[i] & set_bit):
#             x = x ^ arr[i]
#         else:
#             y = y ^ arr[i]
#     print("Two Odd occurring numbers are: ", x, " and ", y)
# arr=[]
# arr_size=int(input("Enter array size: "))
# for i in range(0,arr_size):
#     number=int(input("Enter element: "))
#     arr.append(number)
# printTwoOdd(arr,arr_size)

# def isPowerOfTwo(x):

#     if(x == 0):

#         return False

#     else:

#         while(x % 2 == 0):

#              x /= 2

#     return (x == 1)
# print(isPowerOfTwo(int(input("Enter a number: "))))

# def power2(number):

#     if (number == 0):

#         return 0

#     if ((number & (~(number - 1))) == number):

#         return 1

#     return 0
# # print(power2(int(input("Enter a number: "))))

# def isPowerOfFour(x):

#     if(x == 0):

#         return False

#     else:

#         while(x % 4 == 0):

#              x /= 4

#     return (x == 1)
# # print(isPowerOfFour(int(input("Enter a number: "))))

# def powerOf4(number):
#     count = 0
#     if (number & (~(number & (number - 1)))):
#         while(number > 1):

#             number >>= 1
#             print(f"Nmber: {number}")
#             count += 1
#             print(f"Power count: {count}")
#         if(count % 2 == 0):

#             return True

#         else:

#             return False
# # print(powerOf4(int(input("Enter a number: "))))
# def powerOf4(number):
#     print("Input number:", number)

#     count = 0

#     print("\nChecking condition:")
#     print("number:", number)
#     print("number - 1:", number - 1)
#     print("number & (number - 1):", number & (number - 1))
#     print("~(number & (number - 1)):", ~(number & (number - 1)))
#     print("Final condition value:", number & (~(number & (number - 1))))

#     if (number & (~(number & (number - 1)))):
#         print("\nCondition passed → entering loop")

#         while(number > 1):
#             print("\nBefore shift:", number)

#             number >>= 1
#             print("After shift:", number)

#             count += 1
#             print("Power count:", count)

#         print("\nFinal count:", count)

#         if(count % 2 == 0):
#             print("Count is even → Power of 4")
#             return True
#         else:
#             print("Count is odd → Not power of 4")
#             return False

#     else:
#         print("Condition failed → Not a power of 4")
#         return False


# # print("\nResult:", powerOf4(int(input("Enter a number: "))))

# def computexy(x,y):
#     res = 1
#     while (y > 0):
#         if (y % 2 == 0):
#             y = y >> 1
#             x = x * x
#         else:
#             res = res * x
#             y = y - 1
#     return res
# # print(computexy(int(input("Enter base: ")), int(input("Enter exponent: "))))

# def Swap2Numbers(a, b):
#     print(f"Before swapping: a = {a}, b = {b}")
#     a = a ^ b
#     print(a,b)
#     b = a ^ b
#     print(a,b)
#     a = a ^ b
#     print(f"After swapping a= {a}, b= {b}")
# # Swap2Numbers(int(input("Enter a: ")), int(input("Enter b: ")))

# def swap2(a,b):
#     a=(a&b)+(a|b)
#     b=a+(~b)+1
#     a=a+(~b)+1
#     print(f"After swapping a= {a}, b= {b}")
# swap2(int(input("Enter a: ")), int(input("Enter b: ")))


def divide(a,b):
    sign=(-1 if ((a < 0) ^ (b < 0)) else 1)
    a=abs(a)
    b=abs(b)
    quotient=0
    temp=0
    for i in range(31,-1,-1):
        if (temp + (b << i) <= a):
            temp += b << i
            quotient |= 1 << i
    if (sign == -1):
        quotient = -quotient
    return quotient
print(divide(int(input("Enter dividend: ")), int(input("Enter divisor: "))))
