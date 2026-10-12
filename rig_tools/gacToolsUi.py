import importlib
import maya.cmds as cmds

import gacUtilities

importlib.reload(gacUtilities)

def create_pole_control_from_ui(*args):
	
	# Get the control name
	name = cmds.textField('poleControlNameField', query=True, text=True)
	
	# Get the offset position
	offset_x = cmds.floatField('poleOffsetXField', query=True, value=True)
	offset_y = cmds.floatField('poleOffsetYField', query=True, value=True)
	offset_z = cmds.floatField('poleOffsetZField', query=True, value=True)
	size = cmds.floatField('size', query=True, value=True)
	offset_pos = (offset_x, offset_y, offset_z)
	
	# Create the pole control
	gacUtilities.create_pole_control(name, offset_pos, size=size)


def create_ball_control_from_ui(*args):
	
	# Get the control name
	name = cmds.textField('controlNameField', query=True, text=True)
	
	# Get the offset position
	offset_x = cmds.floatField('offsetXField', query=True, value=True)
	offset_y = cmds.floatField('offsetYField', query=True, value=True)
	offset_z = cmds.floatField('offsetZField', query=True, value=True)
	offset_pos = (offset_x, offset_y, offset_z)
	
	# Create the ball control
	gacUtilities.create_ball_control(name, offset_pos)


def show_local_axis_from_ui(*args):
	
	# Get the value from the intField
	value = cmds.intField('localAxisField', query=True, value=True)
	
	# Convert 0 or 1 into False or True
	state = bool(value)
	
	# Show or hide the local axis
	gacUtilities.show_local_axis(state)



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


