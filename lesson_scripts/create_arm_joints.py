def create_arm_joints(locators, side=None):
  '''
  Function creates joints based on arm pivot locator's position
  '''

  # Clear the selection
  cmds.select(clear=True)

  for loc in locators[:3]:
    # Store pivot location data
    pos = cmds.xform(loc, query=True, worldSpace=True, translation=True)
    # Create joints
    jnt = cmds.joint(name=loc.replace('Loc', 'Jnt'), position=pos)

  # Create an arm joint group, parent the shoulder jnt under it
  shld_jnt = locators[0].replace('Loc', 'Jnt')
  arm_jnt_grp = cmds.group(name='L_arm_jnt_Grp', empty=True)
  cmds.parent(shld_jnt, arm_jnt_grp)
