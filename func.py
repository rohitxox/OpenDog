import os
import time
from adafruit_servokit import ServoKit
import concurrent.futures


# dont touch or modify  here----------------------------------------------------------------------------
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
# elbow
kit = ServoKit(channels=16)

from dynamixel_sdk import *

MY_DXL = 'X_SERIES'
# Control table address
if MY_DXL == 'X_SERIES':
    add_torque = 64
    add_goal_pos = 116
    add_present_pos = 132
    baud = 1000000
    velocity_mode = 104
    shutdown = 63
protocol = 2.0
com = '/dev/ttyUSB0'
torque_E = 1  # Value for enabling the torque
torque_D = 0  # Value for disabling the torque
threshold = 15  # Dynamixel moving status threshold
move_for = 250  # max 250 min 44
move_back = -250
velocity_stop = 0
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
# till here----------------------------------------------------------------------------------------

# Motor ID
leg1_ID = [1, 11, 12, 13, 14]
leg2_ID = [2, 21, 22, 23, 24]
leg3_ID = [3, 31, 32, 33, 34]
leg4_ID = [4, 41, 42, 43, 44]


# motor control start from here.
def motor(ID, POS):
    dxl = packetHandler.write4ByteTxRx(portHandler, ID, add_goal_pos, POS)


def torque_en(ID):
    packetHandler.write1ByteTxRx(portHandler, ID, add_torque, torque_E)


def torque_dis(ID):
    packetHandler.write1ByteTxRx(portHandler, ID, add_torque, torque_D)


def wheel_velocity(ID, control):
    packetHandler.write4ByteTxRx(portHandler, ID, velocity_mode, control)


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
        motor(11, 2416)
        motor(12, 2025)
        #
        motor(21, 2416)
        motor(22, 2025)
        #
        motor(31, 2416)
        motor(32, 2025)
        #
        motor(41, 2416)
        motor(42, 2025)

    def down(self):
        motor(11, 2694)
        motor(12, 1339)
        #
        motor(21, 2694)
        motor(22, 1339)
        #
        motor(31, 2694)
        motor(32, 1339)
        #
        motor(41, 2694)
        motor(42, 1339)

    def leg_seq(self):
        # start
        # leg1
        motor(11, 2450)
        motor(12, 2075)
        # leg3
        motor(31, 1966)
        motor(32, 2455)
        # leg2
        motor(21, 1966)
        motor(22, 2455)
        # leg4
        motor(41, 2450)  # mirror of first leg1
        motor(42, 2075)
        time.sleep(0.6)
        # alter
        # leg1
        motor(11, 2090)
        motor(12, 2400)
        # leg3
        motor(31, 2641)
        motor(32, 2075)
        # leg2
        motor(21, 2641)
        motor(22, 2100)
        # leg4#mirror of alter first leg1
        motor(41, 2090)
        motor(42, 2400)
        time.sleep(0.6)

    def elbow(self):
        kit.servo[1].angle = 17
        kit.servo[2].angle = 14
        kit.servo[3].angle = 13
        kit.servo[4].angle = 14

    def vel_move_forward(self):
        wheel_velocity(14, move_for)
        wheel_velocity(24, move_for)
        wheel_velocity(34, move_for)
        wheel_velocity(44, move_for)

    def vel_move_backward(self):
        wheel_velocity(14, move_back)
        wheel_velocity(24, move_back)
        wheel_velocity(34, move_back)
        wheel_velocity(44, move_back)

    def velocity_stop_mode(self):
        wheel_velocity(14, velocity_stop)
        wheel_velocity(24, velocity_stop)
        wheel_velocity(34, velocity_stop)
        wheel_velocity(44, velocity_stop)


    def path(self):
        speed = 44 #rev/min
        distance = speed* time


    def sleep_now(self):
        print("sleeping now")
        disable_motor()
        return "done sleeping"
# main func----------------------------------------------------------------------------------------
command = ''
started = False
stopped = False
start = Motion()
num = 10
# count = 5

while True:
    command = input('->').lower()
    if command == 'stand':
        if started:
            started = True
            print('already robot is standing')
        else:
            print('Robot now standing...!')
            start.enable_motor()
            start.elbow()
            time.sleep(0.5)
            start.stand()

    elif command == 'down':
        if stopped:
            stopped = True
            print("it is down")
        else:
            print("Robot now laying down...!")
            start.down()
            time.sleep(2)
            start.disable_motor()

    elif command == 'walk':
        speed = 44  # rev/min
        distance = speed * time
        count = time
        count = int(input("How far the Robot has to go..? :").lower())
        while count > 0:
            start.leg_seq()
            count -= 1
            result = time.perf_counter()
            start.stand()
        else:
            print(f"distance travelled {disatnce()}")

    elif command == 'for':
        start.vel_move_forward()
    elif command == 'stop':
        start.velocity_stop_mode()
    elif command == 'back':
        start.vel_move_backward()
    elif command == 'q':
        break
    elif command == 'help':
        print("""
These are the command's to control the Robot:
To stand up   -stand
To sit down   -down
walk forward  -walk
move forward  -for
move backward -back
stop motion   -stop
quit          -q

""")
    elif command == "sleep":
            with concurrent.futures.ProcessPoolExecutor() as step:
                if __name__ == '__main__':
                    seq1 = step.submit(sleep_now())
                    #seq2 = step.submit(())
                    print(seq1.result())
    else:
        print("i did't understand that")

finished = time.perf_counter()
print("done",finished)
# Close port
portHandler.closePort()




