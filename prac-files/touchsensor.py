import brickpi
import time

interface=brickpi.Interface()
interface.initialize()


touch_port = 0
touch_port2 = 3

interface.sensorEnable(touch_port2, brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port, brickpi.SensorType.SENSOR_TOUCH)
while True:
    result = interface.getSensorValue(touch_port)
    result2 = interface.getSensorValue(touch_port2)
    touched = 0
    touched2 = 0
    if result:
            touched = result[0]
    if result2:
        touched2 = result2[0]
    print 'sensor1:',touched,' sensor2',touched2

    time.sleep(0.05)

interface.terminate()


