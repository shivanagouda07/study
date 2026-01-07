ec2 = {
    "id": "i-0017a918c78d53a7c",
    "state": "running",
    "type": "t3.micro"

}
if ec2["state"] == "running":
    print("Instance is running")
else:
    print("not running")


# import boto3

# ec2 = boto3.client("ec2", region_name="ap-south-1")

# response = ec2.describe_instances(
#     InstanceIds=["i-0017a918c78d53a7c"]
# )

# state = response["Reservations"][0]["Instances"][0]["State"]["Name"]

# print("Instance state:", state)
