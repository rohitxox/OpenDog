import os
import time
from adafruit_servokit import ServoKit

#dont change from here
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
threshold = 10    # Dynamixel moving status threshold
portHandler = PortHandler(com)
packetHandler = PacketHandler(protocol)
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(baud):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()
#till here

#Motor ID
#leg1
L1motor1 = 11;
L1motor2 = 12;
L1motor3 = 13;
L1motor4 = 14;
#leg2
L2motor1 = 21;
L2motor2 = 22;
L2motor3 = 23;
L2motor4 = 24;
#leg3
L3motor1 = 31;
L3motor2 = 32;
L3motor3 = 33;
L3motor4 = 34;
#leg4
L4motor1 = 41;
L4motor2 = 42;
L4motor3 = 43;
L4motor4 = 44;
#motor control start from here.
    
def enable_motor():    
    packetHandler.write1ByteTxRx(portHandler, L1motor1 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L1motor2 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L1motor3 , add_torque, torque_E)

    packetHandler.write1ByteTxRx(portHandler, L2motor1 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L2motor2 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L2motor3 , add_torque, torque_E)
    
    packetHandler.write1ByteTxRx(portHandler, L3motor1 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L3motor2 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L3motor3 , add_torque, torque_E)
    
    packetHandler.write1ByteTxRx(portHandler, L4motor1 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L4motor2 , add_torque, torque_E)
    packetHandler.write1ByteTxRx(portHandler, L4motor3 , add_torque, torque_E)

def disable_motor():
    packetHandler.write1ByteTxRx(portHandler, L1motor1, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L1motor2, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L1motor3, add_torque, torque_D)
    
    packetHandler.write1ByteTxRx(portHandler, L2motor1, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L2motor2, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L2motor3, add_torque, torque_D)
    
    packetHandler.write1ByteTxRx(portHandler, L3motor1, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L3motor2, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L3motor3, add_torque, torque_D)
    
    packetHandler.write1ByteTxRx(portHandler, L4motor1, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L4motor2, add_torque, torque_D)
    packetHandler.write1ByteTxRx(portHandler, L4motor3, add_torque, torque_D)
    

def motor(ID, POS):
    dxl = packetHandler.write4ByteTxRx(portHandler, ID,add_goal_pos,POS)



def stand():
    motor(11,1629)
    motor(12,2000)
    #
    motor(21,1629)
    motor(22,2000)
    #
    motor(31,1629)
    motor(32,2000)
    #
    motor(41,1629)
    motor(42,2000)




def walk():
    enable_motor()
    #stand()
    time.sleep(1)
  #from here make a creep gait
    motor(11,1634)
    motor(12,1992)
    motor(11,2122)
    motor(12,2290)
    motor(11,1506)
    time.sleep(0.5)
    #
    motor(41,1634)
    motor(42,1992)
    motor(41,2122)
    motor(42,2290)
    motor(41,1506)
    time.sleep(0.5)
    #
    motor(21,2260)
    motor(22,2290)
    motor(21,1416)
    #
    time.sleep(0.5)
    motor(31,1900)
    motor(32,2260)
    motor(31,1400)
    motor(32,2000)
    time.sleep(0.5)
    
    
    
    
    
    
    
    
stand()
    
while True:
    command = input('->').lower()
    if command == "i":
        while True:
            stand()
            walk()
    elif command == "q":
        break
    if command == "s":
        stand()



# Close port
portHandler.closePort()



