aclNum = int(input("What is the IPv4 ACL number? "))

if aclNum >= 1 and aclNum <= 99:
    print("This is a standart IPv4 ACL.")
elif aclNum >= 100 and aclNum <= 199:
    print("This is an extended IPv4 ACL.")
else:
    print("This is a bad IPv4 ACL.")