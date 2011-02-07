#Programer:       Travis Woolery
#Data:            2/1/2011
#LastUpdate:      2/1/2011
#License:         CC-BY, must keep programmers name, and code can't used in other commercial games.
#Doc:             Default weapon class for any weapon.


#Reparent: Where the object should be reparent to. Default render
#Prop: Used to place in the object into the world(1) or player(0). Default 1
#Pos: Places the object at giving location. Default is (0,0,0,0,0,0)


from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import *


class ObjectName:
  def __init__(self, ReparentTo=render, Prop=0, PosHpr=(0,0,0,0,0,0)):
    self.Object = loader.loadModel("WeaponPath")
    #self.Object = Actor("models/panda-model", {"walk": "models/panda-walk4"}) Use this line if they have animations.
    self.Object.flattenStrong()
    self.ObjectSounds = {"TakeOut":[], "PutUp":[], "Attack":[], "Swing":[], "Aim":[], "Shoot":[]}
    #self.ObjectAnimations = {"TakeOut":[], "PutUp":[], "Attack":[], "Swing":[], "Aim":[], "Shoot":[]} Add this line into the DataList if it has any: , "Animation":self.ObjectAnimations
    self.DataList = {"Name":"Mrifle", "Object":self.Object, "Sound":self.ObjectSounds, "DefaultRange":3, "DefaultSpeed":.3, "CurrentSpeed":.3}
    #If animations, use self.Object.loop("animation name") here
    if Prop:
      self.Object.reparentTo(ReparentTo)
      self.Object.setScale(0.015,0.015,0.015)
      self.Object.setPosHpr(PosHpr)

    else:
      self.Object.reparentTo(Reparent)
      self.Object.setScale(0.0055,0.0055,0.0055)



  #----------------------------------------------
  #If called, return the object.
  def __call__(self):
    return self.Object


  #----------------------------------------------
  #Returns information about the object.
  def Data(self, What, Value=""):
    if What in self.DataList:
      if len(Value):
        self.DataList[What] = Value
      else:
        return self.DataList[What]


  #----------------------------------------------
  #Use the object.
  def Use(self):
    #play animation self.Object.play("animation name")
    pass


  #----------------------------------------------
  #Clean up the object.
  def CleanUp(self):
    self.Object.removeNode()
    return None