#This code snippet demonstrates how to convert a list of ASCII values 
# into a bytes object, decode it to a string, and then print it.
b = bytes([72,101,108,108,111])
print(str(b))
s = b.decode('utf-8')
print(s)