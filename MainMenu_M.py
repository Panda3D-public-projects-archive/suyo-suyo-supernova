#Programer:       Travis Woolery
#Created:         2/2/2011
#updated:         2/2/2011
#License:         CC-BY, must keep programmers name, and code can't used in other commercial games.
#Class: LogInMenu()
  #Logs user into global account on server
  #Commands: NetCommands, GoToNewCharMenu, SendNameAndPass, CleanUp

#Class: NewUserMenu()
  #Ask and sends new user information to make a new global account on server
  #Commands: GoToLogInMenu, PlayerMusic, NetCommands, SendNewUserData, CleanUp

#Class: MainMenu()
  #Menu to getting around
  #Commands: NetCommands, CheckFileSystem, SetUpScreen, CleanUp

#Class: SelectGameMenu()
  #Menu with buttons that are base on what is installed the Game folder
  #Commands: SetUpGame, NetCommands, CleanUp




from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *


class LogInMenu:
  def __init__(self, OML):
    global self2
    self2 = OML
    self2.WindowProp.Settings(["Title Mradr's_Prodject", "SizeX 300", "SizeY 548", "FullScreen 0", "UserHasMouse 1"])
    self2.UserWhere = "LogInMenu"

    #Start music.
    self2.AudioMgr.Play(2, self2.MainScreenMusic, 0, "b")

    #We setup the login screen by adding 2 text boxs. One of the texts boxs is for the user name and the other is for the password. Then we add some buttons Logon and Creat a New account.
    #When users click the logon, we go to MainMenu. Or if the the user clicks the Creat A New Account, it sends them to the newuser screen.
    self.Frame = DirectFrame(frameSize=(1,1,0,1))
    self.Background = OnscreenImage(image = 'MainMenu/Images/Boarder.png',parent=render2d)
    self.Logo = OnscreenImage(image = 'MainMenu/Images/Logo.jpg',pos = (0,0,.35),parent=render2d,scale = (.5,.5,.5))
    self.Logon = DirectButton(text = ("| Logon |"),rolloverSound=0,clickSound=0,pos=(0,0,-.35),scale=.08,text_scale=(1.5,1.5),command=self.SendNameAndPass)
    self.Logon.reparentTo(self.Frame)
    self.NameBoxText = OnscreenText(text = "Name", pos=(0,-.6), scale = 0.15)
    self.NameBoxText.reparentTo(self.Frame)
    self.Name = DirectEntry(pos=(-.6,0,-.8),scale=.08,width=10,text_scale=(1.5,1.5),rolloverSound=0,clickSound=0,cursorKeys=1)
    self.Name.reparentTo(self.Frame)
    self.PasswordBoxText = OnscreenText(text = "Password", pos=(0,-1), scale = 0.15)
    self.PasswordBoxText.reparentTo(self.Frame)
    self.Password = DirectEntry(pos=(-.6,0,-1.2),scale=.08,width=10,text_scale=(1.5,1.5),obscured=1,rolloverSound=0,clickSound=0,cursorKeys=1)
    self.Password.reparentTo(self.Frame)
    self.CreatNewUser = DirectButton(text = ("< Creat A New Account >"),rolloverSound=0,clickSound=0,pos=(0,0,-1.5),scale=.08,text_scale=(1.5,1.5),command=self.GoToNewCharMenu)
    self.CreatNewUser.reparentTo(self.Frame)
    self.ExitGame = DirectButton(text = ("< Exit >"),rolloverSound=0,clickSound=0,pos=(0,0,-1.7),scale=.08,text_scale=(1.5,1.5),command=self2.EndGame)
    self.ExitGame.reparentTo(self.Frame)


  ###############################################################################
  def NetCommands(self, data):
    if data[0] == "0" or data[0] == "2":
      self2.AudioMgr.Play(2, "MainMenu/Music/Sounds/accessDa.ogg")
      if data[0] == "2":
        print "That user already log on."
      else:
        print "Error 801810, PassWord or name didnt work."
      print "Server Check-> " + data[0]

    elif data[0] == "1":
      self2.AudioMgr.Play(2, "MainMenu/Music/Sounds/accessPa.ogg")
      print "Server Check-> " + data[0]
      self.CleanUp()
      #Make MainMenu
      self2.MakeMainMenu()


  ###############################################################################
  def GoToNewCharMenu(self):
    self.CleanUp()
    self2.MakeNewUserMenu()


  ###############################################################################
  def SendNameAndPass(self):
    UserName = self.Name.get().lower().strip()
    PassWord = self.Password.get().lower().strip()
    if UserName and PassWord:
      for f in (UserName + PassWord):
        if f not in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
          self2.PopUp("ShowError", "830, Sorry no special characters can be used.")
          self2.AudioMgr.Play(2, "MainMenu/Music/Sounds/accessDa.ogg")
          break
      else:
        self2.Name = UserName
        self2.NetWorkSendFrame["TCP"].append("@& "+UserName+" "+PassWord+"\n")


  ###############################################################################
  def CleanUp(self):
    for x in [self.Frame, self.Background, self.Logo, self.Logon, self.NameBoxText, self.Name, self.PasswordBoxText, self.Password, self.CreatNewUser, self.ExitGame]:
      x.removeNode()




##############################################################################################
class NewUserMenu:
  def __init__(self, OML):
    global self2
    self2 = OML

    self2.UserWhere = "NewAccountMenu"
    #Setup window
    self2.WindowProp.Settings(["Title Mradr's_Prodject", "SizeX 300", "SizeY 548", "FullScreen 0", "UserHasMouse 1"])

    #Start music.
    self2.AudioMgr.Play(2, self2.MainScreenMusic, 0, "b")

    #Content buttons Name, Password, Creat, and Exit
    self.Frame = DirectFrame(frameSize=(1,1,0,1))
    self.Background = OnscreenImage(image = 'MainMenu/Images/Boarder.png',parent=render2d)
    self.Logo = OnscreenImage(image = 'MainMenu/Images/Logo.jpg',pos = (0,0,.35),parent=render2d,scale = (.5,.5,.5))
    self.TitleBoxText = OnscreenText(text = "Creating A New Account", pos=(0,-.35), scale = 0.165)
    self.NameBoxText = OnscreenText(text = "Name", pos=(0,-.6), scale = 0.15)
    self.NameBoxText.reparentTo(self.Frame)
    self.Name = DirectEntry(pos=(-.6,0,-.8),scale=.08,width=10,text_scale=(1.5,1.5),rolloverSound=0,clickSound=0,cursorKeys=1)
    self.Name.reparentTo(self.Frame)
    self.PasswordBoxText = OnscreenText(text = "Password", pos=(0,-1), scale = 0.15)
    self.PasswordBoxText.reparentTo(self.Frame)
    self.Password = DirectEntry(pos=(-.6,0,-1.2),scale=.08,width=10,text_scale=(1.5,1.5),obscured=1,rolloverSound=0,clickSound=0,cursorKeys=1)
    self.Password.reparentTo(self.Frame)
    self.CreatNewUser = DirectButton(text = ("< Creat My New Account >"),rolloverSound=0,clickSound=0,pos=(0,0,-1.5),scale=.08,text_scale=(1.5,1.5),command=self.SendNewUserData)
    self.CreatNewUser.reparentTo(self.Frame)
    self.ExitGame = DirectButton(text = ("| Back |"),rolloverSound=0,clickSound=0,pos=(0,0,-1.7),scale=.08,text_scale=(1.5,1.5),command=self.GoToLogInMenu)
    self.ExitGame.reparentTo(self.Frame)


  ###############################################################################
  def GoToLogInMenu(self):
    self.CleanUp()
    self2.MakeLogInMenu()


  ###############################################################################
  def PlayerMusic(self, Race):
    if Race == "Humen":
      self2.AudioMgr.Play(2, self2.MainScreenMusic, 0, "b")


  ###############################################################################
  def NetCommands(self, data):
    if data[0] == "0":
      self2.PopUp("Nametaken")

    elif data[0] == "1":
      self2.PopUp("Message", "Congratulation, your account was made.\nPlease relogin to get started.")
      self.GoToLogInMenu()


  ###############################################################################
  #This sends the users name and pass to the server by adding a tag then sending it to the server. Again the tag is use by the server to tell what the client wants. In this case the client/user want it to creat a account for them.
  def SendNewUserData(self):
    UserName = self.Name.get().strip()
    PassWord = self.Password.get().strip()
    if UserName and PassWord:
      #Check make sure they're with in the limit size and letters/numbers
      NamePassWord = (UserName + PassWord).lower()
      if len(NamePassWord) <= 20:
        for f in NamePassWord:
          if f not in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            self2.PopUp("ShowError", "830, Sorry no special characters can be used.")
        else:
          #Send Name and Password to server
          self2.NetWorkSendFrame["TCP"].append("NU "+UserName+" "+PassWord)


  ###############################################################################
  def CleanUp(self):
    for x in [self.Frame, self.Background, self.Logo, self.TitleBoxText, self.NameBoxText, self.Name, self.PasswordBoxText, self.Password, self.CreatNewUser, self.ExitGame]:
      x.removeNode()




##############################################################################################
class MainMenu:
  def __init__(self, OML):
    global self2
    self2 = OML

    self2.UserWhere = "MainMenu"
    #Setup window
    self2.WindowProp.Settings(["Title Mradr's_Prodject", "SizeX 600", "SizeY 548", "FullScreen 0", "UserHasMouse 1"])

    #Start the menu music.
    self2.AudioMgr.Play(2, self2.MainScreenMusic, 0, "b")

    #Resetup the frame/grid and put the logon image back up.
    self.Frame = DirectFrame(frameSize=(1,1,0,1))
    self.Background = OnscreenImage(image = 'MainMenu/Images/Boarder.png',parent=render2d)
    #Setup the main menu screen.
    self.Logo = OnscreenImage(image = 'MainMenu/Images/Logo.jpg',pos = (.6,0,.5),parent=render2d,scale = (.3,.3,.3))
    self.GameButton = DirectButton(text = ("Game"),rolloverSound=0,clickSound=0,pos=(-.89,0,.6),scale=.08,text_scale=(1.5,1.5),command=self.SetUpScreen,extraArgs=["Game"])
    self.GameButton.reparentTo(self.Frame)
    self.ChatButton = DirectButton(text = ("Chat"),rolloverSound=0,clickSound=0,pos=(-.93,0,.45),scale=.08,text_scale=(1.5,1.5),command=self.SetUpScreen,extraArgs=["ChatMenu"])
    self.ChatButton.reparentTo(self.Frame)
    self.InformationButton = DirectButton(text = ("Information"),rolloverSound=0,clickSound=0,pos=(.7,0,.1),scale=.08,text_scale=(1.5,1.5), command=self.SetUpScreen,extraArgs=["Information"])
    self.InformationButton.reparentTo(self.Frame)
    self.SettingsButton = DirectButton(text = ("Settings"),rolloverSound=0,clickSound=0,pos=(.71,0,-.05),scale=.08,text_scale=(1.5,1.5), command=self.SetUpScreen,extraArgs=["Settings"])
    self.SettingsButton.reparentTo(self.Frame)
    self.CheckFileButton = DirectButton(text = ("Check Files"),rolloverSound=0,clickSound=0,pos=(.71,0,-.21),scale=.08,text_scale=(1.35,1.35),command=self.CheckFileSystem)
    self.CheckFileButton.reparentTo(self.Frame)
    self.SwitchUsersButton = DirectButton(text = ("Switch Users"),rolloverSound=0,clickSound=0,pos=(-.3,0,-.91),scale=.08,text_scale=(1.35,1.35),command=self.SetUpScreen,extraArgs=["LogInMenu"])
    self.SwitchUsersButton.reparentTo(self.Frame)
    self.LogOutButton = DirectButton(text = ("LogOut"),rolloverSound=0,clickSound=0,pos=(.3,0,-.91),scale=.08,text_scale=(1.35,1.35),command=self2.EndGame)
    self.LogOutButton.reparentTo(self.Frame)


  ###############################################################################
  def NetCommands(self, data):
    if data[0] == "NM":
      print "OH WOW WE GOT MAIL!"


  ###############################################################################
  def CheckFileSystem(self):
    self2.CheckFileSystem()


  ###############################################################################
  def SetUpScreen(self, NameOfScreen):
    self.CleanUp()
    if NameOfScreen == "Game":
      self.MakeGameMenu()
    elif NameOfScreen == "ChatMenu":
      self.MakeChatMenu()
    elif NameOfScreen == "Information":
      self.MakeInformation()
    elif NameOfScreen == "Settings":
      self.MakeSettings()
    elif NameOfScreen == "LogInMenu":
      self2.NetWorkSendFrame["TCP"].append("LogOut\n")
      self.MakeLogInMenu()


  ###############################################################################
  def CleanUp(self):
    for x in [self.Frame, self.Background, self.Logo, self.GameButton, self.ChatButton, self.InformationButton, self.SettingsButton, self.CheckFileButton, self.SwitchUsersButton, self.LogOutButton]:
      x.removeNode()




##############################################################################################
class SelectGameMenu:
  def __init__(self, OML):
    global self2
    self2 = OML

    self.GameList = []
    for Game in os.listdir('Game'):
      print "Loading " + Game,
      try:
        self.GameList[Game] = getattr(__import__("Game."+Game+"."+Game, fromlist = [Game]), Game)(self2)
      except:
        print traceback.format_exception(*sys.exc_info())
      else:
        print "Done"

    self2.UserWhere = "SelectGameMenu"

    self.MyButtonScrolledList = DirectScrolledList(decButton_pos= (0.5, 0, 0), decButton_text = "/\\", decButton_text_scale = 0.08, decButton_borderWidth = (0.01, 0.01),
                                                   incButton_pos= (-0.5, 0, 0), incButton_text = "\/", incButton_text_scale = 0.08, incButton_borderWidth = (0.01, 0.01),
                                                   numItemsVisible = 10, forceHeight = .2, itemFrame_pos = (0, 0, .2))

    for x in self2.InstalledGames+["Back"]:
      self.MyButtonScrolledList.addItem(DirectButton(text = (x),rolloverSound=0,clickSound=0,pos=(0,0,0),scale=.08,text_scale=(1.5,1.5),command=self.SetUpScreen,extraArgs=[str(x)]))


  ###############################################################################
  def SetUpScreen(self, NameOf):
    self.CleanUp()
    if NameOf == "Back":
      self2.MakeMainMenu()
    else:
      self2.MakeGame(NameOf)


  ###############################################################################
  def CleanUp(self):
    self.MyButtonScrolledList.removeNode()



