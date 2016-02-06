import brickpi
import time

interface=brickpi.Interface()
interface.initialize()
motors = [0,1]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

port = 1 # port which ultrasoic sensor is plugged in to

interface.sensorEnable(port, brickpi.SensorType.SENSOR_ULTRASONIC);





motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
#motorParams.minPWM = 20.0
motorParams.minPWM = 19.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
#motorParams.pidParameters.k_p = 516
#motorParams.pidParameters.k_i = 400
#motorParams.pidParameters.k_d = 16.8
motorParams.pidParameters.k_p = 300
motorParams.pidParameters.k_i = 1000
motorParams.pidParameters.k_d = 22

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)

def Right90deg(angle):
    #while True:
        #angle = float(input("Enter a angle to rotate (in radians): "))
        #angle = 4.5

        interface.increaseMotorAngleReferences(motors,[-angle,angle])
        #interface.startLogging("logg")
            #while True:
        while not interface.motorAngleReferencesReached(motors) :
                motorAngles = interface.getMotorAngles(motors)
                #if motorAngles :
                #print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
                time.sleep(0.1)

    #interface.stopLogging("logg")

    #print "Destination reached!"


def Left90deg(angle):
       # while True:
                #angle = float(input("Enter a angle to rotate (in radians): "))
                #angle = 4.5

                interface.increaseMotorAngleReferences(motors,[angle,-angle])
                #interface.startLogging("logg")
                #while True:
                while not interface.motorAngleReferencesReached(motors) :
                        motorAngles = interface.getMotorAngles(motors)
                        #if motorAngles :
                            #print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
                        time.sleep(0.1)

        #interface.stopLogging("logg")

        #print "Destination reached!"


def forward(speed):
    interface.setMotorRotationSpeedReferences(motors,[speed,speed])
       # while True:
                #angle = float(input("Enter a angle to rotate (in radians): "))
                #angle = 4.5

                #interface.increaseMotorAngleReferences(motors,[angle,angle])
                #interface.startLogging("logg")
                #while True:
                #while not interface.motorAngleReferencesReached(motors) :
                #        motorAngles = interface.getMotorAngles(motors)
                        #if motorAngles :
                            #print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
                    #    time.sleep(0.1)

        #interface.stopLogging("logg")

        #print "Destination reached!"

#x = int(input("loop: "))
#angle = float(input("input turn radian: "))
while True:
    usReading = interface.getSensorValue(port)

    if usReading :
        #print usReading
        distance = 30
        kp = 1
        v = -kp*(distance - usReading[0])
        forward(v)
    else:
        print "Failed US reading"

    time.sleep(0.05)

interface.terminate()
#for i in range(0, x):
    #forward(14.2857142857)
    # Right90deg(4.35)




interface.terminate()