mport Adafruit_BBIO.GPIO as GPIO
import time
led=['P9_11','P9_12','P9_13','P9_14']
for i in range(len(led)):
        GPIO.setup(led[i],GPIO.OUT)
        GPIO.output(led[i],GPIO.LOW)
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

