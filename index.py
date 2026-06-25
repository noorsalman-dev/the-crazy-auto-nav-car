from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

motor_in1 = Pin(14, Pin.OUT)
motor_in2 = Pin(15, Pin.OUT)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signal_off = utime.ticks_us()
    while echo.value() == 1:
        signal_on = utime.ticks_us()

    time_passed = signal_on - signal_off
    distance = (time_passed * 0.0343) / 2
    return distance

while True:
    dist = ultra()
    print("Distance:", dist)
    
    if dist < 8.0:
        motor_in1.low()
        motor_in2.low()
    else:
        motor_in1.high()
        motor_in2.low()
        
    utime.sleep(0.2)
