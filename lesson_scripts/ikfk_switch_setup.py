import maya.cmds as cmds

import gacUtilities
from gacUtilities import create_null_node, create_ball_control


def ikfk_switch_setup(side=None):
	'''
	Function sets up the ik fk switch setup.
	
	Args:
		side (str): The side of the arm ('L' or 'R')
	'''
	# Parent constrain the bind arm to the IK and FK arms
	cmds.parentConstraint('L_SHLD_fk_Jnt', 'L_SHLD_bind_Jnt')  # FK
	cmds.parentConstraint('L_elbow_fk_Jnt', 'L_elbow_bind_Jnt')  # FK
	cmds.parentConstraint('L_wrist_fk_Jnt', 'L_wrist_bind_Jnt')  # FK
	
	cmds.parentConstraint('L_SHLD_ik_Jnt', 'L_SHLD_bind_Jnt')  # IK
	cmds.parentConstraint('L_elbow_ik_Jnt', 'L_elbow_bind_Jnt')  # IK
	cmds.parentConstraint('L_wrist_ik_Jnt', 'L_wrist_bind_Jnt')  # IK
	
	# Create the Switch control
	switch_ctrl = create_ball_control('L_switch_Ctrl', offset_pos=(0,40,0))
	wrist_joint = 'L_wrist_bind_Jnt'
	cmds.xform(switch_ctrl,
			worldSpace=True,
			matrix=cmds.xform(
				wrist_joint,
				query=True,
				worldSpace=True,
				matrix=True
		)
	)
	
	# Provide a null node for the switch control
	switch_null = create_null_node('Null', selected_nodes=switch_ctrl, position='suffix')
	
	# Creating Attribute Divider
	cmds.addAttr(switch_ctrl, longName='________________', attributeType='enum', enumName='IKFK:')
	cmds.setAttr(f'{switch_ctrl}.________________', lock=True, channelBox=True)
	
	# Create an IK/FK switch attribute
	cmds.addAttr(switch_ctrl, longName='ikFk', attributeType='double', minValue=0, maxValue=1, defaultValue=0)
	cmds.setAttr(f'{switch_ctrl}.ikFk', keyable=True)
	
	# Create Reverse utility node
	rev_node_name = 'L_ikFkArm_Rev'
	cmds.createNode('reverse', name=rev_node_name)
	
	# Connect switch control to FK constraints
	cmds.connectAttr(f'{switch_ctrl}.ikFk', 'L_SHLD_bind_Jnt_parentConstraint1.L_SHLD_fk_JntW0', force=True)
	cmds.connectAttr(f'{switch_ctrl}.ikFk', 'L_elbow_bind_Jnt_parentConstraint1.L_elbow_fk_JntW0', force=True)
	cmds.connectAttr(f'{switch_ctrl}.ikFk', 'L_wrist_bind_Jnt_parentConstraint1.L_wrist_fk_JntW0', force=True)
	
	# Connect switch control to Reverse node
	cmds.connectAttr(f'{switch_ctrl}.ikFk', f'{rev_node_name}.inputX')
	
	# Connect Reverse node to IK constraints
	cmds.connectAttr(f'{rev_node_name}.outputX', 'L_SHLD_bind_Jnt_parentConstraint1.L_SHLD_ik_JntW1', force=True)
	cmds.connectAttr(f'{rev_node_name}.outputX', 'L_elbow_bind_Jnt_parentConstraint1.L_elbow_ik_JntW1', force=True)
	cmds.connectAttr(f'{rev_node_name}.outputX', 'L_wrist_bind_Jnt_parentConstraint1.L_wrist_ik_JntW1', force=True)
	
	# Connect IK FK arm control vis
	cmds.connectAttr(f'{switch_ctrl}.ikFk', 'L_armFkCtrl_Grp.v')
	cmds.connectAttr(f'{rev_node_name}.outputX', 'L_armIkCtrl_Grp.v')
	
	# Constrain switch control to arm
	cmds.parentConstraint('L_wrist_bind_Jnt', switch_null)
	
	# Clean-up (lock/hide switch control's unused attrs)
	for attr in ['sx', 'sy', 'sz', 'v']:
		cmds.setAttr(f'{switch_ctrl}.{attr}', keyable=False, lock=True)
	# Clean-up (Parent control into hierarchy)
	cmds.parent('L_switch_Ctrl_Null', 'L_armCtrl_Grp')
	
	
	
