import maya.cmds as cmds

from gacUtilities import create_null_node, create_ball_control, create_pole_control


def create_arm_ik(side=None):
    '''
    Function creates an ikHandle for the arm.
    '''

    ik_arm_grp = f'{side}_armIkJnt_Grp'
    if not cmds.objExists(ik_arm_grp):
        cmds.warning(f"Arm IK group: '{ik_arm_grp}' does not exist in the scene file. "
                     "Aborting IK handle creation.")
    else:
        # Create IK Handle
        arm_ikhandle = cmds.ikHandle(
            startJoint=f'{side}_SHLD_ik_Jnt',
            endEffector=f'{side}_wrist_ik_Jnt',
            name=f'{side}_arm_Ikh'
        )

        # Create IK Handle Null node
        cmds.select(arm_ikhandle[0], replace=True)
        null_node = create_null_node('Null', position='suffix')[0]

        # Query the IK handle's position and apply it to the null node
        ikhandle_pos = cmds.xform(
            arm_ikhandle[0],
            query=True,
            worldSpace=True,
            translation=True
        )
        cmds.xform(null_node, translation=ikhandle_pos, worldSpace=True)

        # Create a control for the IK handle
        ik_control = create_ball_control(
            f'{side}_arm_Ikh_Ctrl',
            offset_pos=(0,0,0)
        )

        # Create IK control null node
        cmds.select(ik_control, replace=True)
        ik_control_null = create_null_node('Null', position='suffix')[0]
        cmds.xform(ik_control_null, translation=ikhandle_pos, worldSpace=True)

        # Constrain the IK handle to the IK control
        cmds.parentConstraint(ik_control, arm_ikhandle[0], maintainOffset=False)

        # Create a pole vector control
        pole_pos = cmds.xform(
            f'{side}_elbow_pole_Loc',
            query=True,
            worldSpace=True,
            translation=True
        )
        pole_vector_control = create_pole_control(
            f'{side}_elbow_Pole_Ctrl',
            offset_pos=(0,0,0)
        )
        # Create a null node for the pole vector control
        cmds.select(pole_vector_control, replace=True)
        pole_vector_null = create_null_node('Null', position='suffix')[0]
        cmds.xform(
            pole_vector_null,
            worldSpace=True,
            translation=pole_pos
        )

        # Create Pole Vector constraint
        cmds.poleVectorConstraint(pole_vector_control, arm_ikhandle[0])
