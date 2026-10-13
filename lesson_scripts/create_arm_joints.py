import maya.cmds as cmds

def create_arm_joints(locators, side=None, joint_type='bind'):
    '''
    Function creates joints based on arm pivot locator's position
    '''

    # Clear the selection
    cmds.select(clear=True)

    # Create joints for all locators except elbow_mid and elbow_pole.
    excluded_pivots = {'elbow_mid', 'elbow_pole'}
    for loc in locators:
        source_loc = loc
        pivot_name = loc.replace('_Loc', '')
        source_side = None
        if pivot_name.startswith('L_') or pivot_name.startswith('R_'):
            source_side = pivot_name[0]
            pivot_name = pivot_name[2:]

        if pivot_name in excluded_pivots:
            continue

        # If requested side differs, prefer the matching side locator if it exists.
        if side and source_side and source_side != side:
            side_loc = f'{side}_{pivot_name}_Loc'
            if cmds.objExists(side_loc):
                source_loc = side_loc

        # Store pivot location data
        pos = cmds.xform(source_loc, query=True, worldSpace=True, translation=True)
        # Create joints
        jnt_name = f'{side}_{pivot_name}_{joint_type}_Jnt'
        cmds.joint(name=jnt_name, position=pos)

        # Set override colour for the joint
        cmds.setAttr(f'{jnt_name}.overrideEnabled', 1)
        if side == 'L': # Set colour to blue tone
            if joint_type == 'bind': # Set colour to blue
                cmds.setAttr(f'{jnt_name}.overrideColor', 6)
            if joint_type == 'fk': # Set colour to light blue
                cmds.setAttr(f'{jnt_name}.overrideColor', 29)
            if joint_type == 'ik': # Set colour to dark blue
                cmds.setAttr(f'{jnt_name}.overrideColor', 15)
        elif side == 'R': # Set colour to red tone                
            if joint_type == 'bind': # Set colour to red                    
                cmds.setAttr(f'{jnt_name}.overrideColor', 13)
            if joint_type == 'fk': # Set colour to rust red
                cmds.setAttr(f'{jnt_name}.overrideColor', 12)
            if joint_type == 'ik': # Set colour to dark red
                cmds.setAttr(f'{jnt_name}.overrideColor', 4)
        elif not side:
            cmds.warning('Side not specified for joint: {}'.format(jnt_name))

    # Create an arm joint group, parent the shoulder jnt under it
    shld_jnt = f'{side}_SHLD_{joint_type}_Jnt'

    # Check to see if the principal arm joint group exists before creating it
    arm_jnt_grp = f'{side}_armJnt_Grp'
    if not cmds.objExists(arm_jnt_grp):
        cmds.group(name=arm_jnt_grp, empty=True)

    # Create a group for the joint type if it doesn't exist
    joint_type_grp = f'{side}_arm{joint_type.capitalize()}Jnt_Grp'
    if not cmds.objExists(joint_type_grp):
        cmds.group(name=joint_type_grp, empty=True)

    # Set up hiearchy
    cmds.parent(shld_jnt, joint_type_grp)
    cmds.parent(joint_type_grp, arm_jnt_grp)



def orient_arm_joints(side, joint_type):
    '''
    Orient the arm joints with local X pointing down the bone.

    Args:
        side (str): The side of the arm ('L' or 'R').
        joint_type (str): The type of joint ('bind', 'fk', 'ik').
    '''

    root_joint = '{}_SHLD_{}_Jnt'.format(side, joint_type)

    if cmds.objExists(root_joint):
        cmds.joint(
            root_joint,
            edit=True,
            orientJoint='xzy',
            secondaryAxisOrient='yup',
            autoOrientSecondaryAxis=False,
            children=True,
            zeroScaleOrient=True
        )

    # R side: orientJoint='xyzNeg',
        
def mirror_arm_joints():
    '''
    Mirror the left arm joint chains to the right side,
    create joint groups, and set joint colours.
    '''

    # Create the right arm joint group if it doesn't exist
    right_arm_grp = 'R_armJnt_Grp'
    if not cmds.objExists(right_arm_grp):
        cmds.group(name=right_arm_grp, empty=True)

    # Mirror the bind joint chain
    if cmds.objExists('L_SHLD_bind_Jnt'):
        right_root = cmds.mirrorJoint(
            'L_SHLD_bind_Jnt',
            mirrorYZ=True,
            mirrorBehavior=True,
            searchReplace=('L_', 'R_')
        )[0]

        cmds.group(right_root, name='R_armBindJnt_Grp', parent=right_arm_grp)

        joints = [right_root] + (
            cmds.listRelatives(right_root, allDescendents=True, type='joint') or []
        )

        for jnt_name in joints:
            cmds.setAttr('{}.overrideEnabled'.format(jnt_name), 1)
            cmds.setAttr('{}.overrideColor'.format(jnt_name), 13)

    # Mirror the FK joint chain
    if cmds.objExists('L_SHLD_fk_Jnt'):
        right_root = cmds.mirrorJoint(
            'L_SHLD_fk_Jnt',
            mirrorYZ=True,
            mirrorBehavior=True,
            searchReplace=('L_', 'R_')
        )[0]

        cmds.group(right_root, name='R_armFkJnt_Grp', parent=right_arm_grp)

        joints = [right_root] + (
            cmds.listRelatives(right_root, allDescendents=True, type='joint') or []
        )

        for jnt_name in joints:
            cmds.setAttr('{}.overrideEnabled'.format(jnt_name), 1)
            cmds.setAttr('{}.overrideColor'.format(jnt_name), 12)

    # Mirror the IK joint chain
    if cmds.objExists('L_SHLD_ik_Jnt'):
        right_root = cmds.mirrorJoint(
            'L_SHLD_ik_Jnt',
            mirrorYZ=True,
            mirrorBehavior=True,
            searchReplace=('L_', 'R_')
        )[0]

        cmds.group(right_root, name='R_armIkJnt_Grp', parent=right_arm_grp)

        joints = [right_root] + (
            cmds.listRelatives(right_root, allDescendents=True, type='joint') or []
        )

        for jnt_name in joints:
            cmds.setAttr('{}.overrideEnabled'.format(jnt_name), 1)
            cmds.setAttr('{}.overrideColor'.format(jnt_name), 4)

