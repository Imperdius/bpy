import math
tank = 13.5

validDistance = False

while validDistance == False:
    indistance = (input("Please enter the distance you are travelling in miles "))
    validDistance = True
    try:
        float(indistance)

    except ValueError:
        print("Please enter a number ")
        validDistance = False

distance = float(indistance)

validRoadType = False

while validRoadType == False:
    roadType = input("Are you expecting to be mostly travelling on highways or in cities? Please enter h for highways or c for cities ")

    if roadType == ("c"):
        validRoadType = True
        gallons = distance / 45
        print ("You can travel 204.3 miles between refuling ")
        
    elif roadType == ("h"):
        validRoadType = True
        gallons = distance / 78
        print ("You can travel 354.12 miles between refuling ")
        
    else: print("please enter one of the specified letters ")


miles = gallons * 4.54

tanks = math.floor(miles / 13.5)
strtanks = str(tanks)

print ("You will have to refuel " + strtanks + " times ")




        
        


    
