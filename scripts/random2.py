#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

rospy.init_node('random2')                                
pub = rospy.Publisher('random2', Float32, queue_size=1)  
rate = rospy.Rate(10)                                   
n = random.random()
while not rospy.is_shutdown():
    n = random.random()
    pub.publish(n)
    rate.sleep()

