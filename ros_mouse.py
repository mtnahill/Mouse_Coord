#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy 		# needed for ros to run python
import struct 		# from mouse code
import datetime 	# from mouse code
import time 		# from mouse code
from std_msgs.msg import String		# from ROS tutorial
file = open( "/dev/input/mouse0", "rb" ); # opens mouse file

def talker():	# from ROS tutorial
    x_abs = 0	# from mouse code
    y_abs = 0	# from mouse code
    print(0)
    pub = rospy.Publisher('chatter', String, queue_size=100) #from ROS code
    rospy.init_node('talker', anonymous=True) # from ROS code
    rate = rospy.Rate(100) # 10hz 	# from ROS tutorial
    endloop = 0
    while not rospy.is_shutdown():	# from ROS tutorial
        endloop = endloop + 1 
	print(endloop)
	buf = file.read(3);		# from mouse code
        x,y = struct.unpack( "bb", buf[1:] ); # from mouse code
        x_abs = x_abs+x;		# from mouse code
	y_abs = y_abs+y;		# from mouse code
	st = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] # from mouse code
	mouse_coor_str = "x = %s, y = %s, time = %s" % (x_abs, y_abs, st)
	rospy.loginfo(mouse_coor_str)	# from ROS tutorial
        pub.publish(mouse_coor_str)	# from ROS tutorial
        rate.sleep()			# from ROS tutorial

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
