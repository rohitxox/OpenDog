#include <Dynamixel2Arduino.h>
#define BOARD_BUTTON_PIN        23  


#if defined(ARDUINO_OpenCM904) // When using official ROBOTIS board with DXL circuit.
  #define DXL_SERIAL   Serial3 //OpenCM9.04 EXP Board's DXL port Serial. (Serial1 for the DXL port on the OpenCM 9.04 board)
  #define DEBUG_SERIAL Serial
  const uint8_t DXL_DIR_PIN = 22; //OpenCM9.04 EXP Board's DIR PIN. (28 for the DXL port on the OpenCM 9.04 board)

#endif
 
//leg1
const uint8_t L1motor1 = 11;
const uint8_t L1motor2 = 12;
const uint8_t L1motor3 = 13;
const uint8_t L1motor4 = 14;
//leg2
const uint8_t L2motor1 = 21;
const uint8_t L2motor2 = 22;
const uint8_t L2motor3 = 23;
const uint8_t L2motor4 = 24;
//leg3
const uint8_t L3motor1 = 31;
const uint8_t L3motor2 = 32;
const uint8_t L3motor3 = 33;
const uint8_t L3motor4 = 34;
//leg4
const uint8_t L4motor1 = 41;
const uint8_t L4motor2 = 42;
const uint8_t L4motor3 = 43;
const uint8_t L4motor4 = 44;


Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;

void setup() {
  
  pinMode(BOARD_BUTTON_PIN, INPUT_PULLDOWN);
  DEBUG_SERIAL.begin(115200);
  dxl.begin(1000000);
  dxl.setPortProtocolVersion(2);
  
  //////////////////////////////leg1
  //moto1
  dxl.ping(L1motor1);
  dxl.torqueOff(L1motor1);
  dxl.setOperatingMode(L1motor1, OP_POSITION);
  dxl.torqueOn(L1motor1);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor2
  dxl.ping(L1motor2);
  dxl.torqueOff(L1motor2);
  dxl.setOperatingMode(L1motor2, OP_POSITION);
  dxl.torqueOn(L1motor2);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor3
  dxl.ping(L1motor3);
  dxl.torqueOff(L1motor3);
  dxl.setOperatingMode(L1motor3, OP_POSITION);
  dxl.torqueOn(L1motor3);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //wheelmotor4
  dxl.ping(L1motor4);
  dxl.torqueOff(L1motor4);
  dxl.setOperatingMode(L1motor4, OP_VELOCITY);
  dxl.torqueOn(L1motor4);
/////////////////////////////////
  //////////////////leg2
  //motor1
  dxl.ping(L2motor1);
  dxl.torqueOff(L2motor1);
  dxl.setOperatingMode(L2motor1, OP_POSITION);
  dxl.torqueOn(L2motor1);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor2
  dxl.ping(L2motor2);
  dxl.torqueOff(L2motor2);
  dxl.setOperatingMode(L2motor2, OP_POSITION);
  dxl.torqueOn(L2motor2);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor3
  dxl.ping(L2motor3);
  dxl.torqueOff(L2motor3);
  dxl.setOperatingMode(L2motor3, OP_POSITION);
  dxl.torqueOn(L2motor3);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //wheelmotor4
  dxl.ping(L2motor4);
  dxl.torqueOff(L2motor4);
  dxl.setOperatingMode(L2motor4, OP_VELOCITY);
  dxl.torqueOn(L2motor4);
  ///////////----------------------//////////////////////
    //////////////////////////////leg3
  //moto1
  dxl.ping(L3motor1);
  dxl.torqueOff(L3motor1);
  dxl.setOperatingMode(L3motor1, OP_POSITION);
  dxl.torqueOn(L3motor1);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor2
  dxl.ping(L3motor2);
  dxl.torqueOff(L3motor2);
  dxl.setOperatingMode(L3motor2, OP_POSITION);
  dxl.torqueOn(L3motor2);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor3
  dxl.ping(L3motor3);
  dxl.torqueOff(L3motor3);
  dxl.setOperatingMode(L3motor3, OP_POSITION);
  dxl.torqueOn(L3motor3);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //wheelmotor4
  dxl.ping(L3motor4);
  dxl.torqueOff(L3motor4);
  dxl.setOperatingMode(L3motor4, OP_VELOCITY);
  dxl.torqueOn(L3motor4);
/////////////////////////////////
  //////////////////leg4
  //motor1
  dxl.ping(L4motor1);
  dxl.torqueOff(L4motor1);
  dxl.setOperatingMode(L4motor1, OP_POSITION);
  dxl.torqueOn(L4motor1);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor2
  dxl.ping(L4motor2);
  dxl.torqueOff(L4motor2);
  dxl.setOperatingMode(L4motor2, OP_POSITION);
  dxl.torqueOn(L4motor2);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //motor3
  dxl.ping(L4motor3);
  dxl.torqueOff(L4motor3);
  dxl.setOperatingMode(L4motor3, OP_POSITION);
  dxl.torqueOn(L4motor3);
  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  //dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

  //wheelmotor4
  dxl.ping(L4motor4);
  dxl.torqueOff(L4motor4);
  dxl.setOperatingMode(L4motor4, OP_VELOCITY);
  dxl.torqueOn(L4motor4);
///////////////to run code for once.
  stand();
  delay(1000);
  //walk();
  //wheel();

  
  
}
///////////////////////////////end of config
void stand(){
  dxl.setGoalPosition(L1motor1, 137, UNIT_DEGREE);
  dxl.setGoalPosition(L1motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L1motor3, 180, UNIT_DEGREE);
  //
  dxl.setGoalPosition(L2motor1, 137, UNIT_DEGREE);
  dxl.setGoalPosition(L2motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L2motor3, 180, UNIT_DEGREE);
  //
  dxl.setGoalPosition(L3motor1, 137, UNIT_DEGREE);
  dxl.setGoalPosition(L3motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L3motor3, 180, UNIT_DEGREE);
  //
  dxl.setGoalPosition(L4motor1, 137, UNIT_DEGREE);
  dxl.setGoalPosition(L4motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L4motor3, 180, UNIT_DEGREE);
  /*
   *   //delay(400);
  DEBUG_SERIAL.print("Present Position(degree) : ");
  DEBUG_SERIAL.println(dxl.getPresentPosition(L1motor1));
  DEBUG_SERIAL.println(dxl.getPresentPosition(L4motor1));
   */
}
void wheel(){
  dxl.setGoalVelocity(L1motor4, 60, UNIT_RPM);
  dxl.setGoalVelocity(L2motor4, 60, UNIT_RPM);
  dxl.setGoalVelocity(L3motor4, 60, UNIT_RPM);
  dxl.setGoalVelocity(L4motor4, 60, UNIT_RPM);
}
void counterLeft(){
  dxl.setGoalVelocity(L1motor4, -60, UNIT_RPM);
  dxl.setGoalVelocity(L2motor4,  60, UNIT_RPM);
  dxl.setGoalVelocity(L3motor4,  60, UNIT_RPM);
  dxl.setGoalVelocity(L4motor4, -60, UNIT_RPM);
}
void counterRight(){
  dxl.setGoalVelocity(L1motor4,  60, UNIT_RPM);
  dxl.setGoalVelocity(L2motor4, -60, UNIT_RPM);
  dxl.setGoalVelocity(L3motor4, -60, UNIT_RPM);
  dxl.setGoalVelocity(L4motor4,  60, UNIT_RPM);
}
void stay(){
  dxl.setGoalPosition(L1motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L2motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L3motor2, 180, UNIT_DEGREE);
  dxl.setGoalPosition(L4motor2, 180, UNIT_DEGREE);
}

void walk(){
  //leg1
  dxl.setGoalPosition(L1motor1, 198, UNIT_DEGREE);
  dxl.setGoalPosition(L1motor2, 238, UNIT_DEGREE);
  //leg3
  dxl.setGoalPosition(L3motor1, 130, UNIT_DEGREE);
  dxl.setGoalPosition(L3motor2, 198, UNIT_DEGREE);
  //leg2
  dxl.setGoalPosition(L2motor1, 130, UNIT_DEGREE);
  dxl.setGoalPosition(L2motor2, 198, UNIT_DEGREE);
  //leg4
  dxl.setGoalPosition(L4motor1, 198, UNIT_DEGREE);
  dxl.setGoalPosition(L4motor2, 238, UNIT_DEGREE);
  delay(600);
  //leg1
  dxl.setGoalPosition(L1motor1, 128, UNIT_DEGREE);
  dxl.setGoalPosition(L1motor2, 198, UNIT_DEGREE);
  //leg3
  dxl.setGoalPosition(L3motor1, 198, UNIT_DEGREE);
  dxl.setGoalPosition(L3motor2, 240, UNIT_DEGREE);
  //leg2
  dxl.setGoalPosition(L2motor1, 198, UNIT_DEGREE);
  dxl.setGoalPosition(L2motor2, 240, UNIT_DEGREE);
  //leg4
  dxl.setGoalPosition(L4motor1, 130, UNIT_DEGREE);
  dxl.setGoalPosition(L4motor2, 178, UNIT_DEGREE);
  delay(600);
}

void pace(){
  dxl.setGoalPosition(L1motor1, 137, UNIT_DEGREE);
  int initial_present_position = 0;
  int final_present_position = 180;
  while (abs(180 - initial_present_position) > 90)
  {
    final_present_position   = dxl.getPresentPosition(L1motor1, UNIT_DEGREE);
    initial_present_position = dxl.getPresentPosition(L1motor2, UNIT_DEGREE);
  }
  delay(800);
  dxl.setGoalPosition(L1motor1,220, UNIT_DEGREE);
  
  while (abs(140 - final_present_position) > 90)
  {
    final_present_position = dxl.getPresentPosition(L1motor1, UNIT_DEGREE);
    initial_present_position = dxl.getPresentPosition(L1motor2);
  }
  delay(800);
}

void amble(){
  dxl.setGoalPosition(L2motor1, 135, UNIT_DEGREE);///1
  dxl.setGoalPosition(L3motor1, 135, UNIT_DEGREE);///4
  dxl.setGoalPosition(L2motor2, 235, UNIT_DEGREE);///knee
  dxl.setGoalPosition(L3motor2, 235, UNIT_DEGREE);///kne
  delay(100);
  dxl.setGoalPosition(L1motor1, 135, UNIT_DEGREE);///1
  dxl.setGoalPosition(L4motor1, 135, UNIT_DEGREE);///4
  dxl.setGoalPosition(L1motor2, 170, UNIT_DEGREE);///
  dxl.setGoalPosition(L4motor2, 170, UNIT_DEGREE);///knee
  delay(900);
  dxl.setGoalPosition(L2motor2, 170, UNIT_DEGREE);///knee
  dxl.setGoalPosition(L3motor2, 170, UNIT_DEGREE);///kne
  dxl.setGoalPosition(L1motor2, 235, UNIT_DEGREE);///
  dxl.setGoalPosition(L4motor2, 235, UNIT_DEGREE);///knee
  delay(900);

}
void loop(){
  //walk();
  //amble();
  //wheel;
  
}
