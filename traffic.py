import Adafruit_BBIO.GPIO as GPIO
import time

led=['P9_11','P9_13','P9_15','P9_24','P9_12','P9_14','P9_16','P9_23','P8_11','P8_13','P8_15','P8_17','P8_14','P8_12','P8_16','P8_18']

for i in range(len(led)):
        GPIO.setup(led[i],GPIO.OUT)
        GPIO.output(led[i],GPIO.LOW)


for i in (led):
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,GPIO.LOW)


while True:
        GPIO.output("P9_11",GPIO.HIGH)
        GPIO.output("P9_12",GPIO.LOW)
        GPIO.output("P9_13",GPIO.LOW)
        GPIO.output("P9_14",GPIO.LOW)

        print("HIGH1")
        time.sleep(0.1)


        GPIO.output("P9_11",GPIO.LOW)
        GPIO.output("P9_12",GPIO.HIGH)
        GPIO.output("P9_13",GPIO.LOW)
        GPIO.output("P9_14",GPIO.LOW)

        print("HIGH2")
        time.sleep(0.1)
        GPIO.output("P9_11",GPIO.LOW)
        GPIO.output("P9_12",GPIO.LOW)
        GPIO.output("P9_13",GPIO.HIGH)
        GPIO.output("P9_14",GPIO.LOW)

        print("HIGH3")
        time.sleep(0.1)
        GPIO.output("P9_11",GPIO.LOW)
        GPIO.output("P9_12",GPIO.LOW)
        GPIO.output("P9_13",GPIO.LOW)
        GPIO.output("P9_14",GPIO.HIGH)

        print("HIGH4")

