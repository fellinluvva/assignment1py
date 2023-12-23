print("Sorting values")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
incr = sorted([a, b, c])
print("Sort#1 values by increasing", incr)
# or you can use sorting w/o list
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("Sort#2 values by increasing", a, b, c)
