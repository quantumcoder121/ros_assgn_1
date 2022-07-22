#!/usr/bin/env python3
# license removed for brevity
import rospy
import cv2 as cv
from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def viewfeed(data):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(data, "bgr8")
    edge_frame = cv.Canny(frame, 100, 200)
    final_frame = cv.hconcat(frame, edge_frame)
    cv.imshow("Video feed", final_frame)
    cv.waitKey(0)

def receiver():
    image_sub = rospy.Subscriber('camera_feed', Image, viewfeed)
    rospy.init_node('receiver', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo("node shutting down")
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        receiver()
    except rospy.ROSInterruptException:
        pass