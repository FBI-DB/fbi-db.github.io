import time
import sys

#----VARIBLES-------------------------------------
Accounts = {'Agent11': '01132011'}
CurrentAccount = ""
Creator = "The Government"
update = """"""

#----COMMAND-IMPUT--------------------------------

def Input():
  CMD = str(input(">>"))
  if CMD.lower() in ["cmds","commands"]:
   print("""
   • CMDS - List of Commands
   • Update - Provides information on the most recent update
   • Logout - Logs out of account
   • Access launch code
   """)
   Input();
  elif CMD.lower() in ["logout", "log out"]:
   LogoutCheck();
  elif CMD.lower() in ["5445465446"]:
    UPC();
  elif CMD.lower() in ["45645464564"]:
    print("This command is not done yet.")
    time.sleep(1)
    Input();
  elif CMD.lower() in ["access launch code"]:
    print("Accessing DataBase")
    time.sleep(2)
    print("Obtaining possible combinations")
    time.sleep(2)
    print("00014567...code terminated...access detonated...")
  elif CMD.lower() in ["update"]:
    print(update)
    time.sleep(1)
    Input();
  elif CMD.lower() in ["admin"]:
    print("ENTER THE CODE >> ")
    if CMD.lower() in ["8464523"]:
      print("")
  else:
   print("Invalid Command")
   time.sleep(1)
   Input();

#----TITLE----------------------------------------
def Print(s):
    for c in s:
        sys.stdout.write( '%s' %c )
        sys.stdout.flush()
        time.sleep(0.025)

def StartUp():
  print(update)
  print("""├─────────────────────────────────┤
        █  █▀█ █▀▀ ▀█▀ █▀█
        █▄ █▄█ █▄█ ▄█▄ █ █
├─────────────────────────────────┤
  """, Creator)
        
#----QUESTIONS------------------------------------
def Menu():
 print("")
 AccountCheck = str(input("ENTER THE CODE >> "))
 if AccountCheck.lower() in ["26842", "26842"]:
  User();
 elif AccountCheck.lower() in ["4345009", "4345009"]:
  NewUser(); 
 else:
    print("INVALID CODE")
    time.sleep(1)
    Menu();

def RetryNewAccount():
 AccountCheck = str(input("TYPE EXIT"))
 if AccountCheck.lower() in ["9370"]:
  NewUser();
 elif AccountCheck.lower() in ["exit"]:
  Menu(); 
 else:
    print("Invalid Awnser")
    time.sleep(1)
    RetryNewAccount();

def RetryLoginAccount():
 AccountCheck = str(input("TYPE EXIT >> "))
 if AccountCheck.lower() in ["9370"]:
  User();
 elif AccountCheck.lower() in ["exit"]:
  Menu(); 
 else:
    print("Invalid Awnser")
    time.sleep(1)
    RetryLoginAccount();
    
def RetryLogoutAccount():
 AccountCheck = str(input("Would you like to Retry or Exit?"))
 if AccountCheck.lower() in ["retry"]:
  LogoutCheck();
 elif AccountCheck.lower() in ["exit"]:
  Input();
 else:
    print("Invalid Awnser")
    time.sleep(1)
    RetryLogoutAccount();
    
def LoginOrExit():
 Check = str(input("Would you like to Login or Exit?"))
 if Check.lower() in ["login"]:
  User();
 elif Check.lower() in ["exit"]:
  Menu(); 
 else:
    print("Invalid Awnser")
    time.sleep(1)
    LoginOrExit();
    
def LogoutCheck():
  Check = str(input("Are you sure you want to logout?"))
  if Check.lower() in ["y", "yes"]:
   CurrentAccount = ""
   time.sleep(1)
   print("You successfully logged out")
   time.sleep(1)
   Menu();
  elif Check.lower() in ["n", "no"]:
   Input();
  else:
   print("Invalid Awnser")
   time.sleep(1)
   RetryLogoutAccount();
  
def UsernameCheck():
  Check = str(input("Are you sure you want to change your username?"))
  if Check.lower() in ["y", "yes"]:
   NewUser();
  elif Check.lower() in ["n", "no"]:
   Input();
  else:
   print("Invalid Awnser")
   time.sleep(1)
   RetryLogoutAccount();

def UPC():

  Check = str(input("Are you sure you want to change your Username and/or Password?"))
  if Check.lower() in ["y", "yes"]:

    NUC();
  elif Check.lower() in ["n", "no"]:
   Input();
  else:
   print("Invalid Awnser")
   time.sleep(1)
   RetryLogoutAccount();
   
def NewUsername():
  Check = str(input("New Username:"))
  if CurrentAccount in Accounts:
    Accounts[CurrentAccount] = Check
    
   
   
   
#----USER-----------------------------------------
def User():
  print("WARNING: Login is case sensitive; use with caution")
  Username_Login = str(input("UserName:"))
  Password_Login = str(input("Password:"))
  if Username_Login in Accounts and Accounts[Username_Login] == Password_Login:
    CurrentAccount = Username_Login
    Print("Success!\n")
    time.sleep(1)
    print("Welcome", CurrentAccount,"- Type 'CMDS' for Commands")
    time.sleep(1)
    Input();
  else:
    print("Account was not found")
    time.sleep(1)
    RetryLoginAccount();
    
#----NEW USER-------------------------------------
def NewUser():
  New_Username = str(input("Create Username:"))
  if not New_Username in Accounts:
    New_Password = str(input("Create Password:"))
    Conform_Password = str(input("Confirm Password:"))
    if New_Password == Conform_Password:
      Print("Creating Account...\n")
      time.sleep(3)
      Print("Obtaining information from government database...\n")
      time.sleep(3)
      Print("Success!\n")
      Accounts[New_Username] = New_Password
      time.sleep(2)
      LoginOrExit();
    elif not New_Password == Conform_Password:
      print("Sorry the passwords didin't match")
      time.sleep(1)
      RetryNewAccount();
    else:
      print("Error has Occured")
      time.sleep(1)
      RetryNewAccount();
  else:
      print("Username already exist")
      time.sleep(2)
      RetryNewAccount();

def NUC():
  New_Username = str(input("Create Username:"))
  if not New_Username in Accounts:
    New_Password = str(input("Create Password:"))
    Conform_Password = str(input("Confirm Password:"))
    if New_Password == Conform_Password:
      Print("Creating Account...\n")
      time.sleep(3)
      Print("Obtaining information from government database...\n")
      time.sleep(3)
      Print("Success!\n")
      Accounts[New_Username] = New_Password
      time.sleep(2)
      LoginOrExit();
    elif not New_Password == Conform_Password:
      print("Sorry the passwords didin't match")
      time.sleep(1)
      RetryNewAccount();
    else:
      print("Error has Occured")
      time.sleep(1)
      RetryNewAccount();
  else:
      print("Username already exist")
      time.sleep(2)
      RetryNewAccount();
  
#----START----------------------------------------
StartUp();
Menu();


