'''
Code snippet to skin proxy meshes to their corresponding joints
'''

# create a skinCluster for each proxy mesh with corresponding joint

skin_to_jnt = [
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
]

for jnt in skin_to_jnt:
    # skin proxy mesh to corresponding joint
    if cmds.objExists(jnt):
        mesh = jnt.replace('_Jnt', '_Mesh')
        if cmds.objExists(mesh):
            cmds.skinCluster(jnt, mesh, toSelectedBones=True)
            # Rename skinCluster to follow convention   
            skin_cluster = cmds.ls(cmds.listHistory(mesh), type='skinCluster')[0]
            cmds.rename(skin_cluster, f'{mesh}_SCLS')

