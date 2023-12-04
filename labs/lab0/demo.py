"""
Date: 08/26/2021

Purpose: This script creates an ArmController and uses it to command the arm's
joint positions and gripper.

Try changing the target position to see what the arm does!

"""

import sys
import rospy
import numpy as np
from math import pi

from core.interfaces import ArmController

rospy.init_node('demo')

arm = ArmController()

lims = arm.joint_limits()
print('Joint Limits:',lims)

angles = arm.get_positions()
print('Original position:',angles)

arm.set_arm_speed(0.3)   

# arm.close_gripper()

# q = arm.neutral_position()
# arm.safe_move_to_position(q)
# arm.open_gripper()

# angles = arm.get_positions()
# print('Neutral position:',angles)

q = np.array([-1.2, 1.57, 1.57, -2.07, -1.57, 1.57, 0.7])
arm.safe_move_to_position(q)
# arm.close_gripper()

# angles = arm.get_positions()
# print('Current position:',angles)