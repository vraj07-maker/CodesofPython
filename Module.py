a,b,c=12,13,14
print("\nHello World!")
print(a+b+c)
print(a-b-c ,"\n")

if a<23:
    print("AAAAAAAAAA")
elif c<16:
    print("CCCCCCCCCC")    
else:    
    print("BBBBBBBBBB")


x = 11
y = 15

for i in range(1, 11):
    row_output = ""
    for num in range(x, y +1):
        mul = num * i
        row_output += f"{num} * {i} = {mul}\t"
    print(row_output)


