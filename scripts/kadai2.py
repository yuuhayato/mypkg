#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32

ran1=0
ran2=0

def cb1(message):
    global ran1
    ran1=message.data
def cb2(message):
    global ran2
    ran2=message.data
    mul()

def mul():
    global ran1,ran2
    rospy.loginfo(ran1*ran2)
    return

if __name__ == '__main__':
    rospy.init_node('kadai2')
    sub = rospy.Subscriber('random1', Int32, cb1, queue_size=1)
    sub1 = rospy.Subscriber('random2', Float32, cb2, queue_size=1)
    rospy.spin()

