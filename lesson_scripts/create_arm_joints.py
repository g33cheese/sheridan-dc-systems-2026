import maya.cmds as cmds

def create_arm_joints(locators, side=None, joint_type='bind'):
    '''
    Function creates joints based on arm pivot locator's position
    '''

    # Clear the selection
    cmds.select(clear=True)

    # Create joints for all locators except elbow_mid and elbow_pole.
    excluded_locs = {f'{side}_elbow_mid_Loc', f'{side}_elbow_pole_Loc'}
    for loc in locators:
        if loc in excluded_locs:
            continue

        # Store pivot location data
        pos = cmds.xform(loc, query=True, worldSpace=True, translation=True)
        # Create joints
        pivot_name = loc.replace(f'{side}_', '').replace('_Loc', '')
        jnt_name = f'{side}_{pivot_name}_{joint_type}_Jnt'
        cmds.joint(name=jnt_name, position=pos)

        # Set override colour for the joint
        cmds.setAttr(f'{jnt_name}.overrideEnabled', 1)
        if side == 'L': # Set colour to blue tone
            if joint_type == 'bind': # Set colour to blue
                cmds.setAttr(f'{jnt_name}.overrideColor', 6)
            if joint_type == 'fk': # Set colour to lightblue
                cmds.setAttr(f'{jnt_name}.overrideColor', 29)
            if joint_type == 'ik': # Set colour to red
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
    clav_jnt
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
