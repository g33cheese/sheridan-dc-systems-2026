'''
Module runs the arm creation functions to build the arm setup.

Functions are called from gacUtilities such as create_null_node, create_ball_control, create_pole_control
in the create_arm_ik module.
'''
from maya import cmds
import importlib

import gacUtilities
import create_arm_pivots
import create_arm_joints
import create_arm_ik
import arm_pivot_data

importlib.reload(gacUtilities)
importlib.reload(create_arm_pivots)
importlib.reload(create_arm_joints)
importlib.reload(create_arm_ik) 
importlib.reload(arm_pivot_data) 

# Arm Creation
locators = create_arm_pivots.create_arm_pivots('L')
#arm_pivot_data.save_arm_pivots(['L_SHLD_Loc', 'L_elbow_Loc', 'L_wrist_Loc', 'L_elbow_mid_Loc', 'L_elbow_pole_Loc'])
arm_pivot_data.load_arm_pivots(['L_SHLD_Loc', 'L_elbow_Loc', 'L_wrist_Loc', 'L_elbow_mid_Loc', 'L_elbow_pole_Loc'])
create_arm_joints.create_arm_joints(locators, 'L', 'bind')
create_arm_joints.create_arm_joints(locators, 'L', 'fk')
create_arm_joints.create_arm_joints(locators, 'L', 'ik')
create_arm_ik.create_arm_ik('L')

