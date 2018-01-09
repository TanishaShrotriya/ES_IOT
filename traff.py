mport Adafruit_BBIO.GPIO as GPIO
import time
led = [('r2','P9_11'),('y2','P9_13'),('gs2', 'P9_15'),('gl2', 'P9_24'),('gl1', 'P9_12'),('gs1', 'P9_14'),('y1', 'P9_16'),('r1', 'P9_23'),('r3','P8_11'),('y3', 'P8_13'),('gs3', 'P8_15'),('gl3', 'P8_17'), ('gs4','P8_14'),('gl4', 'P8_12'),('y4', 'P8_16'), ('r4','P8_18')]
for i in led :
        GPIO.setup(i[1], GPIO.OUT)
        GPIO.output(i[1], GPIO.LOW)
        print(i[1])

def glow(name,status) :

        for i in led :
                if(i[0]== name):
                        GPIO.output(i[1],GPIO.HIGH)

        return "HIGH"

