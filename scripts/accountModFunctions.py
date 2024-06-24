import json
class accountMods:
  def __init__(self, level : int, stars : int, artsBoost : int, zenkai : int, friendship : int, CC : int, zeni : int):
    self.level = level
    self.stars = stars
    self.artsBoost = artsBoost
    self.zenkai = zenkai
    self.friendship = friendship
    self.CC = CC
    self.zeni = zeni
      
  def modCustomLevel(self):
    data = None
    if self.level < 1 or self.level > 9999:
      print("Invalid level")
      
    try:
      with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
          data = json.load(f)
  
      for number in range(len(data["unit"]["unitInfo_"])):
        for unit in data["unit"]["unitInfo_"]:
          data["unit"]["unitInfo_"][number]["level"] = self.level
          data["unit"]["unitInfo_"][number]["exp"] = 100000000

    except Exception as Argument:
      os.remove("errorLog.txt")

      errorLog = open("errorLog.txt", "x")

      errorLog.write(str(Argument))

      errorLog.close() 


    with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
      f.truncate(0)
      f.write(json.dumps(data, indent = 4))
      
  def modCustomFriendshipLevel(self):
    data = None
    if self.level < 1 or self.level > 9999:
      print("Invalid level")
      
    try:
      with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
          data = json.load(f)
  
      for number in range(len(data["unit"]["unitInfo_"])):
        for unit in data["unit"]["unitInfo_"]:
          data["unit"]["unitInfo_"][number]["friendshipLevel"] = self.level

    except Exception as Argument:
      os.remove("errorLog.txt")

      errorLog = open("errorLog.txt", "x")

      errorLog.write(str(Argument))

      errorLog.close() 


    with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
      f.truncate(0)
      f.write(json.dumps(data, indent = 4))

  def modCustomArtBoost(self):
    data = None
    
    if self.artsBoost < 1 or self.artsBoost > 99:
      print("Invalid arts boost")

    try:
      with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
          data = json.load(f)
      for number in  range(len(data["unit"]["unitInfo_"])):
        for unit in data["unit"]["unitInfo_"]:
          data["unit"]["unitInfo_"][number]["strikeArtsBoost"] = self.artsBoost
          data["unit"]["unitInfo_"][number]["shotArtsBoost"] = self.artsBoost
          data["unit"]["unitInfo_"][number]["specialArtsBoost"] = self.artsBoost

    except Exception as Argument:
      os.remove("errorLog.txt")

      errorLog = open("errorLog.txt", "x")

      errorLog.write(str(Argument))

      errorLog.close() 


    with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
      f.truncate(0)
      f.write(json.dumps(data, indent = 4))

  def modCustomStars(self):
    data = None
    
    levelDict = {
      0 : 100,    
      1 : 200, 
      2 : 400, 
      3 : 700, 
      4 : 1400, 
      5 : 1900, 
      6 : 2400, 
      7 : 3000, 
      8 : 4000, 
      9 : 5000, 
      10 : 6000, 
      11 : 7000, 
      12 : 8000, 
      13 : 9000, 
      14 : 10000, 
    }

    if self.stars < 1 or self.stars > 14:
      print("Invalid stars.")

    try:
      with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
          data = json.load(f)
      for number in range(len(data["item"]["characterShards_"])):
        for item in data["item"]["characterShards_"]:
          data["item"]["characterShards_"][number]["count"] = levelDict[self.stars]

    except Exception as Argument:
      os.remove("errorLog.txt")

      errorLog = open("errorLog.txt", "x")

      errorLog.write(str(Argument))

      errorLog.close() 


    with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
      f.truncate(0)
      f.write(json.dumps(data, indent = 4))

  def modCustomZenkai(self):
    data = None

    if self.zenkai < 1 or self.zenkai > 7:
      print("Invalid Zenkai level.")

    try:
      with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
          data = json.load(f)
      for number in range(len(data["item"]["characterPlentyShards_"])):
        for item in data["item"]["characterPlentyShards_"]:
          data["item"]["characterPlentyShards_"][number]["count"] = 7000

    except Exception as Argument:
      os.remove("errorLog.txt")

      errorLog = open("errorLog.txt", "x")

      errorLog.write(str(Argument))

      errorLog.close() 


    with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
      f.truncate(0)
      f.write(json.dumps(data, indent = 4))
      
      
  def modFakeCC(self):
        data = None

        try:
          with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
              data = json.load(f)

          data["item"]["stones_"] = self.CC

        except Exception as Argument:
          os.remove("errorLog.txt")

          errorLog = open("errorLog.txt", "x")

          errorLog.write(str(Argument))

          errorLog.close() 

        with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
          f.truncate(0)
          f.write(json.dumps(data, indent = 4))

  def modFakeZeni(self):
        data = None

        try:
          with open("work/89bb4eb5637df3cd96c463a795005065", "r", encoding="utf-8") as f:
              data = json.load(f)

          data["item"]["zeny_"] = self.zeni

        except Exception as Argument:
          os.remove("errorLog.txt")

          errorLog = open("errorLog.txt", "x")

          errorLog.write(str(Argument))

          errorLog.close() 

        with open("work/89bb4eb5637df3cd96c463a795005065", "w", encoding="utf-8") as f:
          f.truncate(0)
          f.write(json.dumps(data, indent = 4))

