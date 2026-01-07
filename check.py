service = "nginx"
status = "running"   # pretend we checked it

if status == "running":
    print(f"{service} is healthy")
else:
    print(f"{service} is DOWN")
