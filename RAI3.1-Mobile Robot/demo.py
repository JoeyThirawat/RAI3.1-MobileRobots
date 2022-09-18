#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose #import Pose object
import time

pos = Pose() # Assign and set default
vel = Twist() # Variable Twist

def position_callback(data):
    global pos
    pos = data
    #print("amcl_pose = {x: %f, y:%f, orientation.z:%f" % (pos.position.x, pos.position.y, pos.orientation.z))

def main():
    rospy.init_node('turtle_commander', anonymous=True)
    rate = rospy.Rate(10) #10 Hz
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose',Pose,position_callback)

    timestart = time.time()

    while not rospy.is_shutdown():

        timenow = time.time()
        counter = timenow - timestart

        # TODO

        if (counter <= 1):
            vel.linear.y = -0.5


        elif (counter > 2 and counter <= 3):
            vel.linear.x = -0.5


        elif (counter > 5 and counter <= 13):

            vel.linear.x = 0.5

        elif (counter > 15 and counter <= 20):

            vel.linear.x = -0.5


        elif (counter > 22 and counter <= 31):

            vel.linear.y = 0.5


        elif (counter > 33 and counter <= 35):

            vel.linear.y = -0.5


        elif (counter > 37 and counter <= 46.86):

            vel.linear.x = -0.5



        else:
            vel.linear.x = 0
            vel.linear.y = 0
            vel.angular.z = 0

        print("Turtle is running",pos)
        print("Time",counter)
        print('\n')

        # END
        pub.publish(vel)
        rate.sleep()

if __name__ == "__main__":
    main()

'''
if __name___== '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass'''