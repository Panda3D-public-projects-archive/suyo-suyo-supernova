#Programer:       Travis Woolery
#Created:         2/2/2011
#updated:         2/2/2011
#License:         CC-BY, must keep programmers name, and code can't used in other commercial games.
#Doc:             Class AudioManger()
#                    Controls all audio plaied in program and sub programs
#                    Commands: Play, Stop, Pause, UnPause, Add, ClearList, Volume, Pitch




from direct.task.Task import Task
from direct.showbase import Audio3DManager


class AudioManger:
  MainScreenMusic = 0
  MenuSoundVal = 0
  SystemVal = 0
  GameMusicVal = 0
  GameSoundVal = 0

  def __init__(self):
    #Variables
    self.AudioData = {}
    self.DefaultSounds = {}
    self.DefaultSounds["ErrorBeep"] = 'MainMenu/Music/Sounds/Error/Error01.ogg'

    #3D Channel
    self.Audio3D = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)

    #System
    self.SystemAudioList = {}

    #Menu
    self.MenuAudioList = {}
    self.MenuAudioList["BackGround"] = loader.loadSfx(self.MainScreenMusic)

    #Game
    self.GameAudioList = {}
    self.GameAudioList["BackGround"] = loader.loadSfx(self.MainScreenMusic)
    self.InVoiceChat = loader.loadSfx(self.MainScreenMusic)
    self.OutVoiceChat = loader.loadSfx(self.MainScreenMusic)

    #Server
    self.ServerAudioList = {}
    self.ServerAudioList["BackGround"] = loader.loadSfx(self.MainScreenMusic)


  #Plays sounds and music base on channel. Channel 1 is system related, Channel 2 is Menu related, Channel 3 is "Game" related, and Channel 4 is Server related.
  #Type is what type of sound it is "b" = Game, and "s" = sound efffect.
  #Path is the sound locaton/path, and Loop 0 is to loop forever, and Loop 1 (default) and or great plays that many times.
  ###############################################################################
  def Play(self, Channel=1, Path='', Loop=1, Type='s'):
    if Channel not in [1,2,3,4] or not Path or Type not in ["s","b"]:
      print "Sorry, please fill out all required information needed, (*Channel(1-4), *Type('s', 'b'), *Path(path), LoopCount(0 or <1)"

    #System sounds
    elif Channel is 1:
      if Path in self.SystemAudioList:
        if self.SystemAudioList[Path].status() == 2:
          self.Stop(1, Path)
      else:
        if Path in self.DefaultSounds:
          self.SystemAudioList[Path] = loader.loadSfx(self.DefaultSounds[Path])
        else:
          self.SystemAudioList[Path] = loader.loadSfx(Path)
      self.SystemAudioList[Path].setVolume(float(self.SystemVal))
      self.SystemAudioList[Path].setLoopCount(Loop)
      self.SystemAudioList[Path].play()

    #Main menu
    elif Channel is 2:
      if Type is "b":
        if self.GameAudioList["BackGround"].status() == 2:
          self.Stop(3)
        if self.MenuAudioList["BackGround"].getName() != loader.loadSfx(Path).getName() or self.MenuAudioList["BackGround"].status() != 2:
          self.MenuAudioList["BackGround"].stop()
          self.MenuAudioList["BackGround"] = loader.loadSfx(Path)
          self.MenuAudioList["BackGround"].setVolume(float(self.MenuMusicVal))
          self.MenuAudioList["BackGround"].setLoopCount(Loop)
          self.MenuAudioList["BackGround"].play()
      else:
        if Path in self.MenuAudioList:
          if self.MenuAudioList[Path].status() == 2:
            self.Stop(1, Path)
        else:
          self.MenuAudioList[Path] = loader.loadSfx(Path)
        self.MenuAudioList[Path].setVolume(float(self.MenuSoundVal))
        self.MenuAudioList[Path].setLoopCount(Loop)
        self.MenuAudioList[Path].play()

    #Game
    elif Channel is 3:
      if Type is "b":
        if self.MenuAudioList["BackGround"].status() == 2:
          self.Stop(2)
        if self.GameAudioList["BackGround"].getName() != loader.loadSfx(self.GamePath+Path).getName() or self.GameAudioList["BackGround"].status() != 2:
          self.GameAudioList["BackGround"].stop()
          self.GameAudioList["BackGround"] = loader.loadSfx(self.GamePath+Path)
          self.GameAudioList["BackGround"].setVolume(float(self.GameMusicVal))
          self.GameAudioList["BackGround"].setLoopCount(Loop)
          self.GameAudioList["BackGround"].play()
      else:
        if Path in self.GameAudioList:
          if self.GameAudioList[Path].status() == 2:
            self.Stop(1, Path)
        else:
          self.GameAudioList[Path] = loader.loadSfx(self.GamePath+Path)
        self.GameAudioList[Path].setVolume(float(self.GameSoundVal))
        self.GameAudioList[Path].setLoopCount(Loop)
        self.GameAudioList[Path].play()

    #Other sounds effects
    elif Channel is 4:
      if Type is "b":
        if self.MenuAudioList["BackGround"].status() == 2:
          self.Stop(2)
        if self.GameAudioList["BackGround"].status() == 2:
          self.Stop(3)
        if self.ServerAudioList["BackGround"].getName() != loader.loadSfx(self.GamePath+Path).getName() or self.ServerAudioList["BackGround"].status() != 2:
          self.ServerAudioList["BackGround"].stop()
          self.ServerAudioList["BackGround"] = loader.loadSfx(self.GamePath+Path)
          self.ServerAudioList["BackGround"].setVolume(float(self.GameMusicVal))
          self.ServerAudioList["BackGround"].setLoopCount(Loop)
          self.ServerAudioList["BackGround"].play()
      else:
        if Path in self.ServerAudioList:
          if self.ServerAudioList[Path].status() == 2:
            self.Stop(4, Path)
        else:
          self.ServerAudioList[Path] = loader.loadSfx(Path)
        self.ServerAudioList[Path].setVolume(float(self.SystemVal))
        self.ServerAudioList[Path].setLoopCount(Loop)
        self.ServerAudioList[Path].play()


  ###############################################################################
  #Stops current playing audio channel("All") or Name
  def Stop(self, Channel=1, Name='All'):
    if Channel is 1:
      if Name in self.SystemAudioList:
        self.SystemAudioList[Name].stop()
      elif Name is "All":
        for name in self.SystemAudioList:
          self.SystemAudioList[name].stop()

    if Channel is 2:
      if Name in self.MenuAudioList:
        self.MenuAudioList[Name].stop()
      elif Name is "All":
        for name in self.MenuAudioList:
          self.MenuAudioList[name].stop()

    elif Channel is 3:
      if Name in self.GameAudioList:
        self.GameAudioList[Name].stop()
      elif Name is "All":
        for name in self.GameAudioList:
          self.GameAudioList[name].stop()

    elif Channel == 4:
      if Name in self.ServerAudioList:
        self.ServerAudioList[Name].stop()
      elif Name is "All":
        for name in self.ServerAudioList:
          self.ServerAudioList[name].stop()


  ###############################################################################
  #Pause the Channel or Name
  def Pause(self, Channel=1, Name=''):
    #Check Channel then Name then store their current time and loop count
    if Channel is 1:
      if Name in self.SystemAudioList:
        self.AudioData[Name] = {"PauseTime":self.SystemAudioList[Name].getTime(), "Loop":self.SystemAudioList[Name].getLoopCount()}
        self.SystemAudioList[Name].stop()
      elif not Name:
        for Name in self.SystemAudioList:
          self.AudioData[Name] = {"PauseTime":self.SystemAudioList[Name].getTime(), "Loop":self.SystemAudioList[Name].getLoopCount()}
          self.SystemAudioList[Name].stop()

    elif Channel is 2:
      if Name in self.MenuAudioList:
        self.AudioData[Name] = {"PauseTime":self.MenuAudioList[Name].getTime(), "Loop":self.MenuAudioList[Name].getLoopCount()}
        self.MenuAudioList[Name].stop()
      elif not Name:
        for Name in self.MenuAudioList:
          self.AudioData[Name] = {"PauseTime":self.MenuAudioList[Name].getTime(), "Loop":self.MenuAudioList[Name].getLoopCount()}
          self.MenuAudioList[Name].stop()

    elif Channel is 3:
      if Name in self.GameAudioList:
        self.AudioData[Name] = {"PauseTime":self.GameAudioList[Name].getTime(), "Loop":self.GameAudioList[Name].getLoopCount()}
        self.GameAudioList[Name].stop()
      elif not Name:
        for Name in self.ServerAudioList:
          self.AudioData[Name] = {"PauseTime":self.GameAudioList[Name].getTime(), "Loop":self.GameAudioList[Name].getLoopCount()}
          self.GameAudioList[Name].stop()

    elif Channel is 4:
      if Name in self.ServerAudioList:
        self.AudioData[Name] = {"PauseTime":self.ServerAudioList[Name].getTime(), "Loop":self.ServerAudioList[Name].getLoopCount()}
        self.ServerAudioList[Name].stop()
      elif not Name:
        for Name in self.ServerAudioList:
          self.AudioData[Name] = {"PauseTime":self.ServerAudioList[Name].getTime(), "Loop":self.ServerAudioList[Name].getLoopCount()}
          self.ServerAudioList[Name].stop()


  ###############################################################################
  #UnPuase Channel or Name
  def UnPause(self, Channel=1, Name=''):
    #Check Channel then Name then reset them back their time and loop count
    if Channel is 1:
      if Name in self.SystemAudioList:
        self.SystemAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
        self.SystemAudioList[Name].setVolume(float(self.SystemVal))
        self.SystemAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
        self.SystemAudioList[Name].play()
      elif not Name:
        for Name in self.SystemAudioList:
          self.SystemAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
          self.SystemAudioList[Name].setVolume(float(self.SystemVal))
          self.SystemAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
          self.SystemAudioList[Name].play()

    elif Channel is 2:
      if self.GameAudioList["BackGround"].status() == 2:
        self.GameAudioList["BackGround"].Stop(3)
      if Name in self.SystemAudioList:
        self.MenuAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
        self.MenuAudioList[Name].setVolume(float(self.MenuMusicVal))
        self.MenuAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
        self.MenuAudioList[Name].play()
      elif not Name:
        for Name in self.SystemAudioList:
          self.MenuAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
          self.MenuAudioList[Name].setVolume(float(self.MenuSoundVal))
          self.MenuAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
          self.MenuAudioList[Name].play()

    elif Channel is 3:
      if self.MenuAudioList["BackGround"].status() == 2:
        self.MenuAudioList["BackGround"].Stop(2)
      if Name in self.GameAudioList:
        self.GameAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
        self.GameAudioList[Name].setVolume(float(self.GameMusicVal))
        self.GameAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
        self.GameAudioList[Name].play()
      elif not Name:
        for Name in self.GameAudioList:
          self.GameAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
          self.GameAudioList[Name].setVolume(float(self.GameSoundVal))
          self.GameAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
          self.GameAudioList[Name].play()

    elif Channel == 4:
      if Name in self.ServerAudioList:
        self.ServerAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
        self.ServerAudioList[Name].setVolume(float(self.GameSoundVal))
        self.ServerAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
        self.ServerAudioList[Name].play()
      elif not Name:
        for Name in self.ServerAudioList:
          self.ServerAudioList[Name].setTime(self.AudioData[Name]["PauseTime"])
          self.ServerAudioList[Name].setVolume(float(self.GameSoundVal))
          self.ServerAudioList[Name].setLoopCount(self.AudioData[Name]["Loop"])
          self.ServerAudioList[Name].play()


  ###############################################################################
  #Add music to a list to be played
  def Add(self, Channel=1, List=''):
    if Channel is 1:
      for x in List:
        self.SystemAudioList[x] = loader.loadSfx(x)

    elif Channel is 2:
      for x in List:
        self.MenuAudioList[x] = loader.loadSfx(x)

    elif Channel is 3:
      for x in List:
        self.GameList[x] = loader.loadSfx(x)

    elif Channel is 4:
      for x in List:
        self.ServerAudioList[x] = loader.loadSfx(x)


  ###############################################################################
  #Clear a list of music to be played
  def ClearList(self, Channel=1):
    if Channel is 1:
      self.SystemAudioList = {}

    elif Channel is 2:
      self.MenuAudioList = {}

    elif Channel is 3:
      self.GameList = {}

    elif Channel is 4:
      self.ServerAudioList = {}

    else:
      self.MenuAudioList = {}
      self.SystemAudioList = {}
      self.ServerAudioList = {}


  ###############################################################################
  #Sets the volume of select channel or song
  def Volume(self, Channel=1, Volume=0, Type="s", Name=""):
    if Channel is 1:
      if Name.strip():
        if Name in self.SystemAudioList:
          self.SystemAudioList[Name].setVolume(float(Volume))
      else:
        self.SystemVal = Volume
        for Name in self.SystemAudioList:
          self.SystemAudioList[Name].setVolume(float(self.SystemVal))

    elif Channel is 2:
      if Name.strip():
        if Name in self.MenuAudioList:
          self.MenuAudioList[Name].setVolume(float(Volume))
      else:
        if Type == "s":
          self.MenuSoundVal = Volume
        elif Type == "b":
          self.MenuMusicVal = Volume

        for Name in self.MenuAudioList:
          if Name is "BackGround":
            self.MenuAudioList[Name].setVolume(float(self.MenuMusicVal))
          else:
            self.MenuAudioList[Name].setVolume(float(self.MenuSoundVal))

    elif Channel is 3:
      if Name.strip():
        if Name in self.GameAudioList:
          self.GameAudioList[Name].setVolume(float(Volume))
      else:
        if Type == "s":
          self.GameSoundVal = Volume
        elif Type == "b":
          self.GameMusicVal = Volume

        for Name in self.GameAudioList:
          if Name is "BackGround":
            self.GameAudioList[Name].setVolume(float(self.GameMusicVal))
          else:
            self.GameAudioList[Name].setVolume(float(self.GameSoundVal))

    elif Channel is 4:
      if Name.strip():
        if Name in self.ServerAudioList:
          self.ServerAudioList[Name].setVolume(float(Volume))
      else:
        if Type is "s":
          self.GameSoundVal = Volume
        elif Type is "b":
          self.GameMusicVal = Volume

        for Name in self.ServerAudioList:
          if Name is "BackGround":
            self.ServerAudioList[Name].setVolume(float(self.GameMusicVal))
          else:
            self.ServerAudioList[Name].setVolume(float(self.GameSoundVal))


  ###############################################################################
  #Sets the pitch of selected channel or song
  def Pitch(self):
    pass


  ###############################################################################
  #Main task to play listed music
  def Main(self):
    for x in self.MenuAudioList:
      pass

    for x in self.SystemAudioList:
      pass

    for x in self.GameList:
      pass