*rain sensor code*
#include<servo.h>
int rain_sensor=A0,servo=3;
servo myservo;
void setup()
{
    serial.begin(9600);
    myservo.attach(servo);
    myservo.write(0);
    }
void loop()
{
    int sensorvalue=analogread(rain_sensor);
    int motor=map(sensorvalue,220,1023,180,0);
    myservo.write(motor);
    serial.println("sensor value is");
    serial.println(sensorvalue);
    serial.println("servo motor rotates by angle");
    serial.println(motor);
    delay(1000);
    }
