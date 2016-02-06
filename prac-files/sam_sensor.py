import brickpi
import time

interface=brickpi.Interface()
interface.initialize()


# left sensor
touch_port = 3
# right sensor
touch_port2 = 0

interface.sensorEnable(touch_port2, brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port, brickpi.SensorType.SENSOR_TOUCH)

motors = [0,1]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 19.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
motorParams.pidParameters.k_p = 300
motorParams.pidParameters.k_i = 1000
motorParams.pidParameters.k_d = 22

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)

def forward(angle): 
        interface.increaseMotorAngleReferences(motors,[angle,angle])
        while not (interface.motorAngleReferencesReached(motors)):
            motorAngles = interface.getMotorAngles(motors)
            #time.sleep(0.1)
        
def Right90deg(angle): 
        interface.increaseMotorAngleReferences(motors,[-angle,angle])
        while not interface.motorAngleReferencesReached(motors) :
                motorAngles = interface.getMotorAngles(motors)
                time.sleep(0.1)    

def Left90deg(angle):
        interface.increaseMotorAngleReferences(motors,[angle,-angle])
        while not interface.motorAngleReferencesReached(motors) :
                        motorAngles = interface.getMotorAngles(motors)
                        time.sleep(0.1)
def reverse(angle):
        interface.increaseMotorAngleReferences(motors, [-angle, -angle])
        while not interface.motorAngleReferencesReached(motors):
                motorAngles = interface.getMotorAngles(motors)
                time.sleep(0.1)

while True:
    interface.setMotorRotationSpeedReferences(motors,[10,10])
    result = interface.getSensorValue(touch_port)
    result2 = interface.getSensorValue(touch_port2)
    
    #forward(5)
    
    touched = 0
    touched2 = 0
    if result:
        touched = result[0]
    if result2:
        touched2 = result2[0]
    #print 'sensor1:',touched,' sensor2',touched2

    #time.sleep(0.05)
    if touched:
        # reverse and turn to the right
        interface.setMotorRotationSpeedReferences(motors,[-3,-3])
        reverse(5)
        time.sleep(0.1)
        Right90deg(3)
        time.sleep(0.1)
    elif touched2:
        # reverse and turn to the left
        interface.setMotorRotationSpeedReferences(motors,[-3,-3])
        reverse(5)
        time.sleep(0.1)
        Left90deg(3)
        time.sleep(0.1)
        

interface.terminate()


