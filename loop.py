# count = 0
# while count<10:
#     print(f"the number is {count}")
#     count+=1

# for i in range(10):
#     print(i)

# num =1
# total=0
# while total<10:
#     total+=num
#     print(f"number {num} : is total  {total} ")
#     num+=1


# user_input = ""
    
# while user_input.lower()  !="exit":
#     user_input = input("Enter a input : ")
#     if user_input.lower()=="exit":
#         print("exit")
#     else:
#         print("not exiting ")



service = False
attempts = 0
max_attempts =5

while not service and attempts<max_attempts:
    attempts+=1
    print(f"the attempting the service {attempts}")
    if attempts==3:
        service=True
        print("service is up")
    else:
        print("servicing is still running")
