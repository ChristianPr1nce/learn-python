# a = int(float(input("What is the length of the room in feet?")))
# b = int(float(input("What is the width of the room in feet?")))
# c = a * b 
# d = c * 0.092903
# if isinstance(a, float) and isinstance(b, float):
#     print("WHAT ARE YOU DOING?")
# else:
#     print(f'you entered dimensions of {a} by {b} feet.\n The area is \n {c} square feet \n {d} square meters')


try:
    a = int(float(input("What is the length of the room in feet?")))
    print(a)
except:
    print("what the fuck nigga thats not a number.")