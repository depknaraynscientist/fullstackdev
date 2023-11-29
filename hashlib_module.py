import hashlib
inp = input("Enter a string to hash : \n")
#encode the string and then use md5 on it
inp_encoded = inp.encode()
print(inp_encoded)
out = hashlib.md5(inp_encoded)
print(out.digest())
print(out.hexdigest())
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
out2 = hashlib.sha256(inp_encoded)
print(out2.digest())
print(out2.hexdigest())