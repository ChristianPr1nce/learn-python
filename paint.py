try:
   length = int(input("What is the length of the Ceiling?"))
   width = int(input("What is the width of the Ceiling?"))
   squarefeet = length * width
   paint = 350
   gallon = squarefeet / paint

   print(f"you will need {round(gallon)} gallons of \n paint to cover {squarefeet} squarefeet")
except:
   print("PLEASE ONLY ADD NUMBERS") 