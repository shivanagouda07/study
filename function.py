def say_hello():
    print("Hii this is just a program")
say_hello()



def check_env(env):
    if env == "prod":
        print("This is production env")
    else:
        print("This is not production env")
    
check_env("dev")

# check_env("prod")

# check_env(" ")