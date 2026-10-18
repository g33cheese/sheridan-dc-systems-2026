#
#  copyright 2017, 2023, Den Turner  -  all rights reserved
#
import sys; sys.dont_write_bytecode=True
import importlib
import inspect

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om


import den_Utilities_v12 as denUt
importlib.reload(denUt)
print(inspect.getfile(inspect.currentframe()), 'is importing', denUt.__file__)



# ---------------------------------------------------------------------------------------
# define Sluggy torso pivot creation command

def den_makeTrexTorsoPivs( prefix='', radius=1.0, dpTime=0.01, size=100 ):
    
    # -- makes torso pivots that can then be re-positioned to match a particular character
    
    TorsoPivGrp = denUt.den_makeGrp( nodeName=prefix+'TorsoPiv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    PelvisPiv = denUt.den_makeLoc( nodeName=prefix+'Pelvis_Piv', pos=(0, size, -size*0.1), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine01Piv = denUt.den_makeLoc( nodeName=prefix+'Spine01_Piv', pos=(0, size, size*0.1), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine02Piv = denUt.den_makeLoc( nodeName=prefix+'Spine02_Piv', pos=(0, size, size*0.2), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    ChestPiv = denUt.den_makeLoc( nodeName=prefix+'Chest_Piv', pos=(0, size, size*0.4), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck01Piv = denUt.den_makeLoc( nodeName=prefix+'Neck01_Piv', pos=(0, size, size*0.5), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck02Piv = denUt.den_makeLoc( nodeName=prefix+'Neck02_Piv', pos=(0, size, size*0.6), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck03Piv = denUt.den_makeLoc( nodeName=prefix+'Neck03_Piv', pos=(0, size, size*0.7), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadPiv = denUt.den_makeLoc( nodeName=prefix+'Head_Piv', pos=(0, size, size*0.8), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadendPiv = denUt.den_makeLoc( nodeName=prefix+'Head_endPiv', pos=(0, size, size*1.0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawPiv = denUt.den_makeLoc( nodeName=prefix+'Jaw_Piv', pos=(0, size*0.9, size*0.8), radius=radius )
    denUt.den_ColorShape(2); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawendPiv = denUt.den_makeLoc( nodeName=prefix+'Jaw_endPiv', pos=(0, size*0.9, size*1.0), radius=radius )
    denUt.den_ColorShape(2); denUt.den_DiagPause( dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.parent( PelvisPiv,Spine01Piv,Spine02Piv,ChestPiv,Neck01Piv,Neck02Piv,Neck03Piv,HeadPiv,HeadendPiv,JawPiv,JawendPiv, TorsoPivGrp )
    cmds.refresh()
    
    return TorsoPivGrp



# ---------------------------------------------------------------------------------------
# define Sluggy torso rig creation command
def den_makeTrexTorsoRig( prefix='', radius=0.7, ctrlRadius=(4.0,5.0,3.0,0.3), displayLocalAxis=False, dpTime=0.01 ):
    #--------------------- testing variables
    #radius = 2.0
    #ctrlRadius=(18.0,20.0,12.0,2.0)
    #displayLocalAxis=False 
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
    #Spine03Pos = cmds.xform( 'Spine03_Piv', ws=True, q=True, t=True )
    #Spine04Pos = cmds.xform( 'Spine04_Piv', ws=True, q=True, t=True )
    ChestPos = cmds.xform( prefix+'Chest_Piv', ws=True, q=True, t=True )
    Neck01Pos = cmds.xform( prefix+'Neck01_Piv', ws=True, q=True, t=True )
    Neck02Pos = cmds.xform( prefix+'Neck02_Piv', ws=True, q=True, t=True )
    Neck03Pos = cmds.xform( prefix+'Neck03_Piv', ws=True, q=True, t=True )
    #Neck04Pos = cmds.xform( 'Neck04_Piv', ws=True, q=True, t=True )
    HeadPos = cmds.xform( prefix+'Head_Piv', ws=True, q=True, t=True )
    HeadEndPos = cmds.xform( prefix+'Head_endPiv', ws=True, q=True, t=True )
    JawPos = cmds.xform( prefix+'Jaw_Piv', ws=True, q=True, t=True )
    JawEndPos = cmds.xform( prefix+'Jaw_endPiv', ws=True, q=True, t=True )
    
    # make sure the TorsoSpaceIN is selected so the first joint will be parented under it when created
    cmds.select( TorsoSpaceIN )
    # -- make the joints
    PelvisJoint = denUt.den_makeJoint( nodeName=prefix+'Pelvis_Jnt', pos=(PelvisPos), radius=radius, leaveSelected=True )
    #print( PelvisJoint, PelvisPos )
    Spine01Joint = denUt.den_makeJoint( nodeName=prefix+'Spine01_Jnt', pos=(Spine01Pos), radius=radius, leaveSelected=True )
    #print( Spine01Joint, Spine01Pos )
    Spine02Joint = denUt.den_makeJoint( nodeName=prefix+'Spine02_Jnt', pos=(Spine02Pos), radius=radius, leaveSelected=True )
    #print( Spine02Joint, Spine02Pos )
    ChestJoint = denUt.den_makeJoint( nodeName=prefix+'Chest_Jnt', pos=(ChestPos), radius=radius, leaveSelected=True )
    #print( ChestJoint, ChestPos )
    Neck01Joint = denUt.den_makeJoint( nodeName=prefix+'Neck01_Jnt', pos=(Neck01Pos), radius=radius, leaveSelected=True )
    #print( Neck01Joint, Neck01Pos )
    Neck02Joint = denUt.den_makeJoint( nodeName=prefix+'Neck02_Jnt', pos=(Neck02Pos), radius=radius, leaveSelected=True )
    #print( Neck02Joint, Neck02Pos )
    Neck03Joint = denUt.den_makeJoint( nodeName=prefix+'Neck03_Jnt', pos=(Neck03Pos), radius=radius, leaveSelected=True )
    #print( Neck03Joint, Neck03Pos )
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
        cmds.setAttr( ChestJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck03Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( HeadJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( JawJoint+'.displayLocalAxis', 1 )
    
    # -- orient the joints
    cmds.joint( PelvisJoint, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True )
    cmds.joint( JawJoint, e=True, oj='yup', zso=True )
    
    # -- set up the ik handles for Spine01, Spine02, Neck
    # -- Pelvis, Cheat, Head will be driven directly by constraints
    cmds.select( Spine01Joint, Spine02Joint )
    Spine01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Spine02Joint, ChestJoint )
    Spine02Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck01Joint, Neck02Joint )
    Neck01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck02Joint, Neck03Joint )
    Neck02Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck03Joint, HeadJoint )
    Neck03Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    
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
    JawCtrl = denUt.den_MakeBall(nodeName=prefix+'Jaw_Ctrl',pos=(0,-ctrlRadius[2],0),radius=ctrlRadius[3],doT=True)
    cmds.xform( t=JawPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # make temporary list of controls to add to Controls list
    stuffToAdd = [PelvisCtrl,ChestCtrl,HeadCtrl,JawCtrl]
    # add controls to Controls list
    TorsoCtrlsALL += stuffToAdd
    print( stuffToAdd )
    print( TorsoCtrlsALL )
    
    # - this loop is here in case more than one spine or neck joint are needed
    VertJoints = [Neck02Joint,Neck03Joint,Spine02Joint]
    print( VertJoints )
    #print NeckCtrlNames
    VertControls = []
    for jx in VertJoints:
        print( jx )
        CtrlName = jx.replace('_Jnt', '_Ctrl')
        print( CtrlName )
        Ctrl = denUt.den_MakeBall(nodeName=CtrlName,pos=(0,ctrlRadius[0],0),radius=0.1*ctrlRadius[0],doT=True)
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
    Spine02Ctrl = VertControls[2]
    
    
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
    Spine02Handle = cmds.parent( Spine02Handle, ChestCtrl ) # make Spine02 ik goal follow Spine03Ctrl
    Neck01Handle = cmds.parent( Neck01Handle, Neck02Ctrl ) # make Neck01 ik goal follow  Neck02Ctrl
    Neck02Handle = cmds.parent( Neck02Handle, Neck03Ctrl ) # make Neck02 ik goal follow  Neck03Ctrl
    Neck03Handle = cmds.parent( Neck03Handle, HeadCtrl ) # make Neck03 ik goal follow  Neck04Ctrl
    
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
    cmds.parentConstraint( ChestJoint, HeadCtrlZero, mo=True ) # makes head control follow chest joint
    
    # distribute influence of pelvis and chest controls to the Vertebrae controls of the spine
    cmds.parentConstraint( PelvisCtrl, ChestCtrl, prefix+'Spine02_CtrlZero', mo=True )
    # spreads the twist forward one joint to avoid last spine joint having no twist
    sc1 = cmds.orientConstraint( PelvisCtrl, prefix+'Spine02_Ctrl', Spine01Handle )
    sc2 = cmds.orientConstraint( prefix+'Spine02_Ctrl', ChestCtrl, Spine02Handle )
    # distribute influence of cheast and head controls to the Vertebrae controls of the neck
    cmds.parentConstraint( ChestCtrl, prefix+'Neck02_CtrlZero', w=3, mo=True )
    cmds.parentConstraint( HeadCtrl, prefix+'Neck02_CtrlZero', w=1, mo=True )
    cmds.parentConstraint( ChestCtrl, prefix+'Neck03_CtrlZero', w=1, mo=True )
    cmds.parentConstraint( HeadCtrl, prefix+'Neck03_CtrlZero', w=3, mo=True )
    cmds.parentConstraint( HeadCtrl, prefix+'Neck03_CtrlZero', w=1, mo=True )
    # spreads the twist forward one joint to avoid last neck joint having no twist
    nc1 = cmds.orientConstraint( ChestCtrl, prefix+'Neck02_Ctrl', Neck01Handle )
    nc2 = cmds.orientConstraint( prefix+'Neck02_Ctrl', prefix+'Neck03_Ctrl', Neck02Handle )
    nc3 = cmds.orientConstraint( prefix+'Neck03_Ctrl', HeadCtrl, Neck03Handle )
    
    for con in [ sc1, sc2, nc1, nc2, nc3 ]:
        print( con )
        cmds.setAttr( con[0]+'.interpType', 2 )
    
    # -- list the jx joints for binding or proxy
    TorsoBindJoints += [ PelvisJoint, Spine01Joint, Spine02Joint, ChestJoint, Neck01Joint, Neck02Joint, Neck03Joint, HeadJoint, JawJoint ]
    
    # -- add the space output nulls
    TorsoSpaceOUTs += denUt.den_AddSpaceOUTs(TorsoBindJoints)
    print( TorsoSpaceOUTs )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, JxJoints, CtrlsALL, GutsALL lists in order
    return TorsoRigGrp, TorsoSpaceINs, TorsoSpaceOUTs, TorsoBindJoints, TorsoCtrlsALL, TorsoGutsALL



def den_makeTrexHindLegPivs( side='L_', prefix='', name='TrexLeg', radius=5.0, kneeDist=50.0, footUpDist=20.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #side='L_'
    #prefix=''
    #name='Leg'
    #radius=5.0
    #kneeDist=70.0
    #footUpDist=40.0
    #dpTime=0.01
    #---------------------
        
    LegPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    
    denUt.den_makeLoc( nodeName='Hip_Piv', pos=(size*0.096, size*0.812, -size*0.253), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Knee_Piv', pos=(size*0.112, size*0.535, -size*0.151), radius=radius  ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Hock_Piv', pos=(size*0.119, size*0.272, -size*0.287), radius=radius  ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ankle_Piv', pos=(size*0.118, size*0.063, -size*0.220), radius=radius  ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ball_Piv', pos=(size*0.120, size*0.017, -size*0.134), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeGrp ( 'BallSole_Piv', pos=(0, 0, 0) ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Toe_Piv', pos=(size*0.124, 0, size*0.001), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    #denUt.den_makeLoc( nodeName='Heel_Piv', pos=(42.0, 1, -75.8), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(3)
    #cmds.polyPlane( name='Heel_Piv', w=7*radius, h=14*radius, sx=1, sy=1, ax=(0,1,0), cuv=2, ch=1 ); cmds.move(42.0,0,-75.8,'Heel_Piv', r=True); cmds.move(0,0,7*radius,'Heel_Piv.vtx[*]', r=True); cmds.setAttr( 'Heel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    cmds.curve( name='Heel_Piv', degree=1, p=[( -1,0,0 ),( 1,0,0 ),( 1,0,2 ),( -1,0,2 ),( -1,0,0 )] ); cmds.move(size*0.118,0,-size*0.214,'Heel_Piv', r=True); cmds.scale(2*radius,0,3.5*radius,'Heel_Piv.cv[*]'); cmds.setAttr( 'Heel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleLF_Piv', pos=(size*0.153, 0, -size*0.134), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleLB_Piv', pos=(size*0.142, 0, -size*0.191), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleRF_Piv', pos=(size*0.081, 0, -size*0.133), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleRB_Piv', pos=(size*0.095, 0, -size*0.190), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    # -- connect the y translate attrs to the xxx to maintain a flat sole
    cmds.connectAttr( 'Ball_Piv.translateX', 'BallSole_Piv.translateX' )
    cmds.connectAttr( 'Ball_Piv.translateZ', 'BallSole_Piv.translateZ' )
    cmds.connectAttr( 'Heel_Piv.translateY', 'BallSole_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'Toe_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleLF_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleRF_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleLB_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleRB_Piv.translateY' )
    
    # - make a set of pivots for the triangle of the reverse two leg bones
    denUt.den_makeLoc( nodeName='KneeMid_Loc', radius=radius*0.5 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(2)
    denUt.den_makeLoc( nodeName='KneePole_Loc', pos=(0, kneeDist, 0), radius=radius*0.5 )
    #cmds.xform ( t=(-40, 80, 0) )
    denUt.den_ColorShape(9)
    cmds.parent( 'KneePole_Loc', 'KneeMid_Loc' )
    
    # - make a second set of pivots for the triangle of the top two leg bones
    denUt.den_makeLoc( nodeName='KneeMid2_Loc', radius=radius*0.5 ) # leave off the L_ so constraint attrs are not confusing when mirrored   ## - new
    denUt.den_ColorShape(2) ## - new
    denUt.den_makeLoc( nodeName='KneePole2_Loc', pos=(0, kneeDist, 0), radius=radius ) ## - new
    denUt.den_ColorShape(9) ## - new
    cmds.parent( 'KneePole2_Loc', 'KneeMid2_Loc' ) ## - new
    # - make a locator to use for orienting the Hock joint
    denUt.den_makeLoc( nodeName='Hock_Loc', radius=radius*0.5 )
    denUt.den_ColorShape(2)
    # - make a locator that shows the up of the foot based on foot pivot locations to aid pivot placement
    denUt.den_makeLoc( nodeName='FootUp_Piv', radius=radius*0.5, pos=(0, footUpDist, footUpDist) )
    denUt.den_ColorShape(14)
    cmds.parent( 'FootUp_Piv', 'Heel_Piv', relative=True )
    
    KneeMidLocPtCon = cmds.pointConstraint( 'Hip_Piv','Ankle_Piv','KneeMid_Loc', mo=False  )[0]
    KneeMidLocAimCon = cmds.aimConstraint( 'Ankle_Piv','KneeMid_Loc', worldUpType='object', worldUpObject='Knee_Piv', mo=False  )[0]
    KneeMidLoc2PtCon = cmds.pointConstraint( 'Hip_Piv','Hock_Piv','KneeMid2_Loc', mo=False  )[0] ## - new
    KneeMidLoc2AimCon = cmds.aimConstraint( 'Hock_Piv','KneeMid2_Loc', worldUpType='object', worldUpObject='Knee_Piv', mo=False  )[0] ## - new
    KneePole2LocPtCon = cmds.pointConstraint( 'KneePole_Loc','KneePole2_Loc', skip='z' )[0] ## - new
    HipPivAimCon = cmds.aimConstraint( 'Knee_Piv','Hip_Piv', worldUpType='object', worldUpObject='Hock_Piv', mo=False  )[0] ## - new
    KneePivAimCon = cmds.aimConstraint( 'Hock_Piv','Knee_Piv', worldUpType='object', worldUpObject='Hip_Piv', mo=False  )[0] ## - new
    HockLocAimCon = cmds.aimConstraint( 'Ankle_Piv','Hock_Loc', worldUpType='object', worldUpObject='KneePole_Loc', mo=False  )[0] ## - new
    HockLocPtCon = cmds.pointConstraint( 'Hock_Piv','Hock_Loc', mo=False  )[0] ## - new
    AnklePivAimCon = cmds.aimConstraint( 'Ball_Piv','Ankle_Piv', worldUpType='object', worldUpObject='FootUp_Piv', mo=False  )[0]
    SoleLFPivAimCon = cmds.aimConstraint( 'SoleLB_Piv','SoleLF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    SoleRFPivAimCon = cmds.aimConstraint( 'SoleRB_Piv','SoleRF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    ToePivAimCon = cmds.aimConstraint( 'Ball_Piv','Toe_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    HeelPivAimCon = cmds.aimConstraint( 'Toe_Piv','Ball_Piv', aimVector=(0,0,1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    
    # - lock down channels the user is not supposed to touch
    cmds.select( LegPivGrp ); denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    cmds.select( 'Hip_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Knee_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Hock_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Hock_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ankle_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ball_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'BallSole_Piv' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Toe_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Heel_Piv' ); denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 1 )
    cmds.select( 'KneeMid_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'KneeMid2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'KneePole_Loc' ); denUt.den_Lock(  0,0,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'KneePole2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FootUp_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleLF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleRF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleLB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleRB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.parent( 'Heel_Piv', 'Hip_Piv', 'Knee_Piv', 'Hock_Piv', 'Hock_Loc', 'KneeMid_Loc', 'KneeMid2_Loc', LegPivGrp )
    cmds.parent( 'Ankle_Piv', 'Ball_Piv', 'BallSole_Piv', 'Toe_Piv', 'SoleLF_Piv', 'SoleLB_Piv', 'SoleRF_Piv', 'SoleRB_Piv', 'Heel_Piv' )
    
    # -- put the L_ back into the node names
    cmds.rename( 'Hip_Piv', side+prefix+'Hip_Piv' )
    cmds.rename( 'Knee_Piv', side+prefix+'Knee_Piv' )
    cmds.rename( 'Hock_Piv', side+prefix+'Hock_Piv' )
    cmds.rename( 'Hock_Loc', side+prefix+'Hock_Loc' ) ## - new
    cmds.rename( 'Ankle_Piv', side+prefix+'Ankle_Piv' )
    cmds.rename( 'Ball_Piv', side+prefix+'Ball_Piv' )
    cmds.rename( 'BallSole_Piv', side+prefix+'BallSole_Piv' )
    cmds.rename( 'Toe_Piv', side+prefix+'Toe_Piv' )
    cmds.rename( 'Heel_Piv', side+prefix+'Heel_Piv' )
    cmds.rename( 'KneeMid_Loc', side+prefix+'KneeMid_Loc' )
    cmds.rename( 'KneeMid2_Loc', side+prefix+'KneeMid2_Loc' ) ## - new
    cmds.rename( 'KneePole_Loc', side+prefix+'KneePole_Loc' )
    cmds.rename( 'KneePole2_Loc', side+prefix+'KneePole2_Loc' ) ## - new
    cmds.rename( 'FootUp_Piv', side+prefix+'FootUp_Piv' )
    cmds.rename( 'SoleLF_Piv', side+prefix+'SoleLF_Piv' )
    cmds.rename( 'SoleRF_Piv', side+prefix+'SoleRF_Piv' )
    cmds.rename( 'SoleLB_Piv', side+prefix+'SoleLB_Piv' )
    cmds.rename( 'SoleRB_Piv', side+prefix+'SoleRB_Piv' )
    cmds.rename( KneeMidLocPtCon, side+KneeMidLocPtCon )
    cmds.rename( KneeMidLocAimCon, side+KneeMidLocAimCon )
    cmds.rename( KneeMidLoc2PtCon, side+KneeMidLoc2PtCon ) ## - new
    cmds.rename( KneeMidLoc2AimCon, side+KneeMidLoc2AimCon ) ## - new
    cmds.rename( KneePole2LocPtCon, side+KneePole2LocPtCon ) ## - new
    cmds.rename( HipPivAimCon, side+HipPivAimCon )
    cmds.rename( AnklePivAimCon, side+AnklePivAimCon )
    cmds.rename( SoleLFPivAimCon, side+SoleLFPivAimCon )
    cmds.rename( SoleRFPivAimCon, side+SoleRFPivAimCon )
    cmds.rename( ToePivAimCon, side+ToePivAimCon )
    cmds.rename( HockLocAimCon, side+HockLocAimCon )
    cmds.rename( HockLocPtCon, side+HockLocPtCon )
    
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( LegPivGrp+'.scaleX', -1 )
    
    return LegPivGrp






# ---------------------------------------------------------------------------------------
def den_makeTrexHindLegRig( side='L_', prefix='', name='TrexLeg', radius=5.0, ctrlRadius=30.0, displayLocalAxis=False, dpTime=0.01 ):
    #--------------------- testing variables
    #side='L_'
    #name='TrexLeg'
    #radius=5.0
    #ctrlRadius=30.0
    #displayLocalAxis=False
    #---------------------
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    denUt.den_DiagPause( dpTime ) # quick refresh to let any pivot constraints re-evaluate
    
    # == set up top groups
    LegRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp' )
    
    # -- set up the return variables
    LegSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    LegSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    LegBindJoints = [] #Set list variable to hold names of all the Jx joints
    LegCtrlsALL = [] #Set list variable to hold names of all the controls
    LegGutsALL = [] #Set list variable to hold names of all the guts
    
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'PelvisSpace_IN' )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, LegRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'CogSpace_IN' )
    CogSpaceIN = cmds.parent( CogSpaceIN, LegRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'AllSpace_IN' )
    AllSpaceIN = cmds.parent( AllSpaceIN, LegRigGrp )[0]
    LegSpaceINs += [ PelvisSpaceIN, CogSpaceIN, AllSpaceIN ]
    LegSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp' )
    LegSkelGrp = cmds.parent( LegSkelGrp, PelvisSpaceIN )[0]
    LegCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp' )
    LegCtrlGrp = cmds.parent( LegCtrlGrp, PelvisSpaceIN )[0]
    # -- make Wrist control space switch constraint
    AnkleCtrlSpace = denUt.den_makeGrp( nodeName=side+prefix+'AnkleCtrl_Space' )
    AnkleCtrlSpace = cmds.parent( AnkleCtrlSpace, LegCtrlGrp )[0]
    AnkleCtrlSpaceConstraint = cmds.parentConstraint( PelvisSpaceIN, AnkleCtrlSpace, weight=0 )
    AnkleCtrlSpaceConstraint = cmds.parentConstraint( CogSpaceIN, AnkleCtrlSpace, weight=0 )
    AnkleCtrlSpaceConstraint = cmds.parentConstraint( AllSpaceIN, AnkleCtrlSpace, weight=1 )
    
    
    # -- set variables for pivot positions
    
    HipPos = cmds.xform( side+prefix+'Hip_Piv', ws=True, q=True, t=True )
    HipPosVec = om.MVector(HipPos[0],HipPos[1],HipPos[2])
    KneePos = cmds.xform( side+prefix+'Knee_Piv', ws=True, q=True, t=True )
    KneePosVec = om.MVector(KneePos[0],KneePos[1],KneePos[2])
    HockPos = cmds.xform( side+prefix+'Hock_Piv', ws=True, q=True, t=True )
    HockPosVec = om.MVector(HockPos[0],HockPos[1],HockPos[2])
    AnklePos = cmds.xform( side+prefix+'Ankle_Piv', ws=True, q=True, t=True )
    AnklePosVec = om.MVector(AnklePos[0],AnklePos[1],AnklePos[2])
    BallPos = cmds.xform( side+prefix+'Ball_Piv', ws=True, q=True, t=True )
    ToePos = cmds.xform( side+prefix+'Toe_Piv', ws=True, q=True, t=True )
    HeelPos = cmds.xform( side+prefix+'Heel_Piv', ws=True, q=True, t=True )
    SoleLFPos = cmds.xform( side+prefix+'SoleLF_Piv', ws=True, q=True, t=True )
    SoleLBPos = cmds.xform( side+prefix+'SoleLB_Piv', ws=True, q=True, t=True )
    SoleRFPos = cmds.xform( side+prefix+'SoleRF_Piv', ws=True, q=True, t=True )
    SoleRBPos = cmds.xform( side+prefix+'SoleLB_Piv', ws=True, q=True, t=True )
    BallSolePos = [ BallPos[0], ToePos[1], BallPos[2] ]
    #print 'BallSolePos', BallSolePos
    KneePolePos = cmds.xform( side+prefix+'KneePole_Loc', ws=True, q=True, t=True )
    KneePole2Pos = cmds.xform( side+prefix+'KneePole2_Loc', ws=True, q=True, t=True )
    
    
    # -- make reverse 2 bone leg joints
    vecA = HipPosVec - KneePosVec
    #print vecA.x, vecA.y, vecA.z
    BoneLenA = om.MVector.length(vecA)
    #print BoneLenA
    
    vecB = KneePosVec - HockPosVec
    #print vecB.x, vecB.y, vecB.z
    BoneLenB = om.MVector.length(vecB)
    #print BoneLenB
    
    vecC = HockPosVec - AnklePosVec
    #print vecC.x, vecC.y, vecC.z
    BoneLenC = om.MVector.length(vecC)
    #print BoneLenC
    
    Leg1JuPivTmp = denUt.den_makeLoc( nodeName=side+prefix+'Leg1Ju_Piv', pos=(HipPos) )
    Leg2JuPivTmp = denUt.den_makeLoc( nodeName=side+prefix+'Leg2Ju_Piv_Tmp' )
    Leg2JuPivTmp = cmds.parent( Leg2JuPivTmp, Leg1JuPivTmp, relative=True )[0]
    Leg1JuPivOri = cmds.orientConstraint( side+prefix+'Knee_Piv', Leg1JuPivTmp, mo=False, offset=(0,0,0) )
    cmds.delete( Leg1JuPivOri )
    cmds.setAttr( Leg2JuPivTmp+'.translateX', BoneLenB )
    
    RevPos = cmds.xform( Leg2JuPivTmp, ws=True, q=True, t=True )
    
    cmds.select( Leg1JuPivTmp )
    Leg1Ju = cmds.joint( n=side+prefix+'Leg1_Ju', p=(HipPos), radius=radius )
    Leg2Ju = cmds.joint( n=side+prefix+'Leg2_Ju', p=(RevPos), radius=radius )
    Leg3Ju = cmds.joint( n=side+prefix+'Leg3_Ju', p=(AnklePos), radius=radius )
    
    # -- make the joints
    cmds.select( clear=True )
    
    HipJoint = cmds.joint( n=side+prefix+'Hip_Jnt', p=(HipPos), radius=radius )
    KneeJoint = cmds.joint( n=side+prefix+'Knee_Jnt', p=(KneePos), radius=radius )
    HockJoint = cmds.joint( n=side+prefix+'Hock_Jnt', p=(HockPos), radius=radius )
    AnkleJoint = cmds.joint( n=side+prefix+'Ankle_Jnt', p=(AnklePos), radius=radius )
    BallJoint = cmds.joint( n=side+prefix+'Ball_Jnt', p=(BallPos), radius=radius )
    ToeJoint = cmds.joint( n=side+prefix+'Toe_Jnt', p=(ToePos), radius=radius )
    
    #print HipJoint, HipPos
    #print KneeJoint, KneePos
    #print AnkleJoint, AnklePos
    #print BallJoint, BallPos
    #print ToeJoint, ToePos
    
    if ( displayLocalAxis ):
        cmds.setAttr( Leg1Ju+'.displayLocalAxis', 1 )
        cmds.setAttr( Leg2Ju+'.displayLocalAxis', 1 )
        cmds.setAttr( Leg3Ju+'.displayLocalAxis', 1 )
        
        cmds.setAttr( HipJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( KneeJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( HockJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( AnkleJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( BallJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ToeJoint+'.displayLocalAxis', 1 )
    
    
    
    # -- orient the joints
    
    #cmds.joint( Leg2Ju, e=True, oj='xzy', secondaryAxisOrient='xup', zso=True )
    cmds.joint( Leg2Ju, e=True, oj='xyz', zso=True )
    #cmds.joint( Leg2Ju, e=True, oj='xzy', secondaryAxisOrient='zdown', aos=True, ch=False, zso=True )
    cmds.joint( Leg3Ju, e=True, oj='none', zso=True )
    cmds.setAttr( Leg3Ju+'.translateX', BoneLenA+BoneLenC )
    Leg1Ju = cmds.parent( Leg1Ju, LegSkelGrp )[0] # -- put hip back under leg skel grp
    
    cmds.select( clear=True )
    cmds.joint( KneeJoint, e=True, oj='xyz', zso=True )
    #cmds.joint( KneeJoint, e=True, oj='xzy', secondaryAxisOrient='zdown', aos=True, ch=False, zso=True )
    HockJoint = cmds.parent( HockJoint, side+prefix+'Hock_Loc' )[0] # -- temp reparent hock
    cmds.joint( HockJoint, e=True, oj='none', zso=True )
    HockJoint = cmds.parent( HockJoint, KneeJoint )[0] # -- put hock back under knee jnt
    cmds.joint( AnkleJoint, e=True, oj='none', zso=True )
    HipJoint = cmds.parent( HipJoint, side+prefix+'Hip_Piv' )[0] # -- temp reparent hip under planar space
    cmds.joint( HipJoint, e=True, oj='none', zso=True )
    HipJoint = cmds.parent( HipJoint, LegSkelGrp )[0] # -- put hip back under leg skel grp
    AnkleJoint = cmds.parent( AnkleJoint, side+prefix+'Ankle_Piv' )[0] # -- temp reparent ankle under planar space
    cmds.joint( BallJoint, e=True, oj='xyz', zso=True )
    cmds.joint( ToeJoint, e=True, oj='none', zso=True )
    AnkleJoint = cmds.parent( AnkleJoint, HockJoint )[0] # -- put ankle back under hock jnt
    
    # -- duplicate the leg to make the FK and IK leg bones
    HipJointIK = cmds.duplicate (HipJoint, name=side+prefix+'Hip_IK' )[0]
    KneeJointIK = cmds.rename (HipJointIK+'|'+side+prefix+'Knee_Jnt', side+prefix+'Knee_IK' )
    HockJointIK = cmds.rename (KneeJointIK+'|'+side+prefix+'Hock_Jnt', side+prefix+'Hock_IK' )
    AnkleJointIK = cmds.rename (HockJointIK+'|'+side+prefix+'Ankle_Jnt', side+prefix+'Ankle_IK' )
    BallJointIK = cmds.rename (AnkleJointIK+'|'+side+prefix+'Ball_Jnt', side+prefix+'Ball_IK' )
    ToeJointIK = cmds.rename (BallJointIK+'|'+side+prefix+'Toe_Jnt', side+prefix+'Toe_IK' )
    #print HipJointIK, '----', KneeJointIK, '----', AnkleJointIK, '----', BallJointIK, '----', ToeJointIK
    HipJointFK = cmds.duplicate (HipJoint, name=side+prefix+'Hip_FK' )[0]
    KneeJointFK = cmds.rename (HipJointFK+'|'+side+prefix+'Knee_Jnt', side+prefix+'Knee_FK' )
    HockJointFK = cmds.rename (KneeJointFK+'|'+side+prefix+'Hock_Jnt', side+prefix+'Hock_FK' )
    AnkleJointFK = cmds.rename (HockJointFK+'|'+side+prefix+'Ankle_Jnt', side+prefix+'Ankle_FK' )
    BallJointFK = cmds.rename (AnkleJointFK+'|'+side+prefix+'Ball_Jnt', side+prefix+'Ball_FK' )
    ToeJointFK = cmds.rename (BallJointFK+'|'+side+prefix+'Toe_Jnt', side+prefix+'Toe_FK' )
    #print HipJointFK, '----', KneeJointFK, '----', AnkleJointFK, '----', BallJointFK, '----', ToeJointFK
    
    # -- make the controls and zero nulls
    
    # -- Hip FK
    HipFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'HipFK_Ctrl', radius=ctrlRadius*1.1, axis='+Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    HipFKCtrl = cmds.parent( HipFKCtrl, HipJointFK, relative=True )
    HipFKCtrl = cmds.parent( HipFKCtrl, LegCtrlGrp )
    HipFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    HipFKCtrlZero = cmds.listRelatives( HipFKCtrl, parent=True, fullPath=True )[0]
    cmds.connectAttr( HipFKCtrl[0]+'.rotate', HipJointFK+'.rotate' )
    cmds.parentConstraint( LegCtrlGrp, HipFKCtrlZero, mo=True )
    #print HipFKCtrl
    # -- Leg Utility
    LegUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(ctrlRadius*0.6,0,ctrlRadius*0.6), radius=ctrlRadius*0.2, Plane='ZX')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# relock after parenting
    LegUtilCtrl = cmds.parent( LegUtilCtrl, HipJointFK, relative=True )
    LegUtilCtrl = cmds.parent( LegUtilCtrl, LegCtrlGrp )
    denUt.den_LockAttr(True,True,True,False)# relock after parenting
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', lock=False, keyable=True )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'Ankle_FK_IK', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'Ankle_FK_IK', lock=False, keyable=True )
    # -- Knee
    KneeCtrl = denUt.den_MakePole( nodeName=side+prefix+'Knee_Ctrl', radius=ctrlRadius*0.3 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=KneePolePos )
    KneeCtrl = cmds.parent( KneeCtrl, LegCtrlGrp )
    KneeCtrl = denUt.den_AddZeroNull()
    # -- Knee2
    Knee2Ctrl = denUt.den_MakePole( nodeName=side+prefix+'Knee2_Ctrl', radius=ctrlRadius*0.15 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=KneePole2Pos )
    Knee2Ctrl = cmds.parent( Knee2Ctrl, KneeCtrl )
    Knee2Ctrl = denUt.den_AddZeroNull()
    
    KneeFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'KneeFK_Ctrl', pos=(0,-ctrlRadius*0.7,0), radius=ctrlRadius*0.5, doT=True, axis='-Y' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    KneeFKCtrl = cmds.parent( KneeFKCtrl, KneeJointFK, relative=True )
    KneeFKCtrl = cmds.parent( KneeFKCtrl, HipFKCtrl )
    KneeFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( KneeFKCtrl[0]+'.rotate', KneeJointFK+'.rotate' )
    #print KneeFKCtrl
    
    # -- Hock
    HockCtrl = denUt.den_MakeCube( nodeName=side+prefix+'Hock_Ctrl', pos=(ctrlRadius*1.0,0,0), radius=ctrlRadius*0.3, doT=True )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=HockPos )
    HockCtrl = cmds.parent( HockCtrl, LegCtrlGrp )
    HockCtrl = denUt.den_AddZeroNull()
    HockCtrlZero = cmds.listRelatives( HockCtrl, parent=True, fullPath=True )[0]
    
    HockFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'HockFK_Ctrl', pos=(0,-ctrlRadius*1.0,0), radius=ctrlRadius*0.3, doT=True, axis='-Y' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    HockFKCtrl = cmds.parent( HockFKCtrl, HockJointFK, relative=True )
    HockFKCtrl = cmds.parent( HockFKCtrl, KneeFKCtrl )
    HockFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( HockFKCtrl[0]+'.rotate', HockJointFK+'.rotate' )
    #print KneeFKCtrl
    
    
    # -- Ankle Controls
    AnkleCtrl = denUt.den_MakeBall( nodeName=side+prefix+'Ankle_Ctrl', radius=ctrlRadius*0.9 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=AnklePos )
    AnkleCtrl = cmds.parent( AnkleCtrl, AnkleCtrlSpace )
    AnkleCtrl = denUt.den_AddZeroNull()
    cmds.setAttr( AnkleCtrl[0]+'.rotateOrder', 1 )
    AnkleCtrlZero = cmds.listRelatives( AnkleCtrl, parent=True, fullPath=True )[0]
    
    AnkleFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'AnkleFK_Ctrl', radius=ctrlRadius*1.1, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    AnkleFKCtrl = cmds.parent( AnkleFKCtrl, AnkleJointFK, relative=True )
    AnkleFKCtrl = cmds.parent( AnkleFKCtrl, HockFKCtrl )
    AnkleFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( AnkleFKCtrl[0]+'.rotate', AnkleJointFK+'.rotate' )
    AnkleFKCtrlZero = cmds.listRelatives( AnkleFKCtrl, parent=True, fullPath=True )[0]
    
    #print AnkleCtrlZero
    BallFKCtrl = denUt.den_MakeSpike(nodeName=side+prefix+'BallFK_Ctrl', radius=ctrlRadius, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    BallFKCtrl = cmds.parent( BallFKCtrl, BallJointFK, relative=True )
    BallFKCtrl = cmds.parent( BallFKCtrl, AnkleFKCtrl )
    BallFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( BallFKCtrl[0]+'.rotate', BallJointFK+'.rotate' )
    BallFKCtrlZero = cmds.listRelatives( BallFKCtrl, parent=True, fullPath=True )[0]
    # -- Foot Utility
    FootUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+'FootUtil_Ctrl', pos=(ctrlRadius,ctrlRadius,0), radius=ctrlRadius*0.2, Plane='XY')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    FootUtilCtrl = cmds.parent( FootUtilCtrl, AnkleCtrl, relative=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootRock', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRock', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRoll', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootPivot', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootTwist', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootTwist', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'HeelPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'HeelPivot', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'ToeRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'ToeRoll', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'ToePivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'ToePivot', lock=False, keyable=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'ToeBend', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'ToeBend', lock=False, keyable=True )
    
    
    # -- connect up the Ankle control space switcher
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'PelvisSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', AnkleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'PelvisSpace_INW0' )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'CogSpace', AnkleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'CogSpace_INW1' )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'AllSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'AllSpace', AnkleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'AllSpace_INW2' )
    
    # -- set up Leg FK_IK blending
    Hip_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Hip_ikFk_pairBlend' )
    cmds.setAttr( Hip_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( HipJointFK+'.rotate', Hip_pairBlend+'.inRotate1' )
    cmds.connectAttr( HipJointIK+'.rotate', Hip_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Hip_pairBlend+'.weight' )
    cmds.connectAttr( Hip_pairBlend+'.outRotate', HipJoint+'.rotate' )
    
    Knee_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Knee_ikFk_pairBlend' )
    cmds.setAttr( Knee_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( KneeJointFK+'.rotate', Knee_pairBlend+'.inRotate1' )
    cmds.connectAttr( KneeJointIK+'.rotate', Knee_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Knee_pairBlend+'.weight' )
    cmds.connectAttr( Knee_pairBlend+'.outRotate', KneeJoint+'.rotate' )
    
    Hock_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Hock_ikFk_pairBlend' )
    cmds.setAttr( Hock_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( HockJointFK+'.rotate', Hock_pairBlend+'.inRotate1' )
    cmds.connectAttr( HockJointIK+'.rotate', Hock_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Hock_pairBlend+'.weight' )
    cmds.connectAttr( Hock_pairBlend+'.outRotate', HockJoint+'.rotate' )
    
    Ankle_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Ankle_ikFk_pairBlend' )
    cmds.setAttr( Ankle_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( AnkleJointFK+'.rotate', Ankle_pairBlend+'.inRotate1' )
    cmds.connectAttr( AnkleJointIK+'.rotate', Ankle_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Ankle_pairBlend+'.weight' )
    cmds.connectAttr( Ankle_pairBlend+'.outRotate', AnkleJoint+'.rotate' )
    
    Ball_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Ball_ikFk_pairBlend' )
    cmds.setAttr( Ball_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( BallJointFK+'.rotate', Ball_pairBlend+'.inRotate1' )
    cmds.connectAttr( BallJointIK+'.rotate', Ball_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Ball_pairBlend+'.weight' )
    cmds.connectAttr( Ball_pairBlend+'.outRotate', BallJoint+'.rotate' )
    
    
    # -- make the reverse foot
    
    footPivs = [ 'Heel_Piv', 'BallSole_Piv', 'SoleLF_Piv', 'SoleRF_Piv', 'Toe_Piv', 'Ball_Piv', 'Ankle_Piv' ]
    footJnts = []
    for i,footPiv in enumerate(footPivs):
        prevNum = i-1
        nameRoot = footPiv.replace('_Piv','')
        #print( 'nameRoot', nameRoot, i )
        footJnt = cmds.joint( n=side+prefix+nameRoot+'Rev_Jx', radius=radius*0.7 )
        footPiv = side+prefix+footPivs[i]
        footJnt = cmds.parent( footJnt, footPiv, relative=True )
        cmds.joint( footJnt, e=True, oj='none', zso=True, radius=radius*0.7 )
        if i != 0:
            footJnt = cmds.parent( footJnt, footJnts[prevNum], relative=False )
        else:
            footJnt = cmds.parent( footJnt, world=True )
        footJnts = footJnts + [footJnt]
    #print(footJnts[5])
    #cmds.joint( footJnts[5], e=True, oj='none', zso=True, radius=radius*0.7 ); denUt.den_DiagPause( 0.02 )
    
    #print footJnts
    RevHeelJoint = footJnts[0]
    RevBallSoleJoint = footJnts[1]
    RevSoleLFJoint = footJnts[2]
    RevSoleRFJoint = footJnts[3]
    RevToeJoint = footJnts[4]
    RevBallJoint = footJnts[5]
    RevAnkleJoint = footJnts[6]
    #print RevHeelJoint
    
    # -- make the reverse Hock bits
    AnkleLiftCtrl = denUt.den_MakeCube( nodeName=side+prefix+'AnkleLift_Ctrl', radius=ctrlRadius*0.2, pos=(0,0.7*ctrlRadius,0), doT=True )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    AnkleLiftCtrl = cmds.parent( AnkleLiftCtrl, RevAnkleJoint, relative=True )
    AnkleLiftCtrl = denUt.den_AddZeroNull()
    AnkleLiftCtrlZero = cmds.listRelatives( AnkleLiftCtrl, parent=True, fullPath=True )[0]
    
    RevHockLoc = cmds.spaceLocator( name=side+prefix+'RevHock_Loc' )
    RevHockLoc = cmds.parent( RevHockLoc, AnkleLiftCtrl, relative=True )
    print( HockCtrl )
    RevHocLocAimCon = cmds.aimConstraint( HockCtrl, RevHockLoc, worldUpType='object', worldUpObject=KneeCtrl[0] )[0]
    
    
    # -- make the ik handles
    cmds.select( Leg1Ju, Leg3Ju )
    LegIK2handle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    LegIK2handle = cmds.parent( LegIK2handle, AnkleLiftCtrl )[0]
    cmds.poleVectorConstraint( KneeCtrl, LegIK2handle )
    cmds.setAttr( LegIK2handle+'.twist', 180 )
    cmds.setAttr( LegIK2handle+'.translate', 0,0,0 )
    
    HockCtrlZeroCon = cmds.parentConstraint( Leg2Ju, HockCtrlZero, mo=True )[0]
    
    #=============================================================================================================='''
    cmds.select( HipJointIK, HockJointIK )
    LegIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    LegIKhandle = cmds.parent( LegIKhandle, RevHockLoc )[0]
    cmds.poleVectorConstraint( Knee2Ctrl, LegIKhandle )
    
    cmds.select( HockJointIK, AnkleJointIK )
    HockIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    HockIKhandle = cmds.parent( HockIKhandle, AnkleLiftCtrl )[0]
    cmds.poleVectorConstraint( KneeCtrl, HockIKhandle )
    cmds.setAttr( HockIKhandle+'.twist', 180 )
    
    cmds.select( AnkleJointIK, BallJointIK )
    BallIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    BallIKhandle = cmds.parent( BallIKhandle, RevBallJoint )[0]
    cmds.select( BallJointIK, ToeJointIK )
    ToeIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    ToeIKhandle = cmds.parent( ToeIKhandle, RevToeJoint )[0]
    
    # -- add utility nodes and connect attrs for foot roll
    footHeelRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footHeelRoll_unitConversion' )
    footHeelRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footHeelRoll_clamp' )
    cmds.setAttr( footHeelRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footHeelRoll_clamp+'.minR', -180 )
    footBallRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footBallRoll_unitConversion' )
    footBallRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footBallRoll_clamp' )
    cmds.setAttr( footBallRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footBallRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRoll', footHeelRoll_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRoll', footBallRoll_clamp+'.inputR' )
    cmds.connectAttr( footHeelRoll_clamp+'.outputR', footHeelRoll_unitConversion+'.input' )
    cmds.connectAttr( footBallRoll_clamp+'.outputR', footBallRoll_unitConversion+'.input' )
    cmds.connectAttr( footHeelRoll_unitConversion+'.output', RevHeelJoint[0]+'.rotateX' )
    cmds.connectAttr( footBallRoll_unitConversion+'.output', RevBallJoint[0]+'.rotateX' )
    
    # -- add utility nodes and connect attrs for foot rock
    footSoleLFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footSoleLFRock_unitConversion' )
    footSoleLFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footSoleLFRock_clamp' )
    cmds.setAttr( footSoleLFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footSoleLFRock_clamp+'.minR', -180 )
    footSoleRFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footSoleRFRock_unitConversion' )
    footSoleRFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footSoleRFRock_clamp' )
    cmds.setAttr( footSoleRFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footSoleRFRock_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRock', footSoleLFRock_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRock', footSoleRFRock_clamp+'.inputR' )
    cmds.connectAttr( footSoleLFRock_clamp+'.outputR', footSoleLFRock_unitConversion+'.input' )
    cmds.connectAttr( footSoleRFRock_clamp+'.outputR', footSoleRFRock_unitConversion+'.input' )
    cmds.connectAttr( footSoleLFRock_unitConversion+'.output', RevSoleLFJoint[0]+'.rotateZ' )
    cmds.connectAttr( footSoleRFRock_unitConversion+'.output', RevSoleRFJoint[0]+'.rotateZ' )
    # -- connect foot pivot
    footBallSolePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footBallSolePivot_unitConversion' )
    cmds.setAttr( footBallSolePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootPivot', footBallSolePivot_unitConversion+'.input' )
    cmds.connectAttr( footBallSolePivot_unitConversion+'.output', RevBallSoleJoint[0]+'.rotateY' )
    # -- connect foot twist
    footBallTwist_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footBallTwist_unitConversion' )
    cmds.setAttr( footBallTwist_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootTwist', footBallTwist_unitConversion+'.input' )
    cmds.connectAttr( footBallTwist_unitConversion+'.output', RevBallJoint[0]+'.rotateZ' )
    # -- connect heel pivot
    footHeelPivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footHeelPivot_unitConversion' )
    cmds.setAttr( footHeelPivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'HeelPivot', footHeelPivot_unitConversion+'.input' )
    cmds.connectAttr( footHeelPivot_unitConversion+'.output', RevHeelJoint[0]+'.rotateY' )
    # -- connect toe roll
    footToeRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footToeRoll_unitConversion' )
    footToeRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footToeRoll_clamp' )
    cmds.setAttr( footToeRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footToeRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'ToeRoll', footToeRoll_clamp+'.inputR' )
    cmds.connectAttr( footToeRoll_clamp+'.outputR', footToeRoll_unitConversion+'.input' )
    cmds.connectAttr( footToeRoll_unitConversion+'.output', RevToeJoint[0]+'.rotateX' )
    # -- connect toe pivot
    footToePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footToePivot_unitConversion' )
    cmds.setAttr( footToePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'ToePivot', footToePivot_unitConversion+'.input' )
    cmds.connectAttr( footToePivot_unitConversion+'.output', RevToeJoint[0]+'.rotateY' )
    
    # -- connect toe bend
    footToeBend_unitConversionIn = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footToeBend_unitConversionIn' )
    footToeBend_unitConversionOut = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footToeBend_unitConversionOut' )
    cmds.setAttr( footToeBend_unitConversionIn+'.conversionFactor', 57.29578 )
    cmds.setAttr( footToeBend_unitConversionOut+'.conversionFactor', 0.01745 )
    footToeBend_addDL = cmds.shadingNode( 'addDL', asUtility=True, n=side+prefix+'footToeBend_addDL' )
    cmds.disconnectAttr( BallJointIK+'.rotate', Ball_pairBlend+'.inRotate2' )
    cmds.connectAttr( BallJointIK+'.rotateZ', footToeBend_unitConversionIn+'.input' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'ToeBend', footToeBend_addDL+'.input1' )
    cmds.connectAttr( footToeBend_unitConversionIn+'.output', footToeBend_addDL+'.input2' )
    cmds.connectAttr( footToeBend_addDL+'.output', footToeBend_unitConversionOut+'.input' )
    cmds.connectAttr( BallJointIK+'.rotateX', Ball_pairBlend+'.inRotate2.inRotateX2' )
    cmds.connectAttr( BallJointIK+'.rotateY', Ball_pairBlend+'.inRotate2.inRotateY2' )
    cmds.connectAttr( footToeBend_unitConversionOut+'.output', Ball_pairBlend+'.inRotate2.inRotateZ2' )
    #cmds.connectAttr( footToeBend_unitConversion+'.output', RevToeBendLoc[0]+'.rotateX' )
    
    # -- add the space output nulls
    AnkleSpaceOUT = denUt.den_makeGrp( nodeName=side+prefix+'AnkleSpace_OUT' )
    AnkleSpaceOUT = cmds.parent( AnkleSpaceOUT, AnkleJoint )
    LegSpaceOUTs += AnkleSpaceOUT
    
    # -- parent in the reverse foot
    RevHeelJoint = cmds.parent( RevHeelJoint, AnkleCtrl )
    
    
    if side == 'R_':
        cmds.setAttr( LegRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- cleanup temp crap
    cmds.delete( Leg1JuPivTmp )
    
    # -- list the joints for binding
    LegBindJoints += [ HipJoint, KneeJoint, HockJoint, AnkleJoint, BallJoint ]
    LegCtrlsALL += [ HipFKCtrl[0], KneeFKCtrl[0], AnkleFKCtrl[0], HockFKCtrl[0], BallFKCtrl[0], KneeCtrl[0], Knee2Ctrl[0], HockCtrl[0], AnkleCtrl[0], AnkleLiftCtrl[0], LegUtilCtrl[0], FootUtilCtrl[0] ]
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, JxJoints, CtrlsALL, GutsALL lists in order
    return LegRigGrp, LegSpaceINs, LegSpaceOUTs, LegBindJoints, LegCtrlsALL, LegGutsALL





def den_makeToePivs( side='L_', prefix='', name='Toe', toeList=['A','B','C','D','E'], numJnts=[3,3,3,3,3], radius=1.0, footPos=(0,0,0), toeListNameOnly=False, dpTime=0.01, size=1.1 ):
    #--------------------- testing variables
    #side='L_'
    #name='Toe'
    #toeList=['A','B','C','D','E']
    #numJnts=[3,3,3,3,3]
    #radius=1.0
    #footPos=(0,0,0)
    #---------------------
    
    lenToes = len(toeList)
    lenJnts = len(numJnts)
    if ( lenToes != lenJnts ):
        print( 'WARNING:', toeList, 'does not have the same number of entries as', numJnts, ' - unexpected results are possible' )
    
    ToesPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    for i,toe in enumerate(toeList):
        if toeListNameOnly:
            name = ''
        ToePivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+toe+'Piv_Grp' )
        ToePivGrp = cmds.parent( ToePivGrp, ToesPivGrp )
        toePivNames = []
        #print 'toe', toe
        #print 'numJnts', numJnts[number]
        last = numJnts[i]
        it = i
        for i in range(numJnts[i]+1):
            if ( i != last ):
                toePivNum = '%02d' % (i+1,)
                toePivName = side+prefix+name+toe+toePivNum+'_Piv'
            else:
                toePivNum = '%02d' % (i,)
                toePivName = side+prefix+name+toe+'End_Piv'
            toePivNames += [toePivName]
            upPivName = side+prefix+name+toe+'Up_Piv'
            print( toePivNum, toePivName )
            toePivX = 3*size*(0.0+it)+footPos[0]
            toePivY = footPos[1]
            toePivZ = 2*size*(0.0+i)+footPos[2]
            if ( i != last ):
                ToePiv = denUt.den_makeLoc( nodeName=toePivName, pos=(toePivX,toePivY,toePivZ), radius=radius )
            else:
                ToePiv = denUt.den_makeLoc( nodeName=toePivName, pos=(toePivX,toePivY,toePivZ), radius=radius*0.5 )
            denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
            ToePiv = cmds.parent( ToePiv, ToePivGrp )
            if i == 0:
                ToePiv = denUt.den_makeLoc( nodeName=upPivName, pos=(toePivX,toePivY-2*size,toePivZ), radius=radius )
                denUt.den_ColorShape(14); denUt.den_DiagPause( dpTime )
                denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
                ToePiv = cmds.parent( ToePiv, ToePivGrp )
            else:
                print( 'constraining', toePivNames[i-1], 'to', toePivNames[i] )
                cmds.aimConstraint( toePivNames[i], toePivNames[i-1], worldUpType='object', worldUpObject=upPivName, mo=False )
        print( toePivNames )
        for piv in toePivNames:
            cmds.select( piv ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( ToesPivGrp+'.scaleX', -1 )
    
    return ToesPivGrp





def den_makeToeRig( side='L_', prefix='', name='Toe', toeList=['A','B','C','D','E'], radius=1.0, doIK=False, toeListNameOnly=False, dpTime=0.01 ):
    #--------------------- testing variables
    #side='L_'
    #name='Toe'
    #toeList=['A','B','C','D','E']
    #radius=1.0
    #---------------------
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    # == set up top groups
    print( 'toeList =', toeList )
    ToeRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp' )
    
    # -- set up the return variables
    ToeSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    ToeSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    ToeBindJoints = [] #Set list variable to hold names of all the Jx joints
    ToeCtrlsALL = [] #Set list variable to hold names of all the controls
    ToeGutsALL = [] #Set list variable to hold names of all the guts
    
    AnkleSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'AnkleSpace_IN' )
    AnkleSpaceIN = cmds.parent( AnkleSpaceIN, ToeRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'AllSpace_IN' )
    AllSpaceIN = cmds.parent( AllSpaceIN, ToeRigGrp )[0]
    ToeSpaceINs += [ AnkleSpaceIN, AllSpaceIN ]
    ToeSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp' )
    ToeSkelGrp = cmds.parent( ToeSkelGrp, AnkleSpaceIN )[0]
    ToeFKCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'FKCtrl_Grp' )
    ToeFKCtrlGrp = cmds.parent( ToeFKCtrlGrp, AnkleSpaceIN )[0]
    ToeIKCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'IKCtrl_Grp' )
    ToeIKCtrlGrp = cmds.parent( ToeIKCtrlGrp, AllSpaceIN )[0]
    #print ToeRigGrp, ToeSkelGrp, ToeFKCtrlGrp
    
    ToeUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(radius,-5*radius,-2*radius), radius=radius, Plane='XY')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    ToeCtrlsALL += [ToeUtilCtrl]
    cmds.addAttr( ToeUtilCtrl, longName=side+prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ToeUtilCtrl+'.'+side+prefix+name+'_FK_IK', lock=False, keyable=True )
    cmds.addAttr( ToeUtilCtrl, longName=side+prefix+name+'_IK_Ctrls_Visible', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ToeUtilCtrl+'.'+side+prefix+name+'_IK_Ctrls_Visible', lock=False, keyable=True )
    cmds.addAttr( ToeUtilCtrl, longName=side+prefix+name+'_FK_Ctrls_Visible', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ToeUtilCtrl+'.'+side+prefix+name+'_FK_Ctrls_Visible', lock=False, keyable=True )
    
    print( 'beginning for loop...' )
    for toe in toeList:
        if toeListNameOnly:
            nname = ''
        else:
            nname = name
        # --------- create and orient the joints
        toePivs = cmds.ls( side+prefix+nname+toe+'*_Piv' )
        #print( toePivs )
        toePivs = [item for item in toePivs if 'Up' not in item] # - remove the 'Up' from the list
        #print( toePivs )
        last = len(toePivs)-1
        for i, toePiv in enumerate(toePivs):
            toePivPos = cmds.xform( toePiv, ws=True, q=True, t=True )
            if i == 0:
                cmds.select( clear=True )
            toeJointName = toePiv.replace( '_Piv', '_Jnt' )
            toeJoint = cmds.joint( n=toeJointName, p=(toePivPos), radius=radius )
            # temp reparent joint under pivot to do orient, then put back
            toeJointPop = cmds.listRelatives( toeJoint, parent=True ); print( 'toeJointPop', toeJointPop )
            toeJoint = cmds.parent( toeJoint, toePiv )
            cmds.joint( toeJoint, e=True, oj='none', zso=True )
            if i > 0:
                toeJoint = cmds.parent( toeJoint, toeJointPop )
            
            if i == 0:
                toeRootJoint = toeJoint
            
            if i == last:
                toeEndJoint = cmds.rename( toeJoint, side+prefix+nname+toe+'_end' )
                print( 'BOO!', toeEndJoint )
            
            if i != last:
                ToeBindJoints += [toeJoint]
            denUt.den_DiagPause( dpTime )
            
        cmds.joint( toeEndJoint, e=True, oj='none', zso=True )
        cmds.parent( toeRootJoint, ToeSkelGrp )
        
        # ---------- create and connect the FK Controls
        for i, toePiv in enumerate(toePivs):
            if i < last:
                toeJoint = toePiv.replace('_Piv','_Jnt')
                toeFKCtrl = denUt.den_MakeArrowR( nodeName=toePiv.replace('_Piv','FK_Ctrl'), pos=(0,-3*radius,0), radius=radius, doT=True, axis='-Y' )
                denUt.den_ColorShapeRGB(rgb=(1,0,1))
                denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
                toeFKCtrl = cmds.parent( toeFKCtrl, toeJoint, relative=True )
                if i == 0:
                    toeFKCtrl = cmds.parent( toeFKCtrl, ToeFKCtrlGrp )
                else:
                    toeFKCtrlParent = toePivs[i-1].replace('_Piv','FK_Ctrl')
                    toeFKCtrl = cmds.parent( toeFKCtrl, toeFKCtrlParent )
                toeFKCtrl = denUt.den_AddZeroNull()
                ToeCtrlsALL += toeFKCtrl
                denUt.den_LockAttr(True,False,True,False)# relock after parenting
                cmds.connectAttr( toeFKCtrl[0]+'.rotate', toeJoint+'.rotate' )
                cmds.connectAttr( ToeUtilCtrl+'.'+side+prefix+name+'_FK_Ctrls_Visible', toeFKCtrl[0]+'.visibility' )
                if i == 0 and toe == toeList[0]:
                    cmds.select(ToeUtilCtrl)
                    denUt.den_UnLockAttr(True,True,True,True)# relock after parenting
                    ToeUtilCtrl = cmds.parent( ToeUtilCtrl, toeFKCtrl, relative=True )
                    ToeUtilCtrl = cmds.parent( ToeUtilCtrl, ToeFKCtrlGrp )[0]
                    denUt.den_LockAttr(True,True,True,False)# relock after parenting
            denUt.den_DiagPause( dpTime )
        #print( 'toeRootJoint =', toeRootJoint )
        foo = cmds.listRelatives( toeRootJoint, allDescendents=True, type='joint' )
        #print( 'toeRootJoint children =', foo )
        toeJoints = [toeRootJoint]+foo[::-1] # the [::-1] reverses the order of the output from listRelatives, which comes out reversed for some goddam reason
        print( 'toeJoints =', toeJoints )
        
        # ---------- create and connect the IK handles
        if doIK:
            for i, toePiv in enumerate(toePivs):
                if i > 0:
                    currJoint = toeJoints[i]
                    prevJoint = toeJoints[i-1]
                    #print currJoint, prevJoint
                    cmds.select( prevJoint, currJoint )
                    toeHandle = denUt.den_AddIKHandle()
                    toeHandle = cmds.ls( toeHandle )[0]
                    #print 'toeHandle', toeHandle
                    toePivPos = cmds.xform( currJoint, ws=True, q=True, t=True )
                    toePivRot = cmds.xform( currJoint, ws=True, q=True, ro=True )
                    toeHandleRoot = toeHandle.replace('_JntIkh','')
                    #print 'toeHandleRoot', toeHandleRoot
                    toeIKCtrl = denUt.den_MakeCube( nodeName=toeHandleRoot+'IK_Ctrl', pos=(0,-2.5*radius,0), radius=radius*0.5, doT=True )
                    denUt.den_ColorShapeRGB(rgb=(1,0,1))
                    toeIKCtrl = denUt.den_AddZeroNull()
                    ToeCtrlsALL += toeIKCtrl
                    toeIKCtrlZero = cmds.listRelatives( toeIKCtrl, parent=True, fullPath=True )
                    #print toeIKCtrlZero
                    #cmds.move( toePivPos[0], toePivPos[1], toePivPos[2], toeIKCtrlZero )
                    cmds.xform( toeIKCtrlZero, t=toePivPos, ro=toePivRot )
                    cmds.connectAttr( ToeUtilCtrl+'.'+side+prefix+name+'_FK_IK', toeHandle+'.ikBlend' )
                    cmds.connectAttr( ToeUtilCtrl+'.'+side+prefix+name+'_IK_Ctrls_Visible', toeIKCtrl[0]+'.visibility' )
                    cmds.parent( toeHandle, toeIKCtrl )
                    toeIKCtrlZero = cmds.parent( toeIKCtrlZero, ToeIKCtrlGrp )
                denUt.den_DiagPause( dpTime )
    
    
    if side == 'R_':
        cmds.setAttr( ToeRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, JxJoints, CtrlsALL, GutsALL lists in order
    return ToeRigGrp, ToeSpaceINs, ToeSpaceOUTs, ToeBindJoints, ToeCtrlsALL, ToeGutsALL





