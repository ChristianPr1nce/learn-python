try:
   length = int(input("What is the length of the Ceiling?"))
   width = int(input("What is the width of the Ceiling?"))
   squarefeet = length * width
   paint = 32.516064
   gallon = 1 
   # gallon cover area = 350sqf
   # if paint => squarefeet:
   #  paint 
   # 
   print(f"you will need {gallon} gallons of \n paint to cover {squarefeet} squarefeet")
except:
   print("PLEASE ONLY ADD NUMBERS") 