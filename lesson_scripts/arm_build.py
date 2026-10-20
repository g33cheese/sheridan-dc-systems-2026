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
importlib.reload(create_arm_fk)

#---------- Arm Creation ----------#

# Create pivots locators
locators = create_arm_pivots.create_arm_pivots('L')
right_locators = create_arm_pivots.mirror_arm_pivots()

# Save/Load pivot location data
#arm_pivot_data.save_arm_pivots(['L_SHLD_Loc', 'L_elbow_Loc', 'L_wrist_Loc', 'L_elbow_mid_Loc', 'L_elbow_pole_Loc'])
arm_pivot_data.load_arm_pivots(['L_SHLD_Loc', 'L_elbow_Loc', 'L_wrist_Loc', 'L_elbow_mid_Loc', 'L_elbow_pole_Loc'])

# Create arm joints
# Left Side ----------------------#
for joint_type in ['bind', 'fk', 'ik']:
  create_arm_joints.create_arm_joints(locators, 'L', joint_type) # Creation in a for loop

create_arm_joints.create_arm_joints(locators, 'L', 'bind') # Creation one joint type at a time
create_arm_joints.create_arm_joints(locators, 'L', 'fk')
create_arm_joints.create_arm_joints(locators, 'L', 'ik')

# Right Side ----------------------#
create_arm_joints.create_arm_joints(right_locators, 'R', 'bind')
create_arm_joints.create_arm_joints(right_locators, 'R', 'fk')
create_arm_joints.create_arm_joints(right_locators, 'R', 'ik')

# Orient the arm joint chains
# Left Side ----------------------#
create_arm_joints.orient_arm_joints('L', 'bind')
create_arm_joints.orient_arm_joints('L', 'fk')
create_arm_joints.orient_arm_joints('L', 'ik')

# Right Side ----------------------#
create_arm_joints.orient_arm_joints('R', 'bind')
create_arm_joints.orient_arm_joints('R', 'fk')
create_arm_joints.orient_arm_joints('R', 'ik')

# Create arm ik setup
create_arm_ik.create_arm_ik('L')


#---------- Right-side ----------#

# Create arm ik setup
create_arm_ik.create_arm_ik('L')
cmds.rename('effector1', 'L_arm_effector')

# Create arm fk setup
create_arm_fk.create_arm_fk(side='L')

#---------- Right-side ----------#

# Mirror the joint chains to the right side
create_arm_joints.mirror_arm_joints()

# Create R arm ik setup
create_arm_ik.create_arm_ik('R')

# Create arm fk setup
create_arm_fk.create_arm_fk(side='R')

