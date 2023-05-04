#!/usr/bin python3
'''
Checklist:
Square: Done
Dance: Done
Move to wall: Done
Safe to dance: Done
Check which side is shorter: Need to do
'''
from teacher import PiggyParent
import sys
import time
from random import randint, choice

times = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
safeArray = []
evalDict = {}
leftArray = []
rightArray = []
goAngle = 0

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1575  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "a": ("safeToDance", self.safe_to_dance),
                "u": ("Square", self.square),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "i" :("Ian", self.ian),
                "z" :("Scan", self.scan),
                "m" :("moveToWall", self.moveToWall),
                #"e" :("evalSide", self.evalSide),
                "b" :("betterES", self.betterES),
                "p" :("pain", self.pain)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    def ian(self):
      print("Here is a first line")
      print("Bosnia is so based")
      self.fwd()
      time.sleep(2)
      self.stop()
      
      self.right()
      time.sleep(2)
      self.stop()

    def square(self):
      for x in range(4):
        self.fwd()
        time.sleep(0.95)
        self.stop()
        
        self.right()
        time.sleep(0.95)
        self.stop()
      
    def dance(self):
      # TODO: check to see if it's safe before dancing
      self.left()
      time.sleep(choice(times))
      self.stop()
      self.fwd()
      time.sleep(choice(times))
      self.stop()
      for i in range(randint(1, 3)):
        self.right()
        time.sleep(choice(times))
        self.stop()
        self.left()
        time.sleep(choice(times))
        self.stop()
      self.fwd()         
      time.sleep(0.5)
      self.stop()

    def safe_to_dance(self):
      for i in range(10):
        self.turn_by_deg(36)
        if (self.read_distance() < 100):
          safeArray.append("unsafe")
      if (len(safeArray) != 0):
        print("It is not safe to dance")
      elif (len(safeArray) == 0):
        self.dance()
        print(safeArray)
      safeArray.clear()
        
    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()
    
    def moveToWall(self):
      while True:
        if (self.read_distance() > 40):
          self.fwd()
        elif (self.read_distance() < 40):
          self.stop()
          self.turn_by_deg(180)

    def pain(self):
      while True:
        self.fwd()
        if (self.read_distance < 50):
          self.stop()
          self.turn_by_deg(90)
          self.servo(2000)
          self.fwd()
          if (self.read_distance() > 100):
            self.stop()
            self.servo(1575)
            self.turn_by_deg(-90)
            
    """
    def evalSide(self):
      #fix while true?
      while True:
        self.fwd()
        if (self.read_distance() < 100):
          self.stop()
          self.servo(1000)
          for i in range(100):
            self.servo(1000 + 10 * i)
            #THIS THIS PART IS WRONG v
            if (self.read_distance() < 70):
              if (1000 + (10 * i) > 1500):
                leftArray.append(2000 - (1000 + (10 * i)))
              elif (1000 + (10 * i) < 1500):
                rightArray.append((10 * i))
          self.servo(1575)
          leftArray.sort()
          rightArray.sort()
          if (len(leftArray) != 0):
            evalDict["left"] = leftArray[0]
          if (len(rightArray) != 0):
            evalDict["right"] = rightArray[0]
          if (evalDict.get("right") > evalDict.get("left")):
            self.left(90)
            self.fwd()
            self.sleep(1)
            self.stop()
            self.left(-90)
          elif (evalDict.get("left") > evalDict.get("right")):
            self.right(90)
            self.fwd()
            self.sleep(1)
            self.stop()
            self.right(-90)
          leftArray.clear()
          rightArray.clear()
          evalDict.clear()
          """
        #Empty evalDict
    #IN THE PROCESS OF BES
    def betterES(self):
      while True:
        self.fwd()
        if (self.read_distance() < 50):
          self.servo(1000)
          evalDict["right"] = self.read_distance()
          self.servo(2000)
          evalDict["left"] = self.read_distance()
          if (evalDict["right"] > evalDict["left"]):
            #left
            self.turn_by_deg(90)
            self.fwd()
  
    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
      """Sweep the servo and populate the scan_data dictionary"""
      for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 10):
        self.servo(angle)
        self.scan_data[angle] = self.read_distance()
      print(self.scan_data)
      print(len(self.scan_data))

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
