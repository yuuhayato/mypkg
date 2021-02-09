#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('random1')                                
pub = rospy.Publisher('random1', Int32, queue_size=1)  
rate = rospy.Rate(10)                                   
n = random.randint(1,10)
while not rospy.is_shutdown():
    n = random.randint(1,10)
    pub.publish(n)
    rate.sleep()

