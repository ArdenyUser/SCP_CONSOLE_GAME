fire5 = "0"
fire4 = "0"
notice5 = "NONE"
notice4 = "NONE"
print("Welcome to the SCP Console!")
print("Enter in your access code:")
code = input("CODE: ")
if code == "4":
  print("LOGGING IN AS RESEARCHER")
  print("Type status to learn about your notice, or logout to leave.")
  True
  while True:
    if fire4 == "1":
      False
      import main
    x = input("RESEARHCER$ ")
    if x == "status":
      print(notice4)
    if x == "logout":
      False
      import main
if code == "5":
  print("LOGGING IN AS OMNI ASSISTENT")
  print("Type status to learn about your notice, or logout to leave.")
  True
  while True:
    if fire5 == "1":
      False
      import main
    x = input("HELPER$ ")
    if x == "status":
      print(notice5)
    if x == "logout":
      False
      import main
if code == "OMNI":
  print("LOGGING IN AS OMNI")
  print("Type doc.me to learn about you, or logout to leave.")
  True
  while True:
    x = input("OMNI$ ")
    if x == "logout":
      False
      import main
    if x == "doc.me":
      print("You may edit levels, fire people, and accept test and veto them. Your Inter code is 6701")
      print("Type inter to DOC fire or give status to someone.")
    if x == "inter":
          option = input("1: FIRE 2: GIVE NOTICE 3: DONE [ENTER OPTION NO.] ") 
          if option == "1":
            classx = input("What level will you fire: ")
            if classx == "5": 
              fire5 = "1"
              print("SUCCESS")
            if classx == "4":
              fire4 = "1"
              print("SUCCESS")
          if option == "2":
            classx = input("Enter level to give notice to: ")
            if classx == "5":
              data = input("DATA: ")
              notice5 = data
            if classx == "4":
              data = input("DATA: ")
              notice4 = data

