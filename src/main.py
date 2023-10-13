#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
mBottomLeft = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
mBottomRight = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
mTopLeft = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
mTopRight = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
controller_1 = Controller(PRIMARY)
Gyroscope = Inertial(Ports.PORT19)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:
#	Author:
#	Created:
#	Configuration:
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

def pre_autonomous():
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here
    def RightSide():
        mBottomLeft.set_velocity(100, PERCENT)
        mBottomRight.set_velocity(100,PERCENT)
        mTopLeft.set_velocity(100, PERCENT)
        mTopRight.set_velocity(100, PERCENT)
        mBottomLeft.set_stopping(BRAKE)
        mBottomRight.set_stopping(BRAKE)
        mTopLeft.set_stopping(BRAKE)
        mTopRight.set_stopping(BRAKE)
        Gyroscope.set_heading(1, DEGREES)
        mBottomLeft.spin(REVERSE)
        mBottomRight.spin(FORWARD)
        mTopLeft.spin(FORWARD)
        mTopRight.spin(REVERSE)
        wait(1, SECONDS)
        mBottomLeft.stop()
        mBottomRight.stop()
        mTopLeft.stop()
        mTopRight.stop()
        wait(1, SECONDS)
        mBottomLeft.spin(FORWARD)
        mBottomRight.spin(REVERSE)
        mTopLeft.spin(REVERSE)
        mTopRight.spin(FORWARD)
        wait(2, SECONDS)
        mBottomLeft.stop()
        mBottomRight.stop()
        mTopLeft.stop()
        mTopRight.stop()
        wait(1, SECONDS)
        mBottomLeft.spin(REVERSE)
        mBottomRight.spin(FORWARD)
        mTopLeft.spin(FORWARD)
        mTopRight.spin(REVERSE)
        wait(1, SECONDS)
        mBottomLeft.stop()
        mBottomRight.stop()
        mTopLeft.stop()
        mTopRight.stop()

        





        


    RightSide()
        

def user_control():
    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:
        mBottomLeft.set_stopping(HOLD)
        mBottomRight.set_stopping(HOLD)
        mTopLeft.set_stopping(HOLD)
        mTopRight.set_stopping(HOLD)
        mBottomLeft.set_velocity(controller_1.axis3.position()-controller_1.axis4.position()-controller_1.axis1.position(),PERCENT)
        mBottomRight.set_velocity(controller_1.axis3.position()+controller_1.axis4.position()-controller_1.axis1.position(),PERCENT)
        mTopLeft.set_velocity(controller_1.axis3.position()+controller_1.axis4.position()+controller_1.axis1.position(),PERCENT)
        mTopRight.set_velocity(controller_1.axis3.position()-controller_1.axis4.position()+controller_1.axis1.position(),PERCENT)
        mBottomLeft.spin(FORWARD);
        mBottomRight.spin(FORWARD);
        mTopLeft.spin(FORWARD)
        mTopRight.spin(FORWARD)

# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()
