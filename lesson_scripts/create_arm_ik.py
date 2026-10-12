def create_arm_ik(locators, side=None):
  '''
  Function creates an ikHandle for the arm.
  '''

  if not cmds.objExists('*_arm_jnt_Grp'):
    cmds.warning('Arm joints do not exist in the scene file. '
      'Aborting ikHandle creation.')
  else:
    # Create IK Handle
    arm_ikhandle = cmds.ikHandle(startJoint='L_SHLD_Jnt', endEffector='L_wrist_Jnt', name='L_arm_Ikh')

    # Create IK Handle Null node
    ikhandle_pos = cmds.xform(arm_ikhandle[0], query=True, worldSpace=True, translation=True)
    null_node = cmds.group(name=f'{arm_ikhandle[0]}_Null', empty=True)
    cmds.xform(null_node, translation=ikhandle_pos, worldSpace=True)
    cmds.parent(arm_ikhandle[0], null_node)

    # Create Pole Vector
    cmds.poleVectorConstraint('L_elbow_pole_Loc', arm_ikhandle[0])
