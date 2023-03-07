#COOKING SIMULATOR
import random
import os



inventory = ["money,15","apple,1", "water,1"]
#inventory = ["money,10", "fish,5", "leef,3", "bruz,15", "bread,4", "meat,5"]

recipes = ["salad:leef,3:5",
           "appleJuice:apple,1;water,1:4",
           "friedMushrooms:mushroom,2:4",
           "seaweedChips:seaweed,4:5",
           "friedRice:rice,2:6"]

t2Recipes = ["strawberryJam:strawberry,2;sugar,1:12",
             "sandwich:bread,2;leef,2;cheese,1:15",
             "applePie:apple,3;floue,1;sugar,1:16",
             "strawberryIcecream:milk,1;egg,2;sugar,1;strawberry,2:22",
             "cake:flour,2;egg,2;milk,1;strawberry,4:30"]

t3Recipes = ["fishAndChips:fish,2;bread,2:20",
             "sushi:seaweed,4;rice,2;salmon,1:30",
             "cannedLobster:lobster,2;tincan,1;water,1:35",
             "fishSoup:fish,2;water,2;leef,2:25"]

t4Recipes = ["steak:meat,2;leef,1:30",
             "hamburger:bread,2;meat,1;leef,2;cheese,1:45",
             "meatballs:meat,4:30",
             "lasagne:meat,3;cheese,2:30",
             "hotdog:meat,1;bread,1:30",
             "ultraProteinMix:meat,4;fine,2;fish,3;salmon,2;lobster,2:80",
             "grilledHuman:human,1;leef,4;cheese,2:100"]



shop = ["fishingRod,25","bait,1","huntingRifle,100","bullet,3","bread,2","flour,4","egg,5","sugar,3","cheese,3"]

#itemValue = [""]


console = False


#-------------------MENU---------------------
def Menu():
    while(True):
        Clear()
        print ("Cooking Simulator [2023] \n")
        
        print ("1 - START")
        print ("2 - OPTIONS")
        print ("3 - EXIT")

        inputVal = input("")

        if(inputVal == "1"):
            #start
            Start()
            
        elif(inputVal == "2"):
            #options
            Options()
            
        elif(inputVal == "3"):
            #exit
            break
        
        else:
            Invalid()


def Options():
    
        while(True):
            Clear()
            global console
            print ("Options \n")
            print ("1 - Console " + str(console))
            print ("b - Back")

            inputVal = input("")

            if(inputVal == "1"):
                
                Clear()
                print("1 - Console clear")
                print("2 - Show clear as \"##clear##\"")

                inVal = input("")

                if(inVal == "1"):
                    console = True
                elif(inVal == "2"):
                    console = False
                else:
                    Invalid()
                
            elif(inputVal == "b"):
                #options
                break
            
            else:
                Invalid()
                
                
#--------------------GAMEPLAY------------------
def Start():
    while (True):
        Clear()
        print ("CROSSROADS")
        print ("Where to go ")

        print("      ,      ")
        print("     <|==>   ")
        print("   <==|=>    ")
        print("      |      ")
        print("--.__,|~_,~-~")
        print("")
        
        
        print ("1 - Kitchen")
        print ("2 - Forest")
        print ("3 - Pond")
        print ("4 - Shop")
        print ("b - HOME (Main Menu)")
        print ("i - Inventory")

        inputVal = input("")
        
        if(inputVal == "1"):
             Kitchen()   
                
        elif(inputVal == "2"):
            Forest()

        elif(inputVal == "3"):
            Pond()

        elif(inputVal == "4"):
            Shop()

        elif(inputVal == "b"):
            break

        elif(inputVal == "i"):
            Inventory()

        else:
            Invalid()


#---KITCHEN---
def Kitchen():
    while (True):
        Clear()
        print ("KITCHEN \n")

        print("     ||     ___       ")
        print("    /__\   |   |___   ")
        print("___ ____ __|   |   |__")
        print("   |*__ |  |  -|  ´|  ")
        print("___|[__]| ´|___|___|__")
        print("")
        
        print ("1 - Cook")
        print ("b - Back")
        print ("i - Inventory")

        inputVal = input("")
        
        if(inputVal == "1"):
            while (True):
                Clear()
                print ("RECEPIE \n")
                Recipe()
                print ("b - Back")
                print ("i - Inventory")

                inVal = input("")            

                if(inVal == "b"):
                    #back
                    break

                elif(inVal == "i"):
                    Inventory()

                elif(int(inVal)-1 < len(recipes) and inVal != ''):
                    Craft(recipes[int(inVal)-1])

                else:
                    Invalid()
                    
        elif(inputVal == "b"):
            #back
            break

        elif(inputVal == "i"):
            Inventory()
            
        else:
            Invalid()
        
#---FOREST---
def Forest():


    
    while (True):
        Clear()
        print ("FOREST \n")
        
        print("    /\        /\/\    /\   ")
        print("   /  \      /  \ \  /  \  ")
        print("_  /__\      /__\ \  /__\  ")
        print(" '-,||,'-._,~.||,|_,~.||_,.")
        print("")
        
        print ("1 - Hunt")
        print ("2 - Gather")
        print ("b - Back")
        print ("i - Inventory")

        inputVal = input("")
        
        if(inputVal == "1"):
            #hunt
            if(CheckItem("huntingRifle", 1) and CheckItem("bullet", 1)):

                recipes.extend(t4Recipes)
                t4Recipes.clear()
                
                Drops(["meat,40", "fineMeat,10", "human,1"],2)
                AddItem("bullet", -1)
                Enter("")
            else:
                Enter("Missing: huntingRifle or Bullets")                
                
                
        elif(inputVal == "2"):
            #gather
            Drops(["leef,50","strawberry,30","mushroom,20","apple,20"],5)
            Enter("")

        elif(inputVal == "b"):
            break

        elif(inputVal == "i"):
            Inventory()
            
        else:
            Invalid()

#---POND---
def Pond():

    while (True):
        Clear()
        print ("POND \n")

        print(".__   .    .   .,  ,-  . '  ,  |   _|.")
        print("   '-.|_ |          , .    _|.-'--´   ")   
        print("        ´',   ,   . | || .´           ")
        print("           '~~'~~^'~'~''~´            ")
        print("")
          
        print ("1 - Fish")
        print ("2 - Gather")
        print ("b - Back")
        print ("i - Inventory")

        inputVal = input("")
        
        if(inputVal == "1"):
            #fish
            if(CheckItem("fishingRod", 1) and CheckItem("bait", 1)):

                recipes.extend(t3Recipes)
                t3Recipes.clear()
                
                Drops(["fish,40", "salmon,10", "lobster,10", "tinCan,15"],2)
                AddItem("bait", -1)
                Enter("")
            else:
                Enter("Missing: fishingRod or bait")                
                
        elif(inputVal == "2"):
            #gather
            Drops(["Seaweed,50", "rice,30", "water,80"],5)
            Enter("")

        elif(inputVal == "b"):
            break

        elif(inputVal == "i"):
            Inventory()
            
        else:
            Invalid()

#---SHOP---
def Shop():
    while (True):
        Clear()
        print ("SHOP \n")

        print("      __.^,_|_|__      ")
        print("     [___________]     ")
        print("      | | $$$ | |      ")
        print("______|_|_____|_|______")
        print("")
        
        print ("1 - BUY")
        print ("2 - SELL")
        print ("b - Back")
        print ("i - Inventory")

        inputVal = input("")
        
        if(inputVal == "1"):
            #buy
            while (True):
                Clear()
                print ("SHOP - BUY \n")
                print ("Money: ", inventory[0].split(',')[1] + "\n")
                
                Buy()
                print ("b - Back")
                print ("i - Inventory")

                inVal = input("")            

                if(inVal == "b"):
                    #back
                    break

                elif(inVal == "i"):
                    Inventory()
                
                elif(int(inVal)-1 < len(shop)):
                    SpendMoney(int(inVal)-1)

                else:
                    Invalid()
                           
                
        elif(inputVal == "2"):
            #sell
            while (True):
                Clear()
                print ("SHOP - SELL \n")
                Sell()
                print ("b - Back")
                print ("i - Inventory")

                inVal = input("")            

                if(inVal == "b"):
                    #back
                    break

                elif(inVal == "i"):
                    Inventory()
                
                elif(int(inVal)-1 < len(recipes)):
                    EarnMoney(int(inVal)-1)

                else:
                    Invalid()

        elif(inputVal == "b"):
            break

        elif(inputVal == "i"):
            Inventory()
            
        else:
            Invalid()

#--------------------INVENTORY------------------
def Inventory():
    print("INVENTORY:")
        
    for i in range(0,len(inventory)): 
        item = inventory[i].split(',')
        print (item[0] + " (" + item[1] + ")")
    input ("enter")
    print ("")

def AddItem(addItem, amount):
    newItem = True
    for i in range(0,len(inventory)):
        item = inventory[i].split(',')
        
        if(item[0] == addItem):
            item[1] = int(item[1]) + amount
            inventory[i] = (item[0] + "," + str(item[1]))
            newItem = False
            break
    if(newItem):
        inventory.append(addItem + "," + str(amount))

        #remove item if item[1] == 0


def CheckItem(checkItem, amount):
    newItem = True
    for i in range(0,len(inventory)):
        item = inventory[i].split(',')
        
        if(item[0] == checkItem and int(item[1]) >= amount):
            return True


    return False

def checkItemQuant(checkItem):
    notFound = True
    for i in range(0,len(inventory)):
        item = inventory[i].split(',')
        if(item[0] == checkItem):
            #print(item[0])
            notFound = False
            return int(item[1])
            
    if(notFound):
        return 0 

#-----------------Recipe/shop-------------------
def Recipe():
    for i in range(0, len(recipes)):
        recipe = recipes[i].split(':')
        items = recipe[1].split(';')
        print (str(i +1) + " - " + recipe[0] + " = ", end='')
        for j in range(0,len(items)):
            item = items[j].split(',')
            print (item[0] + "(" + item[1] + "), ", end='')

        print("(value - " + recipe[2] + ") (" + CraftCheck(recipe[1]) + ")")
            

def Buy():

    recipes.extend(t2Recipes)
    t2Recipes.clear()
    
    for i in range(0,len(shop)):
        item = shop[i].split(',')
        print(str(i+1) + " - " + item[0] + " (Cost: " + item[1] + ")")

def SpendMoney(index):
    item = shop[index].split(',')
    money = inventory[0].split(',')
    if(CheckItem(money[0], int(item[1]))):
        AddItem(money[0], -int(item[1]))
        AddItem(item[0], 1)

        print ("-Spent: " + item[1] + " Money")
        Enter ("+Bought: " + item[0])
    else:
        Enter("Not Enough")


def Sell():
    for i in range(0,len(recipes)):
        item = recipes[i].split(':')
        #print(item[0])
        #print(str(checkItemQuant(item[0])))
        print(str(i+1) + " - " + item[0] + " (value: " + item[2] + ") (Have: " + str(checkItemQuant(item[0])) + ")")

#change to fit with recepie instead of shop
def EarnMoney(index):
    item = recipes[index].split(':')
    money = inventory[0].split(',')
    if(CheckItem(item[0], 1)):
        AddItem(money[0], int(item[2]))
        AddItem(item[0], -1)

        print ("-Sold: " + item[0])
        Enter ("+Earned: " + item[2] + " Money")
    else:
        Enter("Not Enough")
   
#-----------------SYSTEMS-----------------------
def Drops(items, times):
    #Format("item,weight"): "meat,5", "fine meat,1"
    for t in range(0, times):
        #print ("drop try")
        for i in range(0,len(items)):
            item = items[i].split(',')
            #print (item)
            value = random.randint(0, 100)
            #print (value)
            if(int(item[1]) > value):
                AddItem(item[0], 1)
                print ("+Got: " + item[0])            
    return

        
def Craft(recipe):
    #check items, then remove them and add out item

    recipeDiv = recipe.split(':')
    outItem = recipeDiv[0]
    items = recipeDiv[1].split(';')
    
    
    enough = False
    
    #check
    for i in range(0,len(items)):
        item = items[i].split(',')
        if(CheckItem(item[0], int(item[1]))):
            enough = True
            
        else:            
            Enter("Not Enough")
            enough = False
            break
    if(enough):
        
        #remove
        for i in range(0,len(items)):
            #print (item)
            item = items[i].split(',')
            print ("-Used: " + item[0] + " (" + item[1] + ")")
            AddItem(item[0], -int(item[1]))

        #add
        AddItem(outItem, 1)
        #print (outItem)
            

        Enter("+Made: " + outItem)

def CraftCheck(checkItems):
    #check items, then remove them and add out item

    items = checkItems.split(';')
    
    
    enough = False
    
    #check
    for i in range(0,len(items)):
        item = items[i].split(',')
        if(CheckItem(item[0], int(item[1]))):
            enough = True
        else:
            return("Craftable: NO")
            break
            
    if(enough):
        return("Craftable: YES")
    else:            
        return("Craftable: NO")



def Invalid():
    Enter("INVALID")

def Clear():
    if(console):
        os.system('cls')
    else:
        print("##clear##")

def Enter(prompt):
    if(prompt == ""):
        input ("enter")
    else:
        print (prompt)
        input ("enter")



Menu()
































