#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
import random

rospy.init_node('test')                                
pub = rospy.Publisher('test', Int32, queue_size=1)  
rate = rospy.Rate(10)                                   
n = random.randint(11,20)
while not rospy.is_shutdown():
    n = random.randint(11,20)
    pub.publish(n)
    rate.sleep()

