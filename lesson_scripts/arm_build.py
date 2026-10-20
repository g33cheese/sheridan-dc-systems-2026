import sys

sys.path.append('M:/scripts')


'''
Module runs the arm creation functions to build the arm setup.

Functions are called from gacUtilities such as create_null_node, create_ball_control, create_pole_control
in the createArmIk module.
'''
from maya import cmds
import importlib

import gacUtilities
import createArmPivots
import createArmJoints
import createArmIk
import armPivotData
import createArmFk

importlib.reload(gacUtilities)
importlib.reload(createArmPivots)
importlib.reload(createArmJoints)
importlib.reload(createArmIk)
importlib.reload(armPivotData)
importlib.reload(createArmFk)

#---------- Arm Creation ----------#
def arm_build():
	'''
	This function builds the arm.
	'''

	# Create pivots locators
	locators = createArmPivots.create_arm_pivots('L')
	
	# Save/Load pivot location data
	#armPivotData.save_arm_pivots(['L_SHLD_Loc', 'L_elbow_Loc', 'L_wrist_Loc', 'L_elbow_mid_Loc', 'L_elbow_pole_Loc'])
	armPivotData.load_arm_pivots(['L_SHLD_Loc', 'L_elbow_Loc', 'L_wrist_Loc', 'L_elbow_mid_Loc', 'L_elbow_pole_Loc'])
	
	# Create arm joints
	# Left Side ----------------------#
	createArmJoints.create_arm_joints(locators, 'L', 'bind') # Creation one joint type at a time
	createArmJoints.create_arm_joints(locators, 'L', 'fk')
	createArmJoints.create_arm_joints(locators, 'L', 'ik')
	
	# Orient the arm joint chains
	# Left Side ----------------------#
	createArmJoints.orient_arm_joints('L', 'bind')
	createArmJoints.orient_arm_joints('L', 'fk')
	createArmJoints.orient_arm_joints('L', 'ik')
	
	# Create arm ik setup
	createArmIk.create_arm_ik('L')
	
	# Create L arm fk setup
	createArmFk.create_arm_fk(side='L')
	
	# Create IK/FK switch


arm_build()


#---------- Right-side ----------#

# Create the R arm pivots
right_locators = createArmPivots.mirror_arm_pivots()

# Right Side ----------------------#
createArmJoints.create_arm_joints(right_locators, 'R', 'bind')
createArmJoints.create_arm_joints(right_locators, 'R', 'fk')
createArmJoints.create_arm_joints(right_locators, 'R', 'ik')

# Mirror the joint chains to the right side
# createArmJoints.mirror_arm_joints()

# Orient joints
createArmJoints.orient_arm_joints('R', 'bind')
createArmJoints.orient_arm_joints('R', 'fk')
createArmJoints.orient_arm_joints('R', 'ik')

# Create R arm ik setup
createArmIk.create_arm_ik('R')

# Create R arm fk setup
createArmFk.create_arm_fk(side='R')

# Mirror R-side behaviour


# Create IK/FK Switch


#----- Clean-up - Set up final hierarchy -----#

# Create a top group for your arm rig
top_group = cmds.group(empty=True, name='rig')

# Create top arm group
top_arm_group = 'rig_arm_Grp'
cmds.parent(cmds.group(empty=True, name=top_arm_group), top_group)

# Create an IK arm group
ik_arm_group = 'L_armIkCtrl_Grp'
cmds.parent('L_arm_Ikh_Null', 'L_arm_Ikh_Ctrl_Null', 'L_elbow_Pole_Ctrl_Null', cmds.group(empty=True, name=ik_arm_group))

# Create a control group
control_arm_group = 'L_armCtrl_Grp'
fk_arm_group = 'L_armFkCtrl_Grp'
cmds.parent(cmds.group(fk_arm_group, ik_arm_group, name=control_arm_group), top_arm_group)

# Parent Joint and Pivot groups to top arm group
cmds.parent('L_armJnt_Grp', 'L_arm_pivot_Grp', top_arm_group)


#----- Right Side Stuff -----#
# Create a R arm pivot group and parent the pivot locators to it
cmds.parent(['R_SHLD_Loc', 'R_elbow_Loc', 'R_wrist_Loc', 'R_elbow_mid_Loc', 'R_elbow_pole_Loc'], cmds.group(empty=True, name='R_arm_pivot_Grp'))
