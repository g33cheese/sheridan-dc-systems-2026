import sys; sys.dont_write_bytecode=True
import importlib
import maya.cmds as cmds

import den_Utilities_v12 as denUt
importlib.reload(denUt)
print(denUt.__file__)

import den_BipedRigTools_v12c as denBR
importlib.reload(denBR)
print(denBR.__file__)

import den_SluggyRigTools_v12 as denSR
importlib.reload(denSR)
print(denSR.__file__)

import den_TrexRigTools_v12c as denTR
importlib.reload(denTR)
print(denTR.__file__)



def PPathUI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'PythonProj_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'PythonProj_Window' )

    # - find out what the maya workspace is
    myProjDir = cmds.workspace( q=True, rootDirectory=True )


    # - make the window object
    myPythonProjWindow = cmds.window( 'PythonProj_Window' )

    # - make a single column object inside the window object
    cmds.columnLayout( adjustableColumn=True )
    # - make a two column layout inside the single column oject
    myLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1,'right',10), columnWidth=((1,160),(2,360)) )
    # - make a label and a textfield in the two column object
    cmds.text( label='Project Scripts Folder --' )
    projName = cmds.textField( text=myProjDir+'scripts/ShelfTools' )
    # - jump back up to the single column object
    cmds.setParent('..')


    #- build the commands that the buttons execute

    # - command to print out the paths in the python path
    def printPythonPathList(foo):
        for pythonPath in sys.path:
            print( 'path----', pythonPath )


    # - command to add my custom path to the python path
    def myCommand(foo):
        doCmd = True
        projString = cmds.textField( projName, query=True, text=True )
        print( 'projString =', projString )
        for pythonPath in sys.path:
            print( pythonPath )
            if pythonPath == projString:
                print( 'WARNING', pythonPath, 'already exits, not adding' )
                doCmd = False
        if doCmd:
            print( 'adding', projString, 'to the python path' )
            sys.path.append( projString )



    # - make the button objects that execute the commands
    cmds.button( label='Add Projects Scripts folder specified above to the Python Path' , command=myCommand )
    cmds.button( label='Print Python Path List', command=printPythonPathList )



    # - make the window object visible on screen
    cmds.showWindow( myPythonProjWindow )


def RyanPPUI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'PythonProj_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'PythonProj_Window' )
    
    # - find out what the maya workspace is
    myProjDir = cmds.workspace( q=True, rootDirectory=True )
    
    
    # - make the window object
    myPythonProjWindow = cmds.window( 'PythonProj_Window' )
    
    # - make a single column object inside the window object
    cmds.columnLayout( adjustableColumn=True )
    
    """By Ryan"""
    
    """Make a function to call the file browser window""" 
    def ryan_OpenFolderBrowser(ignore):
        folderSelected = cmds.fileDialog2( caption="Select the scripts folder", dialogStyle=2, okc="select", fm=3 )
        
        if folderSelected:
            cmds.textField( projName, edit=True, text=folderSelected[0] )
            print("Selected scripts file path: " + folderSelected[0])
        else:
            print("No folder selected")
    
    """Make a button to open the browser window for the users"""     
    cmds.button( label="Browse Scripts Folder", command = ryan_OpenFolderBrowser )
    
    """Ryan Out"""
    
    # - make a two column layout inside the single column oject
    myLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1,'right',10), columnWidth=((1,160),(2,360)) )
    
    
    # - make a label and a textfield in the two column object
    cmds.text( label='Project Scripts Folder --' )
    projName = cmds.textField( text=myProjDir+'scripts/ShelfTools' )
    
    # - jump back up to the single column object
    cmds.setParent('..')
    
    
    #- build the commands that the buttons execute
    
    # - command to print out the paths in the python path
    def printPythonPathList(ignore):
        for pythonPath in sys.path:
            print( 'path----', pythonPath )
    
    
    # - command to add my custom path to the python path
    def myCommand(ignore):
        doCmd = True
        projString = cmds.textField( projName, query=True, text=True )
        print( 'projString =', projString )
        for pythonPath in sys.path:
            print( pythonPath )
            if pythonPath == projString:
                print( 'WARNING', pythonPath, 'already exits, not adding' )
                doCmd = False
        if doCmd:
            print( 'adding', projString, 'to the python path' )
            sys.path.append( projString )
    
    
    
    # - make the button objects that execute the commands
    cmds.button( label='Add Projects Scripts folder specified above to the Python Path' , command=myCommand )
    cmds.button( label='Print Python Path List', command=printPythonPathList )
    
    
    
    # - make the window object visible on screen
    cmds.showWindow( myPythonProjWindow )


def AxisUI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'ShowHideLocalAxis_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'ShowHideLocalAxis_Window' )

    # - make the window object
    ShowHideLocalAxisWindow = cmds.window( 'ShowHideLocalAxis_Window' )


    cmds.columnLayout( adjustableColumn=True )

    cmds.button( label='display local axis', command='denUt.den_ShowLocalAxis(1)' )
    cmds.button( label='hide local axis', command='denUt.den_ShowLocalAxis(0)' )

    #denUt.den_ShowLocalAxis(0)



    # - make the window object visible on screen
    cmds.showWindow( ShowHideLocalAxisWindow )


def Many1UI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'CombineShapesIntoOneNode_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'CombineShapesIntoOneNode_Window' )

    # - make the window object
    CombineShapesIntoOneNodeWindow = cmds.window( 'CombineShapesIntoOneNode_Window' )

    # - make a single column object inside the window object
    cmds.columnLayout( adjustableColumn=True )

    # - make a two column layout for the rqdius and the doT of the Ctrl
    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 100), (2, 100)] )
    cmds.text( label='use World Space' )
    worldSpace_YN = cmds.intField()
    cmds.setParent('..')

    # - make a command that builds the Ctrl
    def makeCmd(ignore):
        worldSpaceValue = cmds.intField( worldSpace_YN, query=True, value=True)
        denUt.den_CombineShapesIntoOneNode( worldSpace=worldSpaceValue )

    # - make a button to execute the command
    cmds.button ( label='Combine Shapes', command=makeCmd )


    # - make the window object visible on screen
    cmds.showWindow( CombineShapesIntoOneNodeWindow )


def ColorUI():
    if (cmds.window("Color_Window", exists=True)):
        cmds.deleteUI("Color_Window")
    Color_Window = cmds.window( 'Color_Window', title="Color Nodes", topLeftCorner = [160,240], toolbox = True)

    cmds.columnLayout( adjustableColumn=True )


    cmds.text( label='Change Shape Override Color', height=50 )

    cmds.rowColumnLayout( numberOfColumns = 4, columnWidth = [(1,60), (2,60), (3,60), (4,60), (5,60)], height = 200 )

    cmds.button( label='Reset', backgroundColor = [0.188,0.188,0.188], command = 'denUt.den_ColorShape(0)' )
    cmds.button( label='Color 01', backgroundColor = [0,0,0], command = 'denUt.den_ColorShape(1)' )
    cmds.button( label='Color 02', backgroundColor = [0.25,0.25,0.25], command = 'denUt.den_ColorShape(2)' )
    cmds.button( label='Color 03', backgroundColor = [0.6,0.6,0.6], command = 'denUt.den_ColorShape(3)' )
    cmds.button( label='Color 04', backgroundColor = [0.6,0,0.16], command = 'denUt.den_ColorShape(4)' )
    cmds.button( label='Color 05', backgroundColor = [0,0.01,0.38], command = 'denUt.den_ColorShape(5)' )
    cmds.button( label='Color 06', backgroundColor = [0,0,0.99], command = 'denUt.den_ColorShape(6)' )
    cmds.button( label='Color 07', backgroundColor = [0,0.27,0.1], command = 'denUt.den_ColorShape(7)' )
    cmds.button( label='Color 08', backgroundColor = [0.15,0,0.26], command = 'denUt.den_ColorShape(8)' )
    cmds.button( label='Color 09', backgroundColor = [0.79,0,0.79], command = 'denUt.den_ColorShape(9)' )
    cmds.button( label='Color 10', backgroundColor = [0.54,0.28,0.2], command = 'denUt.den_ColorShape(10)' )
    cmds.button( label='Color 11', backgroundColor = [0.25,0.14,0.12], command = 'denUt.den_ColorShape(11)' )
    cmds.button( label='Color 12', backgroundColor = [0.6,0.15,0], command = 'denUt.den_ColorShape(12)' )
    cmds.button( label='Color 13', backgroundColor = [1,0,0], command = 'denUt.den_ColorShape(13)' )
    cmds.button( label='Color 14', backgroundColor = [0,1,0], command = 'denUt.den_ColorShape(14)' )
    cmds.button( label='Color 15', backgroundColor = [0,0.26,0.6], command = 'denUt.den_ColorShape(15)' )
    cmds.button( label='Color 16', backgroundColor = [1,1,1], command = 'denUt.den_ColorShape(16)' )
    cmds.button( label='Color 17', backgroundColor = [1,1,0], command = 'denUt.den_ColorShape(17)' )
    cmds.button( label='Color 18', backgroundColor = [0.39,0.86,1], command = 'denUt.den_ColorShape(18)' )
    cmds.button( label='Color 19', backgroundColor = [0.26,1,0.64], command = 'denUt.den_ColorShape(19)' )
    cmds.button( label='Color 20', backgroundColor = [1,0.69,0.69], command = 'denUt.den_ColorShape(20)' )
    cmds.button( label='Color 21', backgroundColor = [0.89,0.67,0.47], command = 'denUt.den_ColorShape(21)' )
    cmds.button( label='Color 22', backgroundColor = [1,1,0.4], command = 'denUt.den_ColorShape(22)' )
    cmds.button( label='Color 23', backgroundColor = [0,0.6,0.33], command = 'denUt.den_ColorShape(23)' )
    cmds.button( label='Color 24', backgroundColor = [0.63,0.42,0.19], command = 'denUt.den_ColorShape(24)' )
    cmds.button( label='Color 25', backgroundColor = [0.62,0.63,0.19], command = 'denUt.den_ColorShape(25)' )
    cmds.button( label='Color 26', backgroundColor = [0.41,0.63,0.19], command = 'denUt.den_ColorShape(26)' )
    cmds.button( label='Color 27', backgroundColor = [0.19,0.64,0.36], command = 'denUt.den_ColorShape(27)' )
    cmds.button( label='Color 28', backgroundColor = [0.19,0.64,0.63], command = 'denUt.den_ColorShape(28)' )
    cmds.button( label='Color 29', backgroundColor = [0.19,0.40,0.63], command = 'denUt.den_ColorShape(29)' )
    cmds.button( label='Color 30', backgroundColor = [0.44,0.19,0.64], command = 'denUt.den_ColorShape(30)' )
    cmds.button( label='Color 31', backgroundColor = [0.64,0.18,0.42], command = 'denUt.den_ColorShape(31)' )

    cmds.setParent('..')

    cmds.button( label='turn off Shapes color override', command = 'denUt.den_ColorShape(den_color=0, override=False)' )


    cmds.text( label=' ', height=50 )
    cmds.text( label='Change Objects Override Color', height=50 )

    cmds.rowColumnLayout( numberOfColumns = 4, columnWidth = [(1,60), (2,60), (3,60), (4,60), (5,60)], height = 200 )

    cmds.button( label='Reset', backgroundColor = [0.188,0.188,0.188], command = 'denUt.den_ColorObject(0)' )
    cmds.button( label='Color 01', backgroundColor = [0,0,0], command = 'denUt.den_ColorObject(1)' )
    cmds.button( label='Color 02', backgroundColor = [0.25,0.25,0.25], command = 'denUt.den_ColorObject(2)' )
    cmds.button( label='Color 03', backgroundColor = [0.6,0.6,0.6], command = 'denUt.den_ColorObject(3)' )
    cmds.button( label='Color 04', backgroundColor = [0.6,0,0.16], command = 'denUt.den_ColorObject(4)' )
    cmds.button( label='Color 05', backgroundColor = [0,0.01,0.38], command = 'denUt.den_ColorObject(5)' )
    cmds.button( label='Color 06', backgroundColor = [0,0,0.99], command = 'denUt.den_ColorObject(6)' )
    cmds.button( label='Color 07', backgroundColor = [0,0.27,0.1], command = 'denUt.den_ColorObject(7)' )
    cmds.button( label='Color 08', backgroundColor = [0.15,0,0.26], command = 'denUt.den_ColorObject(8)' )
    cmds.button( label='Color 09', backgroundColor = [0.79,0,0.79], command = 'denUt.den_ColorObject(9)' )
    cmds.button( label='Color 10', backgroundColor = [0.54,0.28,0.2], command = 'denUt.den_ColorObject(10)' )
    cmds.button( label='Color 11', backgroundColor = [0.25,0.14,0.12], command = 'denUt.den_ColorObject(11)' )
    cmds.button( label='Color 12', backgroundColor = [0.6,0.15,0], command = 'denUt.den_ColorObject(12)' )
    cmds.button( label='Color 13', backgroundColor = [1,0,0], command = 'denUt.den_ColorObject(13)' )
    cmds.button( label='Color 14', backgroundColor = [0,1,0], command = 'denUt.den_ColorObject(14)' )
    cmds.button( label='Color 15', backgroundColor = [0,0.26,0.6], command = 'denUt.den_ColorObject(15)' )
    cmds.button( label='Color 16', backgroundColor = [1,1,1], command = 'denUt.den_ColorObject(16)' )
    cmds.button( label='Color 17', backgroundColor = [1,1,0], command = 'denUt.den_ColorObject(17)' )
    cmds.button( label='Color 18', backgroundColor = [0.39,0.86,1], command = 'denUt.den_ColorObject(18)' )
    cmds.button( label='Color 19', backgroundColor = [0.26,1,0.64], command = 'denUt.den_ColorObject(19)' )
    cmds.button( label='Color 20', backgroundColor = [1,0.69,0.69], command = 'denUt.den_ColorObject(20)' )
    cmds.button( label='Color 21', backgroundColor = [0.89,0.67,0.47], command = 'denUt.den_ColorObject(21)' )
    cmds.button( label='Color 22', backgroundColor = [1,1,0.4], command = 'denUt.den_ColorObject(22)' )
    cmds.button( label='Color 23', backgroundColor = [0,0.6,0.33], command = 'denUt.den_ColorObject(23)' )
    cmds.button( label='Color 24', backgroundColor = [0.63,0.42,0.19], command = 'denUt.den_ColorObject(24)' )
    cmds.button( label='Color 25', backgroundColor = [0.62,0.63,0.19], command = 'denUt.den_ColorObject(25)' )
    cmds.button( label='Color 26', backgroundColor = [0.41,0.63,0.19], command = 'denUt.den_ColorObject(26)' )
    cmds.button( label='Color 27', backgroundColor = [0.19,0.64,0.36], command = 'denUt.den_ColorObject(27)' )
    cmds.button( label='Color 28', backgroundColor = [0.19,0.64,0.63], command = 'denUt.den_ColorObject(28)' )
    cmds.button( label='Color 29', backgroundColor = [0.19,0.40,0.63], command = 'denUt.den_ColorObject(29)' )
    cmds.button( label='Color 30', backgroundColor = [0.44,0.19,0.64], command = 'denUt.den_ColorObject(30)' )
    cmds.button( label='Color 31', backgroundColor = [0.64,0.18,0.42], command = 'denUt.den_ColorObject(31)' )

    cmds.setParent('..')


    cmds.button( label='turn off Objects color override', command = 'denUt.den_ColorObject(den_color=0, override=False)' )

    cmds.showWindow(Color_Window)


def LockUI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'LockUnlock_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'LockUnlock_Window' )

    # - make the window object
    LockUnlockWindow = cmds.window( 'LockUnlock_Window' )


    cmds.columnLayout( adjustableColumn=True )

    cmds.button( label='Lock All', command='denUt.den_LockAttr()' )
    cmds.button( label='Unlock All', command='denUt.den_UnLockAttr()' )
    cmds.button( label='Lock Translate', command='denUt.den_LockAttr( denR=False, denS=False, denV=False )' )
    cmds.button( label='Unlock Translate', command='denUt.den_UnLockAttr( denR=False, denS=False, denV=False )' )
    cmds.button( label='Lock Rotate', command='denUt.den_LockAttr( denT=False, denS=False, denV=False )' )
    cmds.button( label='Unlock Rotate', command='denUt.den_UnLockAttr( denT=False, denS=False, denV=False )' )
    cmds.button( label='Lock Scale', command='denUt.den_LockAttr( denT=False, denR=False, denV=False )' )
    cmds.button( label='Unlock Scale', command='denUt.den_UnLockAttr( denT=False, denR=False, denV=False )' )
    cmds.button( label='Lock Visibility', command='denUt.den_LockAttr( denT=False, denR=False, denS=False )' )
    cmds.button( label='Unlock Visibility', command='denUt.den_UnLockAttr( denT=False, denR=False, denS=False )' )

    #denUt.den_ShowLocalAxis(0)



    # - make the window object visible on screen
    cmds.showWindow( LockUnlockWindow )


def AddIKUI():
    if (cmds.window("AddIKHandle_Window", exists=True)):
        cmds.deleteUI("AddIKHandle_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('AddIKHandle_Window')

    cmds.columnLayout( adjustableColumn=True )

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 160), (2, 160)] )
    cmds.text( label='Handle Type' )
    handleType = cmds.textField( text='ikSCsolver', ann='enter only ikSCsolver or ikRPsolver - other solvers not supported' )
    cmds.text( label='Make Up Object' )
    makeUp = cmds.intField( ann='up object ignored with ikSCsolver' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Up Object Position' )
    posX = cmds.floatField( value=0 )
    posY = cmds.floatField( value=10 )
    posZ = cmds.floatField( value=0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        handleTypeString = cmds.textField( handleType, query=True, text=True)
        makeUpValue = cmds.intField( makeUp, query=True, value=True)
        posValue = (cmds.floatField( posX, query=True, value=True),cmds.floatField( posY, query=True, value=True),cmds.floatField( posZ, query=True, value=True))
        denUt.den_AddIKHandle(handleType=handleTypeString,makeUp=makeUpValue,upPos=posValue)

    cmds.button ( label='Make IK Handle', command=makeCmd )

    cmds.showWindow(labelWindow)



def BallUI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'BallCtrl_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'BallCtrl_Window' )
    
    # - make the window object
    BallCtrlWindow = cmds.window( 'BallCtrl_Window' )
    
    # - make a single column object inside the window object
    cmds.columnLayout( adjustableColumn=True )
    
    # - make a 2 column layout for the name of the Ctrl
    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Ball Control'  )
    nodeName_Ball = cmds.textField( text='Ball_Ctrl' )
    cmds.setParent('..')
    
    # - make a 4 column layout for the position of the Ctrl
    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Ball Shape\n from its own center pivot\n (used for T style contros)'  )
    posX_Ball = cmds.floatField( value=0 )
    posY_Ball = cmds.floatField( value=0 )
    posZ_Ball = cmds.floatField( value=0 )
    cmds.setParent('..')
    
    # - make a two column layout for the rqdius and the doT of the Ctrl
    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the Ball Shape'  )
    radius_Ball = cmds.floatField( value=1.0 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the center of the Ball Shape\n to make a T style Control'  )
    doT_Ball = cmds.intField()
    cmds.setParent('..')
    
    # - make a command that builds the Ctrl
    def makeCmd(foo):
        nodeNameString = cmds.textField( nodeName_Ball, query=True, text=True )
        posValueX = cmds.floatField( posX_Ball, query=True, value=True )
        posValueY = cmds.floatField( posY_Ball, query=True, value=True )
        posValueZ = cmds.floatField( posZ_Ball, query=True, value=True )
        posValue = ( posValueX, posValueY, posValueZ )
        radiusValue = cmds.floatField( radius_Ball, query=True, value=True)
        doTValue = cmds.intField( doT_Ball, query=True, value=True)
        denUt.den_MakeBall( nodeName=nodeNameString, pos=posValue, radius=radiusValue, doT=doTValue )
    
    # - make a button to execute the command
    cmds.button ( label='Make Ball Control', command=makeCmd, ann='Make the Ball Control\n using the options spcified above' )
    
    
    # - make the window object visible on screen
    cmds.showWindow( BallCtrlWindow )


def PoleUI():
    # - if the window already exitst, get rid of it
    if (cmds.window( 'PoleCtrl_Window', exists=True )):
        print( 'found existing UI, deleting' )
        cmds.deleteUI( 'PoleCtrl_Window' )

    # - make the window object
    PoleCtrlWindow = cmds.window( 'PoleCtrl_Window' )

    # - make a single column object inside the window object
    cmds.columnLayout( adjustableColumn=True )

    # - make a 2 column layout for the name of the Ctrl
    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Pole Control'  )
    nodeName_Pole = cmds.textField( text='Pole_Ctrl' )
    cmds.setParent('..')

    # - make a 4 column layout for the position of the Ctrl
    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Pole Shape\n from its own center pivot\n (used for T style contros)'  )
    posX_Pole = cmds.floatField( value=0 )
    posY_Pole = cmds.floatField( value=0 )
    posZ_Pole = cmds.floatField( value=0 )
    cmds.setParent('..')

    # - make a two column layout for the rqdius and the doT of the Ctrl
    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the Pole Shape'  )
    radius_Pole = cmds.floatField( value=1.0 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the center of the Pole Shape\n to make a T style Control'  )
    doT_Pole = cmds.intField()
    cmds.setParent('..')

    # - make a command that builds the Ctrl
    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Pole, query=True, text=True )
        posValueX = cmds.floatField( posX_Pole, query=True, value=True )
        posValueY = cmds.floatField( posY_Pole, query=True, value=True )
        posValueZ = cmds.floatField( posZ_Pole, query=True, value=True )
        posValue = ( posValueX, posValueY, posValueZ )
        radiusValue = cmds.floatField( radius_Pole, query=True, value=True)
        doTValue = cmds.intField( doT_Pole, query=True, value=True)
        denUt.den_MakePole( nodeName=nodeNameString, pos=posValue, radius=radiusValue, doT=doTValue )

    # - make a button to execute the command
    cmds.button ( label='Make Pole Control', command=makeCmd, ann='Make the Pole Control\n using the options spcified above' )


    # - make the window object visible on screen
    cmds.showWindow( PoleCtrlWindow )


def CubeUI():
    if (cmds.window("CubeCtrl_Window", exists=True)):
        cmds.deleteUI("CubeCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('CubeCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Cube Control' )
    nodeName_Cube = cmds.textField( text='Cube_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Cube Shape\n from its own center pivot\n (used for T style contros)'  )
    posX_Cube = cmds.floatField( value=0 )
    posY_Cube = cmds.floatField( value=0 )
    posZ_Cube = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the Cube Shape' )
    radius_Cube = cmds.floatField( value=1 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the center of the Cube Shape\n to make a T style Control' )
    doT_Cube = cmds.intField()
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Cube, query=True, text=True)
        posValue = (cmds.floatField( posX_Cube, query=True, value=True),cmds.floatField( posY_Cube, query=True, value=True),cmds.floatField( posZ_Cube, query=True, value=True))
        radiusValue = cmds.floatField( radius_Cube, query=True, value=True)
        doTValue = cmds.intField( doT_Cube, query=True, value=True)
        denUt.den_MakeCube(nodeName=nodeNameString,pos=posValue,radius=radiusValue,doT=doTValue)

    cmds.button ( label='Make Cube Control', command=makeCmd, ann='Make the Cube Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def SpikeUI():
    if (cmds.window("SpikeCtrl_Window", exists=True)):
        cmds.deleteUI("SpikeCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('SpikeCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Spike Control' )
    nodeName_Spike = cmds.textField( text='Spike_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Spike Control\n from its own center pivot\n (used for T style contros)' )
    posX_Spike = cmds.floatField( value=0 )
    posY_Spike = cmds.floatField( value=0 )
    posZ_Spike = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the Spike Shape' )
    radius_Spike = cmds.floatField( value=1 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the point of the Spike Shape\n to make a T style Control' )
    doT_Spike = cmds.intField()
    cmds.text( label='Axis', ann='choose which axis the wide end of the Spike Shape lies along' )
    axis_Spike = cmds.textField( text='+Y' )
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Spike, query=True, text=True)
        posValue = (cmds.floatField( posX_Spike, query=True, value=True),cmds.floatField( posY_Spike, query=True, value=True),cmds.floatField( posZ_Spike, query=True, value=True))
        radiusValue = cmds.floatField( radius_Spike, query=True, value=True)
        doTValue = cmds.intField( doT_Spike, query=True, value=True)
        axisString = cmds.textField( axis_Spike, query=True, text=True)
        denUt.den_MakeSpike(nodeName=nodeNameString,pos=posValue,radius=radiusValue,doT=doTValue,axis=axisString)

    cmds.button ( label='Make Spike Control', command=makeCmd, ann='Make the Ball Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def ArrowTUI():
    if (cmds.window("ArrowTCtrl_Window", exists=True)):
        cmds.deleteUI("ArrowTCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ArrowTCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the ArrowT Control' )
    nodeName_ArrowT = cmds.textField( text='ArrowT_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the ArrowT Shape\n from its own center pivot\n (used for T style contros)' )
    posX_ArrowT = cmds.floatField( value=0 )
    posY_ArrowT = cmds.floatField( value=0 )
    posZ_ArrowT = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the ArrowT Shape' )
    radius_ArrowT = cmds.floatField( value=1 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the base of the ArrowT Shape\n to make a T style Control' )
    doT_ArrowT = cmds.intField()
    cmds.text( label='Up Axis', ann='choose the Up axis for the ArrowT Shape\n ( like a sign post the arow is nailed onto )\n\n ( enter only +X, -X, +Y, -Y, +Z, or -Z )' )
    axis_ArrowT = cmds.textField( text='+Y' )
    cmds.text( label='Flip', ann='choose whether to flip the ArrowT Shape 90deg. around the Up Axis'  )
    flip_ArrowT = cmds.intField()
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_ArrowT, query=True, text=True)
        posValue = (cmds.floatField( posX_ArrowT, query=True, value=True),cmds.floatField( posY_ArrowT, query=True, value=True),cmds.floatField( posZ_ArrowT, query=True, value=True))
        radiusValue = cmds.floatField( radius_ArrowT, query=True, value=True)
        doTValue = cmds.intField( doT_ArrowT, query=True, value=True)
        axisString = cmds.textField( axis_ArrowT, query=True, text=True)
        flipValue = cmds.intField( flip_ArrowT, query=True, value=True)
        denUt.den_MakeArrowT(nodeName=nodeNameString,pos=posValue,radius=radiusValue,doT=doTValue,axis=axisString,flip=flipValue)

    cmds.button ( label='Make ArrowT Control', command=makeCmd, ann='Make the ArrowT Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def ArrowRUI():
    if (cmds.window("ArrowRCtrl_Window", exists=True)):
        cmds.deleteUI("ArrowRCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ArrowRCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the ArrowR Control' )
    nodeName_ArrowR = cmds.textField( text='ArrowR_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the ArrowR Shape\n from its own center pivot\n (used for T style contros)' )
    posX_ArrowR = cmds.floatField( value=0 )
    posY_ArrowR = cmds.floatField( value=0 )
    posZ_ArrowR = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the ArrowR Shape' )
    radius_ArrowR = cmds.floatField( value=1 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the base of the ArrowR Shape\n to make a T style Control' )
    doT_ArrowR = cmds.intField()
    cmds.text( label='Up Axis', ann='choose the Up axis for the ArrowR Shape\n ( like a sign post the arow is nailed onto )\n\n ( enter only +X, -X, +Y, -Y, +Z, or -Z )' )
    axis_ArrowR = cmds.textField( text='+Y' )
    cmds.text( label='Flip', ann='choose whether to flip the ArrowR Shape 90deg around the Axis' )
    flip_ArrowR = cmds.intField()
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_ArrowR, query=True, text=True)
        posValue = (cmds.floatField( posX_ArrowR, query=True, value=True),cmds.floatField( posY_ArrowR, query=True, value=True),cmds.floatField( posZ_ArrowR, query=True, value=True))
        radiusValue = cmds.floatField( radius_ArrowR, query=True, value=True)
        doTValue = cmds.intField( doT_ArrowR, query=True, value=True)
        axisString = cmds.textField( axis_ArrowR, query=True, text=True)
        flipValue = cmds.intField( flip_ArrowR, query=True, value=True)
        denUt.den_MakeArrowR(nodeName=nodeNameString,pos=posValue,radius=radiusValue,doT=doTValue,axis=axisString,flip=flipValue)

    cmds.button ( label='Make ArrowR Control', command=makeCmd, ann='Make the ArrowR Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def GearUI():
    if (cmds.window("GearCtrl_Window", exists=True)):
        cmds.deleteUI("GearCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('GearCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Gear Control' )
    nodeName_Gear = cmds.textField( text='Gear_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Gear Shape\n from its own center pivot\n (used for T style contros)' )
    posX_Gear = cmds.floatField( value=0 )
    posY_Gear = cmds.floatField( value=0 )
    posZ_Gear = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the Gear Shape' )
    radius_Gear = cmds.floatField( value=1 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the center of the Gear Shape\n to make a T style Control' )
    doT_Gear = cmds.intField()
    cmds.text( label='Plane', ann='choose the plane the Gear Shape lies flat on\n\n (enter only XY, YZ, or ZX)' )
    Plane_Gear = cmds.textField( text='XY' )
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Gear, query=True, text=True)
        posValue = (cmds.floatField( posX_Gear, query=True, value=True),cmds.floatField( posY_Gear, query=True, value=True),cmds.floatField( posZ_Gear, query=True, value=True))
        radiusValue = cmds.floatField( radius_Gear, query=True, value=True)
        doTValue = cmds.intField( doT_Gear, query=True, value=True)
        PlaneString = cmds.textField( Plane_Gear, query=True, text=True)
        denUt.den_MakeGear(nodeName=nodeNameString,pos=posValue,radius=radiusValue,doT=doTValue,Plane=PlaneString)

    cmds.button ( label='Make Gear Control', command=makeCmd )

    cmds.showWindow(labelWindow)


def LabelUI():
    if (cmds.window("LabelCtrl_Window", exists=True)):
        cmds.deleteUI("LabelCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('LabelCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Label Control' )
    nodeName_Label = cmds.textField( text='Label_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Label Shape\n from its own center pivot\n (used for T style contros)' )
    posX_Label = cmds.floatField( value=0 )
    posY_Label = cmds.floatField( value=0 )
    posZ_Label = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius', ann='Size of the Label Shape' )
    radius_Label = cmds.floatField( value=10 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the base of the Label Shape\n to make a T style Control' )
    doT_Label = cmds.intField()
    cmds.text( label='Label', ann='Specify the text you want in your Label' )
    label_Label = cmds.textField( text='your label here' )
    cmds.text( label='Do Circle', ann='Add a cirle at the Control origin to act as the Start Circle' )
    doCircle_Label = cmds.intField( value=1 )
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Label, query=True, text=True)
        posValue = (cmds.floatField( posX_Label, query=True, value=True),cmds.floatField( posY_Label, query=True, value=True),cmds.floatField( posZ_Label, query=True, value=True))
        radiusValue = cmds.floatField( radius_Label, query=True, value=True)
        doTValue = cmds.intField( doT_Label, query=True, value=True)
        labelString = cmds.textField( label_Label, query=True, text=True)
        doCircleValue = cmds.intField( doCircle_Label, query=True, value=True)
        denUt.den_MakeLabel(nodeName=nodeNameString,pos=posValue,radius=radiusValue,doT=doTValue,label=labelString,doCircle=doCircleValue)

    cmds.button ( label='Make Label Control', command=makeCmd, ann='Make the Label Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def HandUI():
    if (cmds.window("HandCtrl_Window", exists=True)):
        cmds.deleteUI("HandCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('HandCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Hand Control' )
    nodeName_Hand = cmds.textField( text='Hand_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Hand Shape\n from its own center pivot\n (used for T style contros)' )
    posX_Hand = cmds.floatField( value=0 )
    posY_Hand = cmds.floatField( value=0 )
    posZ_Hand = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Length', ann='Length of the Hand Shape' )
    length_Hand = cmds.floatField( value=10 )
    cmds.text( label='Width', ann='Width of the Hand Shape' )
    width_Hand = cmds.floatField( value=7 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the base of the Hand Shape\n to make a T style Control' )
    doT_Hand = cmds.intField()
    cmds.text( label='Flip Side', ann='Mirror the Hand Shape' )
    flipSide_Hand = cmds.intField()
    cmds.text( label='Plane', ann='choose the plane that the Hand Shape lies on\n\n ( enter only XY, YZ, or ZX )' )
    Plane_Hand = cmds.textField( text='ZX' )
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Hand, query=True, text=True)
        posValue = (cmds.floatField( posX_Hand, query=True, value=True),cmds.floatField( posY_Hand, query=True, value=True),cmds.floatField( posZ_Hand, query=True, value=True))
        lengthValue = cmds.floatField( length_Hand, query=True, value=True)
        widthValue = cmds.floatField( width_Hand, query=True, value=True)
        doTValue = cmds.intField( doT_Hand, query=True, value=True)
        flipSideValue = cmds.intField( flipSide_Hand, query=True, value=True)
        PlaneString = cmds.textField( Plane_Hand, query=True, text=True)
        denUt.den_MakeHand(nodeName=nodeNameString,pos=posValue,length=lengthValue,width=widthValue,doT=doTValue,flipSide=flipSideValue,Plane=PlaneString)

    cmds.button ( label='Make Hand Control', command=makeCmd, ann='Make the Hand Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def FootUI():
    if (cmds.window("FootCtrl_Window", exists=True)):
        cmds.deleteUI("FootCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('FootCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Foot Control' )
    nodeName_Foot = cmds.textField( text='Foot_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Foot Shape\n from its own center pivot\n (used for T style contros)' )
    posX_Foot = cmds.floatField( value=0 )
    posY_Foot = cmds.floatField( value=0 )
    posZ_Foot = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Length', ann='Length of the Foot Shape' )
    length_Foot = cmds.floatField( value=10 )
    cmds.text( label='Width', ann='Width of the Foot Shape' )
    width_Foot = cmds.floatField( value=7 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the base of the Foot Shape\n to make a T style Control' )
    doT_Foot = cmds.intField()
    cmds.text( label='Flip Side', ann='Mirror the Foot Shape' )
    flipSide_Foot = cmds.intField()
    cmds.text( label='Plane', ann='choose the plane that the Foot Shape lies on\n\n ( enter only XY, YZ, or ZX )' )
    Plane_Foot = cmds.textField( text='ZX' )
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Foot, query=True, text=True)
        posValue = (cmds.floatField( posX_Foot, query=True, value=True),cmds.floatField( posY_Foot, query=True, value=True),cmds.floatField( posZ_Foot, query=True, value=True))
        lengthValue = cmds.floatField( length_Foot, query=True, value=True)
        widthValue = cmds.floatField( width_Foot, query=True, value=True)
        doTValue = cmds.intField( doT_Foot, query=True, value=True)
        flipSideValue = cmds.intField( flipSide_Foot, query=True, value=True)
        PlaneString = cmds.textField( Plane_Foot, query=True, text=True)
        denUt.den_MakeFoot(nodeName=nodeNameString,pos=posValue,length=lengthValue,width=widthValue,doT=doTValue,flipSide=flipSideValue,Plane=PlaneString)

    cmds.button ( label='Make Foot Control', command=makeCmd, ann='Make the Foot Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)


def PawUI():
    if (cmds.window("PawCtrl_Window", exists=True)):
        cmds.deleteUI("PawCtrl_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('PawCtrl_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Node Name', ann='Name of the Paw Control' )
    nodeName_Paw = cmds.textField( text='Paw_Ctrl' )
    cmds.setParent('..')

    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Position', ann='Offset of the Paw Shape\n from its own center pivot\n (used for T style contros)' )
    posX_Paw = cmds.floatField( value=0 )
    posY_Paw = cmds.floatField( value=0 )
    posZ_Paw = cmds.floatField( value=0 )
    cmds.setParent('..')

    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Length', ann='Length of the Paw Shape' )
    length_Paw = cmds.floatField( value=10 )
    cmds.text( label='Width', ann='Width of the Paw Shape' )
    width_Paw = cmds.floatField( value=7 )
    cmds.text( label='Do T', ann='Add a line from the Control origin to the base of the Paw Shape\n to make a T style Control' )
    doT_Paw = cmds.intField()
    cmds.text( label='Flip Side', ann='Mirror the Paw Shape' )
    flipSide_Paw = cmds.intField()
    cmds.text( label='Plane', ann='choose the plane that the Paw Shape lies on\n\n ( enter only XY, YZ, or ZX )' )
    Plane_Paw = cmds.textField( text='ZX' )
    cmds.setParent('..')

    def makeCmd(ignore):
        nodeNameString = cmds.textField( nodeName_Paw, query=True, text=True)
        posValue = (cmds.floatField( posX_Paw, query=True, value=True),cmds.floatField( posY_Paw, query=True, value=True),cmds.floatField( posZ_Paw, query=True, value=True))
        lengthValue = cmds.floatField( length_Paw, query=True, value=True)
        widthValue = cmds.floatField( width_Paw, query=True, value=True)
        doTValue = cmds.intField( doT_Paw, query=True, value=True)
        flipSideValue = cmds.intField( flipSide_Paw, query=True, value=True)
        PlaneString = cmds.textField( Plane_Paw, query=True, text=True)
        denUt.den_MakePaw(nodeName=nodeNameString,pos=posValue,length=lengthValue,width=widthValue,doT=doTValue,flipSide=flipSideValue,Plane=PlaneString)

    cmds.button ( label='Make Paw Control', command=makeCmd, ann='Make the Paw Control\n using the options spcified above' )

    cmds.showWindow(labelWindow)



def BasePUI():
    if (cmds.window("BasePiv_Window", exists=True)):
        cmds.deleteUI("BasePiv_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('BasePiv_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Creature Name' )
    nameField = cmds.textField( text='creature_name_here' )
    cmds.text( label='Radius', ann='Size of locators'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        denBR.den_makeBasePiv(name=name,radius=radius)

    cmds.button ( label='Make Base Piv', command=makeCmd )

    cmds.showWindow(labelWindow)


def TorsoPUI():
    if (cmds.window("TorsoPiv_Window", exists=True)):
        cmds.deleteUI("TorsoPiv_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('TorsoPiv_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    #cmds.text( label='Creature Name' )
    #nameField = cmds.textField( text='creature_name_here' )
    cmds.text( label='Radius', ann='Size of locators'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        radius = cmds.floatField( radiusField, query=True, value=True)
        denBR.den_makeBipedTorsoPivs(radius=radius)

    cmds.button ( label='Make Torso Pivs', command=makeCmd )

    cmds.showWindow(labelWindow)


def ArmPUI():
    if (cmds.window("ArmPiv_Window", exists=True)):
        cmds.deleteUI("ArmPiv_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ArmPiv_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Arm' )
    cmds.text( label='Radius', ann='Size of locators'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.text( label='Elbow Distance', ann='distance of elbow locator from elbow joint'  )
    elbowDistField = cmds.floatField( value=10.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        elbowDist = cmds.floatField( elbowDistField, query=True, value=True)
        denBR.den_makeBipedArmPivs(side=side,name=name,radius=radius,elbowDist=elbowDist)

    cmds.button ( label='Make Arm Pivs', command=makeCmd )

    cmds.showWindow(labelWindow)


def HandPUI():
    if (cmds.window("HandPiv_Window", exists=True)):
        cmds.deleteUI("HandPiv_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('HandPiv_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Hand' )
    cmds.text( label='Radius', ann='Size of locators'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.text( label='Knee Distance', ann='distance of knee locator from knee joint'  )
    knuckleUpDistField = cmds.floatField( value=3.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        knuckleUpDist = cmds.floatField( knuckleUpDistField, query=True, value=True)
        denBR.den_makeBipedHandPivs( side=side, name=name, radius=radius, knuckleUpDist=knuckleUpDist )

    cmds.button ( label='Make Hand Pivs', command=makeCmd )

    cmds.showWindow(labelWindow)


def LegPUI():
    if (cmds.window("LegPiv_Window", exists=True)):
        cmds.deleteUI("LegPiv_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('LegPiv_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Leg' )
    cmds.text( label='Radius', ann='Size of locators'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.text( label='Knee Distance', ann='distance of knee locator from knee joint'  )
    kneeDistField = cmds.floatField( value=10.0 )
    cmds.text( label='Foot Up Distance', ann='distance of foot up locator above the foot'  )
    footUpDistField = cmds.floatField( value=5.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        kneeDist = cmds.floatField( kneeDistField, query=True, value=True)
        footUpDist = cmds.floatField( footUpDistField, query=True, value=True)
        denBR.den_makeBipedLegPivs( side=side, name=name, radius=radius, kneeDist=kneeDist, footUpDist=footUpDist )

    cmds.button ( label='Make Leg Pivs', command=makeCmd )

    cmds.showWindow(labelWindow)


def BaseRUI():
    if (cmds.window("BaseRig_Window", exists=True)):
        cmds.deleteUI("BaseRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('BaseRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Label' )
    labelField = cmds.textField( text='creature_name_here' )
    cmds.text( label='Control Radius', ann='Size of base circles'  )
    ctrlRadiusField = cmds.floatField( value=30.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        label = cmds.textField( labelField, query=True, text=True)
        ctrlRadius = cmds.floatField( ctrlRadiusField, query=True, value=True)
        denBR.den_makeBaseRig( label=label, ctrlRadius=ctrlRadius )

    cmds.button ( label='Make Base Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


def TorsoRUI():
    if (cmds.window("TorsoRig_Window", exists=True)):
        cmds.deleteUI("TorsoRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('TorsoRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 180), (2, 120)] )
    cmds.text( label='Radius', ann='Size of Joints'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.text( label='Pelvis Control Radius', ann='Size of Pelvis Control'  )
    pelvisRadiusField = cmds.floatField( value=18.0 )
    cmds.text( label='Chest Control Radius', ann='Size of Chest Control'  )
    chestRadiusField = cmds.floatField( value=20.0 )
    cmds.text( label='Head Control Radius', ann='Size of Head Control'  )
    headRadiusField = cmds.floatField( value=12.0 )
    cmds.text( label='Jaw Control Radius', ann='Size of Jaw Control'  )
    jawRadiusField = cmds.floatField( value=2.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        radius = cmds.floatField( radiusField, query=True, value=True)
        pelvisRadius = cmds.floatField( pelvisRadiusField, query=True, value=True)
        chestRadius = cmds.floatField( chestRadiusField, query=True, value=True)
        headRadius = cmds.floatField( headRadiusField, query=True, value=True)
        jawRadius = cmds.floatField( jawRadiusField, query=True, value=True)
        denBR.den_makeBipedTorsoRig( radius=radius, ctrlRadius=(pelvisRadius,chestRadius,headRadius,jawRadius) )

    cmds.button ( label='Make Torso Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


def ArmRUI():
    if (cmds.window("ArmRig_Window", exists=True)):
        cmds.deleteUI("ArmRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ArmRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 150), (2, 120)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Arm' )
    cmds.text( label='Radius', ann='Size of Joints'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.text( label='Control Radius', ann='Basic Size of Controls'  )
    ctrlRadiusField = cmds.floatField( value=10.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        ctrlRadius = cmds.floatField( ctrlRadiusField, query=True, value=True)
        denBR.den_makeBipedArmRig(side=side, name=name, radius=radius, ctrlRadius=ctrlRadius )

    cmds.button ( label='Make Arm Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


def HandRUI():
    if (cmds.window("HandRig_Window", exists=True)):
        cmds.deleteUI("HandRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('HandRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 150), (2, 120)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Hand' )
    cmds.text( label='Radius', ann='Size of Joints'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        denBR.den_makeBipedHandRig( side=side, name=name, radius=radius )

    cmds.button ( label='Make Hand Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


def LegRUI():
    if (cmds.window("LegRig_Window", exists=True)):
        cmds.deleteUI("LegRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('LegRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 150), (2, 120)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Leg' )
    cmds.text( label='Radius', ann='Size of Joints'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.text( label='Control Radius', ann='Basic Size of Controls'  )
    ctrlRadiusField = cmds.floatField( value=10.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        ctrlRadius = cmds.floatField( ctrlRadiusField, query=True, value=True)
        denBR.den_makeBipedLegRig(side=side, name=name, radius=radius, ctrlRadius=ctrlRadius )

    cmds.button ( label='Make Leg Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


def TwistRUI():
    if (cmds.window("ArmTwists_Window", exists=True)):
        cmds.deleteUI("ArmTwists_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ArmTwists_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 150), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='Arm' )
    cmds.text( label='Radius', ann='Size of Joints'  )
    radiusField = cmds.floatField( value=1.0 )
    cmds.setParent('..')

    # - make a 4 column layout for the 3 part arguements
    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 150), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Twist Anchor Joints', ann='Joints that will anchor the twist mechanism'  )
    Anchor1Field = cmds.textField( text='Shld' )
    Anchor2Field = cmds.textField( text='Elbow' )
    Anchor3Field = cmds.textField( text='Wrist' )
    cmds.text( label='Control Position Offset', ann='offset of the twist root control icon'  )
    ctrlXposField = cmds.floatField( value=-10 )
    ctrlYposField = cmds.floatField( value=0 )
    ctrlZposField = cmds.floatField( value=-10 )
    cmds.text( label='Control Up Vector', ann='control up vector'  )
    ctrlXupvecField = cmds.floatField( value=0 )
    ctrlYupvecField = cmds.floatField( value=0 )
    ctrlZupvecField = cmds.floatField( value=-1 )
    cmds.setParent('..')

    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True )
        name = cmds.textField( nameField, query=True, text=True )
        radius = cmds.floatField( radiusField, query=True, value=True)
        Anchor1 = cmds.textField( Anchor1Field, query=True, text=True )
        Anchor2 = cmds.textField( Anchor2Field, query=True, text=True )
        Anchor3 = cmds.textField( Anchor3Field, query=True, text=True )
        Joints = [Anchor1,Anchor2,Anchor3]
        posX = cmds.floatField( ctrlXposField, query=True, value=True )
        posY = cmds.floatField( ctrlYposField, query=True, value=True )
        posZ = cmds.floatField( ctrlZposField, query=True, value=True )
        ctrlPos = ( posX, posY, posZ )
        upX = cmds.floatField( ctrlXupvecField, query=True, value=True )
        upY = cmds.floatField( ctrlYupvecField, query=True, value=True )
        upZ = cmds.floatField( ctrlZupvecField, query=True, value=True )
        ctrlUpVec = ( upX, upY, upZ )
        denBR.den_makeTwists( side=side, name=name, radius=radius, Joints=Joints, ctrlPos=ctrlPos, ctrlUpVec=ctrlUpVec )

    cmds.button ( label='Make Arm Twists', command=makeCmd )
    
    cmds.showWindow(labelWindow)


def TrLegPUI():
    if (cmds.window("TrexLegPiv_Window", exists=True)):
        cmds.deleteUI("TrexLegPiv_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('TrexLegPiv_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='TrexLeg' )
    cmds.text( label='Radius', ann='Size of locators'  )
    radiusField = cmds.floatField( value=5.0 )
    #cmds.text( label='Knee Distance', ann='distance of knee locator from knee joint'  )
    #kneeDistField = cmds.floatField( value=10.0 )
    #cmds.text( label='Foot Up Distance', ann='distance of foot up locator above the foot'  )
    #footUpDistField = cmds.floatField( value=5.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        #kneeDist = cmds.floatField( kneeDistField, query=True, value=True)
        #footUpDist = cmds.floatField( footUpDistField, query=True, value=True)
        denTR.den_makeTrexHindLegPivs( side=side, name=name, radius=radius )

    cmds.button ( label='Make Trex Leg Pivs', command=makeCmd )

    cmds.showWindow(labelWindow)


def TrLegRUI():
    if (cmds.window("TrexLegRig_Window", exists=True)):
        cmds.deleteUI("TrexLegRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('TrexLegRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 150), (2, 120)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Name' )
    nameField = cmds.textField( text='TrexLeg' )
    cmds.text( label='Radius', ann='Size of Joints'  )
    radiusField = cmds.floatField( value=5.0 )
    cmds.text( label='Control Radius', ann='Basic Size of Controls'  )
    ctrlRadiusField = cmds.floatField( value=30.0 )
    cmds.setParent('..')


    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        name = cmds.textField( nameField, query=True, text=True)
        radius = cmds.floatField( radiusField, query=True, value=True)
        ctrlRadius = cmds.floatField( ctrlRadiusField, query=True, value=True)
        denTR.den_makeTrexHindLegRig(side=side, name=name, radius=radius, ctrlRadius=ctrlRadius )

    cmds.button ( label='Make Trex Leg Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


def ToePUI():
    if (cmds.window("ToePivs_Window", exists=True)):
        cmds.deleteUI("ToePivs_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ToePivs_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Toe List' )
    toeListField = cmds.textField( text='A B C D E' )
    cmds.text( label='Joints per Toe' )
    numJntsField = cmds.textField( text='3 3 3 3 3' )
    cmds.setParent('..')


    one = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Radius' )
    radius = cmds.floatField( value=5.0 )
    cmds.setParent('..')


    poslayout = cmds.rowColumnLayout( numberOfColumns=4, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 80), (3, 80), (4, 80)] )
    cmds.text( label='Foot Position' )
    posX = cmds.floatField( value=10 )
    posY = cmds.floatField( value=0 )
    posZ = cmds.floatField( value=0 )
    cmds.setParent('..')



    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        toeList = cmds.textField( toeListField, query=True, text=True)
        toeList = toeList.split()
        print( toeList )
        numJnts = cmds.textField( numJntsField, query=True, text=True)
        print( numJnts )
        numJnts = numJnts.split()
        numJnts = [int(i) for i in numJnts]
        #numJnts = map(int,numJnts.split())
        print( numJnts )
        radiusValue = cmds.floatField( radius, query=True, value=True)
        posValue = (cmds.floatField( posX, query=True, value=True),cmds.floatField( posY, query=True, value=True),cmds.floatField( posZ, query=True, value=True))
        denTR.den_makeToePivs(side=side, toeList=toeList, numJnts=numJnts, radius=radiusValue, footPos=posValue)

    cmds.button ( label='Make Toe Pivs', command=makeCmd )

    cmds.showWindow(labelWindow)


def ToeRUI():
    if (cmds.window("ToeRig_Window", exists=True)):
        cmds.deleteUI("ToeRig_Window")

    #    Create a window with a some fields for entering text.
    labelWindow = cmds.window('ToeRig_Window')

    cmds.columnLayout( adjustableColumn=True )

    nodeNameLayout = cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 10), columnWidth=[(1, 80), (2, 240)] )
    cmds.text( label='Side' )
    sideField = cmds.textField( text='L_' )
    cmds.text( label='Toe List' )
    toeListField = cmds.textField( text='A B C D E' )
    cmds.setParent('..')



    '''
    toeList = cmds.textField( toeListField, query=True, text=True)
    print toeList, toeList.split()
    numJnts = cmds.textField( numJntsField, query=True, text=True)
    print numJnts, map(int,numJnts.split())
    '''

    def makeCmd(ignore):
        side = cmds.textField( sideField, query=True, text=True)
        toeList = cmds.textField( toeListField, query=True, text=True)
        toeList = toeList.split()
        denTR.den_makeToeRig( side=side, toeList=toeList )

    cmds.button ( label='Make Toe Rig', command=makeCmd )

    cmds.showWindow(labelWindow)


# end