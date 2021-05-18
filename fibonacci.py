i = 0
a = 0
b = 1

print("0\n1\n")
while i < 10:
    print(a+b)
    c = a
    a = b
    b = c+b
    i+=1