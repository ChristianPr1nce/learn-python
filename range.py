try:
   africans = ["nigga", "criminal", "tall", "slave", "biggestdicksize"]
   westernpeople = ["rich", 'colonizer', 'white', 'averagedicksize']
   easternpeople = ["masterofmath", "smalleyes", 'decentwealth', 'firstcivilization', 'smallestdick']
   
   name = input("\n africans \n westernpeople \n eastern people \n Select A Category:")

  # check if name == africans:
   # print africans
   if name == "africans":
      for niggers in africans:
         print(niggers)
   
   # check if name == westernpeople:
   #  print westernpeople
   elif name == "westernpeople":
      for anglosaxons in westernpeople:
         print(anglosaxons)
   
   # check if name == easternpeople:
   # print easternpeople
   elif name == "easternpeople":
      for yellowmonkeyas in easternpeople:
         print(yellowmonkeyas)
   else:
      print("PLEASE SELECT A CATEGROY")
   
except:
   print("how did we get here? ")     


