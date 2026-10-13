import maya.cmds as cmds

def create_arm_pivots(side=None):
    '''
    Function creates arm pivot locators.
    Locators need to be positioned before joint creation.
    '''

    arm_pivots = [
        'SHLD',
        'elbow',
        'wrist',
        'elbow_mid',
        'elbow_pole',
    ]

    #--------- Generate Locators/Pivots ---------#
    grp_node = cmds.group(name=f'{side}_arm_pivot_Grp', empty=True)
    locators = []

    # Clear the selection
    cmds.select(clear=True)

    for arm_pivot in arm_pivots:
        loc_name = f'{side}_{arm_pivot}_Loc'
        loc = cmds.spaceLocator(name=loc_name)
        cmds.parent(loc, grp_node)
        locators.append(loc_name)

    cmds.parent(f'{side}_elbow_pole_Loc', f'{side}_elbow_mid_Loc')
    cmds.setAttr(f'{side}_elbow_pole_Loc.translateZ', -40)

    # Offseting elbow + wrist locators at start for better visibility
    cmds.setAttr(f'{side}_elbow_Loc.translateX', 10)
    cmds.setAttr(f'{side}_wrist_Loc.translateX', 20)

    # Constraining elbow_mid_Loc half-way between shoulder/wrist
    cmds.pointConstraint(f'{side}_SHLD_Loc', f'{side}_elbow_mid_Loc', maintainOffset=False)
    cmds.pointConstraint(f'{side}_wrist_Loc', f'{side}_elbow_mid_Loc', maintainOffset=False)

    cmds.select(clear=True)

    return locators


def mirror_arm_pivots():
    '''
    Create right arm pivots from the left arm pivot locations.
    '''

    # Define the left and right pivot names
    left_pivots = [
        'L_SHLD_Loc',
        'L_elbow_Loc',
        'L_wrist_Loc',
        'L_elbow_mid_Loc',
        'L_elbow_pole_Loc'
    ]

    right_locators = []

    for left_pivot in left_pivots:
        # Check if the left pivot exists
        if not cmds.objExists(left_pivot):
            cmds.warning('Pivot locator not found: {}'.format(left_pivot))
            continue

        # Get the left pivot world-space position
        position = cmds.xform(left_pivot, query=True, worldSpace=True, translation=True)

        # Mirror the X position
        mirrored_position = [-position[0],  position[1],  position[2]]

        # Create the right pivot name
        right_pivot = left_pivot.replace('L_', 'R_', 1)

        # Create the right pivot locator
        if cmds.objExists(right_pivot):
            cmds.warning('Right pivot already exists: {}'.format(right_pivot))
            right_locators.append(right_pivot)
            continue

        right_pivot = cmds.spaceLocator(name=right_pivot)[0]

        # Apply the mirrored position
        cmds.xform(right_pivot, worldSpace=True, translation=mirrored_position)
        right_locators.append(right_pivot)

    return right_locators
