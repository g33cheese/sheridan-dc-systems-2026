import importlib

import maya.cmds as cmds

import gacUtilities
importlib.reload(gacUtilities)
from gacUtilities import create_null_node, create_ball_control


def create_arm_fk(side=None):
    '''
    Function creates an FK arm setup for the specified side (left or right).

    Args:
        side (str): The side of the arm ('L' or 'R') for which to create the FK arm setup.
    '''
    # Clear the current selection in Maya
    cmds.select(clear=True)

    # Check to see if the FK arm group exists
    fk_arm_grp = f'{side}_armFkJnt_Grp'
    if not cmds.objExists(fk_arm_grp):
        cmds.warning(f"Arm FK group: '{fk_arm_grp}' does not exist in the scene file. "
                     "Aborting FK arm creation.")
    # If the FK arm group exists, create the FK Arm Control group
    else:
        # Create a gr
        fk_arm_ctrl_grp = cmds.group(empty=True, name=f'{side}_armFkCtrl_Grp')

        # Create FK Arm Controls
        shoulder_ctrl = create_ball_control(f'{side}_SHLD_fkCtrl', offset_pos=(0,0,0))
        elbow_ctrl = create_ball_control(f'{side}_elbow_fkCtrl', offset_pos=(0,0,0))
        wrist_ctrl = create_ball_control(f'{side}_wrist_fkCtrl', offset_pos=(0,0,0))

        # Position FK controls at the corresponding joint locations
        cmds.xform(shoulder_ctrl, worldSpace=True, matrix=cmds.xform(f'{side}_SHLD_fk_Jnt', query=True, worldSpace=True, matrix=True))
        cmds.xform(elbow_ctrl,
                   worldSpace=True,
                   matrix=cmds.xform(
                       f'{side}_elbow_fk_Jnt',
                       query=True,
                       worldSpace=True,
                       matrix=True
            )
        )
        cmds.xform(wrist_ctrl,
                   worldSpace=True,
                   matrix=cmds.xform(
                       f'{side}_wrist_fk_Jnt',
                       query=True,
                       worldSpace=True,
                       matrix=True
            )
        )
        
        # Create null nodes for FK controls
        shoulder_null = create_null_node('Null', selected_nodes=shoulder_ctrl, position='suffix')
        elbow_null = create_null_node('Null', selected_nodes=elbow_ctrl, position='suffix')
        wrist_null = create_null_node('Null', selected_nodes=wrist_ctrl, position='suffix')

        # Parent FK null nodes to create the FK hierarchy
        cmds.parent(shoulder_null, fk_arm_ctrl_grp)
        cmds.parent(elbow_null, shoulder_ctrl)
        cmds.parent(wrist_null, elbow_ctrl)

        # Constrain FK controls to their corresponding joints
        cmds.parentConstraint(shoulder_ctrl, f'{side}_SHLD_fk_Jnt', maintainOffset=True)
        cmds.parentConstraint(elbow_ctrl, f'{side}_elbow_fk_Jnt', maintainOffset=True)
        cmds.parentConstraint(wrist_ctrl, f'{side}_wrist_fk_Jnt', maintainOffset=True)

        # Clean-up
        for ctl in [shoulder_ctrl, elbow_ctrl, wrist_ctrl]:
            for attr in ['sx', 'sy', 'sz', 'v']:
                cmds.setAttr(f'{ctl}.{attr}', lock=True, keyable=False)

        # Return the FK arm control group and individual controls
        return fk_arm_ctrl_grp[0], shoulder_ctrl, elbow_ctrl, wrist_ctrl

