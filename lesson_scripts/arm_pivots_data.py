'''
This script provides functions to save and load the world-space positions of arm pivot locators in Maya.
'''

import os
import json
import maya.cmds as cmds

filepath = r'C:\Users\garve\OneDrive\Documents\maya\scripts'

def save_arm_pivots(pivots, filepath=filepath):
    '''
    Save the current world-space positions of the specified arm pivots.
    
    Args:
        pivots (list): List of arm pivot locator names to save.
        filepath (str): Path to the directory where the arm pivot JSON file will be stored.
    '''

    # Get the JSON file path
    json_path = f'{filepath}\\arm_pivots.json'

    # Get the current pivot positions
    pivot_data = {}

    for pivot in pivots:
        if cmds.objExists(pivot):
            pivot_data[pivot] = {
                'translation': cmds.xform(
                    pivot,
                    query=True,
                    worldSpace=True,
                    translation=True
                )
            }
        else:
            cmds.warning('Arm pivot locator not found: {}'.format(pivot))

    # Save the pivot data to JSON
    with open(json_path, 'w') as json_file:
        json.dump(pivot_data, json_file, indent=4)

    print('Arm pivot data saved to: {}'.format(json_path))


def load_arm_pivots(pivots, filepath=filepath):
    '''
    Load saved world-space positions and apply them to the specified arm pivots.

    Args:
        pivots (list): List of arm pivot locator names to apply the saved data to.
        filepath (str): Path to the directory where the arm pivot JSON file is stored.
    '''

    # Get the JSON file path
    json_path = f'{filepath}\\arm_pivots.json'

    # Check if the JSON file exists
    if not os.path.exists(json_path):
        cmds.warning('Arm pivot data file not found: {}'.format(json_path))
        return

    # Load the pivot data from JSON
    with open(json_path, 'r') as json_file:
        pivot_data = json.load(json_file)

    # Apply the saved positions to the specified pivots
    for pivot in pivots:
        if pivot in pivot_data and cmds.objExists(pivot):
            cmds.xform(
                pivot,
                worldSpace=True,
                translation=pivot_data[pivot]['translation']
            )
        elif pivot not in pivot_data:
            cmds.warning('No saved data found for: {}'.format(pivot))
        else:
            cmds.warning('Arm pivot locator not found: {}'.format(pivot))

