'''
GAC Tools UI

This module contains the user interface for accessing common rigging utilities in Maya.
'''

import importlib

import maya.cmds as cmds

import gacUtilities

importlib.reload(gacUtilities)

def show_local_axis_from_ui(*args):
	
	# Show or hide the local axis
	gacUtilities.show_local_axis()


def create_joint_from_ui(*args):
	
	# Get the joint name
	name = cmds.textField('nodeNameField', query=True, text=True)

	# Get the joint size
	size = cmds.floatField('nodeSizeField', query=True, value=True)

	# Create the joint
	gacUtilities.create_joint(name, size=size)


def create_locator_from_ui(*args):
	
	# Get the locator name
	name = cmds.textField('nodeNameField', query=True, text=True)

	# Get the locator size
	size = cmds.floatField('nodeSizeField', query=True, value=True)

	# Create the locator
	gacUtilities.create_locator(name, size=size)


def create_null_node_from_ui(*args):

	# Get the null name
	name = cmds.textField('nullNameField', query=True, text=True)

	# Get the prefix/suffix selection
	state = cmds.radioButtonGrp('nullStateRadio', query=True, select=True) 

	# Convert the radio button selection
	if state == 1:
		state = 'prefix'
	else:
		state = 'suffix'

	# Create the null node
	gacUtilities.create_null_node(name, state)
	

def create_pole_control_from_ui(*args):
	
	# Get the control name
	name = cmds.textField('nodeNameField', query=True, text=True)
	
	# Get the control size
	size = cmds.floatField('nodeSizeField', query=True, value=True)
	
	# Get the offset position
	offset_x = cmds.floatField('poleOffsetXField', query=True, value=True)
	offset_y = cmds.floatField('poleOffsetYField', query=True, value=True)
	offset_z = cmds.floatField('poleOffsetZField', query=True, value=True)
	
	offset_pos = (offset_x, offset_y, offset_z)
	
	# Create the pole control
	gacUtilities.create_pole_control(
		name,
		offset_pos,
		size=size
	)


def create_ball_control_from_ui(*args):
	
	# Get the control name
	name = cmds.textField(
		'nodeNameField',
		query=True,
		text=True
	)
	
	# Get the offset position
	offset_x = cmds.floatField('offsetXField', query=True, value=True)
	offset_y = cmds.floatField('offsetYField', query=True, value=True)
	offset_z = cmds.floatField('offsetZField', query=True, value=True)
	
	offset_pos = (offset_x, offset_y, offset_z)
	
	# Create the ball control
	gacUtilities.create_ball_control(
		name,
		offset_pos
	)


def create_rigger_tools_ui():
	'''
	Rigger Tools UI
	
	Creates a simple Maya UI for accessing common rigging utilities.
	'''

	window_name = 'riggerToolsWindow'

	if cmds.window(window_name, exists=True):
		cmds.deleteUI(window_name)

	cmds.window(window_name, title='Rigger Tools', widthHeight=(400, 500))

	cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
	
	# ----------------------------------------------------------------------
	# Local Axis
	# ----------------------------------------------------------------------

	cmds.separator(height=10)

	cmds.button(label='Show Local Axis', command=show_local_axis_from_ui)

	cmds.separator(height=10)


	# ----------------------------------------------------------------------
	# Snap
	# ----------------------------------------------------------------------
	
	cmds.separator(height=10)

	cmds.button(label='Snap to Object', command=gacUtilities.snap_tool)

	cmds.separator(height=10)


	# ----------------------------------------------------------------------
	# Find Centre of Selection
	# ----------------------------------------------------------------------
	
	cmds.separator(height=10)
	
	cmds.button(label='Find Centre of Selection', command=gacUtilities.find_centre_of_selection)

	cmds.separator(height=10)


	# ----------------------------------------------------------------------
	# Create Locator/Joint
	# ----------------------------------------------------------------------

	# Labels
	cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 200))

	cmds.text(label='Input Node Name:')
	cmds.text(label='Input Locator/Joint Size:')

	# Return to the parent layout
	cmds.setParent('..')

	# Input fields
	cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 200))
	cmds.textField('nodeNameField', text='node')
	cmds.floatField('nodeSizeField', value=1.0, minValue=0.001)

	# Return to the parent layout
	cmds.setParent('..')

	# Create buttons
	cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 200))
	cmds.button(label='Create Locator', command=create_locator_from_ui)
	cmds.button(label='Create Joint', command=create_joint_from_ui)

	# Return to the parent layout
	cmds.setParent('..')

	cmds.separator(height=10)


	# ----------------------------------------------------------------------
	# Null
	# ----------------------------------------------------------------------

	cmds.text(label='Input Null Name:')

	cmds.textField('nullNameField', text='null')

	cmds.text(label='Name Position:')

	cmds.radioButtonGrp(
		'nullStateRadio',
		labelArray2=['Prefix', 'Suffix'],
		numberOfRadioButtons=2,
		select=2
	)

	cmds.button(label='Create Null Node', command=create_null_node_from_ui)

	cmds.separator(height=10)


	# ----------------------------------------------------------------------
	# Ball Control
	# ----------------------------------------------------------------------
	
	# Control name input
	cmds.text(label='Input Ball Control Name:')
	cmds.textField('controlNameField', text='ball_control')
	
	# Offset pos value input
	cmds.text(label='Input Offset Position Values:')
	cmds.floatField(
		'offsetXField',
		value=0,
		annotation='Sets the X position of the ball control.\n'
					'Example: Enter 2 to offset the control 2 units to the side.'
	)
	cmds.floatField(
		'offsetYField',
		value=0,
		annotation='Sets the Y position of the ball control.\n'
					'Example: Enter 2 to offset the control 2 units upwards.'
	)
	cmds.floatField(
		'offsetZField',
		value=0,
		annotation='Sets the Z position of the ball control.\n'
					'Example: Enter 2 to offset the control 2 units forward.'
	)
	
	# Create button
	cmds.button(
		label='Create Ball Control',
		annotation='Creates a three-circle ball control.\n'
						'The control shapes can be offset from the\n'
						'from the pivot based off user input.',
		command=create_ball_control_from_ui
	)	

	
	# ----------------------------------------------------------------------
	# Pole Control
	# ----------------------------------------------------------------------
	
	# Control name input
	cmds.text(label='Input Pole Control Name:')
	cmds.textField('poleControlNameField', text='pole_control')
	
	# Offset pos value input
	cmds.text(label='Input Size Value:')
	
	cmds.floatField(
	'size',
	value=1,
	annotation='Input a size value for the pole control shape'
	)
	
	cmds.text(label='Input Offset Position Values:')
	
	cmds.floatField(
		'poleOffsetXField',
		value=0,
		annotation='Sets the X position of the pole control.\n'
					'Example: Enter 2 to offset the control 2 units to the side.'
	)
	cmds.floatField(
		'poleOffsetYField',
		value=0,
		annotation='Sets the Y position of the pole control.\n'
					'Example: Enter 2 to offset the control 2 units upwards.'
	)
	cmds.floatField(
		'poleOffsetZField',
		value=0,
		annotation='Sets the Z position of the pole control.\n'
					'Example: Enter 2 to offset the control 2 units forward.'
	)
	
	# Create button
	cmds.button(
		label='Create Pole Control',
		annotation='Creates a three-circle pole control.\n'
						'The control shapes can be offset from the\n'
						'from the pivot based off user input.',
		command=create_pole_control_from_ui
	)
	cmds.separator(height=10)


	# ----------------------------------------------------------------------
	# Skinning 
	# ----------------------------------------------------------------------

	cmds.separator(height=10)

	cmds.button(label='Bind Like', command=gacUtilities.bind_like)

	cmds.separator(height=10)


	cmds.showWindow(window_name)



def create_rigger_tools_ui():
	'''
	Rigger Tools UI
	
	Creates a simple Maya UI for accessing common rigging utilities.
	'''

	window_name = 'riggerToolsWindow'

	if cmds.window(window_name, exists=True):
		cmds.deleteUI(window_name)

	cmds.window(window_name, title='Rigger Tools', widthHeight=(200, 250))

	cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
	
	# -----------------------------------
	# Local Axis
	# -----------------------------------

	cmds.text(label='Input local Axis State:')
	
	cmds.intField(
		'localAxisField',
		value=1,
		minValue=0,
		maxValue=1,
		annotation='Enter 1 to show the local axis.\n'
					'Enter 0 to hide the local axis.'
		)
	
	cmds.button(label='Show Local Axis', command=show_local_axis_from_ui)

	cmds.separator(height=10)
	
	# -----------------------------------
	# Ball Control
	# -----------------------------------
	
	# Control name input
	cmds.text(label='Input Ball Control Name:')
	cmds.textField('controlNameField', text='ball_control')
	
	# Offset pos value input
	cmds.text(label='Input Offset Position Values:')
	cmds.floatField(
		'offsetXField',
		value=0,
		annotation='Sets the X position of the ball control.\n'
					'Example: Enter 2 to offset the control 2 units to the side.'
	)
	cmds.floatField(
		'offsetYField',
		value=0,
		annotation='Sets the Y position of the ball control.\n'
					'Example: Enter 2 to offset the control 2 units upwards.'
	)
	cmds.floatField(
		'offsetZField',
		value=0,
		annotation='Sets the Z position of the ball control.\n'
					'Example: Enter 2 to offset the control 2 units forward.'
	)
	
	# Create button
	cmds.button(
		label='Create Ball Control',
		annotation='Creates a three-circle ball control.\n'
						'The control shapes can be offset from the\n'
						'from the pivot based off user input.',
		command=create_ball_control_from_ui
	)
	
	
	# -----------------------------------
	# Pole Control
	# -----------------------------------
	
	# Control name input
	cmds.text(label='Input Pole Control Name:')
	cmds.textField('poleControlNameField', text='pole_control')
	
	# Offset pos value input
	cmds.text(label='Input Size Value:')
	
	cmds.floatField(
	'size',
	value=1,
	annotation='Input a size value for the pole control shape'
	)
	
	cmds.text(label='Input Offset Position Values:')
	
	cmds.floatField(
		'poleOffsetXField',
		value=0,
		annotation='Sets the X position of the pole control.\n'
					'Example: Enter 2 to offset the control 2 units to the side.'
	)
	cmds.floatField(
		'poleOffsetYField',
		value=0,
		annotation='Sets the Y position of the pole control.\n'
					'Example: Enter 2 to offset the control 2 units upwards.'
	)
	cmds.floatField(
		'poleOffsetZField',
		value=0,
		annotation='Sets the Z position of the pole control.\n'
					'Example: Enter 2 to offset the control 2 units forward.'
	)
	
	# Create button
	cmds.button(
		label='Create Pole Control',
		annotation='Creates a three-circle pole control.\n'
						'The control shapes can be offset from the\n'
						'from the pivot based off user input.',
		command=create_pole_control_from_ui
	)
	cmds.separator(height=10)
	
	
	# -----------------------------------
	# Snap
	# -----------------------------------
	
	cmds.button(label='Snap to Object', command=gacUtilities.snap_tool)

	cmds.showWindow(window_name)

