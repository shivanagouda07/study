# def say_hello():
#     print("Hii this is just a program")
# say_hello()


#function name
# def check_env(env):
#     if env == "prod":
#         print("This is production env")
#     else:
#         print("This is not production env")
        
#     # calling a method   
# check_env("prod")

# check_env("prod")

# check_env(" ")


# def hello():
#     print("Hii hello,  how are you")

# hello()

# def geet(env):
#     print("This is to infrom you that ")
#     print("where practice makse man perfect example")

# geet("hello")


# def add(a,b):
#     print(f"adding of 2 numabers is : {a+b}")

# add(10,20)



def check_status(env):
    if env == "service":
        return "running"
    else:
        return "stopped"
service = "server"
status = check_status(service)
print(status)