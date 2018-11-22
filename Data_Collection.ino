#include<Wire.h>
const int MPU=0x68; 
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ,prevAcX,prevAcY,prevAcZ,prevGyX,prevGyY,prevGyZ;
int led_pin =13;
int counter=0,counter1=0;
void setup(){
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B); 
  Wire.write(0);    
  Wire.endTransmission(true);
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
}
void loop(){
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,12,true);
  int rainValue = analogRead(A3);
  int moistureValue = analogRead(A2);  
  AcX=Wire.read()<<8|Wire.read();    
  AcY=Wire.read()<<8|Wire.read();  
  AcZ=Wire.read()<<8|Wire.read();  
  GyX=Wire.read()<<8|Wire.read();  
  GyY=Wire.read()<<8|Wire.read();  
  GyZ=Wire.read()<<8|Wire.read();
  if(counter1>10)
    counter=0;
  if(counter!=0)  
  if(rainValue < 360 || moistureValue < 500||abs(AcX-prevAcX)>1000||abs(AcY-prevAcY)>1000||abs(AcZ-prevAcZ)>1000||abs(GyX-prevGyX)>1000||abs(GyY-prevGyY)>1000||abs(GyZ-prevGyZ)>1000)
  {
    counter1=1;
    while(counter1<=5)
    {
      Serial.print("Accelerometer: ");
      Serial.print("X = "); Serial.print(AcX);
      Serial.print(" | Y = "); Serial.print(AcY);
      Serial.print(" | Z = "); Serial.println(AcZ); 
      
      Serial.print("Gyroscope: ");
      Serial.print("X = "); Serial.print(GyX);
      Serial.print(" | Y = "); Serial.print(GyY);
      Serial.print(" | Z = "); Serial.println(GyZ);
      Serial.println(" ");
      Serial.println(" ");
      Serial.print("rain data = "); Serial.print(rainValue);
      Serial.println(" ");
      Serial.print("moisture data = "); Serial.print(moistureValue);
      Serial.println(" ");
      Serial.println(" ");
      Wire.beginTransmission(MPU);
      Wire.write(0x3B);  
      Wire.endTransmission(false);
      Wire.requestFrom(MPU,12,true);
      rainValue = analogRead(A3);
      moistureValue = analogRead(A2);  
      AcX=Wire.read()<<8|Wire.read();    
      AcY=Wire.read()<<8|Wire.read();  
      AcZ=Wire.read()<<8|Wire.read();  
      GyX=Wire.read()<<8|Wire.read();  
      GyY=Wire.read()<<8|Wire.read();  
      GyZ=Wire.read()<<8|Wire.read();
      prevAcX=AcX;
      prevAcY=AcY;
      prevAcZ=AcZ;
      prevGyX=GyX;
      prevGyY=GyY;
      prevGyZ=GyZ;
      counter1++;
      delay(3000);
    }
  }
  prevAcX=AcX;
  prevAcY=AcY;
  prevAcZ=AcZ;
  prevGyX=GyX;
  prevGyY=GyY;
  prevGyZ=GyZ;
  counter1=0;
  counter++;
}

