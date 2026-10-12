def create_arm_pivots(side=None):
  '''
  Function creates arm pivot locators.
  Locators need to be positioned before joint creation.
  '''

  arm_pivots = [
    'L_SHLD',
    'L_elbow',
    'L_wrist',
    'L_elbow_mid',
    'L_elbow_pole',
    ]

  #--------- Generate Locators/Pivots ---------#
  grp_node = cmds.group(name='L_arm_pivot_Grp', empty=True)
  locators = []

  for arm_pivot in arm_pivots:
    loc_name = f'{arm_pivot}_Loc'
    loc = cmds.spaceLocator(name=loc_name)
    cmds.parent(loc, grp_node)
    locators.append(loc_name)

  cmds.parent('L_elbow_pole_Loc', 'L_elbow_mid_Loc')
  cmds.setAttr('L_elbow_pole_Loc.translateZ', -40)

  # Offseting elbow + wrist locators at start for better visibility
  cmds.setAttr('L_elbow_Loc.translateX', 10)
  cmds.setAttr('L_wrist_Loc.translateX', 20)

  # Constraining elbow_mid_Loc half-way between shoulder/wrist
  cmds.pointConstraint('L_SHLD_Loc', 'L_elbow_mid_Loc', maintainOffset=False)
  cmds.pointConstraint('L_wrist_Loc', 'L_elbow_mid_Loc', maintainOffset=False)

  return locators
