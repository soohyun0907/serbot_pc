#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

#include "opencv_apps/RectArrayStamped.h"
import rospy
from std_msgs.msg import String
from opencv_apps.msg import RectArrayStamped
pub = None
hello = None

def peopledetect_callback(data):
    rospy.loginfo(rospy.get_caller_id() + ': face detect received: %s', data.rects)
    if len(data.rects)>0: 
      pub.publish(hello)


def listener():
    global pub
    global hello

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('peopledetect_listener_node', anonymous=True)
    pub = rospy.Publisher('/play_sound_file', String, queue_size=10)
    hello = rospy.get_param('hello', '/home/chuck/Downloads/1.mp3')

    rospy.Subscriber('/people_detect/found', RectArrayStamped, peopledetect_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

