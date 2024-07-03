try:
   #ask user lenght
   length = int(input("What is the length of the Ceiling?"))
   #ask user width
   width = int(input("What is the width of the Ceiling?"))
   # length * width to squarefeet
   squarefeet = length * width
   # set paint variable
   paint = 350
   # set gallon variable
   gallon = squarefeet / paint
   #print results
   print(f"you will need {round(gallon)} gallons of \n paint to cover {squarefeet} squarefeet")
except:
   print("PLEASE ONLY ADD NUMBERS") 