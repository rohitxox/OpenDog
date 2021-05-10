import os
import time
from adafruit_servokit import ServoKit

#dont touch or modify  here----------------------------------------------------------------------------
if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
#elbow
kit = ServoKit(channels=16)

from dynamixel_sdk import * 
MY_DXL = 'X_SERIES'     
# Control table address
if MY_DXL == 'X_SERIES':
    add_torque            = 64
    add_goal_pos          = 116
    add_present_pos       = 132    
    baud                  = 1000000
protocol  = 2.0
com                  = '/dev/ttyUSB0'
torque_E  = 1     # Value for enabling the torque
torque_D  = 0     # Value for disabling the torque
threshold = 5    # Dynamixel moving status threshold
portHandler = PortHandler(com)
packetHandler = PacketHandler(protocol)
# Open port
if portHandler.openPort():
    print("Connecting to Robot")
else:
    print("Failed to connect Robot")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(baud):
    print("Connected....!")
else:
    print("Failed to Sync")
    print("Press any key to terminate...")
    getch()
    quit()
#till here----------------------------------------------------------------------------------------

#Motor ID
leg1_ID = [1, 11, 12, 13, 14]
leg2_ID = [2, 21, 22, 23, 24]
leg3_ID = [3, 31, 32, 33, 34]
leg4_ID = [4, 41, 42, 43, 44]
#motor control start from here.
def motor(ID, POS):
    dxl = packetHandler.write4ByteTxRx(portHandler, ID,add_goal_pos,POS)
  
  
def torque_en(ID):
    packetHandler.write1ByteTxRx(portHandler, ID , add_torque, torque_E)


def torque_dis(ID):
    packetHandler.write1ByteTxRx(portHandler, ID, add_torque, torque_D)
    

class Motion:
    def enable_motor(self):    
        torque_en(11)
        torque_en(12)
        torque_en(13)
        torque_en(14)
        #
        torque_en(21)
        torque_en(22)
        torque_en(23)
        torque_en(24)
        #
        torque_en(31)
        torque_en(32)
        torque_en(33)
        torque_en(34)
        #
        torque_en(41)
        torque_en(42)
        torque_en(43)
        torque_en(44)
        
        
    def disable_motor(self):
        torque_dis(11)
        torque_dis(12)
        torque_dis(13)
        torque_dis(14)
        #
        torque_dis(21)
        torque_dis(22)
        torque_dis(23)
        torque_dis(24)
        #
        torque_dis(31)
        torque_dis(32)
        torque_dis(33)
        torque_dis(34)
        #
        torque_dis(41)
        torque_dis(42)
        torque_dis(43)
        torque_dis(44)


    def stand(self):
        motor(11,1629)
        motor(12,2000)
        #
        motor(21,1629)
        motor(22,2000)
        #
        motor(31,1629)
        motor(32,2100)
        #5
        motor(41,1629)
        motor(42,2100)


    def down(self):
        time.sleep(1)
        motor(12,1279)
        motor(22,1279)
        motor(32,1279)
        motor(42,1279)
        time.sleep(0.1)
        motor(31,1400)
        motor(41,1400)
        motor(11,1400)
        motor(21,1400)


    def elbow(self):
        kit.servo[1].angle = 14
        kit.servo[2].angle = 14
        kit.servo[3].angle = 13
        kit.servo[4].angle = 14



    
#main func----------------------------------------------------------------------------------------
command = ''
started = False
stopped = False
start = Motion()
while True:
    command = input('->').lower()
    if command == 'stand':
        if started:
            started = True
            print('already robot is standing')
            
        else:
            print('Robot now standing')
            start.enable_motor()
            start.elbow()
            time.sleep(1)
            start.stand()
    elif command == 'down':
        if stopped:
            stopped = True
            print("it is down")
                 
        else:
            start.down()
            time.sleep(2)
            start.disable_motor()
    
    elif command == 'walk':
        walk()
 
    elif command == 'quit':
        break
    else:
        print("i did't understand that")
    

# Close port
portHandler.closePort()




