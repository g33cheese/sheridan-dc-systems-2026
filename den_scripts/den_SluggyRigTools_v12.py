#
#  copyright 2017, 2023, Den Turner  -  all rights reserved
#
import sys; sys.dont_write_bytecode=True
import importlib
import inspect

import maya.cmds as cmds
import maya.mel as mel
#import maya.OpenMaya as om


import den_Utilities_v12 as denUt
importlib.reload(denUt)
print(inspect.getfile(inspect.currentframe()), 'is importing', denUt.__file__)



# ---------------------------------------------------------------------------------------
# define Sluggy torso pivot creation command

def den_makeSlugTorsoPivs( prefix='', radius=1.0, dpTime=0.01, size=100  ):
    
    # -- makes torso pivots that can then be re-positioned to match a particular character
    
    TorsoPivGrp = denUt.den_makeGrp( nodeName=prefix+'TorsoPiv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    
    PelvisPiv = denUt.den_makeLoc( nodeName=prefix+'Pelvis_Piv', pos=(0, size, -size*0.1*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine01Piv = denUt.den_makeLoc( nodeName=prefix+'Spine01_Piv', pos=(0, size, size*0.1*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine02Piv = denUt.den_makeLoc( nodeName=prefix+'Spine02_Piv', pos=(0, size, size*0.2*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine03Piv = denUt.den_makeLoc( nodeName=prefix+'Spine03_Piv', pos=(0, size, size*0.3*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine04Piv = denUt.den_makeLoc( nodeName=prefix+'Spine04_Piv', pos=(0, size, size*0.4*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    ChestPiv = denUt.den_makeLoc( nodeName=prefix+'Chest_Piv', pos=(0, size, size*0.5*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck01Piv = denUt.den_makeLoc( nodeName=prefix+'Neck01_Piv', pos=(0, size, size*0.7*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck02Piv = denUt.den_makeLoc( nodeName=prefix+'Neck02_Piv', pos=(0, size, size*0.8*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck03Piv = denUt.den_makeLoc( nodeName=prefix+'Neck03_Piv', pos=(0, size, size*0.9*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck04Piv = denUt.den_makeLoc( nodeName=prefix+'Neck04_Piv', pos=(0, size, size*1.0*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadPiv = denUt.den_makeLoc( nodeName=prefix+'Head_Piv', pos=(0, size, size*1.1*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadEndPiv = denUt.den_makeLoc( nodeName=prefix+'HeadEnd_Piv', pos=(0, size, size*1.3*2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawPiv = denUt.den_makeLoc( nodeName=prefix+'Jaw_Piv', pos=(0, size*0.8, size*1.1*2), radius=radius )
    denUt.den_ColorShape(2); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawEndPiv = denUt.den_makeLoc( nodeName=prefix+'JawEnd_Piv', pos=(0, size*0.8, size*1.3*2), radius=radius )
    denUt.den_ColorShape(2); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    
    cmds.parent( PelvisPiv,Spine01Piv,Spine02Piv,Spine03Piv,Spine04Piv,ChestPiv,Neck01Piv,Neck02Piv,Neck03Piv,Neck04Piv,HeadPiv,HeadEndPiv,JawPiv,JawEndPiv, TorsoPivGrp )
    cmds.refresh()
    return TorsoPivGrp




# ---------------------------------------------------------------------------------------
# define Sluggy torso rig creation command
def den_makeSlugTorsoRig( prefix='', radius=0.7, ctrlRadius=(4.0,5.0,3.0,0.3), displayLocalAxis=False, dpTime=0.01 ):
    #--------------------- testing variables
    #prefix=''
    #radius=0.7
    #ctrlRadius=(4.0,5.0,3.0,0.3)
    #displayLocalAxis=True
    #dpTime=0.01
    #---------------------
    
    # -- make the Torso rig top group
    TorsoRigGrp = denUt.den_makeGrp( nodeName=prefix+'Torso_Grp', pos=(0,0,0) )
    
    # -- set up the return variables
    TorsoSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    TorsoSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    TorsoBindJoints = [] #Set list variable to hold names of all the Jx joints
    TorsoCtrlsALL = [] #Set list variable to hold names of all the controls
    TorsoGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Torso SpaceIN
    TorsoSpaceIN = denUt.den_makeGrp( nodeName=prefix+'TorsoSpace_IN', pos=(0,0,0) )
    TorsoSpaceIN = cmds.parent( TorsoSpaceIN, TorsoRigGrp )
    TorsoSpaceINs += TorsoSpaceIN
    
    # -- set variables for pivot positions
    PelvisPos = cmds.xform( prefix+'Pelvis_Piv', ws=True, q=True, t=True )
    Spine01Pos = cmds.xform( prefix+'Spine01_Piv', ws=True, q=True, t=True )
    Spine02Pos = cmds.xform( prefix+'Spine02_Piv', ws=True, q=True, t=True )
    Spine03Pos = cmds.xform( prefix+'Spine03_Piv', ws=True, q=True, t=True )
    Spine04Pos = cmds.xform( prefix+'Spine04_Piv', ws=True, q=True, t=True )
    ChestPos = cmds.xform( prefix+'Chest_Piv', ws=True, q=True, t=True )
    Neck01Pos = cmds.xform( prefix+'Neck01_Piv', ws=True, q=True, t=True )
    Neck02Pos = cmds.xform( prefix+'Neck02_Piv', ws=True, q=True, t=True )
    Neck03Pos = cmds.xform( prefix+'Neck03_Piv', ws=True, q=True, t=True )
    Neck04Pos = cmds.xform( prefix+'Neck04_Piv', ws=True, q=True, t=True )
    HeadPos = cmds.xform( prefix+'Head_Piv', ws=True, q=True, t=True )
    HeadEndPos = cmds.xform( prefix+'HeadEnd_Piv', ws=True, q=True, t=True )
    JawPos = cmds.xform( prefix+'Jaw_Piv', ws=True, q=True, t=True )
    JawEndPos = cmds.xform( prefix+'JawEnd_Piv', ws=True, q=True, t=True )
    
    # make sure the TorsoSpaceIN is selected so the first joint will be parented under it when created
    cmds.select( TorsoSpaceIN )
    # -- make the joints
    PelvisJoint = denUt.den_makeJoint( nodeName=prefix+'Pelvis_Jnt', pos=(PelvisPos), radius=radius, leaveSelected=True )
    #print( PelvisJoint, PelvisPos )
    Spine01Joint = denUt.den_makeJoint( nodeName=prefix+'Spine01_Jnt', pos=(Spine01Pos), radius=radius, leaveSelected=True )
    #print( Spine01Joint, Spine01Pos )
    Spine02Joint = denUt.den_makeJoint( nodeName=prefix+'Spine02_Jnt', pos=(Spine02Pos), radius=radius, leaveSelected=True )
    #print( Spine02Joint, Spine02Pos )
    Spine03Joint = denUt.den_makeJoint( nodeName=prefix+'Spine03_Jnt', pos=(Spine03Pos), radius=radius, leaveSelected=True )
    #print( Spine03Joint, Spine03Pos )
    Spine04Joint = denUt.den_makeJoint( nodeName=prefix+'Spine04_Jnt', pos=(Spine04Pos), radius=radius, leaveSelected=True )
    #print( Spine04Joint, Spine04Pos )
    ChestJoint = denUt.den_makeJoint( nodeName=prefix+'Chest_Jnt', pos=(ChestPos), radius=radius, leaveSelected=True )
    #print( ChestJoint, ChestPos )
    Neck01Joint = denUt.den_makeJoint( nodeName=prefix+'Neck01_Jnt', pos=(Neck01Pos), radius=radius, leaveSelected=True )
    #print( Neck01Joint, Neck01Pos )
    Neck02Joint = denUt.den_makeJoint( nodeName=prefix+'Neck02_Jnt', pos=(Neck02Pos), radius=radius, leaveSelected=True )
    #print( Neck02Joint, Neck02Pos )
    Neck03Joint = denUt.den_makeJoint( nodeName=prefix+'Neck03_Jnt', pos=(Neck03Pos), radius=radius, leaveSelected=True )
    #print( Neck03Joint, Neck03Pos )
    Neck04Joint = denUt.den_makeJoint( nodeName=prefix+'Neck04_Jnt', pos=(Neck04Pos), radius=radius, leaveSelected=True )
    #print( Neck04Joint, Neck04Pos )
    HeadJoint = denUt.den_makeJoint( nodeName=prefix+'Head_Jnt', pos=(HeadPos), radius=radius, leaveSelected=True )
    #print( HeadJoint, HeadPos )
    HeadEndJoint = denUt.den_makeJoint( nodeName=prefix+'Head_end', pos=(HeadEndPos), radius=radius*0.4, leaveSelected=False )
    #print( HeadEndJoint, HeadEndPos )
    cmds.select(HeadJoint)
    JawJoint = denUt.den_makeJoint( nodeName=prefix+'Jaw_Jnt', pos=(JawPos), radius=radius, leaveSelected=True )
    #print( JawJoint, JawPos )
    JawEndJoint = denUt.den_makeJoint( nodeName=prefix+'Jaw_end', pos=(JawEndPos), radius=radius*0.4, leaveSelected=True )
    #print( JawJoint, JawPos )
    
    # make temporary list of joints to add to Guts list
    #stuffToAdd = [PelvisJoint,Spine01Joint,Spine02Joint,Spine03Joint,Spine04Joint,ChestJoint,Neck01Joint,Neck02Joint,Neck03Joint,Neck04Joint,HeadJoint,HeadEndJoint,JawJoint,JawEndJoint]
    # add to Guts list
    #TorsoGutsALL += stuffToAdd
    #print( stuffToAdd )
    #print( TorsoGutsALL )
    
    if ( displayLocalAxis ):
        cmds.setAttr( PelvisJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( Spine01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Spine02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Spine03Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Spine04Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( ChestJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck03Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck04Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( HeadJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( JawJoint+'.displayLocalAxis', 1 )
    
    # -- orient the joints
    cmds.joint( PelvisJoint, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True )
    cmds.joint( JawJoint, e=True, oj='yup', zso=True )
    
    # -- set up the ik handles for Spine01, Spine02, Neck
    # -- Pelvis, Cheat, Head will be driven directly by constraints
    cmds.select( Spine01Joint, Spine02Joint )
    Spine01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Spine02Joint, Spine03Joint )
    Spine02Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Spine03Joint, Spine04Joint )
    Spine03Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Spine04Joint, ChestJoint )
    Spine04Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck01Joint, Neck02Joint )
    Neck01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck02Joint, Neck03Joint )
    Neck02Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck03Joint, Neck04Joint )
    Neck03Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck04Joint, HeadJoint )
    Neck04Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    
    # -- make the controls and zero nulls
    
    # -- Pelvis
    PelvisCtrl = denUt.den_MakeBall(nodeName=prefix+'Pelvis_Ctrl',pos=(0,0,0),radius=ctrlRadius[0],doT=False)
    cmds.xform( t=PelvisPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Chest
    ChestCtrl = denUt.den_MakeBall(nodeName=prefix+'Chest_Ctrl',pos=(0,0,0),radius=ctrlRadius[1],doT=False)
    cmds.xform( t=ChestPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Head
    HeadCtrl = denUt.den_MakeBall(nodeName=prefix+'Head_Ctrl',pos=(0,0,0),radius=ctrlRadius[2],doT=False)
    cmds.xform( t=HeadPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Jaw
    JawCtrl = denUt.den_MakeBall(nodeName=prefix+'Jaw_Ctrl',pos=(0,-1.2,0),radius=ctrlRadius[3],doT=True)
    cmds.xform( t=JawPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # make temporary list of controls to add to Controls list
    stuffToAdd = [PelvisCtrl,ChestCtrl,HeadCtrl,JawCtrl]
    # add controls to Controls list
    TorsoCtrlsALL += stuffToAdd
    print( stuffToAdd )
    print( TorsoCtrlsALL )
    
    # - this loop is here in case more than one spine or neck joint are needed
    VertJoints = [Neck02Joint,Neck03Joint,Neck04Joint,Spine02Joint,Spine03Joint,Spine04Joint]
    print( VertJoints )
    #print NeckCtrlNames
    VertControls = []
    for jx in VertJoints:
        print( jx )
        CtrlName = jx.replace('_Jnt', '_Ctrl')
        print( CtrlName )
        Ctrl = denUt.den_MakeBall(nodeName=CtrlName,pos=(0,2,0),radius=0.3,doT=True)
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        Ctrl = cmds.parent( Ctrl, jx, relative=True )
        Ctrl = cmds.parent( Ctrl, TorsoSpaceIN )
        Ctrl = denUt.den_AddZeroNull()
        VertControls += Ctrl
        denUt.den_DiagPause( dpTime )
    
    # add controls to Controls list
    TorsoCtrlsALL += VertControls
    print( VertControls )
    print( TorsoCtrlsALL )
    
    Neck02Ctrl = VertControls[0]
    Neck03Ctrl = VertControls[1]
    Neck04Ctrl = VertControls[2]
    Spine02Ctrl = VertControls[3]
    Spine03Ctrl = VertControls[4]
    Spine04Ctrl = VertControls[5]
    
    
    # -- make locators for certain joints including 2 for Spine02 for blended pos
    PelvisLoc = cmds.spaceLocator (n=prefix+'Pelvis_JntLoc')
    PelvisLoc = cmds.parent( PelvisLoc, PelvisJoint, relative=True )
    PelvisLoc = cmds.parent( PelvisLoc, PelvisCtrl )
    
    ChestLoc = cmds.spaceLocator (n=prefix+'Chest_JntLoc')
    ChestLoc = cmds.parent( ChestLoc, ChestJoint, relative=True )
    ChestLoc = cmds.parent( ChestLoc, ChestCtrl )
    
    HeadLoc = cmds.spaceLocator (n=prefix+'Head_JntLoc')
    HeadLoc = cmds.parent( HeadLoc, HeadJoint, relative=True )
    HeadLoc = cmds.parent( HeadLoc, HeadCtrl )
    
    # make temporary list of locators to add to Guts list
    #stuffToAdd = [PelvisLoc,ChestLoc,HeadLoc]
    # add locators to Guts list
    #TorsoGutsALL += stuffToAdd
    #print( stuffToAdd )
    #print( TorsoGutsALL )
    
    # -- reparent some things
    Spine01Handle = cmds.parent( Spine01Handle, Spine02Ctrl ) # make Spine01 ik goal follow Spine02Ctrl
    Spine02Handle = cmds.parent( Spine02Handle, Spine03Ctrl ) # make Spine02 ik goal follow Spine03Ctrl
    Spine03Handle = cmds.parent( Spine03Handle, Spine04Ctrl ) # make Spine03 ik goal follow Spine04Ctrl
    Spine04Handle = cmds.parent( Spine04Handle, ChestCtrl ) # make Spine04 ik goal follow ChestCtrl
    Neck01Handle = cmds.parent( Neck01Handle, Neck02Ctrl ) # make Neck01 ik goal follow  Neck02Ctrl
    Neck02Handle = cmds.parent( Neck02Handle, Neck03Ctrl ) # make Neck02 ik goal follow  Neck03Ctrl
    Neck03Handle = cmds.parent( Neck03Handle, Neck04Ctrl ) # make Neck03 ik goal follow  Neck04Ctrl
    Neck04Handle = cmds.parent( Neck04Handle, HeadCtrl ) # make Neck04 ik goal follow  HeadCtrl
    
    JawCtrl = cmds.parent( JawCtrl, HeadCtrl )
    HeadCtrl = cmds.parent( HeadCtrl, ChestCtrl )
    ChestCtrl = cmds.parent( ChestCtrl, TorsoSpaceIN )
    PelvisCtrl = cmds.parent( PelvisCtrl, TorsoSpaceIN )
    
    # -- add the zero nulls
    cmds.select( PelvisCtrl )
    PelvisCtrl = denUt.den_AddZeroNull()
    cmds.select( ChestCtrl )
    ChestCtrl = denUt.den_AddZeroNull()
    cmds.select( HeadCtrl )
    HeadCtrl = denUt.den_AddZeroNull()
    HeadCtrlZero = cmds.listRelatives( HeadCtrl, parent=True )
    cmds.select( JawCtrl )
    JawCtrl = denUt.den_AddZeroNull()
    JawCtrlZero = cmds.listRelatives( JawCtrl, parent=True )
    
    # -- make constraints
    cmds.parentConstraint( PelvisLoc, PelvisJoint, mo=True ) # makes pelvis joint follow pelvis control
    cmds.orientConstraint( ChestLoc, ChestJoint, mo=True ) # makes chest joint orient follow chest control
    cmds.orientConstraint( HeadLoc, HeadJoint, mo=True ) # makes head joint orient follow head control
    cmds.parentConstraint( JawCtrl, JawJoint, mo=True ) # makes jaw joint follow jaw control
    cmds.parentConstraint( HeadJoint, JawCtrlZero, mo=True ) # makes jaw control stay on the head joint
    #cmds.parentConstraint( ChestJoint, HeadCtrlZero, mo=True ) # makes head control follow chest joint
    
    # distribute influence of pelvis and chest controls to the Vertebrae controls of the spine
    cmds.parentConstraint( PelvisCtrl, ChestCtrl, prefix+'Spine03_CtrlZero', mo=True )
    cmds.parentConstraint( prefix+'Spine03_Ctrl', prefix+'Spine02_CtrlZero', w=1, mo=True )
    cmds.parentConstraint( PelvisCtrl, prefix+'Spine02_CtrlZero', w=2, mo=True )
    cmds.parentConstraint( prefix+'Spine03_Ctrl', prefix+'Spine04_CtrlZero', w=1, mo=True )
    cmds.parentConstraint( ChestCtrl, prefix+'Spine04_CtrlZero', w=2, mo=True )
    # spreads the twist forward one joint to avoid last spine joint having no twist
    sc1 = cmds.orientConstraint( PelvisCtrl, prefix+'Spine02_Ctrl', Spine01Handle, mo=True  )
    sc2 = cmds.orientConstraint( prefix+'Spine02_Ctrl', prefix+'Spine03_Ctrl', Spine02Handle, mo=True  )
    sc3 = cmds.orientConstraint( prefix+'Spine03_Ctrl', prefix+'Spine04_Ctrl', Spine03Handle, mo=True  )
    sc4 = cmds.orientConstraint( prefix+'Spine04_Ctrl', ChestCtrl, Spine04Handle, mo=True  )
    # distribute influence of cheast and head controls to the Vertebrae controls of the neck
    cmds.parentConstraint( ChestCtrl, HeadCtrl, prefix+'Neck03_CtrlZero', mo=True )
    cmds.parentConstraint( prefix+'Neck03_Ctrl', prefix+'Neck02_CtrlZero', w=1, mo=True )
    cmds.parentConstraint( ChestCtrl, prefix+'Neck02_CtrlZero', w=2, mo=True )
    cmds.parentConstraint( prefix+'Neck03_Ctrl', prefix+'Neck04_CtrlZero', w=1, mo=True )
    cmds.parentConstraint( HeadCtrl, prefix+'Neck04_CtrlZero', w=2, mo=True )
    # spreads the twist forward one joint to avoid last neck joint having no twist
    nc1 = cmds.orientConstraint( ChestCtrl, prefix+'Neck02_Ctrl', Neck01Handle, mo=True  )
    nc2 = cmds.orientConstraint( prefix+'Neck02_Ctrl', prefix+'Neck03_Ctrl', Neck02Handle, mo=True  )
    nc3 = cmds.orientConstraint( prefix+'Neck03_Ctrl', prefix+'Neck04_Ctrl', Neck03Handle, mo=True  )
    nc4 = cmds.orientConstraint( prefix+'Neck04_Ctrl', HeadCtrl, Neck04Handle, mo=True  )
    
    for con in [ sc1, sc2, sc3, sc4, nc1, nc2, nc3, nc4 ]:
        print( con )
        cmds.setAttr( con[0]+'.interpType', 2 )
    
    # -- list the jx joints for binding or proxy
    TorsoBindJoints += [ PelvisJoint, Spine01Joint, Spine02Joint, Spine03Joint, Spine04Joint, ChestJoint, Neck01Joint, Neck02Joint, Neck03Joint, Neck04Joint, HeadJoint, JawJoint ]
    
    # -- add the space output nulls
    TorsoSpaceOUTs += denUt.den_AddSpaceOUTs(TorsoBindJoints)
    print( TorsoSpaceOUTs )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return TorsoRigGrp, TorsoSpaceINs, TorsoSpaceOUTs, TorsoBindJoints, TorsoCtrlsALL, TorsoGutsALL





# ---------------------------------------------------------------------------------------
# define Sluggy tail pivots creation command

def den_makeTailPivs( prefix='', name='Tail', jointCount=8, radius=1.0, dpTime=0.01, size=100 ):
    #name='Tail'
    #jointCount = 8
    #radius=0.2
    
    TailPivGrp = denUt.den_makeGrp( nodeName=prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    for jx in range(jointCount+1):
        jxStr = str(jx+1)
        jxStrPad = jxStr.rjust(2,'0')
        jxEnd = str(jx)
        jxEndPad = jxEnd.rjust(2,'0')
        print( jx, jxStr, jxStrPad )
        piv = denUt.den_makeLoc( nodeName=prefix+name+jxStrPad+'_Piv', pos=(0, size, 0-jx*size*0.2), radius=radius )
        denUt.den_ColorShape(20)
        denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
        if (jx == jointCount):
            print( 'piv =', piv )
            piv = cmds.rename( piv, prefix+name+'End_Piv' )
            print( 'piv =', piv )
        cmds.parent( piv, TailPivGrp )
        denUt.den_DiagPause( dpTime )
    
    cmds.refresh()
    return TailPivGrp



# ---------------------------------------------------------------------------------------
# define Sluggy tail rig creation command (for FK only tail)

def den_makeTailRigFK( prefix='', name='Tail', jointCount=8, radius=0.7, ctrlRadius=2.0, secondaryAxisOrient='yup', dpTime=0.01 ):
    #name='Tail'
    #jointCount = 8
    
    TailRigGrp = denUt.den_makeGrp( nodeName=prefix+name+'Rig_Grp', pos=(0,0,0) )
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'PelvisSpace_IN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, TailRigGrp )[0]
    TailSpaceOUTs = [] # make empty list to contain spaceOUTs as they are created
    TailBindJoints = [] # make empty list to contain Jx joints as they are created
    TailEndJoint = []
    TailFKCtrls = []
    #TailCtrls = []
    
    #Set variables to hold names of all the controls and guts
    TailCtrlsALL = []
    TailGutsALL = []
    
    # - make the joints
    cmds.select( PelvisSpaceIN )
    for i in range(jointCount+1):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        if (i == jointCount):
            TailPos = cmds.xform( prefix+name+'End_Piv', ws=True, q=True, t=True )
            TailJnt = denUt.den_makeJoint( nodeName=prefix+name+'_end', pos=(TailPos), radius=radius*0.4, leaveSelected=True )
            TailJnt = cmds.ls( TailJnt )
            TailEndJoint += TailJnt
            print( 'TailEndJoint =', TailEndJoint )
            print( TailJnt )
        else:
            TailPos = cmds.xform( prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
            TailJnt = denUt.den_makeJoint( nodeName=prefix+name+iStrPad+'_Jnt', pos=(TailPos), radius=radius, leaveSelected=True )
            TailJntOUT = denUt.den_makeGrp( nodeName=prefix+name+iStrPad+'Space_OUT', pos=(0,0,0) ) # make a spaceOUT to go with the Jx
            TailJntOUT = cmds.parent( TailJntOUT, TailJnt ) # parent the spaceOU to the Jx
            cmds.select( TailJnt )
            TailSpaceOUTs += TailJntOUT
            TailJnt = cmds.ls( TailJnt )
            TailBindJoints += TailJnt
            print( TailJnt )
        denUt.den_DiagPause( dpTime )
    
    denUt.den_DiagPause( dpTime )
    cmds.joint( prefix+name+'01_Jnt', e=True, oj='xyz', secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True )
    cmds.joint( TailEndJoint, e=True, oj='none', zso=True )
    denUt.den_DiagPause( dpTime )
    print( '----------------------------------------------------' )
    print( 'done with the joints - now to do the control objects' )
    print( '----------------------------------------------------' )
    
    # - make the FK controls
    for i in range(jointCount):
        ctrlTaperRadius = ctrlRadius*(1+(1-float(i/jointCount)))
        print( 'ctrlTaperRadius =', ctrlTaperRadius )
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        TailPos = cmds.xform( prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
        TailJnt = TailBindJoints[i]
        TailJntParent = cmds.listRelatives( TailJnt, parent=True, fullPath=True )
        TailFKCtrl = denUt.den_MakeSpike(nodeName=prefix+name+iStrPad+'FK_Ctrl',pos=(0,1.5*ctrlTaperRadius,0),radius=ctrlRadius,doT=True)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        TailFKCtrl = cmds.parent( TailFKCtrl, TailJnt, relative=True )
        if i==0 :
            TailFKCtrl = cmds.parent( TailFKCtrl, TailJntParent )
        else:
            TailFKCtrl = cmds.parent( TailFKCtrl, TailFKCtrls[i-1] )
        TailFKCtrl = denUt.den_AddZeroNull()
        TailFKCtrl = cmds.ls( TailFKCtrl )
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        cmds.connectAttr( TailFKCtrl[0]+'.rotate', TailJnt+'.rotate' )
        print( TailFKCtrl )
        TailFKCtrls += TailFKCtrl
        denUt.den_DiagPause( dpTime )
    
    
    # add joints to Guts list
    TailGutsALL += TailBindJoints
    # add controls to Controls list
    TailCtrlsALL += TailFKCtrls
    
    #print( TailBindJoints )
    cmds.refresh()
    
    # -- return the tail rig group node, list of spaceIN's, list of spaceOUT's, list of Jx joints
    return TailRigGrp, [PelvisSpaceIN], TailSpaceOUTs, TailBindJoints, TailCtrlsALL, TailGutsALL




# ---------------------------------------------------------------------------------------
# define Sluggy tail rig creation command (for IK only tail)

def den_makeTailRigIK( prefix='', name='Tail', jointCount=8, radius=0.7, ctrlRadius=2.0, controlJoints=(1,5,8), secondaryAxisOrient='yup', dpTime=0.01 ):
    #name='Tail'
    #jointCount = 8
    #controlJoints=(1,5,8)
    
    if (controlJoints[0] != 1) or (controlJoints[-1] != jointCount):
        print( 'ERROR in controlJoint kwarg - first number must be 1 and last number must be equal to jointCount kwarg' )
        exit()
    TailRigGrp = denUt.den_makeGrp( nodeName=prefix+name+'Rig_Grp', pos=(0,0,0) )
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'PelvisSpace_IN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, TailRigGrp )[0]
    TailSpaceOUTs = [] # make empty list to contain spaceOUTs as they are created
    TailBindJoints = [] # make empty list to contain Jx joints as they are created
    TailEndJoint = []
    #TailFKCtrls = []
    TailIKCtrls = []
    TailBallCtrls = []
    TailHandles = []
    
    #Set variables to hold names of all the controls and guts
    TailCtrlsALL = []
    TailGutsALL = []
    
    # - make the joints
    cmds.select( PelvisSpaceIN )
    for i in range(jointCount+1):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        if (i == jointCount):
            TailPos = cmds.xform( prefix+name+'End_Piv', ws=True, q=True, t=True )
            TailJnt = denUt.den_makeJoint( nodeName=prefix+name+'_end', pos=(TailPos), radius=radius*0.4, leaveSelected=True )
            TailJnt = cmds.ls( TailJnt )
            TailEndJoint += TailJnt
            print( 'TailEndJoint =', TailEndJoint )
            print( TailJnt )
        else:
            TailPos = cmds.xform( prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
            TailJnt = denUt.den_makeJoint( nodeName=prefix+name+iStrPad+'_Jnt', pos=(TailPos), radius=radius, leaveSelected=True )
            TailJntOUT = denUt.den_makeGrp( nodeName=prefix+name+iStrPad+'Space_OUT', pos=(0,0,0) ) # make a spaceOUT to go with the Jx
            TailJntOUT = cmds.parent( TailJntOUT, TailJnt ) # parent the spaceOU to the Jx
            cmds.select( TailJnt )
            TailSpaceOUTs += TailJntOUT
            TailJnt = cmds.ls( TailJnt )
            TailBindJoints += TailJnt
            print( TailJnt )
        denUt.den_DiagPause( dpTime )
    
    denUt.den_DiagPause( dpTime )
    cmds.joint( prefix+name+'01_Jnt', e=True, oj='xyz', secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True )
    cmds.joint( TailEndJoint, e=True, oj='none', zso=True )
    denUt.den_DiagPause( dpTime )
    print( '----------------------------------------------------' )
    print( 'done with the joints - now to do the control objects' )
    print( '----------------------------------------------------' )
    
    TailJntAll = TailBindJoints + TailEndJoint
    print( TailJntAll )
    # - make the IK controls
    for i in range(jointCount+1):
        ctrlTaperRadius = ctrlRadius*(1+2*(1-float(i/jointCount)))
        print( 'ctrlTaperRadius =', ctrlTaperRadius )
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( 'controls loop ', 'i =', i, '  ', iStr, iStrPad )
        TailJnt = TailJntAll[i] ###
        TailJntParent = cmds.listRelatives( TailJnt, parent=True, fullPath=True )
        
        if (i != 0 ):# dont add a small control for the base of the tail
            for jnt in controlJoints:
                if (i == jnt):# check if the current joint is a joint that gets a larger IK control
                    jntStr = str(jnt)
                    jntStrPad = jntStr.rjust(2,'0')
                    print( '    i =', i, '  ik jnt=', jnt, jntStr, jntStrPad, TailJntParent )
                    TailBallCtrl = denUt.den_MakeBall(nodeName=prefix+name+jntStrPad+'_Ctrl',pos=(0,0,0),radius=ctrlTaperRadius,doT=False)
                    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
                    TailBallCtrl = cmds.parent( TailBallCtrl, TailJntParent, relative=True )
                    TailBallCtrl = cmds.parent( TailBallCtrl, PelvisSpaceIN )
                    TailBallCtrl = denUt.den_AddZeroNull()
                    TailBallCtrls += TailBallCtrl
                    denUt.den_LockAttr(False,False,True,False)# relock after parenting
                    denUt.den_ColorShapeRGB(rgb=(1,0,1))
                    denUt.den_DiagPause( dpTime )
            # -------
            cmds.select( TailJntParent, TailJnt )
            TailHandle = denUt.den_AddIKHandle('ikSCsolver',False)
            TailIKCtrl = denUt.den_MakeCube(nodeName=prefix+name+iStrPad+'IK_Ctrl',pos=(0,1.5*ctrlTaperRadius,0),radius=radius*0.5,doT=True)
            denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting    time.sleep(seconds)
    
            TailIKCtrl = cmds.parent( TailIKCtrl, TailJnt, relative=True )
            TailIKCtrl = cmds.parent( TailIKCtrl, PelvisSpaceIN )
            # -------
            if (i == jointCount):
                #print TailIKCtrl
                TailIKCtrl = cmds.rename( TailIKCtrl, prefix+name+'end_Ctrl' )
                TailIKCtrl = cmds.ls( TailIKCtrl, long=True )
            cmds.select( TailIKCtrl )
            TailIKCtrl = denUt.den_AddZeroNull()
            TailIKCtrl = cmds.ls( TailIKCtrl )
            denUt.den_LockAttr(False,True,True,False)# relock after parenting
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            TailHandle = cmds.parent( TailHandle, TailIKCtrl )
            TailIKCtrls += TailIKCtrl
            TailHandles += TailHandle
            denUt.den_DiagPause( dpTime )
    print( '----------------------------------------------------' )
    print( 'done with control objects - now to do the constraint' )
    print( '----------------------------------------------------' )
    
    
    i = 0 # initialize the counter variable
    for ball in controlJoints:#loop for each integer in controlJoints
        ballStr = str(ball)
        ballStrPad = ballStr.rjust(2,'0')
        ci = ball-2#sets the index to use with the TailIKCtrls list variable for balls that are not in-betweens
        print( '=== doing ball', ball )
        if ball != controlJoints[-1]: # check to see if it is the last ball
            xCurr = ball+1 # starts by setting the current number to the number of the first in-between joint
            xLast = controlJoints[i+1]-1 # finds the number of the last in-between joint
            ballNextStrPad = str(xLast+1).rjust(2,'0') # find the number of the next ball - uses last in-between and adds one
            print( 'for ball', ball, ' xCurr starts at', xCurr, ' xLast =', xLast )
            if i == 0: # is it the first ball?
                print( ball, ballStrPad, ballNextStrPad, cmds.ls( prefix+name+ballStrPad+'_Ctrl' ), ballStrPad, 'is the FIRST ball' )
            else:
                #print ball, TailIKCtrls[ci]
                TailIKCtrlZero = cmds.listRelatives( TailIKCtrls[ci], parent=True, fullPath=True )
                TailBallCtrl = cmds.ls( prefix+name+ballStrPad+'_Ctrl' )
                print( ball, ballStrPad, ballNextStrPad, TailBallCtrl, TailIKCtrlZero, ballStrPad, 'is an in-between ball' )
                cmds.parentConstraint( TailBallCtrl, TailIKCtrlZero, mo=True )
            #print xLast-xCurr
            w1 = float((xLast+1)-xCurr) #sets the first weight to equal the total number of in-betweens
            w2 = 1.0
            while (xCurr <= xLast): #this will loop over each in-between
                TailIKCtrlZero = cmds.listRelatives( TailIKCtrls[xCurr-2], parent=True, fullPath=True )
                TailBallCtrl_w1 = cmds.ls( prefix+name+ballStrPad+'_Ctrl' )
                TailBallCtrl_w2 = cmds.ls( prefix+name+ballNextStrPad+'_Ctrl' )
                cmds.parentConstraint( TailBallCtrl_w1, TailIKCtrlZero, mo=True, w=pow(w1,2) ) # the pow() makes the weight distribution curvy instead of linear
                cmds.parentConstraint( TailBallCtrl_w2, TailIKCtrlZero, mo=True, w=pow(w2,2) )
                print( 'xCurr =', xCurr, TailBallCtrl_w1[0]+' w1 =', w1, TailBallCtrl_w2[0]+' w2 =', w2, TailIKCtrlZero, 'floats in-between '+ballStrPad+' and '+ballNextStrPad )
                xCurr += 1 # move on to the next one
                w1 -= 1
                w2 += 1
                denUt.den_DiagPause( dpTime )
        else:
            #print TailJnt, ball, 'LAST'
            TailIKCtrlZero = cmds.listRelatives( TailIKCtrls[ci], parent=True, fullPath=True )
            TailEndCtrlZero = cmds.listRelatives( TailIKCtrls[ci+1], parent=True, fullPath=True )
            TailBallCtrl = cmds.ls( prefix+name+ballStrPad+'_Ctrl' )
            print( ball, TailBallCtrl, TailIKCtrlZero, ballStrPad, 'is the LAST ball' )
            print( TailEndCtrlZero )
            cmds.parentConstraint( TailBallCtrl, TailIKCtrlZero, mo=True )
            cmds.parentConstraint( TailBallCtrl, TailEndCtrlZero, mo=True )
        i += 1 # move the counter on to the next ball
    denUt.den_DiagPause( dpTime )
    
    # add joints to Guts list
    TailGutsALL += TailBindJoints
    # add controls to Controls list
    TailCtrlsALL += TailIKCtrls
    TailCtrlsALL += TailBallCtrls
    
    cmds.refresh()

    return TailRigGrp, [PelvisSpaceIN], TailSpaceOUTs, TailBindJoints, TailCtrlsALL, TailGutsALL





# ---------------------------------------------------------------------------------------
# define Sluggy tail rig creation command (for full IK/FK blendable tail)

def den_makeTailRig( prefix='', name='Tail', jointCount=8, radius=0.7, ctrlRadius=2.0, controlJoints=(1,5,8), secondaryAxisOrient='yup', dpTime=0.01 ):
    #name='Tail'
    #jointCount = 8
    #controlJoints=(1,5,8)
    
    if (controlJoints[0] != 1) or (controlJoints[-1] != jointCount):
        print( 'ERROR in controlJoint kwarg - first number must be 1 and last number must be equal to jointCount kwarg' )
        exit()
    TailRigGrp = denUt.den_makeGrp( nodeName=prefix+name+'Rig_Grp', pos=(0,0,0) )
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'PelvisSpace_IN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, TailRigGrp )[0]
    TailSpaceOUTs = [] # make empty list to contain spaceOUTs as they are created
    TailBindJoints = [] # make empty list to contain Jx joints as they are created
    TailEndJoint = []
    TailFKCtrls = []
    TailIKCtrls = []
    TailBallCtrls = []
    TailHandles = []
    
    TailUtilCtrl = denUt.den_MakeGear( nodeName=prefix+name+'Util_Ctrl', pos=(ctrlRadius,ctrlRadius*4,0), radius=radius, Plane='XY')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    fkikAttr = cmds.addAttr( TailUtilCtrl, longName=prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    print(fkikAttr)
    cmds.setAttr( TailUtilCtrl+'.'+prefix+name+'_FK_IK', lock=False, keyable=True, channelBox=True )
    cmds.setAttr( TailUtilCtrl+'.'+prefix+name+'_FK_IK', keyable=True )
    
    
    #Set variables to hold names of all the controls and guts
    TailCtrlsALL = []
    TailGutsALL = []
    
    # - make the joints
    cmds.select( PelvisSpaceIN )
    for i in range(jointCount+1):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        if (i == jointCount):
            TailPos = cmds.xform( prefix+name+'End_Piv', ws=True, q=True, t=True )
            TailJnt = denUt.den_makeJoint( nodeName=prefix+name+'_end', pos=(TailPos), radius=radius*0.4, leaveSelected=True )
            TailJnt = cmds.ls( TailJnt )
            TailEndJoint += TailJnt
            print( 'TailEndJoint =', TailEndJoint )
            print( TailJnt )
        else:
            TailPos = cmds.xform( prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
            TailJnt = denUt.den_makeJoint( nodeName=prefix+name+iStrPad+'_Jnt', pos=(TailPos), radius=radius, leaveSelected=True )
            TailJntOUT = denUt.den_makeGrp( nodeName=prefix+name+iStrPad+'Space_OUT', pos=(0,0,0) ) # make a spaceOUT to go with the Jx
            TailJntOUT = cmds.parent( TailJntOUT, TailJnt ) # parent the spaceOU to the Jx
            cmds.select( TailJnt )
            TailSpaceOUTs += TailJntOUT
            TailJnt = cmds.ls( TailJnt )
            TailBindJoints += TailJnt
            print( TailJnt )
        denUt.den_DiagPause( dpTime )
    
    denUt.den_DiagPause( dpTime )
    cmds.joint( prefix+name+'01_Jnt', e=True, oj='xyz', secondaryAxisOrient=secondaryAxisOrient, ch=True, zso=True )
    cmds.joint( TailEndJoint, e=True, oj='none', zso=True )
    denUt.den_DiagPause( dpTime )
    print( '----------------------------------------------------' )
    print( 'done with the joints - now to do the control objects' )
    print( '----------------------------------------------------' )
    
    TailJntAll = TailBindJoints + TailEndJoint
    print( TailJntAll )
    
    # - make the FK controls
    for i in range(jointCount):
        ctrlTaperRadius = ctrlRadius*(1+(1-float(i/jointCount)))
        print( 'ctrlTaperRadius =', ctrlTaperRadius )
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        TailPos = cmds.xform( prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
        TailJnt = TailBindJoints[i]
        TailJntParent = cmds.listRelatives( TailJnt, parent=True, fullPath=True )
        TailFKCtrl = denUt.den_MakeSpike(nodeName=prefix+name+iStrPad+'FK_Ctrl',pos=(0,1.5*ctrlTaperRadius,0),radius=ctrlRadius,doT=True)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        TailFKCtrl = cmds.parent( TailFKCtrl, TailJnt, relative=True )
        if i == 0 :
            TailFKCtrl = cmds.parent( TailFKCtrl, TailJntParent )
        else:
            TailFKCtrl = cmds.parent( TailFKCtrl, TailFKCtrls[i-1] )
        TailFKCtrl = denUt.den_AddZeroNull()
        TailFKCtrl = cmds.ls( TailFKCtrl )
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        cmds.connectAttr( TailFKCtrl[0]+'.rotate', TailJnt+'.rotate' )
        print( TailFKCtrl )
        TailFKCtrls += TailFKCtrl
        if i == 0:
            print( 'first tail Ctrl' )
            cmds.select(TailUtilCtrl)
            denUt.den_UnLockAttr(True,True,True,True)# relock after parenting
            TailUtilCtrl = cmds.parent( TailUtilCtrl, TailFKCtrl, relative=True )
            TailUtilCtrl = cmds.parent( TailUtilCtrl, PelvisSpaceIN )
            denUt.den_LockAttr(True,True,True,False)# relock after parenting
        denUt.den_DiagPause( dpTime )
    
    # - make the IK controls
    for i in range(jointCount+1):
        ctrlTaperRadius = ctrlRadius*(1+(1-float(i/jointCount)))
        print( 'ctrlTaperRadius =', ctrlTaperRadius )
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( 'controls loop ', 'i =', i, '  ', iStr, iStrPad )
        TailJnt = TailJntAll[i] ###
        TailJntParent = cmds.listRelatives( TailJnt, parent=True, fullPath=True )
        
        if (i != 0 ):# dont add a small control for the base of the tail
            for jnt in controlJoints:
                if (i == jnt):# check if the current joint is a joint that gets a larger IK control
                    jntStr = str(jnt)
                    jntStrPad = jntStr.rjust(2,'0')
                    print( '    i =', i, '  ik jnt=', jnt, jntStr, jntStrPad, TailJntParent )
                    #'''
                    TailBallCtrl = denUt.den_MakeBall(nodeName=prefix+name+jntStrPad+'_Ctrl',pos=(0,0,0),radius=ctrlTaperRadius,doT=False)
                    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
                    TailBallCtrl = cmds.parent( TailBallCtrl, TailJntParent, relative=True )
                    TailBallCtrl = cmds.parent( TailBallCtrl, PelvisSpaceIN )
                    TailBallCtrl = denUt.den_AddZeroNull()
                    TailBallCtrls += TailBallCtrl
                    denUt.den_LockAttr(False,False,True,False)# relock after parenting
                    denUt.den_ColorShapeRGB(rgb=(1,0,1))
                    denUt.den_DiagPause( dpTime )
                    #'''
            # -------
            cmds.select( TailJntParent, TailJnt )
            TailHandle = denUt.den_AddIKHandle('ikSCsolver',False)
            TailIKCtrl = denUt.den_MakeCube(nodeName=prefix+name+iStrPad+'IK_Ctrl',pos=(0,1.5*ctrlTaperRadius,0),radius=radius*0.5,doT=True)
            denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting    time.sleep(seconds)
    
            TailIKCtrl = cmds.parent( TailIKCtrl, TailJnt, relative=True )
            TailIKCtrl = cmds.parent( TailIKCtrl, PelvisSpaceIN )
            # -------
            if (i == jointCount):
                #print TailIKCtrl
                TailIKCtrl = cmds.rename( TailIKCtrl, prefix+name+'end_Ctrl' )
                TailIKCtrl = cmds.ls( TailIKCtrl, long=True )
            cmds.select( TailIKCtrl )
            TailIKCtrl = denUt.den_AddZeroNull()
            TailIKCtrl = cmds.ls( TailIKCtrl )
            denUt.den_LockAttr(False,True,True,False)# relock after parenting
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            cmds.connectAttr( TailUtilCtrl[0]+'.'+prefix+name+'_FK_IK', TailHandle+'.ikBlend' )
            TailHandle = cmds.parent( TailHandle, TailIKCtrl )
            TailIKCtrls += TailIKCtrl
            TailHandles += TailHandle
            denUt.den_DiagPause( dpTime )
    print( '----------------------------------------------------' )
    print( 'done with control objects - now to do the constraint' )
    print( '----------------------------------------------------' )
    print( 'TailIKCtrls', TailIKCtrls )
    
    #i = 0 # initialize the counter variable
    for i, ball in enumerate(controlJoints):#loop for each integer in controlJoints
        ballStr = str(ball)
        ballStrPad = ballStr.rjust(2,'0')
        ci = ball-2#sets the index to use with the TailIKCtrls list variable for balls that are not in-betweens
        print( '=== doing ball', ball )
        if ball != controlJoints[-1]: # check to see if it is the last ball
            xCurr = ball+1 # starts by setting the current number to the number of the first in-between joint
            xLast = controlJoints[i+1]-1 # finds the number of the last in-between joint
            ballNextStrPad = str(xLast+1).rjust(2,'0') # find the number of the next ball - uses last in-between and adds one
            print( 'for ball', ball, ' xCurr starts at', xCurr, ' xLast =', xLast )
            if i == 0: # is it the first ball?
                print( ball, ballStrPad, ballNextStrPad, cmds.ls( prefix+name+ballStrPad+'_Ctrl' ), ballStrPad, 'is the FIRST ball' )
            else:
                #print ball, TailIKCtrls[ci]
                TailIKCtrlZero = cmds.listRelatives( TailIKCtrls[ci], parent=True, fullPath=True )
                TailBallCtrl = cmds.ls( prefix+name+ballStrPad+'_Ctrl' )
                print( ball, ballStrPad, ballNextStrPad, TailBallCtrl, TailIKCtrlZero, ballStrPad, 'is an in-between ball' )
                cmds.parentConstraint( TailBallCtrl, TailIKCtrlZero, mo=True )
            #print xLast-xCurr
            w1 = float((xLast+1)-xCurr) #sets the first weight to equal the total number of in-betweens
            w2 = 1.0
            while (xCurr <= xLast): #this will loop over each in-between
                TailIKCtrlZero = cmds.listRelatives( TailIKCtrls[xCurr-2], parent=True, fullPath=True )
                TailBallCtrl_w1 = cmds.ls( prefix+name+ballStrPad+'_Ctrl' )
                TailBallCtrl_w2 = cmds.ls( prefix+name+ballNextStrPad+'_Ctrl' )
                cmds.parentConstraint( TailBallCtrl_w1, TailIKCtrlZero, mo=True, w=pow(w1,2) ) # the pow() makes the weight distribution curvy instead of linear
                cmds.parentConstraint( TailBallCtrl_w2, TailIKCtrlZero, mo=True, w=pow(w2,2) )
                print( 'xCurr =', xCurr, TailBallCtrl_w1[0]+' w1 =', w1, TailBallCtrl_w2[0]+' w2 =', w2, TailIKCtrlZero, 'floats in-between '+ballStrPad+' and '+ballNextStrPad )
                xCurr += 1 # move on to the next one
                w1 -= 1
                w2 += 1
                denUt.den_DiagPause( dpTime )
        else:
            #print TailJnt, ball, 'LAST'
            TailIKCtrlZero = cmds.listRelatives( TailIKCtrls[ci], parent=True, fullPath=True )
            TailEndCtrlZero = cmds.listRelatives( TailIKCtrls[ci+1], parent=True, fullPath=True )
            TailBallCtrl = cmds.ls( prefix+name+ballStrPad+'_Ctrl' )
            print( ball, TailBallCtrl, TailIKCtrlZero, ballStrPad, 'is the LAST ball' )
            print( TailEndCtrlZero )
            cmds.parentConstraint( TailBallCtrl, TailIKCtrlZero, mo=True )
            cmds.parentConstraint( TailBallCtrl, TailEndCtrlZero, mo=True )
        #i += 1 # move the counter on to the next ball
    denUt.den_DiagPause( dpTime )
    
    # add joints to Guts list
    TailGutsALL += TailBindJoints
    # add controls to Controls list
    TailCtrlsALL += TailUtilCtrl
    TailCtrlsALL += TailIKCtrls
    TailCtrlsALL += TailFKCtrls
    TailCtrlsALL += TailBallCtrls
    
    #SpaceOUTs = denUt.den_AddSpaceOUTs(TailBindJoints)
    #print( SpaceOUTs )
        
    cmds.refresh()

    #return TailRigGrp, [PelvisSpaceIN], TailSpaceOUTs, TailBindJoints, TailCtrlsALL, TailGutsALL, TailFKCtrls, TailCtrls, TailHandles
    return TailRigGrp, [PelvisSpaceIN], TailSpaceOUTs, TailBindJoints, TailCtrlsALL, TailGutsALL, TailHandles




# ---------------------------------------------------------------------------------------
# define Sluggy tail rig dynamics creation command 
# works for IK or full IK/FK-blendable tails only - FK tails not supported
# this module works by adding stuff to the existing tail.  It modifies the tail rig instead of building a separate rig part

def den_addTailDynamics( prefix='', name='Tail', TailRigGrp='TailRig_Grp', TailSpaceIN='TailPelvisSpace_IN', TailHandles=[], TailBindJnts=[], nucleusScale=1.0, dpTime=0.01 ):
    #name='Tail'
    #TailRigGrp='TailRig_Grp'
    #TailSpaceIN='TailPelvisSpace_IN'
    #TailHandles = ['Tail01_JntIkh', 'Tail02_JntIkh', 'Tail03_JntIkh', 'Tail04_JntIkh', 'Tail05_JntIkh', 'Tail06_JntIkh', 'Tail07_JntIkh', 'Tail08_JntIkh']
    #TailBindJnts = ['|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt|Tail04_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt|Tail04_Jnt|Tail05_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt|Tail04_Jnt|Tail05_Jnt|Tail06_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt|Tail04_Jnt|Tail05_Jnt|Tail06_Jnt|Tail07_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt|Tail04_Jnt|Tail05_Jnt|Tail06_Jnt|Tail07_Jnt|Tail08_Jnt', '|TailRig_Grp|TailPelvisSpace_IN|Tail01_Jnt|Tail02_Jnt|Tail03_Jnt|Tail04_Jnt|Tail05_Jnt|Tail06_Jnt|Tail07_Jnt|Tail08_Jnt|Tail08_end']
    
    # - use existing tail group and spaceIN to attach the dynamic tail parts
    TailJnts = TailBindJnts + [prefix+name+'_end']
    TailRigGrp = TailRigGrp
    PelvisSpaceIN = TailSpaceIN
    
    # - loop over each joint in the tail and make a curve with a cv at each joint position
    for i in range(len(TailJnts)):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        pos = cmds.xform( TailJnts[i], ws=True, q=True, t=True )# find the joint position
        if (i==0):# if it is the first cv, create the curve with first cv at first joint position...
            print( pos )
            dynCurve = cmds.curve( name=prefix+name+'Crv', degree=1, p=pos )
            print( i, '0' )
        else:# ... otherwise, add cvs to the existing curve
            print( i )
            cmds.curve( dynCurve, a=True, p=pos )
    
        print( dynCurve )
        denUt.den_DiagPause( dpTime )
    
    # - make the curve dynamic ( needs mel )
    cmds.select( dynCurve, r=True )
    mel.eval('makeCurvesDynamic 2 { "0", "0", "1", "1", "0"}')
    
    follicle = cmds.listRelatives( dynCurve, parent=True )
    follicle = cmds.rename( follicle, prefix+name+'_follicle' )
    garbage = cmds.listRelatives( follicle, parent=True )
    follicle = cmds.parent( follicle, PelvisSpaceIN )
    print( 'garbage =', garbage )
    cmds.delete( garbage )
    
    print( 'follicle =', follicle )
    follicleShape = cmds.listRelatives( follicle, shapes=True )
    print( 'follicleShape =', follicleShape )
    cmds.setAttr ( follicleShape[0]+'.pointLock', 1 )
    
    follicleParts = cmds.listConnections( follicleShape )
    print( 'follicleParts =', follicleParts )
    
    dynCurveOut = follicleParts[-1]
    dynCurveOut = cmds.rename( dynCurveOut, prefix+name+'CrvDyn' )
    garbage = cmds.listRelatives( dynCurveOut, parent=True )
    dynCurveOut = cmds.parent( dynCurveOut, TailRigGrp )
    dynCurveOutShape = cmds.listRelatives( dynCurveOut, shapes=True )
    print( 'dynCurveOut =', dynCurveOut )
    print( 'dynCurveOutShape =', dynCurveOutShape )
    print( 'garbage =', garbage )
    cmds.delete( garbage )
    
    hairNode = follicleParts[0]
    hairNode = cmds.parent( hairNode, PelvisSpaceIN )
    hairNode = cmds.rename( hairNode, prefix+name+'_hairSystem' )
    print( 'hairNode =', hairNode )
    hairDynControl = cmds.listRelatives( hairNode, shapes=True )
    hairNucleus = cmds.listConnections( hairDynControl, shapes=True )[1]
    hairNucleus = cmds.parent( hairNucleus, TailRigGrp )
    hairNucleus = cmds.rename( hairNucleus, prefix+name+'_Nucleus' )
    print( 'hairNucleus =', hairNucleus )
    cmds.setAttr( hairNucleus+'.scaleX', nucleusScale )
    cmds.setAttr( hairNucleus+'.scaleY', nucleusScale )
    cmds.setAttr( hairNucleus+'.scaleZ', nucleusScale )
    
    
    segNum = len(TailJnts)-1
    print( 'segNum =', segNum )
    #zeroConstant = cmds.createNode( 'floatConstant', name=prefix+name+'_floatConstant' )
    #cmds.setAttr( zeroConstant+'.inFloat', 0 )
    uvPin = cmds.createNode( 'uvPin', name=prefix+name+'_uvPin' )
    print( 'uvPin =', uvPin )
    
    
    cmds.connectAttr( follicleShape[0]+'.outCurve', uvPin+'.originalGeometry' )
    cmds.connectAttr( dynCurveOutShape[0]+'.worldSpace[0]', uvPin+'.deformedGeometry' )
    
    TailUtilCtrl = cmds.ls( prefix+name+'Util_Ctrl' )[0]
    print( 'TailUtilCtrl =', TailUtilCtrl ) 
    dynAttr = cmds.addAttr( TailUtilCtrl, longName=prefix+name+'_Dyn', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    vAttr = cmds.addAttr( TailUtilCtrl, longName=prefix+name+'_Vconst', defaultValue=0.0 )
    print(dynAttr)
    cmds.setAttr( TailUtilCtrl+'.'+prefix+name+'_Dyn', lock=False, keyable=True, channelBox=True )
    cmds.setAttr( TailUtilCtrl+'.'+prefix+name+'_Dyn', keyable=True )
    
    # - build the rivets
    for i in range(len(TailJnts)):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        if ( i>0 ):
            Uval = i/segNum
            rivet = denUt.den_makeLoc( nodeName=prefix+name+iStrPad+'_Riv', pos=(0, 0, 0), radius=1.1 )
            rivet = cmds.parent( rivet, TailRigGrp )
            print( 'rivet =', rivet )
            cmds.connectAttr( TailUtilCtrl+'.'+prefix+name+'_Vconst', uvPin+'.coordinate['+str(i-1)+'].coordinateV' )
            cmds.setAttr( uvPin+'.coordinate['+str(i-1)+'].coordinateU', Uval )
            cmds.connectAttr( uvPin+'.outputMatrix['+str(i-1)+']', rivet[0]+'.offsetParentMatrix' )
            print( i, Uval )
            TailHandle = TailHandles[i-1]
            TailHandleParent = cmds.listRelatives( TailHandle, parent=True )[0]
            print( 'TailHandle =', TailHandle )
            print( 'TailHandleParent =', TailHandleParent )
            TailHandleCon = cmds.pointConstraint( TailHandleParent, TailHandle, mo=True, w=1 )[0]
            TailHandleCon = cmds.pointConstraint( rivet, TailHandle, mo=True, w=0 )[0]
            print( 'TailHandleCon =', TailHandleCon )
            revNode = cmds.createNode( 'reverse', name=prefix+name+iStrPad+'_reverse' )
            cmds.connectAttr( TailUtilCtrl+'.'+prefix+name+'_Dyn', revNode+'.inputX' )
            cmds.connectAttr( TailUtilCtrl+'.'+prefix+name+'_Dyn', TailHandleCon+'.'+rivet[0]+'W1' )
            cmds.connectAttr( revNode+'.outputX', TailHandleCon+'.'+TailHandleParent+'W0' )
            
        denUt.den_DiagPause( dpTime )
    
    
    denUt.den_DiagPause( dpTime )
    
    cmds.refresh()
    return hairDynControl # returns node that controls dynamics settings for later customization




# ---------------------------------------------------------------------------------------
# define Sluggy fin pivots creation command

def den_makeFinPivs( side='L_', prefix='', name='FinA', jointCount=3, radius=1.0, dpTime=0.01, size=100 ):
    #side='L_'
    #name='FinA'
    #jointCount=3
    #radius=0.2
    
    FinPiv = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    UpPiv = denUt.den_makeLoc( nodeName=side+prefix+name+'_upPiv', pos=(size, size*0.2, 0), radius=radius )
    denUt.den_ColorShape(23)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    UpPiv = cmds.parent( UpPiv, FinPiv )[0]
    pivs = []
    
    for jx in range(jointCount+1):
        jxStr = str(jx+1)
        jxStrPad = jxStr.rjust(2,'0')
        jxPrev = str(jx)
        jxPrevPad = jxPrev.rjust(2,'0')
        #print jx, jxStr, jxStrPad, jxPrevPad
        if (jx == jointCount):
            piv = denUt.den_makeLoc( nodeName=side+prefix+name+jxStrPad+'_Piv', pos=(size+jx*size*0.2, 0, 0-jx*size*0.2), radius=radius*0.5 )
        else:
            piv = denUt.den_makeLoc( nodeName=side+prefix+name+jxStrPad+'_Piv', pos=(size+jx*size*0.2, 0, 0-jx*size*0.2), radius=radius )
        denUt.den_ColorShape(20)
        if (jx == 1):
            pivPrev = cmds.ls( side+prefix+name+jxPrevPad+'_Piv' )
            print( 'piv =', piv, pivPrev, jxStrPad, jxPrevPad )
            cmds.aimConstraint( piv, pivPrev, worldUpType='object', worldUpObject=UpPiv )
            denUt.den_DiagPause( dpTime )
        piv = cmds.parent( piv, FinPiv )
        if (jx == jointCount):
            print( 'piv =', piv )
            piv = cmds.rename( side+prefix+name+jxStrPad+'_Piv', side+prefix+name+'End_Piv' )
            piv = [piv]
            print( 'renamed end piv =', piv )
            #print( side+prefix+name+jxStrPad+'_Piv' )
        pivs += piv
        denUt.den_DiagPause( dpTime )
    
    for piv in pivs:
        cmds.select( piv )
        denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    if side == 'R_':
        cmds.setAttr( FinPiv+'.scaleX', -1 )
    print( pivs )
    cmds.refresh()
    return FinPiv




# ---------------------------------------------------------------------------------------
# define Sluggy fin rig creation command ( FK only )

def den_makeFinRigFK( side='L_', prefix='', name='FinA', jointCount=3, radius=1.0, secondaryAxisOrient='yup', dpTime=0.01 ):
    #side='L_'
    #name='FinA'
    #jointCount=3
    #radius=0.5
    #secondaryAxisOrient='zup'
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    cmds.refresh()
        
    FinRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp', pos=(0,0,0) )
    FinSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'Space_IN', pos=(0,0,0) )
    FinSpaceIN = cmds.parent( FinSpaceIN, FinRigGrp )
    FinBindJoints = []
    
    #Set variables to hold names of all the controls and guts
    FinCtrlsALL = []
    FinGutsALL = []
    
    last_i = 0
    for i in range(jointCount+1):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        
        if (i == jointCount):
            FinPos = cmds.xform( side+prefix+name+'End_Piv', ws=True, q=True, t=True )
        else:
            FinPos = cmds.xform( side+prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
        
        FinJxJoint = denUt.den_makeJoint( nodeName=side+prefix+name+iStrPad+'_Jnt', pos=(FinPos), radius=radius, leaveSelected=True )
        FinJxJoint = cmds.ls( FinJxJoint )
        print( FinJxJoint )
        if (i == jointCount):
            FinJxJoint = cmds.rename( FinJxJoint, side+prefix+name+'_end' )
            FinJxJoint = cmds.ls( FinJxJoint )
            cmds.setAttr( FinJxJoint[0]+'.radius', radius*0.5 )
            print( FinJxJoint )
        else:
            FinBindJoints += FinJxJoint
        last_i += 1
        denUt.den_DiagPause( dpTime )
    last = str(last_i).rjust(2,'0')
    print( last )
    
    # -- orient the joints
    cmds.select( clear=True )
    finLastJoint = cmds.ls( FinBindJoints[-1] )
    print( finLastJoint )
    fin01JointParent = cmds.listRelatives( side+prefix+name+'01_Jnt', parent=True, fullPath=True )
    fin01Joint = cmds.parent( side+prefix+name+'01_Jnt', side+prefix+name+'01_Piv' ) # -- temp reparent finger under planar space
    fin02Joint = cmds.ls( side+prefix+name+'02_Jnt' )
    print( 'last', last, finLastJoint )
    cmds.joint( fin01Joint, e=True, oj='none', zso=True )
    cmds.joint( fin02Joint, e=True, oj='xyz', secondaryAxisOrient=secondaryAxisOrient, zso=True, ch=True )
    cmds.joint( finLastJoint, e=True, oj='none', zso=True )
    fin01Joint = cmds.parent( fin01Joint, fin01JointParent )[0] # -- put finger back
    
    for i in range(jointCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        iEnd = str(i)
        iEndPad = iEnd.rjust(2,'0')
        FinPos = cmds.xform( side+prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
        FinJxJoint = FinBindJoints[i]
        FinJxJointParent = cmds.listRelatives( FinJxJoint, parent=True, fullPath=True )
        
        FinCtrl = denUt.den_MakeSpike(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=radius*2,doT=False)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        FinCtrl = cmds.parent( FinCtrl, FinJxJoint, relative=True )
        FinCtrl = cmds.parent( FinCtrl, FinJxJointParent )
        FinCtrl = denUt.den_AddZeroNull()
        FinCtrlsALL += FinCtrl
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        cmds.connectAttr( FinCtrl[0]+'.rotate', FinJxJoint+'.rotate' )
        denUt.den_DiagPause( dpTime )
    
    print( FinBindJoints )
    cmds.refresh()
    if side == 'R_':
        cmds.setAttr( FinRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    return FinRigGrp, FinSpaceIN, [], FinBindJoints, FinCtrlsALL, FinGutsALL



# ---------------------------------------------------------------------------------------
# define Belly pivs creation command

def den_makeSluggyBellyPivs( prefix='', name='Belly', jointCount=4, radius=0.2, dpTime=0.01, size=100 ):
    #name='Belly'
    #jointCount=4
    #radius=0.2 
    
    size=size*0.2
    
    BellyPiv = denUt.den_makeGrp( nodeName=prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    #jointCount = 8
    for jx in range(jointCount):
        jxStr = str(jx+1)
        jxStrPad = jxStr.rjust(2,'0')
        jxEnd = str(jx)
        jxEndPad = jxEnd.rjust(2,'0')
        print( jx, jxStr, jxStrPad )
        piv = denUt.den_makeLoc( nodeName=prefix+name+jxStrPad+'_Piv', pos=(0, 0, 0+jx*size), radius=radius )
        denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
        denUt.den_ColorShape(20)
        if (jx == jointCount):
            print( 'piv =', piv )
        cmds.parent( piv, BellyPiv )
        denUt.den_DiagPause( dpTime )
    
    cmds.refresh()
    
    PelvisAttPiv = denUt.den_makeLoc( nodeName=prefix+'PelvisAtt_Piv', pos=(0, -size, size), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20)
    Spine03AttPiv = denUt.den_makeLoc( nodeName=prefix+'Spine03Att_Piv', pos=(0, -size, 2*size), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20)
    ChestAttPiv = denUt.den_makeLoc( nodeName=prefix+'ChestAtt_Piv', pos=(0, -size, 3*size), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20)
    cmds.parent( PelvisAttPiv, Spine03AttPiv, ChestAttPiv, BellyPiv )
    
    
    return BellyPiv



# ---------------------------------------------------------------------------------------
# define Belly rig creation command

def den_makeSluggyBellyRig( prefix='', name='Belly', jointCount=4, radius=0.5, dpTime=0.01 ):
    #name='Belly'
    #jointCount=4
    #radius=0.5 
    
    BellyRig = denUt.den_makeGrp( nodeName=prefix+name+'Rig_Grp', pos=(0,0,0) )
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'PelvisSpace_IN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, BellyRig )
    Spine01SpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'Spine01Space_IN', pos=(0,0,0) )
    Spine01SpaceIN = cmds.parent( Spine01SpaceIN, BellyRig )
    Spine02SpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'Spine02Space_IN', pos=(0,0,0) )
    Spine02SpaceIN = cmds.parent( Spine02SpaceIN, BellyRig )
    Spine03SpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'Spine03Space_IN', pos=(0,0,0) )
    Spine03SpaceIN = cmds.parent( Spine03SpaceIN, BellyRig )
    Spine04SpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'Spine04Space_IN', pos=(0,0,0) )
    Spine04SpaceIN = cmds.parent( Spine04SpaceIN, BellyRig )
    ChestSpaceIN = denUt.den_makeGrp( nodeName=prefix+name+'ChestSpace_IN', pos=(0,0,0) )
    ChestSpaceIN = cmds.parent( ChestSpaceIN, BellyRig )
    
    BellySpaceINs = []
    BellySpaceINs += PelvisSpaceIN+Spine01SpaceIN+Spine02SpaceIN+Spine03SpaceIN+Spine04SpaceIN+ChestSpaceIN
    
    #JxJnts = []
    BellyBindJoints = []
    
    #Set variables to hold names of all the controls and guts
    BellyCtrlsALL = []
    BellyGutsALL = []
    
    #jointCount = 8
    for i in range(jointCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        spaceIN = prefix+name+'Spine'+iStrPad+'Space_IN'
        cmds.select( clear=True )
        bellyJxPos = cmds.xform( prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
        print( prefix+name+iStrPad+'_Piv' )
        bellyEndPos = [ bellyJxPos[0], bellyJxPos[1]-4.0*radius, bellyJxPos[2] ]
        print( bellyJxPos )
        print( bellyEndPos )
        bellyJx = denUt.den_makeJoint( nodeName=prefix+name+iStrPad+'_Jnt', pos=(bellyJxPos), radius=radius, leaveSelected=True )
        bellyEnd = denUt.den_makeJoint( nodeName=prefix+name+iStrPad+'_End', pos=(bellyEndPos), radius=radius, leaveSelected=True )
        cmds.joint( bellyJx, e=True, oj='xyz', zso=True, ch=True )
        cmds.select( bellyJx, bellyEnd )
        BellyHandle = denUt.den_AddIKHandle('ikSCsolver',False)
        BellyHandle = cmds.parent( BellyHandle, spaceIN )
        bellyJx = cmds.parent( bellyJx, spaceIN )
        BellyBindJoints += bellyJx
    
    
    for obj in ('Pelvis', 'Spine03', 'Chest'):
        print( obj )
        pos = cmds.xform( prefix+obj+'Att_Piv', ws=True, q=True, t=True )
        loc = denUt.den_makeLoc( nodeName=prefix+obj+'Att_Loc', pos=pos, radius=radius )
        loc = cmds.parent( loc, prefix+name+obj+'Space_IN' )
    
    cmds.pointConstraint( prefix+'PelvisAtt_Loc', prefix+'Belly01_JntIkh', w=1.5, mo=False )
    cmds.pointConstraint( prefix+'Spine03Att_Loc', prefix+'Belly01_JntIkh', w=1, mo=False )
    
    cmds.pointConstraint( prefix+'PelvisAtt_Loc', prefix+'Belly02_JntIkh', w=1, mo=False )
    cmds.pointConstraint( prefix+'Spine03Att_Loc', prefix+'Belly02_JntIkh', w=3, mo=False )
    
    cmds.pointConstraint( prefix+'ChestAtt_Loc', prefix+'Belly03_JntIkh', w=1, mo=False )
    cmds.pointConstraint( prefix+'Spine03Att_Loc', prefix+'Belly03_JntIkh', w=3, mo=False )
    
    cmds.pointConstraint( prefix+'ChestAtt_Loc', prefix+'Belly04_JntIkh', w=2, mo=False )
    cmds.pointConstraint( prefix+'Spine03Att_Loc', prefix+'Belly04_JntIkh', w=1, mo=False )
    
    cmds.parentConstraint( prefix+'BellyChestSpace_IN', prefix+'ChestAtt_Loc', w=3, mo=True )
    cmds.parentConstraint( prefix+'BellySpine04Space_IN', prefix+'ChestAtt_Loc', w=1, mo=True )
    
    cmds.parentConstraint( prefix+'BellySpine03Space_IN', prefix+'Spine03Att_Loc', w=5, mo=True )
    cmds.parentConstraint( prefix+'BellyChestSpace_IN', prefix+'Spine03Att_Loc', w=0.1, mo=True )
    cmds.parentConstraint( prefix+'BellyPelvisSpace_IN', prefix+'Spine03Att_Loc', w=1, mo=True )
    
    
    cmds.refresh()
    

    #print( JxJnts )
    return BellyRig, BellySpaceINs, [], BellyBindJoints, BellyCtrlsALL, BellyGutsALL




def den_MakeStuck( sticky='L_FinA_Sticky', bodyGeo='Body_Geo', StickyJoints=[], dpTime=0.01 ):
    #sticky='L_FinA_Sticky'
    #bodyGeo='Body_Geo'
    #StickyJoints=StickyJoints
    
    
    StickySkinClust = cmds.skinCluster( sticky, StickyJoints, tsb=True, name=sticky+'_skinCluster' )[0]
    
    cmds.select( bodyGeo )
    cmds.select( sticky, add=True  )
    
    # transfer weights from body to sticky patch
    cmds.copySkinWeights( noMirror=True, surfaceAssociation='closestPoint', influenceAssociation='closestJoint' )
    
    StuckName = sticky.replace('_Sticky', '_Stuck')
    StuckLocName = sticky.replace('_Sticky', '_StuckLoc')
    Stuck = denUt.den_makeLoc( nodeName=StuckName, pos=(0, 0, 0), radius=0.2 )
    StuckLoc = denUt.den_makeLoc( nodeName=StuckLocName, pos=(0, 0, 0), radius=0.2 )
    StuckLoc = cmds.parent( StuckLoc, Stuck )
    print( 'Stuck -', Stuck )
    
    cmds.select( sticky+'Shape.f[0]' )
    cmds.select( Stuck, add=True )
    cmds.pointOnPolyConstraint( )
    
    return Stuck, StuckLoc



# ====================================================================================
def den_makeWebPivs( side='L_', prefix='', name='WebA', radius=0.2, ctrlCount=3, up=[0,1,0], dpTime=0.01 ):
    #side='L_'
    #name='Web'
    #radius=0.2
    #ctrlCount=3
    #up=[0.1,1.0,0.0]
    
    WebPiv = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp', pos=(0,0,0) )
    WebPivName = cmds.ls( WebPiv )[0]
    print( WebPiv )
    cmds.addAttr( WebPiv, longName='up_vector', at='double3' )
    cmds.addAttr( WebPiv, longName='up_vectorX', at='double', parent='up_vector' )
    cmds.addAttr( WebPiv, longName='up_vectorY', at='double', parent='up_vector' )
    cmds.addAttr( WebPiv, longName='up_vectorZ', at='double', parent='up_vector' )
    cmds.setAttr( WebPivName+'.up_vector', up[0], up[1], up[2] )
    
    for jx in range(ctrlCount+1):
        jxStr = str(jx)
        jxStrPad = jxStr.rjust(2,'0')
        jxPrev = str(jx-1)
        jxPrevPad = jxPrev.rjust(2,'0')
        print( jx, jxStr, jxStrPad,jxPrevPad )
        piv = denUt.den_makeLoc( nodeName=side+prefix+name+jxStrPad+'_Piv', pos=(4+jx, 0, 0-jx), radius=radius )
        if (jx > 0):
            pivPrev = cmds.ls( side+prefix+name+jxPrevPad+'_Piv' )
            print( 'piv =', piv, pivPrev, jxStrPad, jxPrevPad )
            print( 'aim', piv, 'at', pivPrev )
            aimCon = cmds.aimConstraint( pivPrev, piv, aimVector=[-1,0,0], worldUpType='vector', worldUpVector=up )
            print( aimCon[0] )
            cmds.connectAttr( WebPivName+'.up_vector', aimCon[0]+'.worldUpVector' )
            if (jx == ctrlCount):
                print( 'last', pivPrev, piv )
        #cmds.setAttr( piv[0]+'.displayLocalAxis', 1 )
        cmds.parent( piv, WebPiv )
        denUt.den_DiagPause( dpTime )
    
    
    if side == 'R_':
        cmds.setAttr( WebPiv+'.scaleX', -1 )
    
    cmds.refresh()
    return WebPiv


'''
# ====================================================================================
def den_makeWebRig( side='L_', prefix='', name='WebA', ctrlCount=3, radius=0.3, makeJnts=True, dpTime=0.01 ):
    #side='L_'
    #name='Web'
    #ctrlCount=3
    #radius = 0.3
    
    WebMesh = cmds.ls( side+prefix+name+'_Mesh' )[0]
    if WebMesh == '':
        print( 'ERROR - no such geometry', side+prefix+name+'_Mesh' )
    else:
        print( 'found', side+prefix+name+'_Mesh' )
    
    #side = 'R_'
    sideColor = 6
    if side == 'R_':
        upX = cmds.getAttr( side+prefix+name+'Piv_Grp.up_vectorX' )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', -1*upX )# up vector for pivots needs to be mirrored because up vector is in world space not object space
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        cmds.setAttr( WebMesh+'.scaleX', -1 )
        sideColor = 13
    
    cmds.refresh()
    
    WebRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp', pos=(0,0,0) )
    WebBindJoints = []
    WebClusterHandles = []
    
    Faces = cmds.polyEvaluate( WebMesh, face=True )
    Verts = cmds.polyEvaluate( WebMesh, vertex=True )
    print( WebMesh, Faces, Verts )
    
    #cmds.polyAutoProjection( WebMesh, layoutMethod=0, constructionHistory=False, createNewMap=False, layout=2, scaleMode=1, optimize=1, percentageSpace=0.2 )
    
    cmds.select( clear=True )
    
    for i in range(ctrlCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        WebPiv = cmds.ls( side+prefix+name+iStrPad+'_Piv' )
        WebPos = cmds.xform( WebPiv, ws=True, q=True, t=True )
        print( 'i =', i, iStrPad, WebPos )
        WebCtrl = denUt.den_MakeCube(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=radius,doT=False)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        WebCtrl = cmds.parent( WebCtrl, WebPiv, relative=True )
        WebCtrl = cmds.parent( WebCtrl, WebRigGrp )
        WebCtrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(False,True,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    if makeJnts:
        for i in range(Faces):
            #make joint
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_f_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_f_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( clear=True )
            #constrain to face
            cmds.select( WebMesh+'Shape.f['+iStr+']' )
            cmds.select( jntLoc, add=True )
            cmds.pointOnPolyConstraint( maintainOffset=False )
            cmds.select( clear=True )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
        
        print( WebBindJoints )
    
    
    for i in range(Verts):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        
        #make cluster
        cmds.select( WebMesh+'.vtx['+iStr+']' )
        WebCluster = cmds.cluster( name=WebMesh+iStrPad+'_Cluster', rel=True )
        print( WebCluster )
        WebClusterHandle = cmds.ls( WebCluster[1] )
        WebClusterHandle = cmds.parent( WebClusterHandle, WebRigGrp )
        cmds.select( clear=True )
        WebClusterHandles += WebClusterHandle
    
    if makeJnts:
        uvPin = cmds.createNode( 'uvPin', name=side+prefix+name+'_uvPin' )
        print( 'uvPin =', uvPin )
        cmds.connectAttr( WebMesh+'ShapeOrig.outMesh', uvPin+'.originalGeometry' )
        cmds.connectAttr( WebMesh+'Shape.outMesh', uvPin+'.deformedGeometry' )
        for i in range(Verts):
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_cv_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_cv_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( WebMesh+'.map['+iStr+']' )
            WebUV = cmds.polyEditUV( query=True ); print( WebUV )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateU', WebUV[0] )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateV', WebUV[1] )
            cmds.connectAttr( uvPin+'.outputMatrix['+str(i)+']', jntLoc[0]+'.offsetParentMatrix' )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
    
    
    print( WebClusterHandles )
    
    if side == 'R_':
        cmds.setAttr( WebRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', upX )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
        cmds.setAttr( WebMesh+'.scaleX', 1 )
    
    return WebRigGrp, WebBindJoints, WebClusterHandles



# ====================================================================================
def den_makeWebRig2( side='L_', prefix='', name='WebA', ctrlCount=3, radius=0.3, makeJnts=True, dpTime=0.01 ):
    #side='L_'
    #name='Web'
    #ctrlCount=3
    #radius = 0.3
    
    WebMesh = cmds.ls( side+prefix+name+'_Mesh' )[0]
    if WebMesh == '':
        print( 'ERROR - no such geometry', side+prefix+name+'_Mesh' )
    else:
        print( 'found', side+prefix+name+'_Mesh' )
    
    #side = 'R_'
    sideColor = 6
    if side == 'R_':
        upX = cmds.getAttr( side+prefix+name+'Piv_Grp.up_vectorX' )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', -1*upX )# up vector for pivots needs to be mirrored because up vector is in world space not object space
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        cmds.setAttr( WebMesh+'.scaleX', 1 )
        sideColor = 13
    
    cmds.refresh()
    
    WebRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp', pos=(0,0,0) )
    WebBindJoints = []
    WebClusterHandles = []
    
    #cmds.select( WebMesh )
    Faces = cmds.polyEvaluate( WebMesh, face=True )
    Verts = cmds.polyEvaluate( WebMesh, vertex=True )
    print( WebMesh, Faces, Verts )
    
    cmds.select( clear=True )
    
    for i in range(ctrlCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        WebPiv = cmds.ls( side+prefix+name+iStrPad+'_Piv' )
        WebPos = cmds.xform( WebPiv, ws=True, q=True, t=True )
        print( 'i =', i, iStrPad, WebPos )
        WebCtrl = denUt.den_MakeCube(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=radius,doT=False)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        WebCtrl = cmds.parent( WebCtrl, WebPiv, relative=True )
        WebCtrl = cmds.parent( WebCtrl, WebRigGrp )
        WebCtrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(False,True,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    if (0):
        for i in range(Faces):
            #make joint
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_f_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_f_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( clear=True )
            #constrain to face
            cmds.select( WebMesh+'Shape.f['+iStr+']' )
            cmds.select( jntLoc, add=True )
            cmds.pointOnPolyConstraint( maintainOffset=False )
            cmds.select( clear=True )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
        
        print( WebBindJoints )
    
    
    for i in range(Verts):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        
        #make cluster
        cmds.select( WebMesh+'.vtx['+iStr+']' )
        WebCluster = cmds.cluster( name=WebMesh+iStrPad+'_Cluster', rel=True )
        print( WebCluster )
        WebClusterHandle = cmds.ls( WebCluster[1] )
        WebClusterHandle = cmds.parent( WebClusterHandle, WebRigGrp )
        cmds.select( clear=True )
        WebClusterHandles += WebClusterHandle
    
    if makeJnts:
        uvPin = cmds.createNode( 'uvPin', name=side+prefix+name+'_uvPin' )
        print( 'uvPin =', uvPin )
        cmds.connectAttr( WebMesh+'ShapeOrig.outMesh', uvPin+'.originalGeometry' )
        cmds.connectAttr( WebMesh+'Shape.outMesh', uvPin+'.deformedGeometry' )
        for i in range(Verts):
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_cv_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_cv_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( WebMesh+'.map['+iStr+']' )
            WebUV = cmds.polyEditUV( query=True ); print( WebUV )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateU', WebUV[0] )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateV', WebUV[1] )
            cmds.connectAttr( uvPin+'.outputMatrix['+str(i)+']', jntLoc[0]+'.offsetParentMatrix' )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
    
    
    print( WebClusterHandles )
    
    if side == 'R_':
        cmds.setAttr( WebRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', upX )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
        cmds.setAttr( WebMesh+'.scaleX', -1 )
    
    return WebRigGrp, WebBindJoints, WebClusterHandles
'''


# ====================================================================================
def den_makeWebRig3( side='L_', prefix='', name='WebA', ctrlCount=3, radius=0.3, makeJnts=True, dpTime=0.01 ):
    #side='L_'
    #name='Web'
    #ctrlCount=3
    #radius = 0.3
    #makeJnts=True 
    
    WebMesh = cmds.ls( side+prefix+name+'_Mesh' )[0]
    if WebMesh == '':
        print( 'ERROR - no such geometry', side+prefix+name+'_Mesh' )
    else:
        print( 'found', side+prefix+name+'_Mesh', WebMesh )
    
    #side = 'R_'
    sideColor = 6
    if side == 'R_':
        upX = cmds.getAttr( side+prefix+name+'Piv_Grp.up_vectorX' )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', -1*upX )# up vector for pivots needs to be mirrored because up vector is in world space not object space
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        cmds.setAttr( WebMesh+'.scaleX', 1 )
        sideColor = 13
    
    cmds.refresh()
    
    WebRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp', pos=(0,0,0) )
    WebBindJoints = []
    WebClusterHandles = []
    
    #cmds.select( WebMesh )
    Faces = cmds.polyEvaluate( WebMesh, face=True )
    Verts = cmds.polyEvaluate( WebMesh, vertex=True )
    print( WebMesh, Faces, Verts )
    
    cmds.select( clear=True )
    
    for i in range(ctrlCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        WebPiv = cmds.ls( side+prefix+name+iStrPad+'_Piv' )
        WebPos = cmds.xform( WebPiv, ws=True, q=True, t=True )
        print( 'i =', i, iStrPad, WebPos )
        WebCtrl = denUt.den_MakeCube(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=radius,doT=False)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        WebCtrl = cmds.parent( WebCtrl, WebPiv, relative=True )
        WebCtrl = cmds.parent( WebCtrl, WebRigGrp )
        WebCtrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(False,True,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
        
    for i in range(Verts):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        
        #make cluster
        cmds.select( WebMesh+'.vtx['+iStr+']' )
        WebCluster = cmds.cluster( name=WebMesh+iStrPad+'_Cluster', rel=True )
        print( WebCluster )
        WebClusterHandle = cmds.ls( WebCluster[1] )
        WebClusterHandle = cmds.parent( WebClusterHandle, WebRigGrp )
        cmds.select( clear=True )
        WebClusterHandles += WebClusterHandle
    
    
    if makeJnts:
        cmds.select( WebMesh )
        smoothNode = cmds.polySmooth( dv=1, keepBorder=False ); print( smoothNode )
        Verts = cmds.polyEvaluate( WebMesh, vertex=True ); print( Verts )
        uvPin = cmds.createNode( 'uvPin', name=side+prefix+name+'_uvPin' )
        restSmooth = cmds.duplicate( smoothNode, name=side+prefix+name+'_restSmooth' )[0]
        #restSmooth = cmds.createNode( 'polySmoothFace', name=side+prefix+name+'_restSmooth' )
        print( 'uvPin =', uvPin )
        print( WebMesh )
        cmds.connectAttr( WebMesh+'ShapeOrig.outMesh', restSmooth+'.inputPolymesh' )
        cmds.connectAttr( restSmooth+'.output', uvPin+'.originalGeometry' )
        cmds.connectAttr( WebMesh+'Shape.outMesh', uvPin+'.deformedGeometry' )
        for i in range(Verts):
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_cv_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_cv_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( WebMesh+'.map['+iStr+']' )
            WebUV = cmds.polyEditUV( query=True ); print( WebUV )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateU', WebUV[0] )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateV', WebUV[1] )
            cmds.connectAttr( uvPin+'.outputMatrix['+str(i)+']', jntLoc[0]+'.offsetParentMatrix' )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
    
    
    print( WebClusterHandles )
    
    if side == 'R_':
        cmds.setAttr( WebRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', upX )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
        cmds.setAttr( WebMesh+'.scaleX', -1 )
    
    return WebRigGrp, WebBindJoints, WebClusterHandles



# ====================================================================================
def den_makeWebRig4( side='L_', prefix='', name='WebA', ctrlCount=3, radius=0.3, fromFing='foo', toFing='foo', dpTime=0.01 ):
    #side='L_'
    #name='Web'
    #ctrlCount=3
    #radius = 0.3
    #fromFing='WingFingA'
    #toFing='WingFingB'
    
    WebMesh = cmds.ls( side+prefix+name+'_Mesh' )[0]
    if WebMesh == '':
        print( 'ERROR - no such geometry', side+prefix+name+'_Mesh' )
    else:
        print( 'found', side+prefix+name+'_Mesh', WebMesh )
    
    #side = 'R_'
    sideColor = 6
    if side == 'R_':
        upX = cmds.getAttr( side+prefix+name+'Piv_Grp.up_vectorX' )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', -1*upX )# up vector for pivots needs to be mirrored because up vector is in world space not object space
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        cmds.setAttr( WebMesh+'.scaleX', 1 )
        sideColor = 13
    
    cmds.refresh()
    
    WebRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp', pos=(0,0,0) )
    WebBindJoints = []
    WebClusterHandles = []
    
    Faces = cmds.polyEvaluate( WebMesh, face=True )
    Verts = cmds.polyEvaluate( WebMesh, vertex=True )
    print( WebMesh, Faces, Verts )
    
    cmds.select( clear=True )
    
    for i in range(Verts):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        
        #make cluster
        cmds.select( WebMesh+'.vtx['+iStr+']' )
        WebCluster = cmds.cluster( name=WebMesh+iStrPad+'_Cluster', rel=True )
        print( WebCluster )
        WebClusterHandle = cmds.ls( WebCluster[1] )
        WebClusterHandle = cmds.parent( WebClusterHandle, WebRigGrp )
        cmds.select( clear=True )
        WebClusterHandles += WebClusterHandle
    
    
    for i in range(ctrlCount+1):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        pStr = iStr.rjust(2,'0')+'_Jnt'
        fStr = str(i+1)
        fStr = fStr.rjust(2,'0')+'_Jnt'
        if( i == ctrlCount ):
            fStr = '_end'
            #print( fStr, 'is last' )
        
        if( i > 0 ):
            WebPiv = cmds.ls( side+prefix+name+iStrPad+'_Piv' )
            WebPos = cmds.xform( WebPiv, ws=True, q=True, t=True )
            print( 'i =', i, iStrPad+'_Ctrl', fStr, 'prev =', pStr )
            WebCtrl = denUt.den_MakeCube(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=radius,doT=False)
            denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
            WebCtrl = cmds.parent( WebCtrl, WebPiv, relative=True )
            WebCtrl = cmds.parent( WebCtrl, WebRigGrp )
            WebCtrl = denUt.den_AddZeroNull()
            denUt.den_LockAttr(False,True,True,False)# relock after parenting
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            
            fromJx = cmds.ls( side+prefix+fromFing+fStr )
            fromPrevJx = cmds.ls( side+prefix+fromFing+pStr )
            print( WebCtrl, side+prefix+fromFing+fStr, fromFing, fStr, fromJx, fromPrevJx )
            fromJnt = denUt.den_makeJoint( side+prefix+fromFing+iStrPad+'_WebJnt', radius=radius, pos=(1,0.5,0), leaveSelected=False )
            fromJntLoc = denUt.den_makeLoc( side+prefix+fromFing+iStrPad+'_WebLoc', radius=radius )
            cmds.setAttr( fromJntLoc[0]+'.displayLocalAxis', 1 )
            fromJnt = cmds.parent( fromJnt, fromJntLoc, relative=False )
            fromJntLoc = cmds.parent( fromJntLoc, WebRigGrp, relative=False )
            cmds.pointConstraint( fromJx, fromJntLoc )
            cmds.aimConstraint( fromPrevJx, fromJntLoc, worldUpType='object', worldUpObject=WebCtrl[0],  )
            WebBindJoints += fromJnt
            
            toJx = cmds.ls( side+prefix+toFing+fStr )
            toPrevJx = cmds.ls( side+prefix+toFing+pStr )
            print( WebCtrl, side+prefix+toFing+fStr, toFing, fStr, toJx, toPrevJx )
            toJnt = denUt.den_makeJoint( side+prefix+toFing+iStrPad+'_WebJnt', radius=radius, pos=(1,0.5,0), leaveSelected=False )
            toJntLoc = denUt.den_makeLoc( side+prefix+toFing+iStrPad+'_WebLoc', radius=radius )
            toJnt = cmds.parent( toJnt, toJntLoc, relative=False )
            toJntLoc = cmds.parent( toJntLoc, WebRigGrp, relative=False )
            cmds.setAttr( toJntLoc[0]+'.displayLocalAxis', 1 )
            cmds.pointConstraint( toJx, toJntLoc )
            cmds.aimConstraint( toPrevJx, toJntLoc, worldUpType='object', worldUpObject=WebCtrl[0],  )
            WebBindJoints += toJnt
    
    
    
    print( WebBindJoints )
    print( WebClusterHandles )
    
    if side == 'R_':
        cmds.setAttr( WebRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', upX )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
        cmds.setAttr( WebMesh+'.scaleX', -1 )
    
    return WebRigGrp, WebBindJoints, WebClusterHandles



# ====================================================================================
def den_makeWebBoxRig( side='L_', prefix='', name='WebA', radius=0.3, dpTime=0.01 ):
    #side='L_'
    #name='Web'
    #ctrlCount=3
    #radius = 0.3
    
    WebMesh = cmds.ls( side+prefix+name+'_Box' )[0]
    if WebMesh == '':
        print( 'ERROR - no such geometry', side+prefix+name+'_Box' )
    else:
        print( 'found', side+prefix+name+'_Box' )
    
    #side = 'R_'
    sideColor = 6
    if side == 'R_':
        #upX = cmds.getAttr( side+prefix+name+'Piv_Grp.up_vectorX' )
        #cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', -1*upX )# up vector for pivots needs to be mirrored because up vector is in world space not object space
        #cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        #cmds.setAttr( WebMesh+'.scaleX', -1 )
        sideColor = 13
    
    cmds.refresh()
    
    WebRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'BoxRig_Grp', pos=(0,0,0) )
    #WebBindJoints = []
    WebClusterHandles = []
    
    #Faces = cmds.polyEvaluate( WebMesh, face=True )
    Verts = cmds.polyEvaluate( WebMesh, vertex=True )
    #print( WebMesh, Faces, Verts )
    
    #cmds.polyAutoProjection( WebMesh, layoutMethod=0, constructionHistory=False, createNewMap=False, layout=2, scaleMode=1, optimize=1, percentageSpace=0.2 )
    
    cmds.select( clear=True )
    '''
    for i in range(ctrlCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        WebPiv = cmds.ls( side+prefix+name+iStrPad+'_Piv' )
        WebPos = cmds.xform( WebPiv, ws=True, q=True, t=True )
        print( 'i =', i, iStrPad, WebPos )
        WebCtrl = denUt.den_MakeCube(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=radius,doT=False)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        WebCtrl = cmds.parent( WebCtrl, WebPiv, relative=True )
        WebCtrl = cmds.parent( WebCtrl, WebRigGrp )
        WebCtrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(False,True,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    if makeJnts:
        for i in range(Faces):
            #make joint
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_f_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_f_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( clear=True )
            #constrain to face
            cmds.select( WebMesh+'Shape.f['+iStr+']' )
            cmds.select( jntLoc, add=True )
            cmds.pointOnPolyConstraint( maintainOffset=False )
            cmds.select( clear=True )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
        
        print( WebBindJoints )
    '''
    
    for i in range(Verts):
        iStr = str(i)
        iStrPad = iStr.rjust(2,'0')
        
        #make cluster
        cmds.select( WebMesh+'.vtx['+iStr+']' )
        WebCluster = cmds.cluster( name=WebMesh+iStrPad+'_Cluster', rel=True )
        print( WebCluster )
        WebClusterHandle = cmds.ls( WebCluster[1] )
        WebClusterHandle = cmds.parent( WebClusterHandle, WebRigGrp )
        cmds.select( clear=True )
        WebClusterHandles += WebClusterHandle
    '''
    if makeJnts:
        uvPin = cmds.createNode( 'uvPin', name=side+prefix+name+'_uvPin' )
        print( 'uvPin =', uvPin )
        cmds.connectAttr( WebMesh+'ShapeOrig.outMesh', uvPin+'.originalGeometry' )
        cmds.connectAttr( WebMesh+'Shape.outMesh', uvPin+'.deformedGeometry' )
        for i in range(Verts):
            iStr = str(i)
            iStrPad = iStr.rjust(2,'0')
            jnt = denUt.den_makeJoint( nodeName=WebMesh+iStrPad+'_cv_WebJnt', radius=radius, leaveSelected=False )
            jntLoc = denUt.den_makeLoc( nodeName=WebMesh+iStrPad+'_cv_WebLoc', radius=radius )
            cmds.setAttr( jntLoc[0]+'.displayLocalAxis', 1 )
            jnt = cmds.parent( jnt, jntLoc )
            cmds.select( WebMesh+'.map['+iStr+']' )
            WebUV = cmds.polyEditUV( query=True ); print( WebUV )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateU', WebUV[0] )
            cmds.setAttr( uvPin+'.coordinate['+str(i)+'].coordinateV', WebUV[1] )
            cmds.connectAttr( uvPin+'.outputMatrix['+str(i)+']', jntLoc[0]+'.offsetParentMatrix' )
            cmds.parent( jntLoc, WebRigGrp )
            print( jnt )
            WebBindJoints += jnt
    '''
    
    print( WebClusterHandles )
    
    if side == 'R_':
        #cmds.setAttr( WebRigGrp+'.scaleX', -1 )
        #cmds.setAttr( side+prefix+name+'Piv_Grp.up_vectorX', upX )
        #cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
        #cmds.setAttr( WebMesh+'.scaleX', 1 )
        print( side )
    
    #return WebRigGrp, WebBindJoints, WebClusterHandles
    return WebRigGrp, WebClusterHandles


