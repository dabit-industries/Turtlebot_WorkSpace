#!/usr/bin/env python
import rospy
from kobuki_msgs.msg import SensorState, Sound


def call_back(scanmsg):
    dist = scanmsg.analog_input[3]
    if dist < 150:
         pub.publish(0)

def listener():
    '''Initializes node, creates subscriber, and states callback 
    function.'''
    rospy.init_node('beep_ultrasonic')
    rospy.loginfo("Subscriber Starting")
    rospy.spin()

if __name__ == "__main__":
    '''A Scan_msg class object called sub_obj is created and listener
    function is run''' 
    sub = rospy.Subscriber('/mobile_base/sensors/core', SensorState, call_back)
    pub = rospy.Publisher('/mobile_base/commands/sound',Sound,queue_size=1)
    listener()

