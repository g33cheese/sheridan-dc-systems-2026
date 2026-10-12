import sys
import maya.cmds as cmds


def snap_tool(*args):
	'''
	This function snaps multiple selected objects together.
	
	First selected object is the source.
	Subsequent selected objects are the targets.
	'''
	
	# Selected objects stored in a variable
	sel = cmds.ls(selection=True)
	
	# Check to see if node is selected
	if not sel:
		cmds.warning('Please select a node')
	else:
		# Source variable, object we will snap too
		source = sel[0]
		targets = sel[1:]
		
		for target in targets:
			parent_const = cmds.parentConstraint(source, target)
			cmds.delete(parent_const)


def show_local_axis(state=True):
	'''
	Function toggles selected node(s) local axis display.
	'''
	
	'''
	# Get selected node
	sel = cmds.ls(selection=True)
	node = sel
	
	# Check to see if node is selected
	if not sel:
		cmds.warning('Please select a node')
	
	# Toggle the local axis display
	for each in node:
		# Get current state of local axis display
		current_state = cmds.getAttr(f'{each}.displayLocalAxis')
		cmds.setAttr(f'{each}.displayLocalAxis', not current_state) # f'string
	'''
	
	# Get the selected node
	sel = cmds.ls(selection=True)

	if not sel:
		cmds.warning('Please select a node.')
		return

	node = sel[0]

	# Set the local axis display
	cmds.setAttr(f'{node}.displayLocalAxis', state)


def create_ball_control(name, offset_pos):
	'''
	Create a ball control.
	'''

	# Create the transform
	control = cmds.createNode('transform', name=name)
	
	# Normals for the three circles
	normals = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
	
	for i in range(3):
		shape = cmds.createNode('nurbsCurve', parent=control, name=f'{name}Shape{i + 1}')
		circle = cmds.createNode('makeNurbCircle', name=f'{name}_makeNurbsCircle{i + 1}')
		# Set the normal of the circle
		cmds.setAttr(f'{circle}.normal', normals[i][0], normals[i][1], normals[i][2])
		# Offset the center
		cmds.setAttr(f'{circle}.center', offset_pos[0], offset_pos[1], offset_pos[2])
		cmds.connectAttr(f'{circle}.outputCurve', f'{shape}.create')
		
	
	# Optional curve to connect the controls origin to the offset shape
	t_curve = cmds.curve(degree=1, p=[(0, 0, 0), (offset_pos[0], offset_pos[1], offset_pos[2])], name=f'{name}t_curve')
	
	# Get the curve shape
	t_curve_shape = cmds.listRelatives(t_curve, children=True, shapes=True)[0]
	cmds.setAttr(f'{t_curve_shape}.template', 1)
	
	# Parent the curve shape under the main control
	cmds.parent(t_curve_shape, control, shape=True, relative=True)
	
	# Delete the temp transform
	cmds.delete(t_curve)

	return control


def create_pole_control(name, offset_pos, size=1):
	'''
	Create a three-axis diamond (pole) control.
	'''

	# Create the main control transform
	control = cmds.createNode('transform', name=name)
	
	# Points for each diamond plane
	points = [
		[
			(0, size, 0),
			(size, 0, 0),
			(0, -size, 0),
			(-size, 0, 0),
			(0, size, 0)],
		[
			(0, 0, size),
			(size, 0, 0),
			(0, 0, -size),
			(-size, 0, 0),
			(0, 0, size)
			],
		[
			(0, size, 0),
			(0, 0, size),
			(0, -size, 0),
			(0, 0, -size),
			(0, size, 0)
		]
	]
	
	for i in range(3):
		offset_points = [
			(p[0] + offset_pos[0], p[1] + offset_pos[1], p[2] + offset_pos[2])
			for p in points[i]
		]
		diamond = cmds.curve(degree=1, point=offset_points, name=f'{name}_temp{i + 1}')
		# Get the curve shape
		shape = cmds.listRelatives(diamond, children=True, shapes=True)[0]
		
		# Move the temp transform so the diamond curve sits at offset_pos

		
		# Parent the curve shape under the main control
		cmds.parent(shape, control, shape=True, relative=True)
		cmds.delete(diamond)
	
	# Optional curve to connect the controls origin to the offset shape
	t_curve = cmds.curve(degree=1, p=[(0, 0, 0), (offset_pos[0], offset_pos[1], offset_pos[2])], name=f'{name}t_curve')
	
	# Get the curve shape
	t_curve_shape = cmds.listRelatives(t_curve, children=True, shapes=True)[0]
	cmds.setAttr(f'{t_curve_shape}.template', 1)
	
	# Parent the curve shape under the main control
	cmds.parent(t_curve_shape, control, shape=True, relative=True)
	
	# Delete the temp transform
	cmds.delete(t_curve)

	return control


