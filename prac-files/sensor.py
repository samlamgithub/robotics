import brickpi
import time

interface=brickpi.Interface()
interface.initialize()


touch_port = 1

interface.sensorEnable(touch_port, brickpi.SensorType.SENSOR_TOUCH)
while True:
        result = interface.getSensorValue(touch_port)

        if result:
            touched = result[0]
            print touched

        time.sleep(0.05)

interface.terminate()


