#!/usr/bin/env python
import roslib
import rospy
from std_msgs.msg import String
import serial
import signal
import sys

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

def talker():
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    pub = rospy.Publisher('weight', String, queue_size=10)
    rospy.init_node('talker')
    while not rospy.is_shutdown():
       data= ser.readline() # I have "hi" coming from the arduino as a test run over the serial port
       rospy.loginfo(data)
       pub.publish(String(data))
       rospy.sleep(0.1)

def say(name):
    print('Hello ' + name)
    signal.signal(signal.SIGINT, signal_handler)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass