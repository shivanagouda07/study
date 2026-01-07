# number = 1,2,3,5,4,6,7,8
# for i in number :
#     print(i)

# message = "hello-world"
# for i in message:
#     print(i)



# for loop where used 99.9% in the devops course
# numbers = 1,2,3,4,5,6,7,8,10
# sum =0
# for i in numbers:
#     sum = sum + i
# print(sum)


#multiplication tables
number =int(input("Enter a number for multiplication : "))
print(number)
result =0
for i in range(1,11):
    result =  number * i
    print(number, "*", i, "=", result)