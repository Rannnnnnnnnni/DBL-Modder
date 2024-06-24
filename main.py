import time
import os

from scripts.invert import invert
from scripts.accountModFunctions import accountMods
from stuff.text import main
from stuff.text import account
from stuff.text import units
from stuff.text import main2

restart = True

def unitsModding():
  leave = False

  while not leave:
    chosenOption = input(units+"\n>> ")
  
    if chosenOption == "1":
      mod = accountMods(9999, 14, 99, 7, 9999, 0, 0)
      mod.modCustomLevel()
      mod.modCustomArtBoost()
      mod.modCustomStars()
      mod.modCustomZenkai()
      mod.modCustomFriendshipLevel()

      clear()
  
    elif chosenOption == "2":
      level = int(input("\nEnter level:\n>> "))
      mod = accountMods(level, 0, 0, 0, 0, 0)
      mod.modCustomLevel()

      clear()

    elif chosenOption == "3":
      stars = int(input("\nEnter stars:\n>> "))
      mod = accountMods(0, stars, 0, 0, 0, 0)
      mod.modCustomStars()

      clear()

    elif chosenOption == "4":
      boosts = int(input("\nEnter art boosts:\n>> "))
      mod = accountMods(0, 0, boosts, 0, 0, 0)
      mod.modCustomArtBoost()
  
      clear()

    elif chosenOption == "5":
      zenkai = int(input("\nEnter zenkai:\n>> "))
      mod = accountMods(0, 0, 0, zenkai, 0, 0)
      mod.modCustomZenkai()
    
      clear()
      
    elif chosenOption == "6":
      level = int(input("\nEnter level:\n>> "))
      mod = accountMods(0, 0, 0, 0, amount, 0, 0)
      mod.modCustomFriendshipLevel()
    
      clear()

    elif chosenOption == "7":
      print("\nEncryping file...")
      
      invertFile = invert("89bb4eb5637df3cd96c463a795005065")
      invertFile.finish()
    
      clear()

      leave = True

      print("File Encrpyted, you can find the file in output.")
      
def accountModding():
  leave = False

  while not leave:
    chosenOption = input(account+"\n>> ")
  
    if chosenOption == "1":
      amount = int(input("\nEnter amount:\n>> "))
      mod = accountMods(0, 0, 0, 0, 0, amount, 0)
      mod.modFakeCC()
    
      clear()

      clear()
  
    elif chosenOption == "2":
      amount = int(input("\nEnter amount:\n>> "))
      mod = accountMods(0, 0, 0, 0, 0, 0, amount)
      mod.modFakeZeni()
    
      clear()

    elif chosenOption == "3":
      print("\nEncryping file...")
      
      invertFile = invert("89bb4eb5637df3cd96c463a795005065")
      invertFile.finish()
    
      clear()

      leave = True

      print("File Encrpyted, you can find the file in output.")

def option1(choice):
  leave = False

  while not leave:
    if choice == "1":
      clear()

      accountModding()

    elif choice == "2":
      clear()

      unitsModding()

    else:
      clear()




def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

  time.sleep(1)

while restart:
  chosenFile = input(main+"\n>> ")

  if chosenFile == "1":
    print("\nDecryping file...")
    
    invertFile = invert("89bb4eb5637df3cd96c463a795005065")
    invertFile.invertFile()

    clear()

    choice = input(main2+"\n>> ")

    option1(choice)

  else:
    clear()