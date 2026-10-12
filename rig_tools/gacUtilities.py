'''
GAC Utilities

This module contains utility functions for rigging in Maya.
'''

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


def find_centre_of_selection(*args):
	'''
	Function finds the centre point of the selected objects.
	'''
	
	# Get selected objects
	sel = cmds.ls(selection=True)
	
	# Check to see if nodes are selected
	if not sel:
		cmds.warning('Please select at least one node')
		return None
	
	# Take the position of all selected nodes and find the average position
	position = [0.0, 0.0, 0.0]
	for node in sel:
		pos = cmds.xform(node, query=True, worldSpace=True, translation=True)
		position[0] += pos[0]
		position[1] += pos[1]
		position[2] += pos[2]

	centre = position
	
	# Divide by the number of selected objects to get the average
	num_objects = len(sel)
	centre = [coord / num_objects for coord in position]

	# Create a locator at the calculated centre point
	centre_locator = cmds.spaceLocator(name=f'{sel[0]}_centre_01_loc')[0]
	cmds.xform(centre_locator, worldSpace=True, translation=centre)

	# Set the locator shape's color to increase visibility
	cmds.setAttr(f'{centre_locator}Shape.overrideEnabled', 1)
	cmds.setAttr(f'{centre_locator}Shape.overrideColor', 17)
	
	return centre_locator


def show_local_axis():
	'''
	Function toggles selected node(s) local axis display.
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
		cmds.setAttr(f'{each}.displayLocalAxis', not current_state)
	

def create_joint(name, size=1.0):
	'''
	Create a joint at the selection.

	Args:
		name (str): Name of the joint.
		size (float): Size of the joint.
	
	Returns:
		list: List of created joints.

	'''

	# Get the current selection
	sel = cmds.ls(selection=True)

	if not sel:
		cmds.warning('Nothing is selected. Creating a joint at origin.')

		joint = cmds.createNode('joint', name=f'{name}_01_jnt')
		cmds.setAttr(f'{joint}.radius', size)
		return [joint]

	for index, node in enumerate(sel, start=1):
		# Store the selected node's world-space transform.
		matrix = cmds.xform(
			node,
			query=True,
			worldSpace=True,
			matrix=True
		)

		# Create the joint at the current selection
		joint =cmds.createNode('joint', name=f'{name}_{index:02d}_jnt')
		cmds.xform(joint, worldSpace=True, matrix=matrix)
		cmds.setAttr(f'{joint}.radius', size)

	return [joint]


def create_locator(name, size):
	'''
	Create a locator at the selection.

	Args:
		name (str): Name of the locator.
		size (float): Size of the locator.

	Returns:
		list: List of the created locators.
	'''

	# Get the current selection
	sel = cmds.ls(selection=True)
	if not sel:
		cmds.warning('Nothing is selected. Creating a locator at origin.')

		locator = cmds.spaceLocator(name=f'{name}_01_loc')[0]
		cmds.setAttr(f'{locator}.localScaleX', size)
		cmds.setAttr(f'{locator}.localScaleY', size)
		cmds.setAttr(f'{locator}.localScaleZ', size)

		return [locator]

	locators = []

	for index, node in enumerate(sel, start=1):
		# Store the selected node's world-space transform.
		matrix = cmds.xform(
			node,
			query=True,
			worldSpace=True,
			matrix=True
		)

		# Create the locator at the current selection
		locator = cmds.spaceLocator(name=f'{name}_{index:02d}_loc')[0]

		# Match the selected node's world-space transform
		cmds.xform(locator, worldSpace=True, matrix=matrix)

		# Set the locator's size
		cmds.setAttr(f'{locator}.localScaleX', size)
		cmds.setAttr(f'{locator}.localScaleY', size)
		cmds.setAttr(f'{locator}.localScaleZ', size)

		locators.append(locator)

	return locators



def create_null_node(name, position='suffix'):
	'''
	Create a null node for each selected node.

	Args:
		name (str): Name to add as a prefix or suffix.
		position (str): Whether name is added as a 'prefix' or 'suffix'.

	Returns:
		list: List of created null nodes.
	'''

	sel = cmds.ls(selection=True)

	if not sel:
		cmds.warning('Nothing is selected. Creating null node at origin.')
		null = cmds.group(name=name, empty=True, world=True)

		return [null]

	nulls = []

	for node in sel:

		# Store the selected node's world-space transform.
		matrix = cmds.xform(node, query=True, worldSpace=True, matrix=True)

		# Store the node's current parent
		parent = cmds.listRelatives(node, parent=True)

		# Build the null name.
		if position == 'prefix':
			null_name = f'{name}_{node}'
		else:
			null_name = f'{node}_{name}'

		# Create the null at the origin.
		null = cmds.group(name=null_name,
			empty=True,
			world=True
		)

		# Match the selected node's world-space transform.
		cmds.xform(null, worldSpace=True, matrix=matrix)

		# Parent the null under the selected node's parent (if it exists)
		if parent:
			cmds.parent(null, parent[0])

		# Parent the selected node under the new null.
		cmds.parent(node, null)

		nulls.append(null)

	return nulls


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


def bind_like(*args):
	'''
	Copy the skinning influence from one object to another.
	After the skinCluster is created and the target object is skinned, 
	this function will copy the skinweights from the source object to the target object.

	Args:
		source (str): The source object to copy skinweights from.
		target (str): The target object to copy skinweights to.
		skinCluster (str): The skinCluster node associated with the target object.
	'''

	sel = cmds.ls(selection=True)

	if len(sel) < 2:
		cmds.warning("Please select at least the source and target objects.")
		return

	source = sel[0]
	target = sel[1]

	# Find the source skinCluster node
	source_skin_clusters = cmds.ls(cmds.listHistory(source), type='skinCluster') or []
	if not source_skin_clusters:
		cmds.warning("No skinCluster found on the source object.")
		return

	source_skin_cluster = source_skin_clusters[0]

	# Find the source objects skinCluster influences
	skin_influences = cmds.skinCluster(source, query=True, influence=True)
	if not skin_influences:
		cmds.warning("No skinCluster influences found on the source object.")
		return

	# Select the target object and skin_influences and create a new skinCluster
	cmds.select([target] + skin_influences)
	skin_cluster = cmds.skinCluster(toSelectedBones=True)[0]

	# Copy the skin weights from the source object to the target object
	cmds.copySkinWeights(sourceSkin=source_skin_cluster, destinationSkin=skin_cluster, noMirror=True, surfaceAssociation='closestPoint', influenceAssociation='closestJoint')

	# Rename the skinCluster
	skin_cluster_name = cmds.rename(skin_cluster, f'{target}_SCLS')

	return skin_cluster_name

