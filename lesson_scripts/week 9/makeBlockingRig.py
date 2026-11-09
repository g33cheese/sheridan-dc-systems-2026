'''
Week 9 
Code snippets to build the Stage 2: Blocking Rig 

This includes creating rig module pivots, building the rig, making twists,
mirroring the right side, setting up parent constraints, cleaning the hierarchy,
applying global scale constraints, and connecting proxy geometry.

Grouping the rig groups still needs full implementation

'''

from maya import cmds

import importlib

import den_Utilities_v13 as denUt
import den_BipedRigTools_v13 as denBR


# Create Rig Module Pivots
denBR.den_makeBipedTorsoPivs()
denBR.den_makeBipedLegPivs()
denBR.den_makeBipedArmPivs()
denBR.den_makeBipedHandPivs2()
denBR.den_makeEyePiv()

# Build Rig
denBR.den_makeBipedTorsoRig()
denBR.den_makeBipedArmRig()
denBR.den_makeBipedHandRig()
denBR.den_makeBipedLegRig()
denBR.den_makeEyeRig()

# Make Twist
denBR.den_makeTwists()

# Mirroring is handled by manually duplicating the left side pivots, renaming the 'L_' to 'R_' and then calling...
denBR.den_makeBipedLegRig(side='R_', twistType='twist')
denBR.den_makeBipedArmRig(side='R_', twistType='twist')
denBR.den_makeBipedHandRig(side='R_')
denBR.den_makeEyeRig(side='R_')

# Parent Constraint for modules
cmds.parentConstraint('Cog_Ctrl', 'Torso_SpaceIN', mo=True)  #Torso
for side in ['L', 'R']:
    cmds.parentConstraint('ChestSpace_OUT', f'{side}_Chest_SpaceIN', mo=True)  # Arms
    cmds.parentConstraint('PelvisSpace_OUT', f'{side}_PelvisSpace_IN', mo=True)  # Legs
    cmds.parentConstraint('AllSpace_OUT', f'{side}_AllSpace_IN', mo=True)  # IK Legs
    cmds.parentConstraint(f'{side}_Wrist_SpaceOUT', f'{side}_Wrist_SpaceIN', mo=True)  # Hands
    cmds.parentConstraint('HeadSpace_OUT', f'{side}_EyeSpace_IN', mo=True)  # Eyes

# Clean hierarchy 
pivot_grp = 'Pivot_Grp'
cmds.group(
    'rollerGirl_Piv_Grp',
    'TorsoPiv_Grp',
    'L_LegPiv_Grp',
    'R_LegPiv_Grp',
    'L_ArmPiv_Grp',
    'R_ArmPiv_Grp',
    'L_HandPiv_Grp',
    'L_EyePiv_Grp',
    'R_EyePiv_Grp',
    'R_HandPiv_Grp',
    name=pivot_grp
    )
cmds.setAttr(f'{pivot_grp}.v', 0)

rig_grp = 'Rig_Grp'
cmds.group(
    'Base_Grp',
    'Torso_Grp',
    'L_Leg_Grp',
    'R_Leg_Grp',
    'L_Arm_Grp',
    'R_Arm_Grp',
    'L_EyeRig_Grp',
    'R_EyeRig_Grp',
    'L_Hand_Grp',
    'R_Hand_Grp',
    name=rig_grp
)

# Global Scale
for rig_grp in ['Torso_SpaceIN', 'L_Leg_Grp', 'R_Leg_Grp', 'L_Arm_Grp', 'R_Arm_Grp']:
    cmds.scaleConstraint('All_Ctrl', rig_grp, mo=True)

# 12. Connecting Proxy Geo - Connectboxgeo and Connectproxygeo script
# connects proxy/sushi geo with _Mesh suffix to corresponging joint with _Jnt suffix
denUt.den_connectProxyGeo(Jnts=[
    'Head_Jnt',
    'Jaw_Jnt',
    'L_Eye_Jnt',
    'R_Eye_Jnt',
    'Neck01_Jnt',
    'Chest_Jnt',
    'Spine02_Jnt',
    'Spine01_Jnt',
    'Pelvis_Jnt',
    'L_Clav_Jnt',
    'L_ShldTwist01_Jnt',
    'L_ShldTwist02_Jnt',
    'L_ShldTwist03_Jnt',
    'L_ElbowTwist01_Jnt',
    'L_ElbowTwist02_Jnt',
    'L_ElbowTwist03_Jnt',
    'L_Thumb01_Jnt',
    'L_Thumb02_Jnt',
    'L_Thumb03_Jnt',
    'L_Index00_Jnt',
    'L_Index01_Jnt',
    'L_Index02_Jnt',
    'L_Index03_Jnt',
    'L_Middle00_Jnt',
    'L_Middle01_Jnt',
    'L_Middle02_Jnt',
    'L_Middle03_Jnt',
    'L_Ring00_Jnt',
    'L_Ring01_Jnt',
    'L_Ring02_Jnt',
    'L_Ring03_Jnt',
    'L_Pinky00_Jnt',
    'L_Pinky01_Jnt',
    'L_Pinky02_Jnt',
    'L_Pinky03_Jnt',
    'L_HipTwist01_Jnt',
    'L_HipTwist02_Jnt',
    'L_HipTwist03_Jnt',
    'L_KneeTwist01_Jnt',
    'L_KneeTwist02_Jnt',
    'L_KneeTwist03_Jnt',
    'L_Ankle_Jnt',
    'L_Ball_Jnt',
    'R_Clav_Jnt',
    'R_ShldTwist01_Jnt',
    'R_ShldTwist02_Jnt',
    'R_ShldTwist03_Jnt',
    'R_ElbowTwist01_Jnt',
    'R_ElbowTwist02_Jnt',
    'R_ElbowTwist03_Jnt',
    'R_Thumb01_Jnt',
    'R_Thumb02_Jnt',
    'R_Thumb03_Jnt',
    'R_Index00_Jnt',
    'R_Index01_Jnt',
    'R_Index02_Jnt',
    'R_Index03_Jnt',
    'R_Middle00_Jnt',
    'R_Middle01_Jnt',
    'R_Middle02_Jnt',
    'R_Middle03_Jnt',
    'R_Ring00_Jnt',
    'R_Ring01_Jnt',
    'R_Ring02_Jnt',
    'R_Ring03_Jnt',
    'R_Pinky00_Jnt',
    'R_Pinky01_Jnt',
    'R_Pinky02_Jnt',
    'R_Pinky03_Jnt',
    'R_HipTwist01_Jnt',
    'R_HipTwist02_Jnt',
    'R_HipTwist03_Jnt',
    'R_KneeTwist01_Jnt',
    'R_KneeTwist02_Jnt',
    'R_KneeTwist03_Jnt',
    'R_Ankle_Jnt',
    'R_Ball_Jnt'
])

# Constraint the jx meshes to their corresponding jx joints
jx_mesh = {
'Shld_Jx' : 'Shld_Mesh',
'Elbow_Jx' : 'Elbow_Mesh',
'Hip_Jx' : 'Hip_Mesh'
}

for jx_jnt, mesh in jx_mesh.items():
    for side in ['L', 'R']:
        cmds.parentConstraint(f'{side}_{jx_jnt}', f'{side}_{mesh}', mo=True)
        cmds.scaleConstraint(f'{side}_{jx_jnt}', f'{side}_{mesh}', mo=True)

# Clean-up
rig_to_hide = [
    'L_ArmSkel_Grp',
    'L_HandSkel_Grp',
    'L_LegSkel_Grp',
    'R_ArmSkel_Grp',
    'R_HandSkel_Grp',
    'R_LegSkel_Grp',
    'L_HeelRev_Jx', 
    'R_HeelRev_Jx',
    'L_Eye_Jnt',
    'R_Eye_Jnt',
    'Pelvis_Jnt',
    'Pelvis_Loc',
    'Chest_Loc',
    'Spine01_JntIkh',
    'Spine02_JntIkh',
    'Head_Loc',
    'Neck01_JntIkh',
    'L_Shld_Ikh',
    'R_Shld_Ikh',
    'L_Clav_Ikh',
    'R_Clav_Ikh',
    'L_Eye_LocShape',
    'R_Eye_LocShape'
]
# Hide joints
for rig in rig_to_hide:
    if cmds.objExists(rig):
        cmds.setAttr(f'{rig}.v', 0)

