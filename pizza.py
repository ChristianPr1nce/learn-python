try:
    boxes = int(input("how many pizza boxes do you have?"))
    people = int(input("how many people?"))
    slices = boxes * 12
    eachslice = int(slices / people)
    leftovers = slices % people
    print(f"{boxes} boxes and {people} people \n {eachslice} slices each \n {leftovers} leftovers")
except:
    print('PLEASE ONLY ADD NUMBERS')
