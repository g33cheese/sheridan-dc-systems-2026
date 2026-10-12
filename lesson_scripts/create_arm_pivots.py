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
