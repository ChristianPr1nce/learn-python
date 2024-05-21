import datetime
# age = int(input("Enter age: "))
# hah = 19

# if age > hah:
#     print("welcome")
# else:
#     print("You're not allowed")

current_time = datetime.datetime.now()

current_day = current_time.year

a = int(input("what is your age?"))
b = int(input("what age would you like to retire?"))

c = a - b 
d = current_day + b
if a == b:
    print("YOU CAN RETIRE NOW!!!")
elif a > b:
    print("PLEASE DO THIS PROPERLY!!!")
else:
    print (f"you have {c} years left until you retire.\n you can retire in {d}")
