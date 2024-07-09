#!/usr/bin/env python
"""
    Subscribes to /capture_perception topic.
    Launches the perception model
    Uses the perception model to determine affordances
"""
import rospy

from niryo_moveit.msg import NiryoImageCapture

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard:\n%s", data)

def listener():
    rospy.init_node('Capture_Perception', anonymous=True)
    rospy.Subscriber("/capture_perception", NiryoImageCapture, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()