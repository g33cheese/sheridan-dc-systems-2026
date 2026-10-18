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

#this module is needed because the Sluggy fin is part of the feather maker command code
import den_SluggyRigTools_v12 as denSR
importlib.reload(denSR)
print(denSR.__file__)








# ---------------------------------------------------------------------------------------
def den_makeHorseFrontLegPivs(side='L_', prefix='', name='HorseFrontLeg', radius=2.0, kneeDist=25.0, footUpDist=10.0, dpTime=0.01, size=100 ):
    #side='L_'
    #name='HorseFrontLeg'
    #radius=2.0
    #kneeDist=25.0
    #footUpDist=10.0
    #dpTime=0.01
    
    size = size*0.005
    
    LegPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    
    denUt.den_makeLoc( nodeName='Scap_Piv', pos=(-3.8*size, 146.8*size, 4.2*size), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='Shld_Piv', pos=(4.9*size, 120.9*size, 8.3*size), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    
    denUt.den_makeLoc( nodeName='Elbow_Piv', pos=(8.2*size, 98.9*size, 1.3*size), radius=radius*1.1 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='Fknee_Piv', pos=(10.6*size, 53.5*size, -0.7*size), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='Fankle_Piv', pos=(12.1*size, 12.8*size, -7*size), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='Fball_Piv', pos=(12.1*size, 3.5*size, 4.7*size), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeGrp ( 'FballSole_Piv', pos=(12.1*size, 0, 4.7*size) ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ftoe_Piv', pos=(12.1*size, 0, 15.3*size), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    #denUt.den_makeLoc( nodeName='Fheel_Piv', pos=(12.1, 1, -12), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(3); denUt.den_DiagPause( dpTime )
    cmds.curve( name='Fheel_Piv', degree=1, p=[( -1,0,0 ),( 1,0,0 ),( 1,0,2 ),( -1,0,2 ),( -1,0,0 )] ); cmds.move(12.1*size, 0, -12*size,'Fheel_Piv', r=True); cmds.scale(2*radius,0,2*radius,'Fheel_Piv.cv[*]'); cmds.setAttr( 'Fheel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='FsoleLF_Piv', pos=(18.4*size, 0, 4.1*size), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='FsoleLB_Piv', pos=(16.1*size, 0, -9.4*size), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='FsoleRF_Piv', pos=(7.8*size, 0, 7.8*size), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='FsoleRB_Piv', pos=(8.6*size, 0, -9*size), radius=radius/2 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3); denUt.den_DiagPause( dpTime )
    # -- connect the y translate attrs to the heel to maintain a flat sole
    cmds.connectAttr( 'Fball_Piv.translateX', 'FballSole_Piv.translateX' )
    cmds.connectAttr( 'Fball_Piv.translateZ', 'FballSole_Piv.translateZ' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FballSole_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'Ftoe_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleLF_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleRF_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleLB_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleRB_Piv.translateY' )
    
    cmds.spaceLocator( name='FlegMid_Loc') # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(2)
    #cmds.spaceLocator( name='FkneePole_Loc')
    denUt.den_makeLoc( nodeName='FkneePole_Loc', pos=(0, kneeDist, 0), radius=radius )
    #cmds.xform ( t=(0, 30, 0) )
    denUt.den_ColorShape(9)
    cmds.parent( 'FkneePole_Loc', 'FlegMid_Loc' )
    # - make a locator that shows the up of the foot based on foot pivot locations to aid pivot placement
    #cmds.spaceLocator( name='FfootUp_Piv')
    denUt.den_makeLoc( nodeName='FfootUp_Piv', radius=radius*0.5, pos=(0, footUpDist, footUpDist) )
    #cmds.xform ( t=(5, 10, 0) )
    denUt.den_ColorShape(14)
    cmds.parent( 'FfootUp_Piv', 'Fheel_Piv', relative=True )
    
    LegMidLocPtCon = cmds.pointConstraint( 'Elbow_Piv','Fankle_Piv','FlegMid_Loc', mo=False  )[0]
    LegMidLocAimCon = cmds.aimConstraint( 'Fankle_Piv','FlegMid_Loc', worldUpType='object', worldUpObject='Fknee_Piv', mo=False  )[0]
    ElbowPivAimCon = cmds.aimConstraint( 'Fknee_Piv','Elbow_Piv', worldUpType='object', worldUpObject='Fankle_Piv', mo=False  )[0]
    FanklePivAimCon = cmds.aimConstraint( 'Fball_Piv','Fankle_Piv', worldUpType='object', worldUpObject='FfootUp_Piv', mo=False  )[0]
    FsoleLFPivAimCon = cmds.aimConstraint( 'FsoleLB_Piv','FsoleLF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    FsoleRFPivAimCon = cmds.aimConstraint( 'FsoleRB_Piv','FsoleRF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    FtoePivAimCon = cmds.aimConstraint( 'Fball_Piv','Ftoe_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    HeelPivAimCon = cmds.aimConstraint( 'Ftoe_Piv','Fball_Piv', worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    # aim L_Scap_Piv at scap02, use shoulder to keep up on the triangle plane
    ScapPivAimCon = cmds.aimConstraint( 'Shld_Piv','Scap_Piv', maintainOffset=False, worldUpType='object', worldUpObject='Elbow_Piv' )[0]
    
    cmds.parent( 'Fheel_Piv', LegPivGrp )
    cmds.parent( 'Scap_Piv','Shld_Piv','Elbow_Piv','Fknee_Piv','FlegMid_Loc', LegPivGrp )
    cmds.parent( 'Fankle_Piv','Fball_Piv','FballSole_Piv','Ftoe_Piv','FsoleLF_Piv','FsoleLB_Piv','FsoleRF_Piv','FsoleRB_Piv', 'Fheel_Piv' )
    
    # - lock down channels the user is not supposed to touch
    cmds.select( LegPivGrp ); denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 1 )
    cmds.select( 'Scap_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Shld_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fknee_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'Hock_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'Hock_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fankle_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fball_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FballSole_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ftoe_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fheel_Piv' ); denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 1 )
    cmds.select( 'FlegMid_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'KneeMid2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FkneePole_Loc' ); denUt.den_Lock(  0,0,1 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'KneePole2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FfootUp_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleLF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleRF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleLB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleRB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    
    # -- put the L_ back into the node names
    cmds.rename( 'Scap_Piv', side+prefix+'Scap_Piv' )
    cmds.rename( 'Shld_Piv', side+prefix+'Shld_Piv' )
    cmds.rename( 'Elbow_Piv', side+prefix+'Elbow_Piv' )
    cmds.rename( 'Fknee_Piv', side+prefix+'Fknee_Piv' )
    cmds.rename( 'Fankle_Piv', side+prefix+'Fankle_Piv' )
    cmds.rename( 'Fball_Piv', side+prefix+'Fball_Piv' )
    cmds.rename( 'FballSole_Piv', side+prefix+'FballSole_Piv' )
    cmds.rename( 'Ftoe_Piv', side+prefix+'Ftoe_Piv' )
    cmds.rename( 'Fheel_Piv', side+prefix+'Fheel_Piv' )
    cmds.rename( 'FlegMid_Loc', side+prefix+'FlegMid_Loc' )
    cmds.rename( 'FkneePole_Loc', side+prefix+'FkneePole_Loc' )
    cmds.rename( 'FfootUp_Piv', side+prefix+'FfootUp_Piv' )
    cmds.rename( 'FsoleLF_Piv', side+prefix+'FsoleLF_Piv' )
    cmds.rename( 'FsoleRF_Piv', side+prefix+'FsoleRF_Piv' )
    cmds.rename( 'FsoleLB_Piv', side+prefix+'FsoleLB_Piv' )
    cmds.rename( 'FsoleRB_Piv', side+prefix+'FsoleRB_Piv' )
    cmds.rename( LegMidLocPtCon, side+prefix+LegMidLocPtCon )
    cmds.rename( LegMidLocAimCon, side+prefix+LegMidLocAimCon )
    cmds.rename( ElbowPivAimCon, side+prefix+ElbowPivAimCon )
    cmds.rename( FanklePivAimCon, side+prefix+FanklePivAimCon )
    cmds.rename( FsoleLFPivAimCon, side+prefix+FsoleLFPivAimCon )
    cmds.rename( FsoleRFPivAimCon, side+prefix+FsoleRFPivAimCon )
    cmds.rename( FtoePivAimCon, side+prefix+FtoePivAimCon )
    cmds.rename( ScapPivAimCon, side+prefix+ScapPivAimCon )
    
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( LegPivGrp+'.scaleX', -1 )
    
    return LegPivGrp





# ---------------------------------------------------------------------------------------
# - started with biped leg code
# - search/replaced 'Leg' with 'FQleg'
# - search/replaced 'Pelvis' with 'Chest'
# - search/replaced 'Hip' with 'Elbow'
# - search/replaced 'Knee' with 'Fknee'
# - search/replaced 'Ankle' with 'Fankle'
# - search/replaced 'Ball' with 'Fball' avoiding the ball control
# - search/replaced 'Toe' with 'Ftoe'
# - search/replaced 'Heel' with 'Fheel'
# - search/replaced 'Sole' with 'Fsole' avoiding BallSole
def den_makeHorseFrontLegRig( side='L_', prefix='', name='HorseFrontLeg', radius=2.0, ctrlRadius=15.0, displayLocalAxis=False, dpTime=0.01 ):
    #side='L_'
    #radius=3.0
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    # == set up top groups
    LegRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp' )
    
    # -- set up the return variables
    LegSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    LegSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    LegJxJoints = [] #Set list variable to hold names of all the Jx joints
    LegCtrlsALL = [] #Set list variable to hold names of all the controls
    LegGutsALL = [] #Set list variable to hold names of all the guts
    
    ChestSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'ChestSpace_IN' )
    ChestSpaceIN = cmds.parent( ChestSpaceIN, LegRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'CogSpace_IN' )
    CogSpaceIN = cmds.parent( CogSpaceIN, LegRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'AllSpace_IN' )
    AllSpaceIN = cmds.parent( AllSpaceIN, LegRigGrp )[0]
    
    LegSpaceINs += [ ChestSpaceIN, CogSpaceIN, AllSpaceIN ]
    
    LegSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp' )
    LegSkelGrp = cmds.parent( LegSkelGrp, ChestSpaceIN )[0]
    LegCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp' )
    LegCtrlGrp = cmds.parent( LegCtrlGrp, ChestSpaceIN )[0]
    # -- make Wrist control space switch constraint
    FankleCtrlSpace = denUt.den_makeGrp( nodeName=side+prefix+'FankleCtrl_Space' )
    FankleCtrlSpace = cmds.parent( FankleCtrlSpace, LegCtrlGrp )[0]
    FankleCtrlSpaceConstraint = cmds.parentConstraint( ChestSpaceIN, FankleCtrlSpace, weight=0 )
    FankleCtrlSpaceConstraint = cmds.parentConstraint( CogSpaceIN, FankleCtrlSpace, weight=0 )
    FankleCtrlSpaceConstraint = cmds.parentConstraint( AllSpaceIN, FankleCtrlSpace, weight=1 )
    
    
    # -- set variables for pivot positions
    
    ElbowPos = cmds.xform( side+prefix+'Elbow_Piv', ws=True, q=True, t=True )
    FkneePos = cmds.xform( side+prefix+'Fknee_Piv', ws=True, q=True, t=True )
    FanklePos = cmds.xform( side+prefix+'Fankle_Piv', ws=True, q=True, t=True )
    FballPos = cmds.xform( side+prefix+'Fball_Piv', ws=True, q=True, t=True )
    FtoePos = cmds.xform( side+prefix+'Ftoe_Piv', ws=True, q=True, t=True )
    FheelPos = cmds.xform( side+prefix+'Fheel_Piv', ws=True, q=True, t=True )
    FsoleLFPos = cmds.xform( side+prefix+'FsoleLF_Piv', ws=True, q=True, t=True )
    FsoleLBPos = cmds.xform( side+prefix+'FsoleLB_Piv', ws=True, q=True, t=True )
    FsoleRFPos = cmds.xform( side+prefix+'FsoleRF_Piv', ws=True, q=True, t=True )
    FsoleRBPos = cmds.xform( side+prefix+'FsoleLB_Piv', ws=True, q=True, t=True )
    FballSolePos = [ FballPos[0], FtoePos[1], FballPos[2] ]
    #print 'FballSolePos', FballSolePos
    FkneePolePos = cmds.xform( side+prefix+'FkneePole_Loc', ws=True, q=True, t=True )
    
    
    # -- make the joints
    cmds.select( clear=True )
    
    ElbowJoint = cmds.joint( n=side+prefix+'Elbow_Jnt', p=(ElbowPos), radius=radius ); denUt.den_DiagPause( dpTime )
    FkneeJoint = cmds.joint( n=side+prefix+'Fknee_Jnt', p=(FkneePos), radius=radius ); denUt.den_DiagPause( dpTime )
    FankleJoint = cmds.joint( n=side+prefix+'Fankle_Jnt', p=(FanklePos), radius=radius ); denUt.den_DiagPause( dpTime )
    FballJoint = cmds.joint( n=side+prefix+'Fball_Jnt', p=(FballPos), radius=radius ); denUt.den_DiagPause( dpTime )
    FtoeJoint = cmds.joint( n=side+prefix+'Ftoe_Jx', p=(FtoePos), radius=radius ); denUt.den_DiagPause( dpTime )
    
    #print ElbowJoint, ElbowPos
    #print FkneeJoint, FkneePos
    #print FankleJoint, FanklePos
    #print FballJoint, FballPos
    #print FtoeJoint, FtoePos
    
    if ( displayLocalAxis ):
        cmds.setAttr( ElbowJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FkneeJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FankleJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FballJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FtoeJoint+'.displayLocalAxis', 1 )
    
    
    
    # -- orient the joints
    
    cmds.select( clear=True )
    #cmds.joint( FkneeJoint, e=True, oj='xyz', zso=True )
    cmds.joint( FkneeJoint, e=True, oj='xzy', secondaryAxisOrient='xup', aos=True, ch=False, zso=True )
    cmds.joint( FankleJoint, e=True, oj='none', zso=True )
    ElbowJoint = cmds.parent( ElbowJoint, side+prefix+'Elbow_Piv' )[0] # -- temp reparent hip under planar space
    cmds.joint( ElbowJoint, e=True, oj='none', zso=True )
    ElbowJoint = cmds.parent( ElbowJoint, LegSkelGrp )[0] # -- put hip back under leg skel grp
    FankleJoint = cmds.parent( FankleJoint, side+prefix+'Fankle_Piv' )[0] # -- temp reparent ankle under planar space
    #cmds.joint( FballJoint, e=True, oj='xyz', zso=True )
    cmds.joint( FballJoint, e=True, oj='xzy', secondaryAxisOrient='xup', aos=True, ch=False, zso=True )
    cmds.joint( FtoeJoint, e=True, oj='none', zso=True )
    FankleJoint = cmds.parent( FankleJoint, FkneeJoint )[0] # -- put ankle back under knee jnt
    
    # -- duplicate the leg to make the FK and IK leg bones
    ElbowJointIK = cmds.duplicate (ElbowJoint, name=side+prefix+'Elbow_IK' )[0]
    FkneeJointIK = cmds.rename (ElbowJointIK+'|'+side+prefix+'Fknee_Jnt', side+prefix+'Fknee_IK' )
    FankleJointIK = cmds.rename (FkneeJointIK+'|'+side+prefix+'Fankle_Jnt', side+prefix+'Fankle_IK' )
    FballJointIK = cmds.rename (FankleJointIK+'|'+side+prefix+'Fball_Jnt', side+prefix+'Fball_IK' )
    FtoeJointIK = cmds.rename (FballJointIK+'|'+side+prefix+'Ftoe_Jx', side+prefix+'Ftoe_IK' )
    #print ElbowJointIK, '----', FkneeJointIK, '----', FankleJointIK, '----', FballJointIK, '----', FtoeJointIK
    ElbowJointFK = cmds.duplicate (ElbowJoint, name=side+prefix+'Elbow_FK' )[0]
    FkneeJointFK = cmds.rename (ElbowJointFK+'|'+side+prefix+'Fknee_Jnt', side+prefix+'Fknee_FK' )
    FankleJointFK = cmds.rename (FkneeJointFK+'|'+side+prefix+'Fankle_Jnt', side+prefix+'Fankle_FK' )
    FballJointFK = cmds.rename (FankleJointFK+'|'+side+prefix+'Fball_Jnt', side+prefix+'Fball_FK' )
    FtoeJointFK = cmds.rename (FballJointFK+'|'+side+prefix+'Ftoe_Jx', side+prefix+'Ftoe_FK' )
    #print ElbowJointFK, '----', FkneeJointFK, '----', FankleJointFK, '----', FballJointFK, '----', FtoeJointFK
    
    # -- make the controls and zero nulls
    
    # -- Elbow FK
    ElbowFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'ElbowFK_Ctrl', radius=ctrlRadius, axis='+Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    #ElbowFKCtrl = cmds.rename( ElbowFKCtrl, side+prefix+'ElbowFK_Ctrl' )
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ElbowJointFK, relative=True )
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, LegCtrlGrp )
    ElbowFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    ElbowFKCtrlZero = cmds.listRelatives( ElbowFKCtrl, parent=True, fullPath=True )[0]
    cmds.connectAttr( ElbowFKCtrl[0]+'.rotate', ElbowJointFK+'.rotate' )
    #cmds.parentConstraint( LegCtrlGrp, ElbowFKCtrlZero, mo=True )
    #print ElbowFKCtrl
    # -- Leg Utility
    LegUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(4*radius,0,6*radius), radius=radius, Plane='ZX')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# relock after parenting
    LegUtilCtrl = cmds.parent( LegUtilCtrl, ElbowJointFK, relative=True )
    LegUtilCtrl = cmds.parent( LegUtilCtrl, LegCtrlGrp )
    denUt.den_LockAttr(True,True,True,False)# relock after parenting
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', lock=False, keyable=True )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'Fankle_FK_IK', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'Fankle_FK_IK', lock=False, keyable=True )
    # -- Fknee
    FkneeCtrl = denUt.den_MakePole( nodeName=side+prefix+'Fknee_Ctrl', radius=radius )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=FkneePolePos )
    FkneeCtrl = cmds.parent( FkneeCtrl, LegCtrlGrp )
    FkneeCtrl = denUt.den_AddZeroNull()
    
    FkneeFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'FkneeFK_Ctrl', pos=(0,-0.5*ctrlRadius,0), radius=2*radius, doT=True, axis='-Y' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    FkneeFKCtrl = cmds.parent( FkneeFKCtrl, FkneeJointFK, relative=True )
    FkneeFKCtrl = cmds.parent( FkneeFKCtrl, ElbowFKCtrl )
    FkneeFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( FkneeFKCtrl[0]+'.rotate', FkneeJointFK+'.rotate' )
    #print FkneeFKCtrl
    # -- Fankle Controls
    FankleCtrl = denUt.den_MakeBall( nodeName=side+prefix+'Fankle_Ctrl', radius=1.1*ctrlRadius )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=FanklePos )
    FankleCtrl = cmds.parent( FankleCtrl, FankleCtrlSpace )
    FankleCtrl = denUt.den_AddZeroNull()
    cmds.setAttr( FankleCtrl[0]+'.rotateOrder', 1 )
    FankleCtrlZero = cmds.listRelatives( FankleCtrl, parent=True, fullPath=True )[0]
    
    FankleFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'FankleFK_Ctrl', radius=0.8*ctrlRadius, axis='+Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    FankleFKCtrl = cmds.parent( FankleFKCtrl, FankleJointFK, relative=True )
    FankleFKCtrl = cmds.parent( FankleFKCtrl, FkneeFKCtrl )
    FankleFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( FankleFKCtrl[0]+'.rotate', FankleJointFK+'.rotate' )
    FankleFKCtrlZero = cmds.listRelatives( FankleFKCtrl, parent=True, fullPath=True )[0]
    
    #print FankleCtrlZero
    FballFKCtrl = denUt.den_MakeSpike(nodeName=side+prefix+'FballFK_Ctrl', radius=0.8*ctrlRadius, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    FballFKCtrl = cmds.parent( FballFKCtrl, FballJointFK, relative=True )
    FballFKCtrl = cmds.parent( FballFKCtrl, FankleFKCtrl )
    FballFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( FballFKCtrl[0]+'.rotate', FballJointFK+'.rotate' )
    FballFKCtrlZero = cmds.listRelatives( FballFKCtrl, parent=True, fullPath=True )[0]
    # -- Foot Utility
    FootUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+'FootUtil_Ctrl', pos=(0.5*ctrlRadius,0.5*ctrlRadius,0), radius=radius, Plane='XY')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    FootUtilCtrl = cmds.parent( FootUtilCtrl, FankleCtrl, relative=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootRock', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRock', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRoll', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootPivot', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FootTwist', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootTwist', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FheelPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FheelPivot', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FtoeRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FtoeRoll', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FtoePivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FtoePivot', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+prefix+'FtoeBend', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+prefix+'FtoeBend', lock=False, keyable=True )
    
    # -- connect up the Fankle control space switcher
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'ChestSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'ChestSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'ChestSpace', FankleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'ChestSpace_INW0' )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'CogSpace', FankleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'CogSpace_INW1' )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'AllSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'AllSpace', FankleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'AllSpace_INW2' )
    
    # -- set up Leg FK_IK blending
    Elbow_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Elbow_ikFk_pairBlend' )
    cmds.setAttr( Elbow_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ElbowJointFK+'.rotate', Elbow_pairBlend+'.inRotate1' )
    cmds.connectAttr( ElbowJointIK+'.rotate', Elbow_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Elbow_pairBlend+'.weight' )
    cmds.connectAttr( Elbow_pairBlend+'.outRotate', ElbowJoint+'.rotate' )
    
    Fknee_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Fknee_ikFk_pairBlend' )
    cmds.setAttr( Fknee_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( FkneeJointFK+'.rotate', Fknee_pairBlend+'.inRotate1' )
    cmds.connectAttr( FkneeJointIK+'.rotate', Fknee_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Fknee_pairBlend+'.weight' )
    cmds.connectAttr( Fknee_pairBlend+'.outRotate', FkneeJoint+'.rotate' )
    
    Fankle_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Fankle_ikFk_pairBlend' )
    cmds.setAttr( Fankle_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( FankleJointFK+'.rotate', Fankle_pairBlend+'.inRotate1' )
    cmds.connectAttr( FankleJointIK+'.rotate', Fankle_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Fankle_pairBlend+'.weight' )
    cmds.connectAttr( Fankle_pairBlend+'.outRotate', FankleJoint+'.rotate' )
    
    Fball_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Fball_ikFk_pairBlend' )
    cmds.setAttr( Fball_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( FballJointFK+'.rotate', Fball_pairBlend+'.inRotate1' )
    cmds.connectAttr( FballJointIK+'.rotate', Fball_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Fball_pairBlend+'.weight' )
    cmds.connectAttr( Fball_pairBlend+'.outRotate', FballJoint+'.rotate' )
    
    
    # -- make the reverse foot
    
    footPivs = [ 'Fheel_Piv', 'FballSole_Piv', 'FsoleLF_Piv', 'FsoleRF_Piv', 'Ftoe_Piv', 'Fball_Piv', 'Fankle_Piv' ]
    footJnts = []
    for number,footPiv in enumerate(footPivs):
        prevNum = number-1
        nameRoot = footPiv.replace('_Piv','')
        #print 'nameRoot', nameRoot, number
        footJnt = cmds.joint( n=side+prefix+nameRoot+'Rev_Jx', radius=radius*0.7 )
        footPiv = side+prefix+footPivs[number]
        footJnt = cmds.parent( footJnt, footPiv, relative=True )
        cmds.joint( footJnt, e=True, oj='none', zso=True )
        if number != 0:
            footJnt = cmds.parent( footJnt, footJnts[prevNum] )
        else:
            footJnt = cmds.parent( footJnt, world=True )
        footJnts = footJnts + [footJnt]
    #print(footJnts[5])
    #cmds.joint( footJnts[5], e=True, oj='none', zso=True, radius=radius*0.7 ); denUt.den_DiagPause( 0.02 )
    
    #print footJnts
    RevFheelJoint = footJnts[0]
    RevFballSoleJoint = footJnts[1]
    RevFsoleLFJoint = footJnts[2]
    RevFsoleRFJoint = footJnts[3]
    RevFtoeJoint = footJnts[4]
    RevFballJoint = footJnts[5]
    RevFankleJoint = footJnts[6]
    #print RevFheelJoint
    RevFtoeBendLoc = cmds.spaceLocator( name=side+prefix+'RevFtoeBend_Loc' )
    RevFtoeBendLoc = cmds.parent( RevFtoeBendLoc, RevFtoeJoint, relative=True )
    
    # -- make the ik handles
    cmds.select( ElbowJointIK, FankleJointIK )
    LegIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    LegIKhandle = cmds.parent( LegIKhandle, RevFankleJoint )[0]
    cmds.poleVectorConstraint( FkneeCtrl, LegIKhandle )
    cmds.select( FankleJointIK, FballJointIK )
    FballIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    FballIKhandle = cmds.parent( FballIKhandle, RevFballJoint )[0]
    cmds.select( FballJointIK, FtoeJointIK )
    FtoeIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    FtoeIKhandle = cmds.parent( FtoeIKhandle, RevFtoeBendLoc )[0]
    
    # -- add utility nodes and connect attrs for foot roll
    footFheelRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFheelRoll_unitConversion' )
    footFheelRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footFheelRoll_clamp' )
    cmds.setAttr( footFheelRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFheelRoll_clamp+'.minR', -180 )
    footFballRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFballRoll_unitConversion' )
    footFballRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footFballRoll_clamp' )
    cmds.setAttr( footFballRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFballRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRoll', footFheelRoll_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRoll', footFballRoll_clamp+'.inputR' )
    cmds.connectAttr( footFheelRoll_clamp+'.outputR', footFheelRoll_unitConversion+'.input' )
    cmds.connectAttr( footFballRoll_clamp+'.outputR', footFballRoll_unitConversion+'.input' )
    cmds.connectAttr( footFheelRoll_unitConversion+'.output', RevFheelJoint[0]+'.rotateX' )
    cmds.connectAttr( footFballRoll_unitConversion+'.output', RevFballJoint[0]+'.rotateX' )
    
    # -- add utility nodes and connect attrs for foot rock
    footFsoleLFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFsoleLFRock_unitConversion' )
    footFsoleLFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footFsoleLFRock_clamp' )
    cmds.setAttr( footFsoleLFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFsoleLFRock_clamp+'.minR', -180 )
    footFsoleRFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFsoleRFRock_unitConversion' )
    footFsoleRFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footFsoleRFRock_clamp' )
    cmds.setAttr( footFsoleRFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFsoleRFRock_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRock', footFsoleLFRock_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootRock', footFsoleRFRock_clamp+'.inputR' )
    cmds.connectAttr( footFsoleLFRock_clamp+'.outputR', footFsoleLFRock_unitConversion+'.input' )
    cmds.connectAttr( footFsoleRFRock_clamp+'.outputR', footFsoleRFRock_unitConversion+'.input' )
    cmds.connectAttr( footFsoleLFRock_unitConversion+'.output', RevFsoleLFJoint[0]+'.rotateZ' )
    cmds.connectAttr( footFsoleRFRock_unitConversion+'.output', RevFsoleRFJoint[0]+'.rotateZ' )
    # -- connect foot pivot
    footFballSolePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFballSolePivot_unitConversion' )
    cmds.setAttr( footFballSolePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootPivot', footFballSolePivot_unitConversion+'.input' )
    cmds.connectAttr( footFballSolePivot_unitConversion+'.output', RevFballSoleJoint[0]+'.rotateY' )
    # -- connect foot twist
    footFballTwist_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFballTwist_unitConversion' )
    cmds.setAttr( footFballTwist_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FootTwist', footFballTwist_unitConversion+'.input' )
    cmds.connectAttr( footFballTwist_unitConversion+'.output', RevFballJoint[0]+'.rotateZ' )
    # -- connect heel pivot
    footFheelPivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFheelPivot_unitConversion' )
    cmds.setAttr( footFheelPivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FheelPivot', footFheelPivot_unitConversion+'.input' )
    cmds.connectAttr( footFheelPivot_unitConversion+'.output', RevFheelJoint[0]+'.rotateY' )
    # -- connect heel pivot
    footFtoeRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFtoeRoll_unitConversion' )
    footFtoeRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+'footFtoeRoll_clamp' )
    cmds.setAttr( footFtoeRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFtoeRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FtoeRoll', footFtoeRoll_clamp+'.inputR' )
    cmds.connectAttr( footFtoeRoll_clamp+'.outputR', footFtoeRoll_unitConversion+'.input' )
    cmds.connectAttr( footFtoeRoll_unitConversion+'.output', RevFtoeJoint[0]+'.rotateX' )
    # -- connect heel pivot
    footFtoePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFtoePivot_unitConversion' )
    cmds.setAttr( footFtoePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FtoePivot', footFtoePivot_unitConversion+'.input' )
    cmds.connectAttr( footFtoePivot_unitConversion+'.output', RevFtoeJoint[0]+'.rotateY' )
    
    # -- connect heel pivot
    footFtoeBend_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+prefix+'footFtoeBend_unitConversion' )
    cmds.setAttr( footFtoeBend_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+prefix+'FtoeBend', footFtoeBend_unitConversion+'.input' )
    cmds.connectAttr( footFtoeBend_unitConversion+'.output', RevFtoeBendLoc[0]+'.rotateX' )
    
    # -- add the space output nulls
    FankleSpaceOUT = denUt.den_makeGrp( nodeName=side+prefix+'FankleSpace_OUT' )
    FankleSpaceOUT = cmds.parent( FankleSpaceOUT, FankleJoint )
    LegSpaceOUTs += FankleSpaceOUT
    
    # -- parent in the reverse foot
    RevFheelJoint = cmds.parent( RevFheelJoint, FankleCtrl )
    
    # ====================================================================
    # - this next bit adds the shoulder rig parts
    
    ScapPos = cmds.xform( side+prefix+'Scap_Piv', ws=True, q=True, t=True )
    ShldPos = cmds.xform( side+prefix+'Shld_Piv', ws=True, q=True, t=True )
    
    cmds.select( clear=True )
    ScapJoint = cmds.joint( n=side+prefix+'Scap_Jnt', p=(ScapPos), radius=radius )
    ScapJoint = cmds.parent( ScapJoint, LegSkelGrp )[0]
    ShldJoint = cmds.joint( n=side+prefix+'Shld_Jnt', p=(ShldPos), radius=radius )
    ShldEndJoint = cmds.joint( n=side+prefix+'Shld_End', p=(ElbowPos), radius=radius )
    cmds.select( clear=True )
    #cmds.joint( ShldJoint, e=True, oj='xyz', zso=True )
    cmds.joint( ShldJoint, e=True, oj='xzy', secondaryAxisOrient='xup', aos=True, ch=False, zso=True )
    cmds.joint( ShldEndJoint, e=True, oj='none', zso=True )
    ScapJoint = cmds.parent( ScapJoint, side+prefix+'Scap_Piv' ) # -- temp reparent scap under planar space
    cmds.joint( ScapJoint, e=True, oj='none', zso=True )
    ScapJoint = cmds.parent( ScapJoint, LegSkelGrp )[0] # -- put scap back
    
    if ( displayLocalAxis ):
        cmds.setAttr( ScapJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ShldJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ShldEndJoint+'.displayLocalAxis', 1 )
    
    # -- Shoulder IK Controls
    ShldCtrl = denUt.den_MakePole( nodeName=side+prefix+'Shld_Ctrl', pos=(0,0,1.5*ctrlRadius) ,radius=radius, doT=True)
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=ShldPos )
    ShldCtrl = cmds.parent( ShldCtrl, LegCtrlGrp )
    ShldCtrl = denUt.den_AddZeroNull()
    ShldCtrlZero = cmds.listRelatives( ShldCtrl, parent=True, fullPath=True )
    
    ElbowCtrl = denUt.den_MakeCube( nodeName=side+prefix+'Elbow_Ctrl', pos=(0,0,0) ,radius=0.7*ctrlRadius, doT=False)
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=ElbowPos )
    ElbowCtrl = cmds.parent( ElbowCtrl, LegCtrlGrp )
    ElbowCtrl = denUt.den_AddZeroNull()
    ElbowCtrlZero = cmds.listRelatives( ElbowCtrl, parent=True, fullPath=True )
    
    # - make the front leg FK controls stay with the front leg FK joints
    cmds.pointConstraint( ShldEndJoint, ElbowFKCtrlZero, mo=True )
    
    # -- make the ik handles
    cmds.select( ScapJoint, ShldEndJoint )
    ShldIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver', makeUp=False )
    ShldIKhandle = cmds.parent( ShldIKhandle, ElbowCtrl )
    cmds.poleVectorConstraint( ShldCtrl, ShldIKhandle )
    
    cmds.pointConstraint( ShldEndJoint, ElbowJoint )
    cmds.pointConstraint( ShldEndJoint, ElbowJointFK )
    cmds.pointConstraint( ShldEndJoint, ElbowJointIK )
    
    
    if side == 'R_':
        cmds.setAttr( LegRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- list the joints for binding
    JxJnts = [ ElbowJoint, FkneeJoint, FankleJoint, FballJoint ]
    JxJnts += [ ScapJoint, ShldJoint ]
    print( JxJnts )
    LegJxJoints = JxJnts
        
    LegCtrlsALL += [ ElbowFKCtrl[0], FkneeFKCtrl[0], FankleFKCtrl[0], FballFKCtrl[0], FkneeCtrl[0], FankleCtrl[0], LegUtilCtrl[0], FootUtilCtrl[0], ShldCtrl[0], ElbowCtrl[0] ]
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, JxJoints, CtrlsALL, GutsALL lists in order
    return LegRigGrp, LegSpaceINs, LegSpaceOUTs, LegJxJoints, LegCtrlsALL, LegGutsALL




def den_makeAnyTorsoPivs( prefix='', radius=1.0, spineCount=4, neckCount=4, dpTime=0.01, size=100 ):
    
    # -- makes torso pivots that can then be re-positioned to match a particular character
    size=size*0.025
    TorsoPivGrp = denUt.den_makeGrp( nodeName='TorsoPiv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    denUt.den_makeLoc( nodeName='Pelvis_Piv', pos=(0, 0, 0), radius=1.2*radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    for i in range(spineCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        piv = denUt.den_makeLoc( nodeName='Spine'+iStrPad+'_Piv', pos=(0, 0, 5*(i+1)*size), radius=radius )
        denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
        denUt.den_ColorShape(22); denUt.den_DiagPause( seconds=dpTime )
        cmds.parent( piv, TorsoPivGrp )
        denUt.den_DiagPause( dpTime )
    
    denUt.den_makeLoc( nodeName='Chest_Piv', pos=(0, 0, 5*(spineCount+1)*size), radius=1.2*radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    for i in range(neckCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        piv = denUt.den_makeLoc( nodeName='Neck'+iStrPad+'_Piv', pos=(0, 0, 5*(i+2+spineCount)*size), radius=radius )
        denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
        denUt.den_ColorShape(22); denUt.den_DiagPause( seconds=dpTime )
        cmds.parent( piv, TorsoPivGrp )
        denUt.den_DiagPause( dpTime )
    
    denUt.den_makeLoc( nodeName='Head_Piv', pos=(0, 0, 5*(2+spineCount+neckCount)*size), radius=1.2*radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='HeadEnd_Piv', pos=(0, 0, 5*(4+spineCount+neckCount)*size), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(25); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='Jaw_Piv', pos=(0, -2*size, 5*(2+spineCount+neckCount)*size), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( dpTime )
    denUt.den_makeLoc( nodeName='JawEnd_Piv', pos=(0, -2*size, 5*(4+spineCount+neckCount)*size), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(25); denUt.den_DiagPause( dpTime )
    cmds.parent( 'Pelvis_Piv','Chest_Piv','Head_Piv','HeadEnd_Piv','Jaw_Piv','JawEnd_Piv', TorsoPivGrp )
    cmds.refresh()
    return TorsoPivGrp



# ---------------------------------------------------------------------------------------
# define Any torso rig creation command
def den_makeAnyTorsoRig( prefix='', radius=0.7, ctrlRadius=(4.0,5.0,3.0,0.3), displayLocalAxis=False, spineCount=4, spineSecondaryJoints=[], neckCount=4, neckSecondaryJoints=[], spineAxisOrient='yup', jawAxisOrient='yup', jawPos=(0,-6,0), dpTime=0.01 ):
    #--------------------- testing variables
    #radius=0.7
    #ctrlRadius=(4.0,5.0,3.0,0.3)
    #displayLocalAxis=True 
    #spineCount=9
    #spineSecondaryJoints=[4,7]
    #neckCount=9
    #neckSecondaryJoints=[4,7]
    #spineAxisOrient='yup'
    #jawAxisOrient='yup'
    #---------------------
    
    # -- make the Torso rig top group
    TorsoRigGrp = denUt.den_makeGrp( nodeName='Torso_Grp', pos=(0,0,0) )
    
    # -- set up the return variables
    TorsoSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    TorsoSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    TorsoJxJoints = [] #Set list variable to hold names of all the Jx joints
    TorsoCtrlsALL = [] #Set list variable to hold names of all the controls
    TorsoGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Torso SpaceIN
    TorsoSpaceIN = denUt.den_makeGrp( nodeName='TorsoSpace_IN', pos=(0,0,0) )
    TorsoSpaceIN = cmds.parent( TorsoSpaceIN, TorsoRigGrp )
    TorsoSpaceINs += TorsoSpaceIN
    
    # -- 
    
    
    # make sure the TorsoSpaceIN is selected so the first joint will be parented under it when created
    cmds.select( TorsoSpaceIN )
    # -- make the joints
    PelvisPos = cmds.xform( 'Pelvis_Piv', ws=True, q=True, t=True )
    PelvisJoint = denUt.den_makeJoint( nodeName='Pelvis_Jnt', pos=(PelvisPos), radius=radius, leaveSelected=True )
    TorsoJxJoints += [PelvisJoint]
    #print( PelvisJoint, PelvisPos )
    SpineJoints = []
    for i in range(spineCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        #jxEnd = str(jx)
        #jxEndPad = jxEnd.rjust(2,'0')
        print( i, iStr, iStrPad )
        SpinePos = cmds.xform( 'Spine'+iStrPad+'_Piv', ws=True, q=True, t=True )
        SpineJoint = denUt.den_makeJoint( nodeName='Spine'+iStrPad+'_Jnt', pos=(SpinePos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( dpTime )
        SpineJoints += [SpineJoint]
        TorsoJxJoints += [SpineJoint]
    
    ChestPos = cmds.xform( 'Chest_Piv', ws=True, q=True, t=True )
    ChestJoint = denUt.den_makeJoint( nodeName='Chest_Jnt', pos=(ChestPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( dpTime )
    TorsoJxJoints += [ChestJoint]
    #print( ChestJoint, ChestPos )
    NeckJoints = []
    for i in range(neckCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        #jxEnd = str(jx)
        #jxEndPad = jxEnd.rjust(2,'0')
        print( i, iStr, iStrPad )
        NeckPos = cmds.xform( 'Neck'+iStrPad+'_Piv', ws=True, q=True, t=True )
        NeckJoint = denUt.den_makeJoint( nodeName='Neck'+iStrPad+'_Jnt', pos=(NeckPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( dpTime )
        NeckJoints += [NeckJoint]
        TorsoJxJoints += [NeckJoint]
    
    HeadPos = cmds.xform( 'Head_Piv', ws=True, q=True, t=True )
    HeadJoint = denUt.den_makeJoint( nodeName='Head_Jnt', pos=(HeadPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( dpTime )
    TorsoJxJoints += [HeadJoint]
    #print( HeadJoint, HeadPos )
    HeadEndPos = cmds.xform( 'HeadEnd_Piv', ws=True, q=True, t=True )
    HeadEndJoint = denUt.den_makeJoint( nodeName='Head_end', pos=(HeadEndPos), radius=radius*0.4, leaveSelected=False ); denUt.den_DiagPause( dpTime )
    #print( HeadEndJoint, HeadEndPos )
    cmds.select(HeadJoint)
    JawPos = cmds.xform( 'Jaw_Piv', ws=True, q=True, t=True )
    JawJoint = denUt.den_makeJoint( nodeName='Jaw_Jnt', pos=(JawPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( dpTime )
    TorsoJxJoints += [JawJoint]
    #print( JawJoint, JawPos )
    JawEndPos = cmds.xform( 'JawEnd_Piv', ws=True, q=True, t=True )
    JawEndJoint = denUt.den_makeJoint( nodeName='Jaw_end', pos=(JawEndPos), radius=radius*0.4, leaveSelected=True ); denUt.den_DiagPause( dpTime )
    #print( JawJoint, JawPos )
    print( 'TorsoJxJoints =', TorsoJxJoints )
    print( 'SpineJoints =', SpineJoints )
    print( 'NeckJoints =', NeckJoints )
    # make temporary list of joints to add to Guts list
    #stuffToAdd = [PelvisJoint,Spine01Joint,Spine02Joint,Spine03Joint,Spine04Joint,ChestJoint,Neck01Joint,Neck02Joint,Neck03Joint,Neck04Joint,HeadJoint,HeadEndJoint,JawJoint,JawEndJoint]
    # add to Guts list
    #TorsoGutsALL += stuffToAdd
    #print( stuffToAdd )
    #print( TorsoGutsALL )
    
    if ( displayLocalAxis ):
        for jx in TorsoJxJoints:
            cmds.setAttr( jx+'.displayLocalAxis', 1 )
    
    # -- orient the joints
    cmds.joint( PelvisJoint, e=True, oj='xyz', secondaryAxisOrient=spineAxisOrient, ch=True, zso=True )
    cmds.joint( JawJoint, e=True, oj='xyz', secondaryAxisOrient=jawAxisOrient, zso=True )
    
    # -- set up the ik handles for Spine and Neck
    # -- Pelvis, Cheat, Head will be driven directly by constraints
    
    SpineHandles = []
    for i in range(spineCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        #jxEnd = str(jx)
        #jxEndPad = jxEnd.rjust(2,'0')
        last = spineCount-1
        print( i, iStr, iStrPad )
        if i != last:
            cmds.select( SpineJoints[i], SpineJoints[i+1] )
        else:
            cmds.select( SpineJoints[i], ChestJoint )
        SpineHandle = denUt.den_AddIKHandle('ikSCsolver',False); denUt.den_DiagPause( dpTime )
        SpineHandles += [SpineHandle]
    
    NeckHandles = []
    for i in range(neckCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        #jxEnd = str(jx)
        #jxEndPad = jxEnd.rjust(2,'0')
        last = neckCount-1
        print( i, iStr, iStrPad )
        if i != last:
            cmds.select( NeckJoints[i], NeckJoints[i+1] )
        else:
            cmds.select( NeckJoints[i], HeadJoint )
        NeckHandle = denUt.den_AddIKHandle('ikSCsolver',False); denUt.den_DiagPause( dpTime )
        NeckHandles += [NeckHandle]
    
    
    # -- make the controls and zero nulls
    
    # -- Pelvis
    PelvisCtrl = denUt.den_MakeBall(nodeName='Pelvis_Ctrl',pos=(0,0,0),radius=ctrlRadius[0],doT=False)
    cmds.xform( t=PelvisPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Chest
    ChestCtrl = denUt.den_MakeBall(nodeName='Chest_Ctrl',pos=(0,0,0),radius=ctrlRadius[1],doT=False)
    cmds.xform( t=ChestPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Head
    HeadCtrl = denUt.den_MakeBall(nodeName='Head_Ctrl',pos=(0,0,0),radius=ctrlRadius[2],doT=False)
    cmds.xform( t=HeadPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Jaw
    JawCtrl = denUt.den_MakeBall(nodeName='Jaw_Ctrl',pos=(jawPos[0],jawPos[1],jawPos[2]),radius=ctrlRadius[3],doT=True)
    cmds.xform( t=JawPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # make temporary list of controls to add to Controls list
    stuffToAdd = [PelvisCtrl,ChestCtrl,HeadCtrl,JawCtrl]
    # add controls to Controls list
    TorsoCtrlsALL += stuffToAdd
    print( stuffToAdd )
    print( TorsoCtrlsALL )
    
    # - this loop is here in case more than one spine or neck joint are needed
    
    SpineVertJoints = []
    for i, jx in enumerate(SpineJoints):
        print(i, jx)
        if i != 0:
            SpineVertJoints += [jx]
    NeckVertJoints = []
    for i, jx in enumerate(NeckJoints):
        print(i, jx)
        if i != 0:
            NeckVertJoints += [jx]
    print( SpineVertJoints, NeckVertJoints )
    
    print( spineSecondaryJoints )
    
    SpineLargeControls = []
    SpineVertControls = []
    
    for jx in SpineVertJoints:
        isLargeControl = 0
        SpineCtrlRadius = ctrlRadius[3]
        for i in spineSecondaryJoints:
            iStrPad = '%02d' % (i,)
            if iStrPad in jx:
                SpineCtrlRadius = 3*ctrlRadius[3]
                isLargeControl = 1
                print( iStrPad, SpineCtrlRadius ) 
            else:
                print( iStrPad, SpineCtrlRadius ) 
        CtrlName = jx.replace('_Jnt', '_Ctrl')
        print( CtrlName )
        Ctrl = denUt.den_MakeBall(nodeName=CtrlName,pos=(0,6*ctrlRadius[3],0),radius=SpineCtrlRadius,doT=True)
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        Ctrl = cmds.parent( Ctrl, jx, relative=True )
        Ctrl = cmds.parent( Ctrl, TorsoSpaceIN )
        Ctrl = denUt.den_AddZeroNull()
        if isLargeControl:
            SpineLargeControls += Ctrl
        SpineVertControls += Ctrl
        denUt.den_DiagPause( dpTime )
    print( SpineLargeControls )
    
    NeckLargeControls = []
    NeckVertControls = []
    
    for jx in NeckVertJoints:
        isLargeControl = 0
        NeckCtrlRadius = ctrlRadius[3]
        for i in neckSecondaryJoints:
            iStrPad = '%02d' % (i,)
            if iStrPad in jx:
                NeckCtrlRadius = 3*ctrlRadius[3]
                isLargeControl = 1
                print( iStrPad, NeckCtrlRadius ) 
            else:
                print( iStrPad, NeckCtrlRadius ) 
        CtrlName = jx.replace('_Jnt', '_Ctrl')
        print( CtrlName )
        Ctrl = denUt.den_MakeBall(nodeName=CtrlName,pos=(0,6*ctrlRadius[3],0),radius=NeckCtrlRadius,doT=True)
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        Ctrl = cmds.parent( Ctrl, jx, relative=True )
        Ctrl = cmds.parent( Ctrl, TorsoSpaceIN )
        Ctrl = denUt.den_AddZeroNull()
        if isLargeControl:
            NeckLargeControls += Ctrl
        NeckVertControls += Ctrl
        denUt.den_DiagPause( dpTime )
    print( NeckLargeControls )
    
    # add controls to Controls list
    TorsoCtrlsALL += SpineVertControls + NeckVertControls
    print( SpineVertControls, NeckVertControls )
    print( TorsoCtrlsALL )
    
    
    
    # -- make locators for certain joints including 2 for Spine02 for blended pos
    PelvisLoc = cmds.spaceLocator (n='Pelvis_Loc')
    PelvisLoc = cmds.parent( PelvisLoc, PelvisJoint, relative=True )
    PelvisLoc = cmds.parent( PelvisLoc, PelvisCtrl )
    
    ChestLoc = cmds.spaceLocator (n='Chest_Loc')
    ChestLoc = cmds.parent( ChestLoc, ChestJoint, relative=True )
    ChestLoc = cmds.parent( ChestLoc, ChestCtrl )
    
    HeadLoc = cmds.spaceLocator (n='Head_Loc')
    HeadLoc = cmds.parent( HeadLoc, HeadJoint, relative=True )
    HeadLoc = cmds.parent( HeadLoc, HeadCtrl )
    
    # make temporary list of locators to add to Guts list
    #stuffToAdd = [PelvisLoc,ChestLoc,HeadLoc]
    # add locators to Guts list
    #TorsoGutsALL += stuffToAdd
    #print( stuffToAdd )
    #print( TorsoGutsALL )
    
    # -- reparent some things
    print( SpineHandles )
    SpineIKhParents = SpineVertControls+[ChestCtrl]
    print( SpineIKhParents )
    for i, handle in enumerate(SpineHandles):
        print( handle, SpineIKhParents[i] )
        cmds.parent( handle, SpineIKhParents[i] ) # make Spine01 ik goal follow Spine02Ctrl
    
    print( NeckHandles )
    NeckIKhParents = NeckVertControls+[HeadCtrl]
    print( NeckIKhParents )
    for i, handle in enumerate(NeckHandles):
        print( handle, NeckIKhParents[i] )
        cmds.parent( handle, NeckIKhParents[i] ) # make Spine01 ik goal follow Spine02Ctrl
    
    
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
    
    #============================================================================================================================== left off here may.2 2022
    
    
    print( SpineVertControls )
    print( SpineLargeControls )
    SpineSecondaries = [1]+spineSecondaryJoints+[spineCount+1]
    NeckSecondaries = [1]+neckSecondaryJoints+[neckCount+1]
    print( SpineSecondaries )
    print( NeckSecondaries )
    print( spineSecondaryJoints )
    print( neckSecondaryJoints )
    
    
    exp = 1.0
    for i, ctrl in enumerate(SpineLargeControls):
        print( ctrl )
        length = len(SpineLargeControls)
        w1 = float(i+1)
        w2 = (length+1)-w1
        w1 = pow(w1,exp)
        w2 = pow(w2,exp)
        zeroNull = cmds.listRelatives( ctrl, parent=True, fullPath=True )
        Constraint = cmds.parentConstraint( 'Pelvis_Ctrl', zeroNull, w=w2, mo=True )
        Constraint = cmds.parentConstraint( 'Chest_Ctrl', zeroNull, w=w1, mo=True )
        cmds.setAttr( Constraint[0]+'.interpType', 2 )

    for i, ctrl in enumerate(NeckLargeControls):
        print( ctrl )
        length = len(NeckLargeControls)
        w1 = float(i+1)
        w2 = (length+1)-w1
        w1 = pow(w1,exp)
        w2 = pow(w2,exp)
        zeroNull = cmds.listRelatives( ctrl, parent=True, fullPath=True )
        Constraint = cmds.parentConstraint( 'Chest_Ctrl', zeroNull, w=w2, mo=True )
        Constraint = cmds.parentConstraint( 'Head_Ctrl', zeroNull, w=w1, mo=True )
        cmds.setAttr( Constraint[0]+'.interpType', 2 )
    
    
    SpineIKCtrls = SpineVertControls+['Spine'+str(SpineSecondaries[-1]).rjust(2,'0')+'_Ctrl'] # - add an end for the loop
    print( SpineIKCtrls )
    
    cmds.rename( 'Pelvis_Ctrl', 'Spine'+str(SpineSecondaries[0]).rjust(2,'0')+'_Ctrl' ) # - rename Pelvis to Spine01 for the loop
    cmds.rename( 'Chest_Ctrl', 'Spine'+str(SpineSecondaries[-1]).rjust(2,'0')+'_Ctrl' ) # - rename Pelvis to Spine(last) for the loop
    
    for i, ball in enumerate(SpineSecondaries):#loop for each integer in SpineSecondaries
        ballStr = str(ball)
        ballStrPad = ballStr.rjust(2,'0')
        ci = ball-2#sets the index to use with the SpineIKCtrls list variable for balls that are not in-betweens
        print( '======================================================== doing ball', ball )
        if ball != SpineSecondaries[-1]: # check to see if it is the last ball
            xCurr = ball+1 # starts by setting the current number to the number of the first in-between joint
            xLast = SpineSecondaries[i+1]-1 # finds the number of the last in-between joint
            ballNextStrPad = str(xLast+1).rjust(2,'0') # find the number of the next ball - uses last in-between and adds one
            print( 'for ball', ball, ' xCurr starts at', xCurr, ' xLast =', xLast )
            if i == 0: # is it the first ball?
                print( ball, ballStrPad, ballNextStrPad, cmds.ls( 'Spine'+ballStrPad+'_Ctrl' ), ballStrPad, 'is the FIRST ball' )
            else:
                SpineIKCtrlZero = cmds.listRelatives( SpineIKCtrls[ci], parent=True, fullPath=True )
                SpineBallCtrl = cmds.ls( 'Spine'+ballStrPad+'_Ctrl' )
                print( ball, ballStrPad, ballNextStrPad, SpineBallCtrl, SpineIKCtrlZero, ballStrPad, 'is an in-between ball' )
            w1 = float((xLast+1)-xCurr) #sets the first weight to equal the total number of in-betweens
            w2 = 1.0
            while (xCurr <= xLast): #this will loop over each in-between
                SpineIKCtrlZero = cmds.listRelatives( SpineIKCtrls[xCurr-2], parent=True, fullPath=True )
                SpineBallCtrl_w1 = cmds.ls( 'Spine'+ballStrPad+'_Ctrl' )
                SpineBallCtrl_w2 = cmds.ls( 'Spine'+ballNextStrPad+'_Ctrl' )
                Constraint = cmds.parentConstraint( SpineBallCtrl_w1, SpineIKCtrlZero, mo=True, w=pow(w1,1) ) # the pow() makes the weight distribution curvy instead of linear
                Constraint = cmds.parentConstraint( SpineBallCtrl_w2, SpineIKCtrlZero, mo=True, w=pow(w2,1) )
                cmds.setAttr( Constraint[0]+'.interpType', 2 )
                print( 'xCurr =', xCurr, SpineBallCtrl_w1[0]+' w1 =', w1, SpineBallCtrl_w2[0]+' w2 =', w2, SpineIKCtrlZero, 'floats in-between '+ballStrPad+' and '+ballNextStrPad )
                xCurr += 1 # move on to the next one
                w1 -= 1
                w2 += 1
                denUt.den_DiagPause( dpTime )
        else:
            print( SpineIKCtrls[ci] )
            SpineIKCtrlZero = cmds.listRelatives( SpineIKCtrls[ci], parent=True, fullPath=True )
            SpineBallCtrl = cmds.ls( 'Spine'+ballStrPad+'_Ctrl' )
            print( ball, SpineBallCtrl, SpineIKCtrlZero, ballStrPad, 'is the LAST ball' )
        
    cmds.rename( 'Spine'+str(SpineSecondaries[0]).rjust(2,'0')+'_Ctrl', 'Pelvis_Ctrl' )
    cmds.rename( 'Spine'+str(SpineSecondaries[-1]).rjust(2,'0')+'_Ctrl', 'Chest_Ctrl' )
    
    
    NeckIKCtrls = NeckVertControls+['Neck'+str(NeckSecondaries[-1]).rjust(2,'0')+'_Ctrl'] # - add an end for the loop
    print( NeckIKCtrls )
    
    cmds.rename( 'Chest_Ctrl', 'Neck'+str(NeckSecondaries[0]).rjust(2,'0')+'_Ctrl' ) # - rename Pelvis to Neck01 for the loop
    cmds.rename( 'Head_Ctrl', 'Neck'+str(NeckSecondaries[-1]).rjust(2,'0')+'_Ctrl' ) # - rename Pelvis to Neck(last) for the loop
    
    for i, ball in enumerate(NeckSecondaries):#loop for each integer in NeckSecondaries
        ballStr = str(ball)
        ballStrPad = ballStr.rjust(2,'0')
        ci = ball-2#sets the index to use with the NeckIKCtrls list variable for balls that are not in-betweens
        print( '======================================================== doing ball', ball )
        if ball != NeckSecondaries[-1]: # check to see if it is the last ball
            xCurr = ball+1 # starts by setting the current number to the number of the first in-between joint
            xLast = NeckSecondaries[i+1]-1 # finds the number of the last in-between joint
            ballNextStrPad = str(xLast+1).rjust(2,'0') # find the number of the next ball - uses last in-between and adds one
            print( 'for ball', ball, ' xCurr starts at', xCurr, ' xLast =', xLast )
            if i == 0: # is it the first ball?
                print( ball, ballStrPad, ballNextStrPad, cmds.ls( 'Neck'+ballStrPad+'_Ctrl' ), ballStrPad, 'is the FIRST ball' )
            else:
                NeckIKCtrlZero = cmds.listRelatives( NeckIKCtrls[ci], parent=True, fullPath=True )
                NeckBallCtrl = cmds.ls( 'Neck'+ballStrPad+'_Ctrl' )
                print( ball, ballStrPad, ballNextStrPad, NeckBallCtrl, NeckIKCtrlZero, ballStrPad, 'is an in-between ball' )
            w1 = float((xLast+1)-xCurr) #sets the first weight to equal the total number of in-betweens
            w2 = 1.0
            while (xCurr <= xLast): #this will loop over each in-between
                NeckIKCtrlZero = cmds.listRelatives( NeckIKCtrls[xCurr-2], parent=True, fullPath=True )
                NeckBallCtrl_w1 = cmds.ls( 'Neck'+ballStrPad+'_Ctrl' )
                NeckBallCtrl_w2 = cmds.ls( 'Neck'+ballNextStrPad+'_Ctrl' )
                Constraint = cmds.parentConstraint( NeckBallCtrl_w1, NeckIKCtrlZero, mo=True, w=pow(w1,1) ) # the pow() makes the weight distribution curvy instead of linear
                Constraint = cmds.parentConstraint( NeckBallCtrl_w2, NeckIKCtrlZero, mo=True, w=pow(w2,1) )
                cmds.setAttr( Constraint[0]+'.interpType', 2 )
                print( 'xCurr =', xCurr, NeckBallCtrl_w1[0]+' w1 =', w1, NeckBallCtrl_w2[0]+' w2 =', w2, NeckIKCtrlZero, 'floats in-between '+ballStrPad+' and '+ballNextStrPad )
                xCurr += 1 # move on to the next one
                w1 -= 1
                w2 += 1
                denUt.den_DiagPause( dpTime )
        else:
            print( NeckIKCtrls[ci] )
            NeckIKCtrlZero = cmds.listRelatives( NeckIKCtrls[ci], parent=True, fullPath=True )
            NeckBallCtrl = cmds.ls( 'Neck'+ballStrPad+'_Ctrl' )
            print( ball, NeckBallCtrl, NeckIKCtrlZero, ballStrPad, 'is the LAST ball' )
        
    cmds.rename( 'Neck'+str(NeckSecondaries[0]).rjust(2,'0')+'_Ctrl', 'Chest_Ctrl' )
    cmds.rename( 'Neck'+str(NeckSecondaries[-1]).rjust(2,'0')+'_Ctrl', 'Head_Ctrl' )
    
    
    # -- list the jx joints for binding or proxy
    #TorsoJxJoints += [ PelvisJoint, Spine01Joint, Spine02Joint, Spine03Joint, Spine04Joint, ChestJoint, Neck01Joint, Neck02Joint, Neck03Joint, Neck04Joint, HeadJoint, JawJoint ]
    
    # -- add the space output nulls
    TorsoSpaceOUTs += denUt.den_AddSpaceOUTs(TorsoJxJoints)
    print( TorsoSpaceOUTs )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, JxJoints, CtrlsALL, GutsALL lists in order
    return TorsoRigGrp, TorsoSpaceINs, TorsoSpaceOUTs, TorsoJxJoints, TorsoCtrlsALL, TorsoGutsALL

#den_makeAnyTorsoRig( radius=0.7, ctrlRadius=(4.0,5.0,3.0,0.3), displayLocalAxis=False, spineCount=9, spineSecondaryJoints=[4,7], CtrneckCount=9, neckSecondaryJoints=[4,7] )


def den_makeDogFrontLegPivs( side='L_', prefix='', name='QuadFrontLeg', radius=2.0, elbowDist=15.0, footUpDist=7.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #side='L_'
    #prefix=''
    #name='Leg'
    #radius=2.0
    #elbowDist=15.0
    #footUpDist=7.0
    #dpTime=0.01
    #---------------------
    
    size=size*0.01
    
    LegPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    
    #denUt.den_makeLoc( nodeName='Clav_Piv', pos=(1.2, 288.1, -89.9), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Scap01_Piv', pos=( -size*10.6, size*55.9, size*35.5 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Scap02_Piv', pos=( size*4.7, size*65.7, size*31.4 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    
    denUt.den_makeLoc( nodeName='Shld_Piv', pos=( size*8.3, size*52.9, size*39.0 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Elbow_Piv', pos=( size*9.9, size*36.5, size*34.0 ), radius=radius  ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Fknee_Piv', pos=( size*10.7, size*12.9, size*36.2 ), radius=radius  ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Fankle_Piv', pos=( size*10.7, size*3.9, size*36.2 ), radius=radius  ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Fball_Piv', pos=( size*10.8, size*1.9, size*41.1 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeGrp ( 'FballSole_Piv', pos=(0, 0, 0) ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ftoe_Piv', pos=( size*11.2, 0.0, size*46.9 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    #denUt.den_makeLoc( nodeName='Fheel_Piv', pos=(42.0, 1, -75.8), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(3)
    cmds.curve( name='Fheel_Piv', degree=1, p=[( -1,0,0 ),( 1,0,0 ),( 1,0,2 ),( -1,0,2 ),( -1,0,0 )] ); cmds.move(size*10.6,0,size*37.3,'Fheel_Piv', r=True); cmds.scale(2*radius,0,3.5*radius,'Fheel_Piv.cv[*]'); cmds.setAttr( 'Fheel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='FsoleLF_Piv', pos=( size*14.4, 0.0, size*45.8 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3)
    denUt.den_makeLoc( nodeName='FsoleLB_Piv', pos=( size*13.1, 0.0, size*39.7 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3)
    denUt.den_makeLoc( nodeName='FsoleRF_Piv', pos=( size*6.7, 0.0, size*45.9 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3)
    denUt.den_makeLoc( nodeName='FsoleRB_Piv', pos=( size*8.2, 0.0, size*39.9 ), radius=radius ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(3)
    # -- connect the y translate attrs to the xxx to maintain a flat sole
    cmds.connectAttr( 'Fball_Piv.translateX', 'FballSole_Piv.translateX' )
    cmds.connectAttr( 'Fball_Piv.translateZ', 'FballSole_Piv.translateZ' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FballSole_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'Ftoe_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleLF_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleRF_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleLB_Piv.translateY' )
    #cmds.connectAttr( 'Fheel_Piv.translateY', 'FsoleRB_Piv.translateY' )
    
    # aim L_Scap01_Piv at scap02, use shoulder to keep up on the triangle plane
    cmds.aimConstraint( 'Scap02_Piv','Scap01_Piv', maintainOffset=False, worldUpType='object', worldUpObject='Shld_Piv' )
    
    # - make a set of pivots for the triangle of the reverse two leg bones
    denUt.den_makeLoc( nodeName='FlegMid_Loc', radius=radius*0.5 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(2)
    denUt.den_makeLoc( nodeName='ElbowPole_Loc', pos=(0, elbowDist, 0), radius=radius*0.5 )
    #cmds.xform ( t=(-40, 80, 0) )
    denUt.den_ColorShape(9)
    cmds.parent( 'ElbowPole_Loc', 'FlegMid_Loc' )
    
    # - make a second set of pivots for the triangle of the top two leg bones
    denUt.den_makeLoc( nodeName='FlegMid2_Loc', radius=radius*0.5 ) # leave off the L_ so constraint attrs are not confusing when mirrored   ## - new
    denUt.den_ColorShape(2) ## - new
    denUt.den_makeLoc( nodeName='ElbowPole2_Loc', pos=(0, elbowDist, 0), radius=radius*0.5 ) ## - new
    #cmds.xform ( t=(-40, 80, 0) ) ## - new
    denUt.den_ColorShape(9) ## - new
    cmds.parent( 'ElbowPole2_Loc', 'FlegMid2_Loc' ) ## - new
    # - make a locator to use for orienting the Fknee joint
    denUt.den_makeLoc( nodeName='Fknee_Loc', radius=radius*0.5 )
    denUt.den_ColorShape(2)
    # - make a locator that shows the up of the foot based on foot pivot locations to aid pivot placement
    denUt.den_makeLoc( nodeName='FfootUp_Piv', radius=radius*0.5, pos=(0, footUpDist, footUpDist) )
    #cmds.xform ( t=(20, 40, 0) )
    denUt.den_ColorShape(14)
    cmds.parent( 'FfootUp_Piv', 'Fheel_Piv', relative=True )
    
    FlegMidLocPtCon = cmds.pointConstraint( 'Shld_Piv','Fankle_Piv','FlegMid_Loc', mo=False  )[0]
    FlegMidLocAimCon = cmds.aimConstraint( 'Fankle_Piv','FlegMid_Loc', worldUpType='object', worldUpObject='Elbow_Piv', mo=False  )[0]
    FlegMidLoc2PtCon = cmds.pointConstraint( 'Shld_Piv','Fknee_Piv','FlegMid2_Loc', mo=False  )[0] ## - new
    FlegMidLoc2AimCon = cmds.aimConstraint( 'Fknee_Piv','FlegMid2_Loc', worldUpType='object', worldUpObject='Elbow_Piv', mo=False  )[0] ## - new
    ElbowPole2LocPtCon = cmds.pointConstraint( 'ElbowPole_Loc','ElbowPole2_Loc', skip='z', mo=False  )[0] ## - new
    ShldPivAimCon = cmds.aimConstraint( 'Elbow_Piv','Shld_Piv', worldUpType='object', worldUpObject='Fknee_Piv', mo=False  )[0] ## - new
    ElbowPivAimCon = cmds.aimConstraint( 'Fknee_Piv','Elbow_Piv', worldUpType='object', worldUpObject='Shld_Piv', mo=False  )[0] ## - new
    FkneeLocAimCon = cmds.aimConstraint( 'Fankle_Piv','Fknee_Loc', worldUpType='object', worldUpObject='ElbowPole_Loc', mo=False  )[0] ## - new
    FkneeLocPtCon = cmds.pointConstraint( 'Fknee_Piv','Fknee_Loc', mo=False  )[0] ## - new
    FanklePivAimCon = cmds.aimConstraint( 'Fball_Piv','Fankle_Piv', worldUpType='object', worldUpObject='FfootUp_Piv', mo=False  )[0]
    FsoleLFPivAimCon = cmds.aimConstraint( 'FsoleLB_Piv','FsoleLF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    FsoleRFPivAimCon = cmds.aimConstraint( 'FsoleRB_Piv','FsoleRF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    FtoePivAimCon = cmds.aimConstraint( 'Fball_Piv','Ftoe_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    HeelPivAimCon = cmds.aimConstraint( 'Ftoe_Piv','Fball_Piv', aimVector=(0,0,1), worldUpType='object', worldUpObject='FfootUp_Piv', mo=False )[0]
    #FKneePtCon = cmds.pointConstraint( 'Fankle_Piv','Fknee_Piv', mo=False  )[0]
    
    #cmds.parent( side+'Clav_Piv', side+'Scap01_Piv', side+'Scap02_Piv', LegPivGrp, relative=False )
    cmds.parent( 'Scap01_Piv', 'Scap02_Piv', 'Shld_Piv', 'Elbow_Piv', 'Fknee_Piv', 'Fknee_Loc', 'FlegMid_Loc', 'FlegMid2_Loc', LegPivGrp )
    cmds.parent( 'Fheel_Piv', LegPivGrp )
    cmds.parent( 'Fankle_Piv', 'Fball_Piv', 'FballSole_Piv', 'Ftoe_Piv', 'FsoleLF_Piv', 'FsoleLB_Piv', 'FsoleRF_Piv', 'FsoleRB_Piv', 'Fheel_Piv' )
    
    
    # - lock down channels the user is not supposed to touch 
    cmds.select( LegPivGrp ); denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    cmds.select( 'Scap01_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Scap02_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Shld_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Elbow_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fknee_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fknee_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FlegMid_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FlegMid2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'ElbowPole_Loc' ); denUt.den_Lock(  0,0,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'ElbowPole2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.select( 'Fheel_Piv' ); denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 1 )
    
    cmds.select( 'FfootUp_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fankle_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Fball_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FballSole_Piv' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ftoe_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleLF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleRF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleLB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FsoleRB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    
    # -- put the L_ back into the node names
    #cmds.rename( 'Clav_Piv', side+'Clav_Piv' )
    cmds.rename( 'Scap01_Piv', side+prefix+'Scap01_Piv' )
    cmds.rename( 'Scap02_Piv', side+prefix+'Scap02_Piv' )
    cmds.rename( 'Shld_Piv', side+prefix+'Shld_Piv' )
    cmds.rename( 'Elbow_Piv', side+prefix+'Elbow_Piv' )
    cmds.rename( 'Fknee_Piv', side+prefix+'Fknee_Piv' )
    cmds.rename( 'Fknee_Loc', side+prefix+'Fknee_Loc' ) ## - new
    cmds.rename( 'Fankle_Piv', side+prefix+'Fankle_Piv' )
    cmds.rename( 'Fball_Piv', side+prefix+'Fball_Piv' )
    cmds.rename( 'FballSole_Piv', side+prefix+'FballSole_Piv' )
    cmds.rename( 'Ftoe_Piv', side+prefix+'Ftoe_Piv' )
    cmds.rename( 'Fheel_Piv', side+prefix+'Fheel_Piv' )
    cmds.rename( 'FlegMid_Loc', side+prefix+'FlegMid_Loc' )
    cmds.rename( 'FlegMid2_Loc', side+prefix+'FlegMid2_Loc' ) ## - new
    cmds.rename( 'ElbowPole_Loc', side+prefix+'ElbowPole_Loc' )
    cmds.rename( 'ElbowPole2_Loc', side+prefix+'ElbowPole2_Loc' ) ## - new
    cmds.rename( 'FfootUp_Piv', side+prefix+'FfootUp_Piv' )
    cmds.rename( 'FsoleLF_Piv', side+prefix+'FsoleLF_Piv' )
    cmds.rename( 'FsoleRF_Piv', side+prefix+'FsoleRF_Piv' )
    cmds.rename( 'FsoleLB_Piv', side+prefix+'FsoleLB_Piv' )
    cmds.rename( 'FsoleRB_Piv', side+prefix+'FsoleRB_Piv' )
    cmds.rename( FlegMidLocPtCon, side+prefix+FlegMidLocPtCon )
    cmds.rename( FlegMidLocAimCon, side+prefix+FlegMidLocAimCon )
    cmds.rename( FlegMidLoc2PtCon, side+prefix+FlegMidLoc2PtCon ) ## - new
    cmds.rename( FlegMidLoc2AimCon, side+prefix+FlegMidLoc2AimCon ) ## - new
    cmds.rename( ElbowPole2LocPtCon, side+prefix+ElbowPole2LocPtCon ) ## - new
    cmds.rename( ShldPivAimCon, side+prefix+ShldPivAimCon )
    cmds.rename( FanklePivAimCon, side+prefix+FanklePivAimCon )
    cmds.rename( FsoleLFPivAimCon, side+prefix+FsoleLFPivAimCon )
    cmds.rename( FsoleRFPivAimCon, side+prefix+FsoleRFPivAimCon )
    cmds.rename( FtoePivAimCon, side+prefix+FtoePivAimCon )
    cmds.rename( FkneeLocAimCon, side+prefix+FkneeLocAimCon )
    cmds.rename( FkneeLocPtCon, side+prefix+FkneeLocPtCon )
    
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( LegPivGrp+'.scaleX', -1 )
    
    return LegPivGrp





# ---------------------------------------------------------------------------------------
def den_makeDogFrontLegRig( side='L_', prefix='', name='QuadFrontLeg', radius=2.0, ctrlRadius=6.0, displayLocalAxis=False, dpTime=0.01 ):
    #--------------------- testing variables
    #side='L_'
    #name='QuadLeg'
    #radius=2.0
    #ctrlRadius=6.0
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
    LegJxJoints = [] #Set list variable to hold names of all the Jx joints
    LegCtrlsALL = [] #Set list variable to hold names of all the controls
    LegGutsALL = [] #Set list variable to hold names of all the guts
    
    ChestSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'ChestSpace_IN' )
    ChestSpaceIN = cmds.parent( ChestSpaceIN, LegRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'CogSpace_IN' )
    CogSpaceIN = cmds.parent( CogSpaceIN, LegRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'AllSpace_IN' )
    AllSpaceIN = cmds.parent( AllSpaceIN, LegRigGrp )[0]
    LegSpaceINs += [ ChestSpaceIN, CogSpaceIN, AllSpaceIN ]
    LegSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp' )
    LegSkelGrp = cmds.parent( LegSkelGrp, ChestSpaceIN )[0]
    LegCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp' )
    LegCtrlGrp = cmds.parent( LegCtrlGrp, ChestSpaceIN )[0]
    # -- make Wrist control space switch constraint
    FankleCtrlSpace = denUt.den_makeGrp( nodeName=side+'FankleCtrl_Space' )
    FankleCtrlSpace = cmds.parent( FankleCtrlSpace, LegCtrlGrp )[0]
    FankleCtrlSpaceConstraint = cmds.parentConstraint( ChestSpaceIN, FankleCtrlSpace, weight=0 )
    FankleCtrlSpaceConstraint = cmds.parentConstraint( CogSpaceIN, FankleCtrlSpace, weight=0 )
    FankleCtrlSpaceConstraint = cmds.parentConstraint( AllSpaceIN, FankleCtrlSpace, weight=1 )
    
    
    # -- set variables for pivot positions
    
    ShldPos = cmds.xform( side+'Shld_Piv', ws=True, q=True, t=True )
    ShldPosVec = om.MVector(ShldPos[0],ShldPos[1],ShldPos[2])
    ElbowPos = cmds.xform( side+'Elbow_Piv', ws=True, q=True, t=True )
    ElbowPosVec = om.MVector(ElbowPos[0],ElbowPos[1],ElbowPos[2])
    FkneePos = cmds.xform( side+'Fknee_Piv', ws=True, q=True, t=True )
    FkneePosVec = om.MVector(FkneePos[0],FkneePos[1],FkneePos[2])
    FanklePos = cmds.xform( side+'Fankle_Piv', ws=True, q=True, t=True )
    FanklePosVec = om.MVector(FanklePos[0],FanklePos[1],FanklePos[2])
    FballPos = cmds.xform( side+'Fball_Piv', ws=True, q=True, t=True )
    FtoePos = cmds.xform( side+'Ftoe_Piv', ws=True, q=True, t=True )
    FheelPos = cmds.xform( side+'Fheel_Piv', ws=True, q=True, t=True )
    FsoleLFPos = cmds.xform( side+'FsoleLF_Piv', ws=True, q=True, t=True )
    FsoleLBPos = cmds.xform( side+'FsoleLB_Piv', ws=True, q=True, t=True )
    FsoleRFPos = cmds.xform( side+'FsoleRF_Piv', ws=True, q=True, t=True )
    FsoleRBPos = cmds.xform( side+'FsoleLB_Piv', ws=True, q=True, t=True )
    FballSolePos = [ FballPos[0], FtoePos[1], FballPos[2] ]
    #print 'FballSolePos', FballSolePos
    ElbowPolePos = cmds.xform( side+'ElbowPole_Loc', ws=True, q=True, t=True )
    ElbowPole2Pos = cmds.xform( side+'ElbowPole2_Loc', ws=True, q=True, t=True )
    Scap01Pos = cmds.xform( side+'Scap01_Piv', ws=True, q=True, t=True )
    Scap02Pos = cmds.xform( side+'Scap02_Piv', ws=True, q=True, t=True )
    
    
    # -- make reverse 2 bone leg joints
    vecA = ShldPosVec - ElbowPosVec
    #print vecA.x, vecA.y, vecA.z
    BoneLenA = om.MVector.length(vecA)
    #print BoneLenA
    
    vecB = ElbowPosVec - FkneePosVec
    #print vecB.x, vecB.y, vecB.z
    BoneLenB = om.MVector.length(vecB)
    #print BoneLenB
    
    vecC = FkneePosVec - FanklePosVec
    #print vecC.x, vecC.y, vecC.z
    BoneLenC = om.MVector.length(vecC)
    #print BoneLenC
    
    Leg1JuPivTmp = denUt.den_makeLoc( nodeName=side+prefix+name+'Leg1Ju_Piv', pos=(ShldPos) )
    Leg2JuPivTmp = denUt.den_makeLoc( nodeName=side+prefix+name+'Leg2Ju_Piv_Tmp' )
    Leg2JuPivTmp = cmds.parent( Leg2JuPivTmp, Leg1JuPivTmp, relative=True )[0]
    Leg1JuPivOri = cmds.orientConstraint( side+'Elbow_Piv', Leg1JuPivTmp, mo=False, offset=(0,0,0) )
    cmds.delete( Leg1JuPivOri )
    cmds.setAttr( Leg2JuPivTmp+'.translateX', BoneLenB )
    
    RevPos = cmds.xform( Leg2JuPivTmp, ws=True, q=True, t=True )
    
    cmds.select( Leg1JuPivTmp )
    Leg1Ju = cmds.joint( n=side+prefix+name+'Leg1_Ju', p=(ShldPos), radius=radius ); denUt.den_DiagPause( dpTime )
    Leg2Ju = cmds.joint( n=side+prefix+name+'Leg2_Ju', p=(RevPos), radius=radius ); denUt.den_DiagPause( dpTime )
    Leg3Ju = cmds.joint( n=side+prefix+name+'Leg3_Ju', p=(FanklePos), radius=radius ); denUt.den_DiagPause( dpTime )
    
    # -- make the joints
    cmds.select( clear=True )
    
    ShldJoint = cmds.joint( n=side+'Shld_Jnt', p=(ShldPos), radius=radius ); denUt.den_DiagPause( dpTime )
    ElbowJoint = cmds.joint( n=side+'Elbow_Jnt', p=(ElbowPos), radius=radius ); denUt.den_DiagPause( dpTime )
    FkneeJoint = cmds.joint( n=side+'Fknee_Jnt', p=(FkneePos), radius=radius ); denUt.den_DiagPause( dpTime )
    FankleJoint = cmds.joint( n=side+'Fankle_Jnt', p=(FanklePos), radius=radius ); denUt.den_DiagPause( dpTime )
    FballJoint = cmds.joint( n=side+'Fball_Jnt', p=(FballPos), radius=radius ); denUt.den_DiagPause( dpTime )
    FtoeJoint = cmds.joint( n=side+'Ftoe_Jx', p=(FtoePos), radius=radius ); denUt.den_DiagPause( dpTime )
    
    #print ShldJoint, ShldPos
    #print ElbowJoint, ElbowPos
    #print FankleJoint, FanklePos
    #print FballJoint, FballPos
    #print FtoeJoint, FtoePos
    
    if ( displayLocalAxis ):
        cmds.setAttr( Leg1Ju+'.displayLocalAxis', 1 )
        cmds.setAttr( Leg2Ju+'.displayLocalAxis', 1 )
        cmds.setAttr( Leg3Ju+'.displayLocalAxis', 1 )
        
        cmds.setAttr( ShldJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ElbowJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FkneeJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FankleJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FballJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( FtoeJoint+'.displayLocalAxis', 1 )
    
    cmds.select( clear=True )
    Scap01Joint = cmds.joint( n=side+'Scap01_Jx', p=(Scap01Pos), radius=radius ); denUt.den_DiagPause( dpTime )
    Scap01Joint = cmds.parent( Scap01Joint, LegSkelGrp )[0]
    Scap02Joint = cmds.joint( n=side+'Scap02_Jnt', p=(Scap02Pos), radius=radius ); denUt.den_DiagPause( dpTime )
    Scap03Joint = cmds.joint( n=side+'Scap02_end', p=(ShldPos), radius=radius ); denUt.den_DiagPause( dpTime )
    
    if ( displayLocalAxis ):
        cmds.setAttr( Scap01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Scap02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Scap03Joint+'.displayLocalAxis', 1 )
        
    
    # -- orient the joints
    
    #cmds.joint( Leg2Ju, e=True, oj='xzy', secondaryAxisOrient='xup', zso=True )
    #cmds.joint( Leg2Ju, e=True, oj='xyz', zso=True )
    cmds.joint( Leg2Ju, e=True, oj='xzy', secondaryAxisOrient='xdown', aos=True, ch=False, zso=True )
    cmds.joint( Leg3Ju, e=True, oj='none', zso=True )
    cmds.setAttr( Leg3Ju+'.translateX', BoneLenA+BoneLenC )
    #Leg1Ju = cmds.parent( Leg1Ju, LegSkelGrp )[0] # -- put Shld back under leg skel grp
    
    cmds.select( clear=True )
    #cmds.joint( ElbowJoint, e=True, oj='xyz', zso=True )
    cmds.joint( ElbowJoint, e=True, oj='xzy', secondaryAxisOrient='xdown', aos=True, ch=False, zso=True )
    FkneeJoint = cmds.parent( FkneeJoint, side+'Fknee_Loc' )[0] # -- temp reparent Fknee
    #cmds.joint( FkneeJoint, e=True, oj='none', zso=True )
    cmds.joint( FkneeJoint, e=True, oj='xzy', secondaryAxisOrient='xdown', aos=True, ch=False, zso=True )
    FkneeJoint = cmds.parent( FkneeJoint, ElbowJoint )[0] # -- put Fknee back under knee jnt
    cmds.joint( FankleJoint, e=True, oj='none', zso=True )
    ShldJoint = cmds.parent( ShldJoint, side+'Shld_Piv' )[0] # -- temp reparent Shld under planar space
    cmds.joint( ShldJoint, e=True, oj='none', zso=True )
    #ShldJoint = cmds.parent( ShldJoint, LegSkelGrp )[0] # -- put hip back under leg skel grp
    FankleJoint = cmds.parent( FankleJoint, side+'Fankle_Piv' )[0] # -- temp reparent ankle under planar space
    #cmds.joint( FballJoint, e=True, oj='xyz', zso=True )
    cmds.joint( FballJoint, e=True, oj='xzy', secondaryAxisOrient='xdown', aos=True, ch=False, zso=True )
    cmds.joint( FtoeJoint, e=True, oj='none', zso=True )
    FankleJoint = cmds.parent( FankleJoint, FkneeJoint )[0] # -- put ankle back under hock jnt
    
    cmds.select( clear=True )
    #cmds.joint( Scap02Joint, e=True, oj='xyz', zso=True )
    cmds.joint( Scap02Joint, e=True, oj='xzy', secondaryAxisOrient='ydown', aos=True, ch=False, zso=True )
    cmds.joint( Scap03Joint, e=True, oj='none', zso=True )
    Scap01Joint = cmds.parent( Scap01Joint, side+'Scap01_Piv' ) # -- temp reparent scap under planar space
    cmds.joint( Scap01Joint, e=True, oj='none', zso=True )
    Scap01Joint = cmds.parent( Scap01Joint, LegSkelGrp )[0] # -- put scap back

    ShldJoint = cmds.parent( ShldJoint, Scap03Joint )[0] # -- put hip back under leg skel grp
    Leg1Ju = cmds.parent( Leg1Ju, Scap03Joint )[0] # -- put Shld back under leg skel grp
    
    # -- duplicate the leg to make the FK and IK leg bones
    ShldJointIK = cmds.duplicate (ShldJoint, name=side+'Shld_IK' )[0]
    ElbowJointIK = cmds.rename (ShldJointIK+'|'+side+'Elbow_Jnt', side+'Elbow_IK' )
    FkneeJointIK = cmds.rename (ElbowJointIK+'|'+side+'Fknee_Jnt', side+'Fknee_IK' )
    FankleJointIK = cmds.rename (FkneeJointIK+'|'+side+'Fankle_Jnt', side+'Fankle_IK' )
    FballJointIK = cmds.rename (FankleJointIK+'|'+side+'Fball_Jnt', side+'Fball_IK' )
    FtoeJointIK = cmds.rename (FballJointIK+'|'+side+'Ftoe_Jx', side+'Ftoe_IK' )
    #print ShldJointIK, '----', ElbowJointIK, '----', FankleJointIK, '----', FballJointIK, '----', FtoeJointIK
    ShldJointFK = cmds.duplicate (ShldJoint, name=side+'Shld_FK' )[0]
    ElbowJointFK = cmds.rename (ShldJointFK+'|'+side+'Elbow_Jnt', side+'Elbow_FK' )
    FkneeJointFK = cmds.rename (ElbowJointFK+'|'+side+'Fknee_Jnt', side+'Fknee_FK' )
    FankleJointFK = cmds.rename (FkneeJointFK+'|'+side+'Fankle_Jnt', side+'Fankle_FK' )
    FballJointFK = cmds.rename (FankleJointFK+'|'+side+'Fball_Jnt', side+'Fball_FK' )
    FtoeJointFK = cmds.rename (FballJointFK+'|'+side+'Ftoe_Jx', side+'Ftoe_FK' )
    #print ShldJointFK, '----', ElbowJointFK, '----', FankleJointFK, '----', FballJointFK, '----', FtoeJointFK
    
    # -- make the controls and zero nulls
    
    # -- Shoulder IK Control
    ShldCtrl = denUt.den_MakeCube( nodeName=side+'Shld_Ctrl', pos=(0,0,0) ,radius=ctrlRadius, doT=False)
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=ShldPos )
    ShldCtrl = cmds.parent( ShldCtrl, LegCtrlGrp )
    ShldCtrl = denUt.den_AddZeroNull()
    ShldCtrlZero = cmds.listRelatives( ShldCtrl, parent=True, fullPath=True )
    #ArmCtrlsALL += ShldCtrl # add to the controls list
    # -- Shld FK
    ShldFKCtrl = denUt.den_MakeSpike( nodeName=side+'ShldFK_Ctrl', radius=ctrlRadius*1.1, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ShldFKCtrl = cmds.parent( ShldFKCtrl, ShldJointFK, relative=True )
    ShldFKCtrl = cmds.parent( ShldFKCtrl, LegCtrlGrp )
    ShldFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    ShldFKCtrlZero = cmds.listRelatives( ShldFKCtrl, parent=True, fullPath=True )[0]
    cmds.connectAttr( ShldFKCtrl[0]+'.rotate', ShldJointFK+'.rotate' )
    cmds.parentConstraint( Scap02Joint, ShldFKCtrlZero, mo=True )
    #print ShldFKCtrl
    # -- Leg Utility
    LegUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(ctrlRadius*0.6,0,-ctrlRadius*1.5), radius=ctrlRadius*0.3, Plane='ZX')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# relock after parenting
    LegUtilCtrl = cmds.parent( LegUtilCtrl, ShldJointFK, relative=True )
    LegUtilCtrl = cmds.parent( LegUtilCtrl, LegCtrlGrp )
    denUt.den_LockAttr(True,True,True,False)# relock after parenting
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', lock=False, keyable=True )
    cmds.addAttr( LegUtilCtrl, longName=side+'Fankle_FK_IK', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+'Fankle_FK_IK', lock=False, keyable=True )
    # -- Elbow
    ElbowCtrl = denUt.den_MakePole( nodeName=side+'Elbow_Ctrl', radius=ctrlRadius*0.3 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=ElbowPolePos )
    ElbowCtrl = cmds.parent( ElbowCtrl, LegCtrlGrp )
    ElbowCtrl = denUt.den_AddZeroNull()
    # -- Elbow2
    Elbow2Ctrl = denUt.den_MakePole( nodeName=side+'Elbow2_Ctrl', radius=ctrlRadius*0.15 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=ElbowPole2Pos )
    Elbow2Ctrl = cmds.parent( Elbow2Ctrl, ElbowCtrl )
    Elbow2Ctrl = denUt.den_AddZeroNull()
    
    ElbowFKCtrl = denUt.den_MakeArrowR( nodeName=side+'ElbowFK_Ctrl', pos=(0,-ctrlRadius*0.7,0), radius=ctrlRadius*0.5, doT=True, axis='-Y' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ElbowJointFK, relative=True )
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ShldFKCtrl )
    ElbowFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( ElbowFKCtrl[0]+'.rotate', ElbowJointFK+'.rotate' )
    #print ElbowFKCtrl
    
    # -- Fknee
    FkneeCtrl = denUt.den_MakeCube( nodeName=side+'Fknee_Ctrl', pos=(ctrlRadius*1.0,0,0), radius=ctrlRadius*0.3, doT=True )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=FkneePos )
    FkneeCtrl = cmds.parent( FkneeCtrl, LegCtrlGrp )
    FkneeCtrl = denUt.den_AddZeroNull()
    FkneeCtrlZero = cmds.listRelatives( FkneeCtrl, parent=True, fullPath=True )[0]
    
    FkneeFKCtrl = denUt.den_MakeArrowR( nodeName=side+'FkneeFK_Ctrl', pos=(0,-ctrlRadius*1.0,0), radius=ctrlRadius*0.3, doT=True, axis='-Y' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    FkneeFKCtrl = cmds.parent( FkneeFKCtrl, FkneeJointFK, relative=True )
    FkneeFKCtrl = cmds.parent( FkneeFKCtrl, ElbowFKCtrl )
    FkneeFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( FkneeFKCtrl[0]+'.rotate', FkneeJointFK+'.rotate' )
    #print ElbowFKCtrl
    
    
    # -- Fankle Controls
    FankleCtrl = denUt.den_MakeBall( nodeName=side+'Fankle_Ctrl', radius=ctrlRadius*0.9 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    cmds.xform( t=FanklePos )
    FankleCtrl = cmds.parent( FankleCtrl, FankleCtrlSpace )
    FankleCtrl = denUt.den_AddZeroNull()
    cmds.setAttr( FankleCtrl[0]+'.rotateOrder', 1 )
    FankleCtrlZero = cmds.listRelatives( FankleCtrl, parent=True, fullPath=True )[0]
    
    FankleFKCtrl = denUt.den_MakeSpike( nodeName=side+'FankleFK_Ctrl', radius=ctrlRadius*1.1, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    FankleFKCtrl = cmds.parent( FankleFKCtrl, FankleJointFK, relative=True )
    FankleFKCtrl = cmds.parent( FankleFKCtrl, FkneeFKCtrl )
    FankleFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( FankleFKCtrl[0]+'.rotate', FankleJointFK+'.rotate' )
    FankleFKCtrlZero = cmds.listRelatives( FankleFKCtrl, parent=True, fullPath=True )[0]
    
    #print FankleCtrlZero
    FballFKCtrl = denUt.den_MakeSpike(nodeName=side+'FballFK_Ctrl', radius=ctrlRadius, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    FballFKCtrl = cmds.parent( FballFKCtrl, FballJointFK, relative=True )
    FballFKCtrl = cmds.parent( FballFKCtrl, FankleFKCtrl )
    FballFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( FballFKCtrl[0]+'.rotate', FballJointFK+'.rotate' )
    FballFKCtrlZero = cmds.listRelatives( FballFKCtrl, parent=True, fullPath=True )[0]
    # -- Foot Utility
    FootUtilCtrl = denUt.den_MakeGear( nodeName=side+'FootUtil_Ctrl', pos=(ctrlRadius,ctrlRadius,0), radius=ctrlRadius*0.2, Plane='XY')
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    FootUtilCtrl = cmds.parent( FootUtilCtrl, FankleCtrl, relative=True )
    
    cmds.addAttr( FootUtilCtrl, longName=side+'FootRock', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootRock', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootRock', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FootRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootRoll', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootRoll', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FootPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootPivot', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootPivot', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FootTwist', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootTwist', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FootTwist', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FheelPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FheelPivot', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FheelPivot', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FtoeRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FtoeRoll', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FtoeRoll', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FtoePivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FtoePivot', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FtoePivot', keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=side+'FtoeBend', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FtoeBend', lock=False, keyable=True )
    #cmds.setAttr( FootUtilCtrl[0]+'.'+side+'FtoeBend', keyable=True )
    
    # -- connect up the Fankle control space switcher
    cmds.addAttr( LegUtilCtrl, longName=side+'ChestSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+'ChestSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+'ChestSpace', FankleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'ChestSpace_INW0' )
    cmds.addAttr( LegUtilCtrl, longName=side+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+'CogSpace', FankleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'CogSpace_INW1' )
    cmds.addAttr( LegUtilCtrl, longName=side+'AllSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+'AllSpace', FankleCtrlSpaceConstraint[0]+'.'+side+prefix+name+'AllSpace_INW2' )
    
    # -- set up Leg FK_IK blending
    Shld_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+'Shld_ikFk_pairBlend' )
    cmds.setAttr( Shld_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ShldJointFK+'.rotate', Shld_pairBlend+'.inRotate1' )
    cmds.connectAttr( ShldJointIK+'.rotate', Shld_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Shld_pairBlend+'.weight' )
    cmds.connectAttr( Shld_pairBlend+'.outRotate', ShldJoint+'.rotate' )
    
    Elbow_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+'Elbow_ikFk_pairBlend' )
    cmds.setAttr( Elbow_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ElbowJointFK+'.rotate', Elbow_pairBlend+'.inRotate1' )
    cmds.connectAttr( ElbowJointIK+'.rotate', Elbow_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Elbow_pairBlend+'.weight' )
    cmds.connectAttr( Elbow_pairBlend+'.outRotate', ElbowJoint+'.rotate' )
    
    Fknee_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+'Fknee_ikFk_pairBlend' )
    cmds.setAttr( Fknee_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( FkneeJointFK+'.rotate', Fknee_pairBlend+'.inRotate1' )
    cmds.connectAttr( FkneeJointIK+'.rotate', Fknee_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Fknee_pairBlend+'.weight' )
    cmds.connectAttr( Fknee_pairBlend+'.outRotate', FkneeJoint+'.rotate' )
    
    Fankle_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+'Fankle_ikFk_pairBlend' )
    cmds.setAttr( Fankle_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( FankleJointFK+'.rotate', Fankle_pairBlend+'.inRotate1' )
    cmds.connectAttr( FankleJointIK+'.rotate', Fankle_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Fankle_pairBlend+'.weight' )
    cmds.connectAttr( Fankle_pairBlend+'.outRotate', FankleJoint+'.rotate' )
    
    Fball_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+'Fball_ikFk_pairBlend' )
    cmds.setAttr( Fball_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( FballJointFK+'.rotate', Fball_pairBlend+'.inRotate1' )
    cmds.connectAttr( FballJointIK+'.rotate', Fball_pairBlend+'.inRotate2' )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Fball_pairBlend+'.weight' )
    cmds.connectAttr( Fball_pairBlend+'.outRotate', FballJoint+'.rotate' )
    
    
    # -- make the reverse foot
    
    footPivs = [ 'Fheel_Piv', 'FballSole_Piv', 'FsoleLF_Piv', 'FsoleRF_Piv', 'Ftoe_Piv', 'Fball_Piv', 'Fankle_Piv' ]
    footJnts = []
    for number,footPiv in enumerate(footPivs):
        prevNum = number-1
        nameRoot = footPiv.replace('_Piv','')
        #print( 'nameRoot', nameRoot, number )
        footJnt = cmds.joint( n=side+nameRoot+'Rev_Jx', radius=radius*0.7 )
        footPiv = side+footPivs[number]
        footJnt = cmds.parent( footJnt, footPiv, relative=True )
        cmds.joint( footJnt, e=True, oj='none', zso=True, radius=radius*0.7 )
        if number != 0:
            footJnt = cmds.parent( footJnt, footJnts[prevNum], relative=False )
        else:
            footJnt = cmds.parent( footJnt, world=True )
        footJnts = footJnts + [footJnt]
    #print(footJnts[5])
    #cmds.joint( footJnts[5], e=True, oj='none', zso=True, radius=radius*0.7 ); denUt.den_DiagPause( 0.02 )
    
    #print footJnts
    RevFheelJoint = footJnts[0]
    RevFballSoleJoint = footJnts[1]
    RevFsoleLFJoint = footJnts[2]
    RevFsoleRFJoint = footJnts[3]
    RevFtoeJoint = footJnts[4]
    RevFballJoint = footJnts[5]
    RevFankleJoint = footJnts[6]
    #print RevFheelJoint
    #RevFtoeBendLoc = cmds.spaceLocator( name=side+'RevFtoeBend_Loc' )
    #RevFtoeBendLoc = cmds.parent( RevFtoeBendLoc, RevFtoeJoint, relative=True )
    
    # -- make the reverse Fknee bits
    FankleLiftCtrl = denUt.den_MakeCube( nodeName=side+'FankleLift_Ctrl', radius=ctrlRadius*0.2, pos=(0,0.7*ctrlRadius,0), doT=True )
    denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
    FankleLiftCtrl = cmds.parent( FankleLiftCtrl, RevFankleJoint, relative=True )
    FankleLiftCtrl = denUt.den_AddZeroNull()
    FankleLiftCtrlZero = cmds.listRelatives( FankleLiftCtrl, parent=True, fullPath=True )[0]
    
    RevFkneeLoc = cmds.spaceLocator( name=side+'RevFknee_Loc' )
    #RevFkneeLoc = cmds.parent( RevFkneeLoc, RevFankleJoint, relative=True )
    RevFkneeLoc = cmds.parent( RevFkneeLoc, FankleLiftCtrl, relative=True )
    print( FkneeCtrl )
    RevHocLocAimCon = cmds.aimConstraint( FkneeCtrl, RevFkneeLoc, worldUpType='object', worldUpObject=ElbowCtrl[0] )[0]
    #FkneeCtrlZeroCon = cmds.parentConstraint( Leg2Ju, FkneeCtrlZero, mo=True )[0]
    
    
    # -- make the ik handles
    cmds.select( Leg1Ju, Leg3Ju )
    LegIK2handle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    LegIK2handle = cmds.parent( LegIK2handle, FankleLiftCtrl )[0]
    cmds.poleVectorConstraint( ElbowCtrl, LegIK2handle )
    cmds.setAttr( LegIK2handle+'.twist', 180 )
    cmds.setAttr( LegIK2handle+'.translate', 0,0,0 )
    
    FkneeCtrlZeroCon = cmds.parentConstraint( Leg2Ju, FkneeCtrlZero, mo=True )[0]
    
    #=============================================================================================================='''
    cmds.select( ShldJointIK, FkneeJointIK )
    LegIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    LegIKhandle = cmds.parent( LegIKhandle, RevFkneeLoc )[0]
    cmds.poleVectorConstraint( Elbow2Ctrl, LegIKhandle )
    
    #cmds.select( FkneeJointIK, FankleJointIK )
    #FkneeIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    #FkneeIKhandle = cmds.parent( FkneeIKhandle, FankleLiftCtrl )[0]
    #cmds.poleVectorConstraint( ElbowCtrl, FkneeIKhandle )
    #cmds.setAttr( FkneeIKhandle+'.twist', 180 )
    
    cmds.select( FkneeJointIK, FankleJointIK )
    FkneeIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    FkneeIKhandle = cmds.parent( FkneeIKhandle, FankleLiftCtrl )[0]
    #cmds.setAttr( FkneeIKhandle+'.twist', 180 )
    
    cmds.select( FankleJointIK, FballJointIK )
    FballIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    FballIKhandle = cmds.parent( FballIKhandle, RevFballJoint )[0]
    cmds.select( FballJointIK, FtoeJointIK )
    FtoeIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    FtoeIKhandle = cmds.parent( FtoeIKhandle, RevFtoeJoint )[0]
    
    ScapIKhandle = cmds.ikHandle( startJoint=Scap01Joint, endEffector=Scap03Joint, solver='ikSCsolver', name=Scap01Joint.replace('Jx','Ikh') )
    #print( ScapIKhandle )
    cmds.rename( ScapIKhandle[1], ScapIKhandle[0].replace('Ikh','Eff') )
    ScapIKhandle = cmds.parent( ScapIKhandle[0], ShldCtrl )

    # -- add utility nodes and connect attrs for foot roll
    footFheelRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFheelRoll_unitConversion' )
    footFheelRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+'footFheelRoll_clamp' )
    cmds.setAttr( footFheelRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFheelRoll_clamp+'.minR', -180 )
    footFballRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFballRoll_unitConversion' )
    footFballRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+'footFballRoll_clamp' )
    cmds.setAttr( footFballRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFballRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FootRoll', footFheelRoll_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FootRoll', footFballRoll_clamp+'.inputR' )
    cmds.connectAttr( footFheelRoll_clamp+'.outputR', footFheelRoll_unitConversion+'.input' )
    cmds.connectAttr( footFballRoll_clamp+'.outputR', footFballRoll_unitConversion+'.input' )
    cmds.connectAttr( footFheelRoll_unitConversion+'.output', RevFheelJoint[0]+'.rotateX' )
    cmds.connectAttr( footFballRoll_unitConversion+'.output', RevFballJoint[0]+'.rotateX' )
    
    # -- add utility nodes and connect attrs for foot rock
    footFsoleLFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFsoleLFRock_unitConversion' )
    footFsoleLFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+'footFsoleLFRock_clamp' )
    cmds.setAttr( footFsoleLFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFsoleLFRock_clamp+'.minR', -180 )
    footFsoleRFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFsoleRFRock_unitConversion' )
    footFsoleRFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+'footFsoleRFRock_clamp' )
    cmds.setAttr( footFsoleRFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFsoleRFRock_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FootRock', footFsoleLFRock_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FootRock', footFsoleRFRock_clamp+'.inputR' )
    cmds.connectAttr( footFsoleLFRock_clamp+'.outputR', footFsoleLFRock_unitConversion+'.input' )
    cmds.connectAttr( footFsoleRFRock_clamp+'.outputR', footFsoleRFRock_unitConversion+'.input' )
    cmds.connectAttr( footFsoleLFRock_unitConversion+'.output', RevFsoleLFJoint[0]+'.rotateZ' )
    cmds.connectAttr( footFsoleRFRock_unitConversion+'.output', RevFsoleRFJoint[0]+'.rotateZ' )
    # -- connect foot pivot
    footFballSolePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFballSolePivot_unitConversion' )
    cmds.setAttr( footFballSolePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FootPivot', footFballSolePivot_unitConversion+'.input' )
    cmds.connectAttr( footFballSolePivot_unitConversion+'.output', RevFballSoleJoint[0]+'.rotateY' )
    # -- connect foot twist
    footFballTwist_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFballTwist_unitConversion' )
    cmds.setAttr( footFballTwist_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FootTwist', footFballTwist_unitConversion+'.input' )
    cmds.connectAttr( footFballTwist_unitConversion+'.output', RevFballJoint[0]+'.rotateZ' )
    # -- connect heel pivot
    footFheelPivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFheelPivot_unitConversion' )
    cmds.setAttr( footFheelPivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FheelPivot', footFheelPivot_unitConversion+'.input' )
    cmds.connectAttr( footFheelPivot_unitConversion+'.output', RevFheelJoint[0]+'.rotateY' )
    # -- connect toe roll
    footFtoeRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFtoeRoll_unitConversion' )
    footFtoeRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=side+'footFtoeRoll_clamp' )
    cmds.setAttr( footFtoeRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footFtoeRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FtoeRoll', footFtoeRoll_clamp+'.inputR' )
    cmds.connectAttr( footFtoeRoll_clamp+'.outputR', footFtoeRoll_unitConversion+'.input' )
    cmds.connectAttr( footFtoeRoll_unitConversion+'.output', RevFtoeJoint[0]+'.rotateX' )
    # -- connect toe pivot
    footFtoePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFtoePivot_unitConversion' )
    cmds.setAttr( footFtoePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FtoePivot', footFtoePivot_unitConversion+'.input' )
    cmds.connectAttr( footFtoePivot_unitConversion+'.output', RevFtoeJoint[0]+'.rotateY' )
    
    # -- connect toe bend
    footFtoeBend_unitConversionIn = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFtoeBend_unitConversionIn' )
    footFtoeBend_unitConversionOut = cmds.shadingNode( 'unitConversion', asUtility=True, n=side+'footFtoeBend_unitConversionOut' )
    cmds.setAttr( footFtoeBend_unitConversionIn+'.conversionFactor', 57.29578 )
    cmds.setAttr( footFtoeBend_unitConversionOut+'.conversionFactor', 0.01745 )
    footFtoeBend_addDL = cmds.shadingNode( 'addDL', asUtility=True, n=side+'footFtoeBend_addDL' )
    cmds.disconnectAttr( FballJointIK+'.rotate', Fball_pairBlend+'.inRotate2' )
    cmds.connectAttr( FballJointIK+'.rotateZ', footFtoeBend_unitConversionIn+'.input' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+side+'FtoeBend', footFtoeBend_addDL+'.input1' )
    cmds.connectAttr( footFtoeBend_unitConversionIn+'.output', footFtoeBend_addDL+'.input2' )
    cmds.connectAttr( footFtoeBend_addDL+'.output', footFtoeBend_unitConversionOut+'.input' )
    cmds.connectAttr( FballJointIK+'.rotateX', Fball_pairBlend+'.inRotate2.inRotateX2' )
    cmds.connectAttr( FballJointIK+'.rotateY', Fball_pairBlend+'.inRotate2.inRotateY2' )
    cmds.connectAttr( footFtoeBend_unitConversionOut+'.output', Fball_pairBlend+'.inRotate2.inRotateZ2' )
    #cmds.connectAttr( footFtoeBend_unitConversion+'.output', RevFtoeBendLoc[0]+'.rotateX' )
    
    # -- add the space output nulls
    FankleSpaceOUT = denUt.den_makeGrp( nodeName=side+'FankleSpace_OUT' )
    FankleSpaceOUT = cmds.parent( FankleSpaceOUT, FankleJoint )
    LegSpaceOUTs += FankleSpaceOUT
    
    # -- parent in the reverse foot
    RevFheelJoint = cmds.parent( RevFheelJoint, FankleCtrl )
    
    
    if side == 'R_':
        cmds.setAttr( LegRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- cleanup temp crap
    cmds.delete( Leg1JuPivTmp )
    
    # -- list the joints for binding
    LegJxJoints += [ Scap02Joint, ShldJoint, ElbowJoint, FkneeJoint, FankleJoint ]
    LegCtrlsALL += [ ShldFKCtrl[0], ElbowFKCtrl[0], FankleFKCtrl[0], FkneeFKCtrl[0], FballFKCtrl[0], ElbowCtrl[0], Elbow2Ctrl[0], FkneeCtrl[0], FankleCtrl[0], FankleLiftCtrl[0], LegUtilCtrl[0], FootUtilCtrl[0] ]
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, JxJoints, CtrlsALL, GutsALL lists in order
    return LegRigGrp, LegSpaceINs, LegSpaceOUTs, LegJxJoints, LegCtrlsALL, LegGutsALL




# ---------------------------------------------------------------------------------------
# define Sluggy fin pivots creation command

def den_makeFKappendagePivs( side='L_', prefix='', name='FkaA', jointCount=3, radius=1.0, dpTime=0.01, size=1.1 ):
    #side='L_'
    #name='FkaA'
    #jointCount=3
    #radius=0.2
    
    FkaPiv = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    UpPiv = denUt.den_makeLoc( nodeName=side+prefix+name+'_upPiv', pos=(size*4, size*1, 0), radius=radius )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    denUt.den_ColorShape(3)
    UpPiv = cmds.parent( UpPiv, FkaPiv )[0]
    
    for i in range(jointCount+1):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        iPrev = str(i)
        iPrevPad = iPrev.rjust(2,'0')
        #print i, iStr, iStrPad, iPrevPad
        if (i == jointCount):
            piv = denUt.den_makeLoc( nodeName=side+prefix+name+iStrPad+'_Piv', pos=(size*(4+i), 0, size*(0-i)), radius=radius*0.5 )
        else:
            piv = denUt.den_makeLoc( nodeName=side+prefix+name+iStrPad+'_Piv', pos=(size*(4+i), 0, size*(0-i)), radius=radius )
        denUt.den_ColorShape(20)
        #denUt.den_ShowLocalAxis(1)
        if (i >= 1):
            pivPrev = cmds.ls( side+prefix+name+iPrevPad+'_Piv' )
            print( 'piv =', piv, pivPrev, iStrPad, iPrevPad )
            cmds.aimConstraint( piv, pivPrev, worldUpType='object', worldUpObject=UpPiv )
            cmds.select( pivPrev ) ; denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
            denUt.den_DiagPause( dpTime )
        cmds.parent( piv, FkaPiv )
        if (i == jointCount):
            cmds.rename( side+prefix+name+iStrPad+'_Piv', side+prefix+name+'End_Piv' )
            #print( side+prefix+name+iStrPad+'_Piv' )
        denUt.den_DiagPause( dpTime )
    
    
    if side == 'R_':
        cmds.setAttr( FkaPiv+'.scaleX', -1 )
    
    cmds.refresh()
    return FkaPiv



# ---------------------------------------------------------------------------------------
# define Sluggy fin rig creation command ( FK only )

def den_makeFKappendageRig( side='L_', prefix='', name='FkaA', jointCount=3, radius=1.0, ctrlRadius=2.0, secondaryAxisOrient='yup', spikeAxis='+Y', dpTime=0.01 ):
    #side='L_'
    #name='FkaA'
    #jointCount=3
    #radius=0.5
    #secondaryAxisOrient='zup'
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    cmds.refresh()
        
    FkaRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp', pos=(0,0,0) )
    FkaSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'Space_IN', pos=(0,0,0) )
    FkaSpaceIN = cmds.parent( FkaSpaceIN, FkaRigGrp )
    FkaJxJoints = []
    
    #Set variables to hold names of all the controls and guts
    FkaCtrlsALL = []
    FkaGutsALL = []
    
    last_i = 0
    for i in range(jointCount+1):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        #iEnd = str(i)
        #iEndPad = iEnd.rjust(2,'0')
        print( i, iStr, iStrPad )
        
        if (i == jointCount):
            FkaPiv = cmds.ls( side+prefix+name+'End_Piv' )
        else:
            FkaPiv = cmds.ls( side+prefix+name+iStrPad+'_Piv' )
        FkaPos = cmds.xform( FkaPiv, ws=True, q=True, t=True )
        
        FkaJxJoint = denUt.den_makeJoint( nodeName=side+prefix+name+iStrPad+'_Jnt', pos=(FkaPos), radius=radius, leaveSelected=True )
        FkaJxJoint = cmds.ls( FkaJxJoint )
        print( FkaPiv, FkaJxJoint )
        if (i == jointCount):
            FkaJxJoint = cmds.rename( FkaJxJoint, side+prefix+name+'_end' )
            FkaJxJoint = cmds.ls( FkaJxJoint )
            cmds.setAttr( FkaJxJoint[0]+'.radius', radius*0.5 )
            print( FkaJxJoint )
        else:
            FkaJxJointParent = cmds.listRelatives( FkaJxJoint, parent=True, fullPath=True )
            FkaJxJoint = cmds.parent( FkaJxJoint, FkaPiv )
            cmds.joint( FkaJxJoint, e=True, oj='none', zso=True )
            FkaJxJoint = cmds.parent( FkaJxJoint, FkaJxJointParent )
            FkaJxJoints += FkaJxJoint
        last_i += 1
        denUt.den_DiagPause( dpTime )
    last = str(last_i).rjust(2,'0')
    print( last )
    
    for i in range(jointCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        iEnd = str(i)
        iEndPad = iEnd.rjust(2,'0')
        FkaPos = cmds.xform( side+prefix+name+iStrPad+'_Piv', ws=True, q=True, t=True )
        FkaJxJoint = FkaJxJoints[i]
        FkaJxJointParent = cmds.listRelatives( FkaJxJoint, parent=True, fullPath=True )
        
        FkaCtrl = denUt.den_MakeSpike(nodeName=side+prefix+name+iStrPad+'_Ctrl',pos=(0,0,0),radius=ctrlRadius,doT=False,axis=spikeAxis)
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        FkaCtrl = cmds.parent( FkaCtrl, FkaJxJoint, relative=True )
        FkaCtrl = cmds.parent( FkaCtrl, FkaJxJointParent )
        FkaCtrl = denUt.den_AddZeroNull()
        FkaCtrlsALL += FkaCtrl
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_ColorShapeRGB(rgb=(1,0,1)); denUt.den_DiagPause( dpTime )
        cmds.connectAttr( FkaCtrl[0]+'.rotate', FkaJxJoint+'.rotate' )
        #cmds.setAttr( FkaJxJoint+'.displayLocalAxis', 1 )
        #print FkaJxJoint
        denUt.den_DiagPause( dpTime )
    
    print( FkaJxJoints )
    cmds.refresh()
    if side == 'R_':
        cmds.setAttr( FkaRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    #return FkaRigGrp, FkaJxJoints
    return FkaRigGrp, FkaSpaceIN, [], FkaJxJoints, FkaCtrlsALL, FkaGutsALL


def den_makeCrocArmPivs( side='L_', prefix='', name='Arm', radius=2.0, elbowDist=20.0, footUpDist=10.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #side='L_'
    #name='Arm'
    #radius=2.0
    #elbowDist=20.0
    #---------------------
    size=size*0.01
    foo = side+prefix+name
    # -- makes arm pivots that can then be re-positioned to match a particular character
    ArmPivGrp = denUt.den_makeGrp( nodeName=foo+'Piv_Grp', pos=(0,0,0) )
    denUt.den_makeLoc( nodeName='Clav_Piv', pos=(size*5, size*150, 0), radius=radius ); denUt.den_DiagPause( 0.02 )
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Shld_Piv', pos=(size*20, size*150, -size*5), radius=radius ); denUt.den_DiagPause( 0.02 )
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Elbow_Piv', pos=(size*30, size*120, -size*5), radius=radius ); denUt.den_DiagPause( 0.02 )
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Wrist_Piv', pos=(size*40, size*95, size*5), radius=radius*0.5 ); denUt.den_DiagPause( 0.02 )
    denUt.den_ColorShape(2)
    denUt.den_makeLoc( nodeName='Scap01_Piv', pos=(-size*5, size*145, size*5), radius=radius*0.7 ); denUt.den_DiagPause( 0.02 )
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Scap02_Piv', pos=(size*5, size*150, -size*10), radius=radius*0.7 ); denUt.den_DiagPause( 0.02 )
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ankle_Piv', pos=(size*12.1, size*12.8, -size*7), radius=radius ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ball_Piv', pos=(size*12.1, size*3.5, size*4.7), radius=radius ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeGrp ( 'BallSole_Piv', pos=(size*12.1, 0, size*4.7) ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_makeLoc( nodeName='Toe_Piv', pos=(size*12.1, 0, size*15.3), radius=radius ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    #denUt.den_makeLoc( nodeName='Heel_Piv', pos=(12.1, 1, -12), radius=radius/2 ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(20)
    cmds.curve( name='Heel_Piv', degree=1, p=[( -1,0,0 ),( 1,0,0 ),( 1,0,2 ),( -1,0,2 ),( -1,0,0 )] ); cmds.move(size*12.1, 0, -size*12,'Heel_Piv', r=True); cmds.scale(2*radius,0,3.5*radius,'Heel_Piv.cv[*]'); cmds.setAttr( 'Heel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleLF_Piv', pos=(size*18.4, 0, size*4.1), radius=radius/2 ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleLB_Piv', pos=(size*16.1, 0, -size*9.4), radius=radius/2 ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleRF_Piv', pos=(size*7.8, 0, size*7.8), radius=radius/2 ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleRB_Piv', pos=(size*8.6, 0, -size*9), radius=radius/2 ); denUt.den_DiagPause( 0.02 ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    # -- connect the y translate attrs to the heel to maintain a flat sole, then lock attrs
    cmds.connectAttr( 'Ball_Piv.translateX', 'BallSole_Piv.translateX' )
    cmds.connectAttr( 'Ball_Piv.translateZ', 'BallSole_Piv.translateZ' )
    cmds.connectAttr( 'Toe_Piv.translateY', 'BallSole_Piv.translateY' )
    #cmds.connectAttr( 'Toe_Piv.translateY', 'Heel_Piv.translateY' )
    #cmds.connectAttr( 'Toe_Piv.translateY', 'SoleLF_Piv.translateY' )
    #cmds.connectAttr( 'Toe_Piv.translateY', 'SoleRF_Piv.translateY' )
    #cmds.connectAttr( 'Toe_Piv.translateY', 'SoleLB_Piv.translateY' )
    #cmds.connectAttr( 'Toe_Piv.translateY', 'SoleRB_Piv.translateY' )
    
    denUt.den_makeLoc( nodeName='ElbowMid_Loc', radius=radius/2 )
    denUt.den_ColorShape(2)
    
    denUt.den_makeLoc( nodeName='ElbowPole_Loc', pos=(0, elbowDist, 0), radius=radius )
    denUt.den_ColorShape(9)
    cmds.parent( 'ElbowPole_Loc','ElbowMid_Loc', relative=True )
    
    # make ElbowMid_Loc float between Shld and Wrist
    ElbowMidLocPtCon = cmds.pointConstraint( 'Shld_Piv','Wrist_Piv','ElbowMid_Loc', mo=False )[0]
    ElbowMidLocAimCon = cmds.aimConstraint( 'Wrist_Piv','ElbowMid_Loc', worldUpType='object', worldUpObject='Elbow_Piv', mo=False )[0]
    
    # aim Shld_Piv at elbow, use wrist to keep up on the triangle plane
    ShldPivAimCon = cmds.aimConstraint( 'Elbow_Piv','Shld_Piv', worldUpType='object', worldUpObject='Wrist_Piv', mo=False )[0]
    
    # aim Scap01_Piv at scap02, use shoulder to keep up on the triangle plane
    ScapPivAimCon = cmds.aimConstraint( 'Scap02_Piv','Scap01_Piv', worldUpType='object', worldUpObject='Shld_Piv', mo=False )[0]
    
    # ain Wrist_Piv at the elbow, use L_ArmMid_Loc to keep up on the triangle plane, use aimvector to flip
    WristMidLocAimCon = cmds.aimConstraint( 'Elbow_Piv','Wrist_Piv', worldUpType='object', worldUpObject='ElbowMid_Loc', aimVector=(-1,0,0), mo=False )[0]
    
    # - make a locator that shows the up of the foot based on foot pivot locations to aid pivot placement
    denUt.den_makeLoc( nodeName='FootUp_Piv', radius=radius/2, pos=(0, footUpDist, footUpDist) ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(14)
    cmds.parent( 'FootUp_Piv', 'Heel_Piv', relative=True )

    AnklePivAimCon = cmds.aimConstraint( 'Ball_Piv','Ankle_Piv', worldUpType='object', worldUpObject='FootUp_Piv', mo=False  )[0]
    
    SoleLFPivAimCon = cmds.aimConstraint( 'SoleLB_Piv','SoleLF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    
    SoleRFPivAimCon = cmds.aimConstraint( 'SoleRB_Piv','SoleRF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    
    BallPivAimCon = cmds.aimConstraint( 'Toe_Piv','Ball_Piv', aimVector=(0,0,1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]

    ToePivAimCon = cmds.aimConstraint( 'Ball_Piv','Toe_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    
    WristPtCon = cmds.pointConstraint( 'Ankle_Piv','Wrist_Piv', mo=False )[0]
    #cmds.aimConstraint( 'Toe_Piv', 'Heel_Piv', aimVector=(0,0,1), upVector=(0,1,0), worldUpType="vector", worldUpVector=(0,1,0) )


    # - lock down channels the user is not supposed to touch
    cmds.select( ArmPivGrp ); denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    cmds.select( 'Clav_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Shld_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Elbow_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Wrist_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Scap01_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Scap02_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ankle_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ball_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'BallSole_Piv' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Toe_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Heel_Piv' ); denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 1 )
    cmds.select( 'ElbowMid_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'KneeMid2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'ElbowPole_Loc' ); denUt.den_Lock(  0,0,1 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'KneePole2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FootUp_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleLF_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleRF_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleLB_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleRB_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.parent( 'Heel_Piv','Clav_Piv','Shld_Piv','Elbow_Piv','Wrist_Piv','Scap01_Piv','Scap02_Piv','ElbowMid_Loc', ArmPivGrp )
    cmds.parent( 'Ankle_Piv', 'Ball_Piv', 'BallSole_Piv', 'Toe_Piv', 'SoleLF_Piv', 'SoleLB_Piv', 'SoleRF_Piv', 'SoleRB_Piv', 'Heel_Piv' )
    
    # -- put the L_ back into the node names
    cmds.rename( 'Clav_Piv', foo+'Clav_Piv' )
    cmds.rename( 'Shld_Piv', foo+'Shld_Piv' )
    cmds.rename( 'Elbow_Piv', foo+'Elbow_Piv' )
    cmds.rename( 'Scap01_Piv', foo+'Scap01_Piv' )
    cmds.rename( 'Scap02_Piv', foo+'Scap02_Piv' )
    cmds.rename( 'Wrist_Piv', foo+'Wrist_Piv' )
    cmds.rename( 'Ankle_Piv', foo+'Ankle_Piv' )
    cmds.rename( 'Ball_Piv', foo+'Ball_Piv' )
    cmds.rename( 'BallSole_Piv', foo+'BallSole_Piv' )
    cmds.rename( 'Toe_Piv', foo+'Toe_Piv' )
    cmds.rename( 'Heel_Piv', foo+'Heel_Piv' )
    cmds.rename( 'ElbowMid_Loc', foo+'ElbowMid_Loc' )
    #cmds.rename( 'KneeMid2_Loc', foo+'KneeMid2_Loc' ) ## - new
    cmds.rename( 'ElbowPole_Loc', foo+'ElbowPole_Loc' )
    #cmds.rename( 'KneePole2_Loc', foo+'KneePole2_Loc' ) ## - new
    cmds.rename( 'FootUp_Piv', foo+'FootUp_Piv' )
    cmds.rename( 'SoleLF_Piv', foo+'SoleLF_Piv' )
    cmds.rename( 'SoleRF_Piv', foo+'SoleRF_Piv' )
    cmds.rename( 'SoleLB_Piv', foo+'SoleLB_Piv' )
    cmds.rename( 'SoleRB_Piv', foo+'SoleRB_Piv' )
    cmds.rename( ElbowMidLocPtCon, side+ElbowMidLocPtCon )
    cmds.rename( ElbowMidLocAimCon, side+ElbowMidLocAimCon )
    #cmds.rename( KneeMidLoc2PtCon, side+KneeMidLoc2PtCon )
    #cmds.rename( KneeMidLoc2AimCon, side+KneeMidLoc2AimCon )
    #cmds.rename( KneePole2LocPtCon, side+KneePole2LocPtCon )
    cmds.rename( ShldPivAimCon, side+ShldPivAimCon )
    cmds.rename( ScapPivAimCon, side+ScapPivAimCon )
    cmds.rename( WristMidLocAimCon, side+WristMidLocAimCon )
    cmds.rename( AnklePivAimCon, side+AnklePivAimCon )
    cmds.rename( SoleLFPivAimCon, side+SoleLFPivAimCon )
    cmds.rename( SoleRFPivAimCon, side+SoleRFPivAimCon )
    cmds.rename( ToePivAimCon, side+ToePivAimCon )
    #cmds.rename( HockLocAimCon, side+HockLocAimCon )
    #cmds.rename( HockLocPtCon, side+HockLocPtCon )
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( seconds=0.1 ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( ArmPivGrp+'.scaleX', -1 )
    
    return ArmPivGrp



def den_makeCrocArmRig( side='L_', prefix='', name='Arm', radius=2.0, ctrlRadius=10.0, displayLocalAxis=False ):
    #--------------------- testing variables    
    #side = 'L_'
    #name='Arm'
    #radius=4.0
    #ctrlRadius=20.0
    #displayLocalAxis=True
    #---------------------
    foo = side+prefix+name
    
    # -- if doing right side, change the color and flip the pivots to the left for good/easy mirroring
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( foo+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    denUt.den_DiagPause( seconds=0.1 ) # quick refresh to let scene re-evaluate
    
    
    # -- make the Arm rig top group
    ArmRigGrp = denUt.den_makeGrp( nodeName=foo+'_Grp', pos=(0,0,0) )
    
    # -- set up the return variables
    ArmSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    ArmSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    ArmBindJoints = [] #Set list variable to hold names of all the _Jnt Bind joints
    ArmCtrlsALL = [] #Set list variable to hold names of all the controls
    ArmGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Arm SpaceINs
    HeadSpaceIN = denUt.den_makeGrp( nodeName=foo+'Head_SpaceIN', pos=(0,0,0) )
    HeadSpaceIN = cmds.parent( HeadSpaceIN, ArmRigGrp )[0]
    ChestSpaceIN = denUt.den_makeGrp( nodeName=foo+'Chest_SpaceIN', pos=(0,0,0) )
    ChestSpaceIN = cmds.parent( ChestSpaceIN, ArmRigGrp )[0]
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=foo+'Pelvis_SpaceIN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, ArmRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=foo+'Cog_SpaceIN', pos=(0,0,0) )
    CogSpaceIN = cmds.parent( CogSpaceIN, ArmRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=foo+'All_SpaceIN', pos=(0,0,0) )
    AllSpaceIN = cmds.parent( AllSpaceIN, ArmRigGrp )[0]
    # add all the SpaceINs to the list
    ArmSpaceINs += [ HeadSpaceIN, ChestSpaceIN, PelvisSpaceIN, CogSpaceIN, AllSpaceIN ]
    
    # -- make groups to hold the skeleton and the controls
    ArmSkelGrp = denUt.den_makeGrp( nodeName=foo+'Skel_Grp', pos=(0,0,0) )
    ArmSkelGrp = cmds.parent( ArmSkelGrp, ChestSpaceIN )
    ArmCtrlGrp = denUt.den_makeGrp( nodeName=foo+'Ctrl_Grp', pos=(0,0,0) )
    ArmCtrlGrp = cmds.parent( ArmCtrlGrp, ChestSpaceIN )
    
    # -- make Wrist control space switcher
    WristCtrlSpace = denUt.den_makeGrp( nodeName=foo+'WristCtrl_Space', pos=(0,0,0) )
    WristCtrlSpace = cmds.parent( WristCtrlSpace, ArmCtrlGrp )
    WristCtrlSpaceConstraint = cmds.parentConstraint( HeadSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( ChestSpaceIN, WristCtrlSpace, weight=1 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( PelvisSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( CogSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( AllSpaceIN, WristCtrlSpace, weight=0 )
    
        
    # -- set variables for pivot positions
    
    ClavPos = cmds.xform( foo+'Clav_Piv', ws=True, q=True, t=True )
    ShldPos = cmds.xform( foo+'Shld_Piv', ws=True, q=True, t=True )
    ElbowPos = cmds.xform( foo+'Elbow_Piv', ws=True, q=True, t=True )
    WristPos = cmds.xform( foo+'Wrist_Piv', ws=True, q=True, t=True )
    ElbowPolePos = cmds.xform( foo+'ElbowPole_Loc', ws=True, q=True, t=True )
    Scap01Pos = cmds.xform( foo+'Scap01_Piv', ws=True, q=True, t=True )
    Scap02Pos = cmds.xform( foo+'Scap02_Piv', ws=True, q=True, t=True )
    AnklePos = cmds.xform( foo+'Ankle_Piv', ws=True, q=True, t=True )
    BallPos = cmds.xform( foo+'Ball_Piv', ws=True, q=True, t=True )
    ToePos = cmds.xform( foo+'Toe_Piv', ws=True, q=True, t=True )
    HeelPos = cmds.xform( foo+'Heel_Piv', ws=True, q=True, t=True )
    SoleLFPos = cmds.xform( foo+'SoleLF_Piv', ws=True, q=True, t=True )
    SoleLBPos = cmds.xform( foo+'SoleLB_Piv', ws=True, q=True, t=True )
    SoleRFPos = cmds.xform( foo+'SoleRF_Piv', ws=True, q=True, t=True )
    SoleRBPos = cmds.xform( foo+'SoleLB_Piv', ws=True, q=True, t=True )
    BallSolePos = [ BallPos[0], ToePos[1], BallPos[2] ]
    
    # -- make the joints
    cmds.select( clear=True )
    ClavJoint = cmds.joint( n=foo+'Clav_Jnt', p=(ClavPos), radius=radius ); denUt.den_DiagPause( 0.02 )
    ClavJoint = cmds.parent( ClavJoint, ArmSkelGrp )[0]
    ShldJoint = cmds.joint( n=foo+'Shld_Jnt', p=(ShldPos), radius=radius ); denUt.den_DiagPause( 0.02 )
    ElbowJoint = cmds.joint( n=foo+'Elbow_Jnt', p=(ElbowPos), radius=radius ); denUt.den_DiagPause( 0.02 )
    WristJoint = cmds.joint( n=foo+'Wrist_Jnt', p=(WristPos), radius=radius ); denUt.den_DiagPause( 0.02 )
    BallJoint = cmds.joint( n=foo+'Ball_Jnt', p=(BallPos), radius=radius ); denUt.den_DiagPause( 0.02 )
    ToeJoint = cmds.joint( n=foo+'Toe_Jx', p=(ToePos), radius=radius ); denUt.den_DiagPause( 0.02 )
    
    if ( displayLocalAxis ):
        cmds.setAttr( ClavJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ShldJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ElbowJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( WristJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( BallJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ToeJoint+'.displayLocalAxis', 1 )
    
    cmds.select( clear=True )
    Scap01Joint = cmds.joint( n=foo+'Scap01_Jx', p=(Scap01Pos), radius=radius ); denUt.den_DiagPause( 0.02 )
    Scap01Joint = cmds.parent( Scap01Joint, ArmSkelGrp )[0]
    Scap02Joint = cmds.joint( n=foo+'Scap02_Jnt', p=(Scap02Pos), radius=radius ); denUt.den_DiagPause( 0.02 )
    Scap03Joint = cmds.joint( n=foo+'Scap02_end', p=(ShldPos), radius=radius ); denUt.den_DiagPause( 0.02 )
    
    if ( displayLocalAxis ):
        cmds.setAttr( Scap01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Scap02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Scap03Joint+'.displayLocalAxis', 1 )
    
    # -- make the foot joints
    cmds.select( clear=True )
    
    
    # -- orient the joints
    
    cmds.select( clear=True )
    cmds.joint( ClavJoint, e=True, oj='xyz', secondaryAxisOrient='yup', zso=True )
    
    #cmds.select( clear=True )
    #cmds.joint( ElbowJoint, e=True, oj='xyz', zso=True )
    #cmds.joint( WristJoint, e=True, oj='xyz', zso=True )
    #cmds.joint( BallJoint, e=True, oj='xyz', zso=True )
    cmds.joint( ElbowJoint, e=True, oj='xzy', secondaryAxisOrient='xdown', aos=True, ch=False, zso=True )
    WristJoint = cmds.parent( WristJoint, foo+'Ankle_Piv' ) # -- temp reparent wrist under ankle pivot to make it align with foot rig
    cmds.joint( WristJoint, e=True, oj='none', zso=True )
    WristJoint = cmds.parent( WristJoint, ElbowJoint )[0] # -- put wrist back
    cmds.joint( BallJoint, e=True, oj='xzy', secondaryAxisOrient='xdown', aos=True, ch=False, zso=True )

    cmds.joint( ToeJoint, e=True, oj='none', zso=True )
    ShldJoint = cmds.parent( ShldJoint, foo+'Shld_Piv' ) # -- temp reparent shoulder under planar space
    cmds.joint( ShldJoint, e=True, oj='none', zso=True ) # -- orient joint
    ShldJoint = cmds.parent( ShldJoint, ClavJoint )[0] # -- put shoulder back under clav
    
    #cmds.select( clear=True )
    #cmds.joint( Scap02Joint, e=True, oj='xyz', zso=True )
    cmds.joint( Scap02Joint, e=True, oj='xzy', secondaryAxisOrient='ydown', aos=True, ch=False, zso=True )
    cmds.joint( Scap03Joint, e=True, oj='none', zso=True )
    Scap01Joint = cmds.parent( Scap01Joint, foo+'Scap01_Piv' ) # -- temp reparent scap under planar space
    cmds.joint( Scap01Joint, e=True, oj='none', zso=True )
    Scap01Joint = cmds.parent( Scap01Joint, ArmSkelGrp )[0] # -- put scap back
    
    
    # -- duplicate the arm to make the FK and IK arm bones
    ShldJointIK = cmds.duplicate (ShldJoint, name=foo+'Shld_IK' )[0]
    ElbowJointIK = cmds.rename (ShldJointIK+'|'+foo+'Elbow_Jnt', foo+'Elbow_IK' )
    WristJointIK = cmds.rename (ElbowJointIK+'|'+foo+'Wrist_Jnt', foo+'Wrist_IK' )
    BallJointIK = cmds.rename (WristJointIK+'|'+foo+'Ball_Jnt', foo+'Ball_IK' )
    ToeJointIK = cmds.rename (BallJointIK+'|'+foo+'Toe_Jx', foo+'Toe_IK' )
    #print ShldJointIK, '----', ElbowJointIK, '----', WristJointIK
    ShldJointFK = cmds.duplicate (ShldJoint, name=foo+'Shld_FK' )[0]
    ElbowJointFK = cmds.rename (ShldJointFK+'|'+foo+'Elbow_Jnt', foo+'Elbow_FK' )
    WristJointFK = cmds.rename (ElbowJointFK+'|'+foo+'Wrist_Jnt', foo+'Wrist_FK' )
    BallJointFK = cmds.rename (WristJointFK+'|'+foo+'Ball_Jnt', foo+'Ball_FK' )
    ToeJointFK = cmds.rename (BallJointFK+'|'+foo+'Toe_Jx', foo+'Toe_FK' )
    #print ShldJointFK, '----', ElbowJointFK, '----', WristJointFK
    
    
    
    # -- make the controls and zero nulls
    
    # -- Shoulder IK Control
    ShldCtrl = denUt.den_MakeCube( nodeName=foo+'Shld_Ctrl', pos=(0,0,0) ,radius=0.8*ctrlRadius, doT=False)
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ShldPos )
    ShldCtrl = cmds.parent( ShldCtrl, ArmCtrlGrp )
    ShldCtrl = denUt.den_AddZeroNull()
    ShldCtrlZero = cmds.listRelatives( ShldCtrl, parent=True, fullPath=True )
    ArmCtrlsALL += ShldCtrl # add to the controls list
    
    # -- Shoulder FK Control
    ShldFKCtrl = denUt.den_MakeSpike( nodeName=foo+'ShldFK_Ctrl', pos=(0,0,0) ,radius=ctrlRadius, doT=False, axis='-Z' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ShldFKCtrl = cmds.parent( ShldFKCtrl, ShldJointFK, relative=True )
    ShldFKCtrl = cmds.parent( ShldFKCtrl, ArmCtrlGrp )
    ShldFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    ShldFKCtrlZero = cmds.listRelatives( ShldFKCtrl, parent=True, fullPath=True )
    cmds.connectAttr( ShldFKCtrl[0]+'.rotate', ShldJointFK+'.rotate' )
    cmds.parentConstraint( ClavJoint, ShldFKCtrlZero, mo=True )
    ArmCtrlsALL += ShldFKCtrl # add to the controls list
    
    # -- Arm Utility Control
    ArmUtilCtrl = denUt.den_MakeGear( nodeName=foo+'Util_Ctrl', pos=(ctrlRadius*0.8,ctrlRadius*0.8,0), radius=ctrlRadius*0.3, doT=False, Plane='XY' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ArmUtilCtrl = cmds.parent( ArmUtilCtrl, ShldCtrl, relative=True )
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.addAttr( ArmUtilCtrl, longName=foo+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+foo+'_FK_IK', lock=False, keyable=True )
    ArmCtrlsALL += ArmUtilCtrl # add to the controls list
    
    # -- Elbow IK Controls
    ElbowCtrl = denUt.den_MakePole( nodeName=foo+'Elbow_Ctrl', pos=(0,0,0) , radius=ctrlRadius*0.4, doT=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ElbowPolePos )
    ElbowCtrl = cmds.parent( ElbowCtrl, ArmCtrlGrp )
    ElbowCtrl = denUt.den_AddZeroNull()
    ArmCtrlsALL += ElbowCtrl # add to the controls list
    
    # -- Elbow FK Controls
    ElbowFKCtrl = denUt.den_MakeArrowR( nodeName=foo+'ElbowFK_Ctrl', pos=(0,-ctrlRadius,0), radius=ctrlRadius*0.4, doT=True, axis='-Y', flip=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ElbowJointFK, relative=True )
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ShldFKCtrl )
    ElbowFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( ElbowFKCtrl[0]+'.rotate', ElbowJointFK+'.rotate' )
    ArmCtrlsALL += ElbowFKCtrl # add to the controls list
    
    # -- Wrist IK Controls
    WristCtrl = denUt.den_MakeBall( nodeName=foo+'Wrist_Ctrl', pos=(0,0,0), radius=ctrlRadius*0.7, doT=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=WristPos )
    WristCtrl = cmds.parent( WristCtrl, WristCtrlSpace )
    WristCtrl = denUt.den_AddZeroNull()
    WristCtrlZero = cmds.listRelatives( WristCtrl, parent=True, fullPath=True )
    ArmCtrlsALL += WristCtrl # add to the controls list
    
    # -- Wrist FK Controls
    WristFKCtrl = denUt.den_MakeSpike( nodeName=foo+'WristFK_Ctrl', pos=(0,0,0), radius=ctrlRadius, doT=False, axis='-Z' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    WristFKCtrl = cmds.parent( WristFKCtrl, WristJointFK, relative=True )
    WristFKCtrl = cmds.parent( WristFKCtrl, ElbowFKCtrl )
    WristFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.setAttr( WristFKCtrl[0]+'.rotateOrder', 1 )
    WristFKCtrlZero = cmds.listRelatives( WristFKCtrl, parent=True, fullPath=True )
    cmds.connectAttr( WristFKCtrl[0]+'.rotate', WristJointFK+'.rotate' )
    ArmCtrlsALL += WristFKCtrl # add to the controls list
    
    # -- connect up the IK Wrist control space switcher
    cmds.addAttr( ArmUtilCtrl, longName=foo+'HeadSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+foo+'HeadSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'HeadSpace', WristCtrlSpaceConstraint[0]+'.'+foo+'Head_SpaceINW0' )
    cmds.addAttr( ArmUtilCtrl, longName=foo+'ChestSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+foo+'ChestSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'ChestSpace', WristCtrlSpaceConstraint[0]+'.'+foo+'Chest_SpaceINW1' )
    cmds.addAttr( ArmUtilCtrl, longName=foo+'PelvisSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+foo+'PelvisSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'PelvisSpace', WristCtrlSpaceConstraint[0]+'.'+foo+'Pelvis_SpaceINW2' )
    cmds.addAttr( ArmUtilCtrl, longName=foo+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+foo+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'CogSpace', WristCtrlSpaceConstraint[0]+'.'+foo+'Cog_SpaceINW3' )
    cmds.addAttr( ArmUtilCtrl, longName=foo+'AllSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+foo+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'AllSpace', WristCtrlSpaceConstraint[0]+'.'+foo+'All_SpaceINW4' )
    
    #print AnkleCtrlZero
    BallFKCtrl = denUt.den_MakeSpike(nodeName=foo+'BallFK_Ctrl', radius=ctrlRadius, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    BallFKCtrl = cmds.parent( BallFKCtrl, BallJointFK, relative=True )
    BallFKCtrl = cmds.parent( BallFKCtrl, WristFKCtrl )
    BallFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( BallFKCtrl[0]+'.rotate', BallJointFK+'.rotate' )
    BallFKCtrlZero = cmds.listRelatives( BallFKCtrl, parent=True, fullPath=True )[0]
    
    # -- Foot Utility
    FootUtilCtrl = denUt.den_MakeGear( nodeName=foo+'FootUtil_Ctrl', pos=(ctrlRadius*0.8,ctrlRadius*0.8,0), radius=ctrlRadius*0.3, Plane='XY')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    FootUtilCtrl = cmds.parent( FootUtilCtrl, WristCtrl, relative=True )
    
    cmds.addAttr( FootUtilCtrl, longName=foo+'FootRock', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'FootRock', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'FootRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'FootRoll', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'FootPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'FootPivot', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'FootTwist', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'FootTwist', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'HeelPivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'HeelPivot', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'ToeRoll', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'ToeRoll', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'ToePivot', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'ToePivot', lock=False, keyable=True )
    cmds.addAttr( FootUtilCtrl, longName=foo+'ToeBend', defaultValue=0.0, minValue=-90.0, maxValue=90.0 )
    cmds.setAttr( FootUtilCtrl[0]+'.'+foo+'ToeBend', lock=False, keyable=True )
    
    # -- set up Arm FK_IK blending
    Shld_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=foo+'Shld_ikFk_pairBlend' )
    cmds.setAttr( Shld_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ShldJointFK+'.rotate', Shld_pairBlend+'.inRotate1' )
    cmds.connectAttr( ShldJointIK+'.rotate', Shld_pairBlend+'.inRotate2' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'_FK_IK', Shld_pairBlend+'.weight' )
    cmds.connectAttr( Shld_pairBlend+'.outRotate', ShldJoint+'.rotate' )
    
    Elbow_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=foo+'Elbow_ikFk_pairBlend' )
    cmds.setAttr( Elbow_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ElbowJointFK+'.rotate', Elbow_pairBlend+'.inRotate1' )
    cmds.connectAttr( ElbowJointIK+'.rotate', Elbow_pairBlend+'.inRotate2' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'_FK_IK', Elbow_pairBlend+'.weight' )
    cmds.connectAttr( Elbow_pairBlend+'.outRotate', ElbowJoint+'.rotate' )
    
    Wrist_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=foo+'Wrist_ikFk_pairBlend' )
    cmds.setAttr( Wrist_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( WristJointFK+'.rotate', Wrist_pairBlend+'.inRotate1' )
    cmds.connectAttr( WristJointIK+'.rotate', Wrist_pairBlend+'.inRotate2' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'_FK_IK', Wrist_pairBlend+'.weight' )
    cmds.connectAttr( Wrist_pairBlend+'.outRotate', WristJoint+'.rotate' )
    
    Ball_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=foo+'Ball_ikFk_pairBlend' )
    cmds.setAttr( Ball_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( BallJointFK+'.rotate', Ball_pairBlend+'.inRotate1' )
    cmds.connectAttr( BallJointIK+'.rotate', Ball_pairBlend+'.inRotate2' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+foo+'_FK_IK', Ball_pairBlend+'.weight' )
    cmds.connectAttr( Ball_pairBlend+'.outRotate', BallJoint+'.rotate' )
    
    # -- make the reverse foot
    
    footPivs = [ 'Heel_Piv', 'BallSole_Piv', 'SoleLF_Piv', 'SoleRF_Piv', 'Toe_Piv', 'Ball_Piv', 'Ankle_Piv' ]
    footJnts = []
    for number,footPiv in enumerate(footPivs):
        prevNum = number-1
        nameRoot = footPiv.replace('_Piv','')
        #print 'nameRoot', nameRoot, number
        footJnt = cmds.joint( n=foo+nameRoot+'Rev_Jx', radius=radius*0.7 )
        footPiv = foo+footPivs[number]
        footJnt = cmds.parent( footJnt, footPiv, relative=True )
        cmds.joint( footJnt, e=True, oj='none', zso=True, radius=radius*0.7 ); denUt.den_DiagPause( 0.02 )
        if number != 0:
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
    
    
    # -- Wrist Squish
    WristSquishCtrl = denUt.den_MakeCube( nodeName=side+prefix+'WristSquish_Ctrl', pos=(ctrlRadius*0.5,ctrlRadius*1.0,0), radius=ctrlRadius*0.3, doT=True )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=WristPos )
    WristSquishCtrl = cmds.parent( WristSquishCtrl, RevAnkleJoint )
    WristSquishCtrl = denUt.den_AddZeroNull()
    WristSquishCtrlZero = cmds.listRelatives( WristSquishCtrl, parent=True, fullPath=True )[0]

    # -- make the ik handles
    #print( ShldJointIK, WristJointIK, ClavJoint, ShldJoint, Scap01Joint, Scap03Joint )
    ArmIKhandle = cmds.ikHandle( startJoint=ShldJointIK, endEffector=WristJointIK, solver='ikRPsolver', setupForRPsolver=True, name=ShldJointIK.replace('IK','Ikh') )
    #print( ArmIKhandle )
    cmds.rename( ArmIKhandle[1], ArmIKhandle[0].replace('Ikh','Eff') )
    ArmIKhandle = cmds.parent( ArmIKhandle[0], WristSquishCtrl )
    cmds.poleVectorConstraint( ElbowCtrl, ArmIKhandle )
    
    ClavIKhandle = cmds.ikHandle( startJoint=ClavJoint, endEffector=ShldJoint, solver='ikSCsolver', name=ClavJoint.replace('Jnt','Ikh') )
    #print( ClavIKhandle )
    cmds.rename( ClavIKhandle[1], ClavIKhandle[0].replace('Ikh','Eff') )
    ClavIKhandle = cmds.parent( ClavIKhandle[0], ShldCtrl )
    
    ScapIKhandle = cmds.ikHandle( startJoint=Scap01Joint, endEffector=Scap03Joint, solver='ikSCsolver', name=Scap01Joint.replace('Jx','Ikh') )
    #print( ScapIKhandle )
    cmds.rename( ScapIKhandle[1], ScapIKhandle[0].replace('Ikh','Eff') )
    ScapIKhandle = cmds.parent( ScapIKhandle[0], ClavJoint )
    
    cmds.select( WristJointIK, BallJointIK )
    BallIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    BallIKhandle = cmds.parent( BallIKhandle, RevBallJoint )[0]
    cmds.select( BallJointIK, ToeJointIK )
    ToeIKhandle = denUt.den_AddIKHandle( handleType='ikSCsolver' )
    ToeIKhandle = cmds.parent( ToeIKhandle, RevToeJoint )[0]
    
    # -- add utility nodes and connect attrs for foot roll
    footHeelRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footHeelRoll_unitConversion' )
    footHeelRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=foo+'footHeelRoll_clamp' )
    cmds.setAttr( footHeelRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footHeelRoll_clamp+'.minR', -180 )
    footBallRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footBallRoll_unitConversion' )
    footBallRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=foo+'footBallRoll_clamp' )
    cmds.setAttr( footBallRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footBallRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'FootRoll', footHeelRoll_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'FootRoll', footBallRoll_clamp+'.inputR' )
    cmds.connectAttr( footHeelRoll_clamp+'.outputR', footHeelRoll_unitConversion+'.input' )
    cmds.connectAttr( footBallRoll_clamp+'.outputR', footBallRoll_unitConversion+'.input' )
    cmds.connectAttr( footHeelRoll_unitConversion+'.output', RevHeelJoint[0]+'.rotateX' )
    cmds.connectAttr( footBallRoll_unitConversion+'.output', RevBallJoint[0]+'.rotateX' )
    
    # -- add utility nodes and connect attrs for foot rock
    footSoleLFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footSoleLFRock_unitConversion' )
    footSoleLFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=foo+'footSoleLFRock_clamp' )
    cmds.setAttr( footSoleLFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footSoleLFRock_clamp+'.minR', -180 )
    footSoleRFRock_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footSoleRFRock_unitConversion' )
    footSoleRFRock_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=foo+'footSoleRFRock_clamp' )
    cmds.setAttr( footSoleRFRock_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footSoleRFRock_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'FootRock', footSoleLFRock_clamp+'.inputR' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'FootRock', footSoleRFRock_clamp+'.inputR' )
    cmds.connectAttr( footSoleLFRock_clamp+'.outputR', footSoleLFRock_unitConversion+'.input' )
    cmds.connectAttr( footSoleRFRock_clamp+'.outputR', footSoleRFRock_unitConversion+'.input' )
    cmds.connectAttr( footSoleLFRock_unitConversion+'.output', RevSoleLFJoint[0]+'.rotateZ' )
    cmds.connectAttr( footSoleRFRock_unitConversion+'.output', RevSoleRFJoint[0]+'.rotateZ' )
    # -- connect foot pivot
    footBallSolePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footBallSolePivot_unitConversion' )
    cmds.setAttr( footBallSolePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'FootPivot', footBallSolePivot_unitConversion+'.input' )
    cmds.connectAttr( footBallSolePivot_unitConversion+'.output', RevBallSoleJoint[0]+'.rotateY' )
    # -- connect foot twist
    footBallTwist_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footBallTwist_unitConversion' )
    cmds.setAttr( footBallTwist_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'FootTwist', footBallTwist_unitConversion+'.input' )
    cmds.connectAttr( footBallTwist_unitConversion+'.output', RevBallJoint[0]+'.rotateZ' )
    # -- connect heel pivot
    footHeelPivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footHeelPivot_unitConversion' )
    cmds.setAttr( footHeelPivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'HeelPivot', footHeelPivot_unitConversion+'.input' )
    cmds.connectAttr( footHeelPivot_unitConversion+'.output', RevHeelJoint[0]+'.rotateY' )
    # -- connect toe roll
    footToeRoll_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footToeRoll_unitConversion' )
    footToeRoll_clamp = cmds.shadingNode( 'clamp', asUtility=True, n=foo+'footToeRoll_clamp' )
    cmds.setAttr( footToeRoll_unitConversion+'.conversionFactor', 0.01745 )
    cmds.setAttr( footToeRoll_clamp+'.maxR', 180 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'ToeRoll', footToeRoll_clamp+'.inputR' )
    cmds.connectAttr( footToeRoll_clamp+'.outputR', footToeRoll_unitConversion+'.input' )
    cmds.connectAttr( footToeRoll_unitConversion+'.output', RevToeJoint[0]+'.rotateX' )
    # -- connect toe pivot
    footToePivot_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footToePivot_unitConversion' )
    cmds.setAttr( footToePivot_unitConversion+'.conversionFactor', 0.01745 )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'ToePivot', footToePivot_unitConversion+'.input' )
    cmds.connectAttr( footToePivot_unitConversion+'.output', RevToeJoint[0]+'.rotateY' )
    
    # -- connect toe bend
    footToeBend_unitConversionIn = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footToeBend_unitConversionIn' )
    footToeBend_unitConversionOut = cmds.shadingNode( 'unitConversion', asUtility=True, n=foo+'footToeBend_unitConversionOut' )
    cmds.setAttr( footToeBend_unitConversionIn+'.conversionFactor', 57.29578 )
    cmds.setAttr( footToeBend_unitConversionOut+'.conversionFactor', 0.01745 )
    footToeBend_addDL = cmds.shadingNode( 'addDL', asUtility=True, n=foo+'footToeBend_addDL' )
    cmds.disconnectAttr( BallJointIK+'.rotate', Ball_pairBlend+'.inRotate2' )
    cmds.connectAttr( BallJointIK+'.rotateZ', footToeBend_unitConversionIn+'.input' )
    cmds.connectAttr( FootUtilCtrl[0]+'.'+foo+'ToeBend', footToeBend_addDL+'.input1' )
    cmds.connectAttr( footToeBend_unitConversionIn+'.output', footToeBend_addDL+'.input2' )
    cmds.connectAttr( footToeBend_addDL+'.output', footToeBend_unitConversionOut+'.input' )
    cmds.connectAttr( BallJointIK+'.rotateX', Ball_pairBlend+'.inRotate2.inRotateX2' )
    cmds.connectAttr( BallJointIK+'.rotateY', Ball_pairBlend+'.inRotate2.inRotateY2' )
    cmds.connectAttr( footToeBend_unitConversionOut+'.output', Ball_pairBlend+'.inRotate2.inRotateZ2' )
    
    # -- parent in the reverse foot
    RevHeelJoint = cmds.parent( RevHeelJoint, WristCtrl )
    
    # -- add the wrist SpaceOUT
    WristSpaceOUT = denUt.den_makeGrp( nodeName=foo+'Wrist_SpaceOUT', pos=(0,0,0) )
    WristSpaceOUT = cmds.parent( WristSpaceOUT, WristJoint )
    ArmSpaceOUTs += WristSpaceOUT
    
    
    # -- list the joints for binding
    ArmBindJoints = [ ClavJoint, ShldJoint, ElbowJoint, WristJoint, Scap02Joint, BallJoint ]
    ArmCtrlsALL += [ BallFKCtrl[0], FootUtilCtrl[0] ]
    
    
    # -- flip the right side back where it belongs
    if side == 'R_':
        cmds.setAttr( ArmRigGrp+'.scaleX', -1 )
        cmds.setAttr( foo+'Piv_Grp.scaleX', -1 )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return ArmRigGrp, ArmSpaceINs, ArmSpaceOUTs, ArmBindJoints, ArmCtrlsALL, ArmGutsALL



# ---------------------------------------------------------------------------------------
# Bird Parts

def den_makeBirdTorsoPivs( prefix='', radius=0.5, dpTime=0.01, size=10 ):
    #--------------------- testing variables
    #radius=2.0
    #---------------------
    
    size=size*0.08
    
    # -- makes torso pivots that can then be re-positioned to match a particular character
    
    TorsoPivGrp = denUt.den_makeGrp( nodeName=prefix+'TorsoPiv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    PelvisPiv = denUt.den_makeLoc( nodeName=prefix+'Pelvis_Piv', pos=(0, size*5, -size*1), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )

    TailPiv = denUt.den_makeLoc( nodeName=prefix+'Tail_Piv', pos=(0, size*5, -size*5), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    TailEndPiv = denUt.den_makeLoc( nodeName=prefix+'TailEnd_Piv', pos=(0, size*5, -size*10), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
        
    ChestPiv = denUt.den_makeLoc( nodeName=prefix+'Chest_Piv', pos=(0, size*5, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck01Piv = denUt.den_makeLoc( nodeName=prefix+'Neck01_Piv', pos=(0, size*5, size*3), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck02Piv = denUt.den_makeLoc( nodeName=prefix+'Neck02_Piv', pos=(0, size*6, size*5), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadPiv = denUt.den_makeLoc( nodeName=prefix+'Head_Piv', pos=(0, size*8, size*9), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadEndPiv = denUt.den_makeLoc( nodeName=prefix+'HeadEnd_Piv', pos=(0, size*8, size*12), radius=radius/2 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawPiv = denUt.den_makeLoc( nodeName=prefix+'Jaw_Piv', pos=(0, size*7, size*9), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawEndPiv = denUt.den_makeLoc( nodeName=prefix+'JawEnd_Piv', pos=(0, size*7, size*12), radius=radius/2 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    
    cmds.parent( PelvisPiv,TailPiv,TailEndPiv,ChestPiv,Neck01Piv,Neck02Piv,HeadPiv,HeadEndPiv,JawPiv,JawEndPiv,TorsoPivGrp )
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    return TorsoPivGrp


# ---------------------------------------------------------------------------------------
def den_makeBirdTorsoRig( prefix='', radius=2.0, ctrlRadius=(2.0,3.0,2.0,1.0), displayLocalAxis=False, dpTime = 0.01 ):
    #--------------------- testing variables
    prefix=''
    radius = 0.4
    ctrlRadius=(2.0,3.0,2.0,1.0)
    displayLocalAxis=True
    dpTime = 0.01
    #---------------------
    
    # -- make the Torso rig top group with show/hide attrs 
    TorsoRigGrp = denUt.den_makeGrp( nodeName=prefix+'Torso_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    # -- set up the return variables
    TorsoSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    TorsoSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    TorsoBindJoints = [] #Set list variable to hold names of all the Jx joints
    TorsoCtrlsALL = [] #Set list variable to hold names of all the controls
    TorsoGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Torso SpaceIN
    TorsoSpaceIN = denUt.den_makeGrp( nodeName=prefix+'Torso_SpaceIN', pos=(0,0,0) )
    TorsoSpaceIN = cmds.parent( TorsoSpaceIN, TorsoRigGrp )
    TorsoSpaceINs += TorsoSpaceIN
    
    # -- set variables for pivot positions
    PelvisPos = cmds.xform( prefix+'Pelvis_Piv', ws=True, q=True, t=True )
    TailPos = cmds.xform( prefix+'Tail_Piv', ws=True, q=True, t=True )
    TailEndPos = cmds.xform( prefix+'TailEnd_Piv', ws=True, q=True, t=True )
    ChestPos = cmds.xform( prefix+'Chest_Piv', ws=True, q=True, t=True )
    Neck01Pos = cmds.xform( prefix+'Neck01_Piv', ws=True, q=True, t=True )
    Neck02Pos = cmds.xform( prefix+'Neck02_Piv', ws=True, q=True, t=True )
    HeadPos = cmds.xform( prefix+'Head_Piv', ws=True, q=True, t=True )
    HeadEndPos = cmds.xform( prefix+'HeadEnd_Piv', ws=True, q=True, t=True )
    JawPos = cmds.xform( prefix+'Jaw_Piv', ws=True, q=True, t=True )
    JawEndPos = cmds.xform( prefix+'JawEnd_Piv', ws=True, q=True, t=True )
    
    # make sure the TorsoSpaceIN is selected so the first joint will be parented under it when created
    cmds.select( TorsoSpaceIN )
    # -- make the joints
    PelvisJoint = denUt.den_makeJoint( nodeName=prefix+'Pelvis_Jnt', pos=(PelvisPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    TailJoint = denUt.den_makeJoint( nodeName=prefix+'Tail_Jnt', pos=(TailPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    TailEndJoint = denUt.den_makeJoint( nodeName=prefix+'Tail_end', pos=(TailEndPos), radius=radius*0.4, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    cmds.select( TorsoSpaceIN )
    ChestJoint = denUt.den_makeJoint( nodeName=prefix+'Chest_Jnt', pos=(ChestPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    Neck01Joint = denUt.den_makeJoint( nodeName=prefix+'Neck01_Jnt', pos=(Neck01Pos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    Neck02Joint = denUt.den_makeJoint( nodeName=prefix+'Neck02_Jnt', pos=(Neck02Pos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( Neck01Joint, Neck01Pos )
    HeadJoint = denUt.den_makeJoint( nodeName=prefix+'Head_Jnt', pos=(HeadPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( HeadJoint, HeadPos )
    HeadEndJoint = denUt.den_makeJoint( nodeName=prefix+'Head_end', pos=(HeadEndPos), radius=radius*0.4, leaveSelected=False ); denUt.den_DiagPause( seconds=dpTime )
    #print( HeadEndJoint, HeadEndPos )
    cmds.select(HeadJoint)
    JawJoint = denUt.den_makeJoint( nodeName=prefix+'Jaw_Jnt', pos=(JawPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( JawJoint, JawPos )
    JawEndJoint = denUt.den_makeJoint( nodeName=prefix+'Jaw_end', pos=(JawEndPos), radius=radius*0.4, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( JawJoint, JawPos )
    
    if ( displayLocalAxis ):
        cmds.setAttr( PelvisJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( TailJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( TailEndJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ChestJoint+'.displayLocalAxis', 1 )
        #cmds.setAttr( Neck01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Neck02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( HeadJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( JawJoint+'.displayLocalAxis', 1 )
    
    
    # -- orient the joints
    cmds.joint( PelvisJoint, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True )
    cmds.joint( ChestJoint, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True )
    cmds.joint( JawJoint, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True )
    
    # -- set up the ik handles for Spine01, Spine02, Neck01
    # -- Pelvis, Cheat, Head will be driven directly by constraints
    cmds.select( Neck01Joint, Neck02Joint )
    Neck01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck02Joint, HeadJoint )
    Neck02Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    
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
    JawCtrl = denUt.den_MakeBall(nodeName=prefix+'Jaw_Ctrl',pos=(0,-1,1),radius=0.5*ctrlRadius[3],doT=True)
    cmds.xform( t=JawPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # -- Tail
    TailCtrl = denUt.den_MakeBall(nodeName=prefix+'Tail_Ctrl',pos=(0,3,0),radius=0.5*ctrlRadius[3],doT=True)
    cmds.xform( t=TailPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # make temporary list of controls to add to Controls list
    stuffToAdd = [PelvisCtrl,TailCtrl,ChestCtrl,HeadCtrl,JawCtrl]
    # add controls to Controls list
    TorsoCtrlsALL += stuffToAdd
    print( stuffToAdd )
    print( TorsoCtrlsALL )
    
    # - this loop is here in case more than one spine or neck joint are needed
    VertJoints = [Neck02Joint]
    print( VertJoints )
    #print NeckCtrlNames
    VertControls = []
    for jx in VertJoints:
        print( jx )
        #jxName = cmd.ls
        CtrlName = jx.replace('_Jnt', '_Ctrl')
        print( CtrlName )
        Ctrl = denUt.den_MakeBall(nodeName=CtrlName,pos=(0,2,0),radius=0.3,doT=True)
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        Ctrl = cmds.parent( Ctrl, jx, relative=True )
        Ctrl = cmds.parent( Ctrl, TorsoSpaceIN )
        Ctrl = denUt.den_AddZeroNull()
        denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
        VertControls += Ctrl
        denUt.den_DiagPause( seconds=dpTime )
    
    # add controls to Controls list
    TorsoCtrlsALL += VertControls
    print( VertControls )
    print( TorsoCtrlsALL )
    
    Neck02Ctrl = VertControls[0]
    
    
    # -- make locators for certain joints including 2 for Spine02 for blended pos
    PelvisLoc = cmds.spaceLocator (n=prefix+'Pelvis_Loc')
    PelvisLoc = cmds.parent( PelvisLoc, PelvisJoint, relative=True )
    PelvisLoc = cmds.parent( PelvisLoc, PelvisCtrl )
    
    ChestLoc = cmds.spaceLocator (n=prefix+'Chest_Loc')
    ChestLoc = cmds.parent( ChestLoc, ChestJoint, relative=True )
    ChestLoc = cmds.parent( ChestLoc, ChestCtrl )
    
    HeadLoc = cmds.spaceLocator (n=prefix+'Head_Loc')
    HeadLoc = cmds.parent( HeadLoc, HeadJoint, relative=True )
    HeadLoc = cmds.parent( HeadLoc, HeadCtrl )
    
    # -- reparent some things
    Neck01Handle = cmds.parent( Neck01Handle, Neck02Ctrl ) # make Spine01 ik goal follow Spine02Ctrl
    Neck02Handle = cmds.parent( Neck02Handle, HeadCtrl ) # make neck ik goal follow head
    
    JawCtrl = cmds.parent( JawCtrl, HeadCtrl )
    HeadCtrl = cmds.parent( HeadCtrl, ChestCtrl )
    ChestCtrl = cmds.parent( ChestCtrl, TorsoSpaceIN )
    PelvisCtrl = cmds.parent( PelvisCtrl, TorsoSpaceIN )
    TailCtrl = cmds.parent( TailCtrl, PelvisCtrl )
    
    # -- add the main control zero nulls
    cmds.select( PelvisCtrl )
    PelvisCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    cmds.select( TailCtrl )
    TailCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    cmds.select( ChestCtrl )
    ChestCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  1,1,1 , 0,0,0 , 1,1,1 , 0 )
    cmds.select( HeadCtrl )
    HeadCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    HeadCtrlZero = cmds.listRelatives( HeadCtrl, parent=True )
    cmds.select( JawCtrl )
    JawCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    JawCtrlZero = cmds.listRelatives( JawCtrl, parent=True )
    
    # -- make constraints
    cmds.parentConstraint( PelvisLoc, PelvisJoint, mo=True ) # makes pelvis joint follow pelvis control
    cmds.orientConstraint( ChestLoc, ChestJoint, mo=True ) # makes chest joint orient follow chest control
    cmds.orientConstraint( HeadLoc, HeadJoint, mo=True ) # makes head joint orient follow head control
    cmds.parentConstraint( JawCtrl, JawJoint, mo=True ) # makes jaw joint follow jaw control
    cmds.parentConstraint( HeadJoint, JawCtrlZero, mo=True ) # makes jaw control stay on the head joint
    cmds.parentConstraint( ChestJoint, HeadCtrlZero, mo=True ) # makes head control follow chest joint
    cmds.orientConstraint( TailCtrl, TailJoint, mo=True ) # makes chest joint orient follow chest control
    
    # distribute influence of pelvis and chest controls to the Vertebrae controls of the spine
    cmds.pointConstraint( ChestCtrl, HeadCtrl, prefix+'Neck02_CtrlZero', mo=True )
    # spreads the twist forward one joint to avoid last spine joint having no twist
    sc1 = cmds.orientConstraint( ChestCtrl, prefix+'Neck02_Ctrl', Neck01Handle )
    sc2 = cmds.orientConstraint( prefix+'Neck02_Ctrl', HeadCtrl, Neck02Handle )
    
    for con in [ sc1, sc2 ]:
        print( con )
        cmds.setAttr( con[0]+'.interpType', 2 )
    
    
    # -- list the jx joints for binding or proxy
    TorsoBindJoints += [ PelvisJoint, TailJoint, ChestJoint, Neck01Joint, Neck02Joint, HeadJoint, JawJoint ]
    
    # -- add the space output nulls
    TorsoSpaceOUTs += denUt.den_AddSpaceOUTs(TorsoBindJoints)
    print( TorsoSpaceOUTs )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return TorsoRigGrp, TorsoSpaceINs, TorsoSpaceOUTs, TorsoBindJoints, TorsoCtrlsALL, TorsoGutsALL



def den_makeBirdWingPivs( side='L_', prefix='', name='Wing', radius=2.0, elbowDist=20.0, dpTime=0.01, size=17 ):
    #--------------------- testing variables
    #side='L_'
    #name='Wing'
    #prefix = ''  # - this is here to add a unique identifier to the node names in case there are nore than one arm
    #radius=2.0
    #elbowDist=20.0
    #---------------------
    
    size=size*1/17
    
    # -- makes arm pivots that can then be re-positioned to match a particular character
    WingPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    ShldPiv = denUt.den_makeLoc( nodeName=side+prefix+'Shld_Piv', pos=(size*1, size*8, size*3), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    
    ElbowPiv = denUt.den_makeLoc( nodeName=side+prefix+'Elbow_Piv', pos=(size*4, size*8, size*3), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    WristPiv = denUt.den_makeLoc( nodeName=side+prefix+'Wrist_Piv', pos=(size*8, size*9, size*4), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    
    WristEndPiv = denUt.den_makeLoc( nodeName=side+prefix+'WristEnd_Piv', pos=(size*13, size*9, size*4), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    
    ElbowMidLoc = denUt.den_makeLoc( nodeName=side+prefix+'ElbowMid_Loc', radius=radius/2 )
    denUt.den_ColorShape(2)
    
    ElbowPoleLoc = denUt.den_makeLoc( nodeName=side+prefix+'ElbowPole_Loc', pos=(0, elbowDist, 0), radius=radius )
    denUt.den_ColorShape(9)
    
    cmds.parent( ElbowPoleLoc,ElbowMidLoc, relative=True )
    # lock ElbowPole_Loc transforms (except for translateY) so user cannot move it off the triangle
    denUt.den_Lock(  1,0,1 , 1,1,1 , 1,1,1 , 1 )
    
    # make ElbowMid_Loc float between Shld and Wrist
    cmds.pointConstraint( ShldPiv,WristPiv,ElbowMidLoc, maintainOffset=False )
    # aim ElbowMid_Loc at wrist, up vector towards Elbow.  this puts the L_ElbowPole_Loc on the triangle plane
    cmds.aimConstraint( WristPiv,ElbowMidLoc, maintainOffset=False, worldUpType='object', worldUpObject=ElbowPiv[0] )
    # lock ElbowMid_Loc transforms so user cannot move it off the triangle
    cmds.select(ElbowMidLoc)
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    
    # aim Shld_Piv at elbow, use wrist to keep up on the triangle plane
    cmds.aimConstraint( ElbowPiv,ShldPiv, maintainOffset=False, worldUpType='object', worldUpObject=WristPiv[0] )
    # lock Shld_Piv rotate so user cannot mess up the ain constraint
    cmds.select(ShldPiv)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    # ain Wrist_Piv at the elbow, use L_WingMid_Loc to keep up on the triangle plane, use aimvector to flip
    cmds.aimConstraint( ElbowPiv,WristPiv, maintainOffset=False, worldUpType='object', worldUpObject=ElbowMidLoc[0], aimVector=(-1,0,0) )
    # lock Wrist_Piv rotate so user cannot mess up the ain constraint
    cmds.select(WristPiv)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    #cmds.parent( ClavPiv,ShldPiv,ElbowPiv,WristPiv,Scap01Piv,Scap02Piv,ElbowMidLoc,WingPivGrp )
    cmds.parent( ShldPiv,ElbowPiv,WristPiv,WristEndPiv,ElbowMidLoc,WingPivGrp )
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( WingPivGrp+'.scaleX', -1 )
    
    return WingPivGrp


# ---------------------------------------------------------------------------------------
# define Biped Wing rig creation command

def den_makeBirdWingRig( side='L_', prefix='', name='Wing', radius=0.5, ctrlRadius=3.0, displayLocalAxis=False, twistType='none', dpTime = 0.01 ):
    #--------------------- testing variables    
    #side = 'L_'
    #name='Wing'
    #radius=2.0
    #ctrlRadius=10.0
    #displayLocalAxis=False
    #---------------------
    
    if( twistType == 'none' ) or ( twistType == 'twist' ) or ( twistType == 'ribbon' ):
        print( 'doing twistType \''+twistType+'\'' )
    else:
        print( 'ERROR - twistType must be  \'none\' or \'twist\' or \'ribbon\' - nothing else will work' )
        #exit (1)
    
    # -- if doing right side, change the color and flip the pivots to the left for good/easy mirroring
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    
    # -- make the Wing rig top group
    WingRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp', pos=(0,0,0) )
    
    # -- set up the return variables
    WingSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    WingSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    WingBindJoints = [] #Set list variable to hold names of all the _Jnt Bind joints
    WingCtrlsALL = [] #Set list variable to hold names of all the controls
    WingGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Wing SpaceINs
    HeadSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Head_SpaceIN', pos=(0,0,0) )
    HeadSpaceIN = cmds.parent( HeadSpaceIN, WingRigGrp )[0]
    ChestSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Chest_SpaceIN', pos=(0,0,0) )
    ChestSpaceIN = cmds.parent( ChestSpaceIN, WingRigGrp )[0]
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Pelvis_SpaceIN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, WingRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Cog_SpaceIN', pos=(0,0,0) )
    CogSpaceIN = cmds.parent( CogSpaceIN, WingRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'All_SpaceIN', pos=(0,0,0) )
    AllSpaceIN = cmds.parent( AllSpaceIN, WingRigGrp )[0]
    # add all the SpaceINs to the list
    WingSpaceINs += [ HeadSpaceIN, ChestSpaceIN, PelvisSpaceIN, CogSpaceIN, AllSpaceIN ]
    
    # -- make groups to hold the skeleton and the controls
    WingSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp', pos=(0,0,0) )
    WingSkelGrp = cmds.parent( WingSkelGrp, ChestSpaceIN )
    WingCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp', pos=(0,0,0) )
    WingCtrlGrp = cmds.parent( WingCtrlGrp, ChestSpaceIN )
    
    # -- make Wrist control space switcher
    WristCtrlSpace = denUt.den_makeGrp( nodeName=side+prefix+'WristCtrl_Space', pos=(0,0,0) )
    WristCtrlSpace = cmds.parent( WristCtrlSpace, WingCtrlGrp )
    WristCtrlSpaceConstraint = cmds.parentConstraint( HeadSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( ChestSpaceIN, WristCtrlSpace, weight=1 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( PelvisSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( CogSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( AllSpaceIN, WristCtrlSpace, weight=0 )
    
        
    # -- set variables for pivot positions
    
    #ClavPos = cmds.xform( side+prefix+'Clav_Piv', ws=True, q=True, t=True )
    ShldPos = cmds.xform( side+prefix+'Shld_Piv', ws=True, q=True, t=True )
    ElbowPos = cmds.xform( side+prefix+'Elbow_Piv', ws=True, q=True, t=True )
    WristPos = cmds.xform( side+prefix+'Wrist_Piv', ws=True, q=True, t=True )
    WristEndPos = cmds.xform( side+prefix+'WristEnd_Piv', ws=True, q=True, t=True )
    ElbowPolePos = cmds.xform( side+prefix+'ElbowPole_Loc', ws=True, q=True, t=True )
    
    # -- make the joints
    cmds.select( clear=True )
    ShldJoint = cmds.joint( n=side+prefix+'Shld_Jnt', p=(ShldPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    ShldJoint = cmds.parent( ShldJoint, WingSkelGrp )[0]
    ElbowJoint = cmds.joint( n=side+prefix+'Elbow_Jnt', p=(ElbowPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    WristJoint = cmds.joint( n=side+prefix+'Wrist_Jnt', p=(WristPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    WristEndJoint = cmds.joint( n=side+prefix+'Wrist_end', p=(WristEndPos), radius=radius*0.4 ); denUt.den_DiagPause( seconds=dpTime )
    
    if ( displayLocalAxis ):
        #cmds.setAttr( ClavJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ShldJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ElbowJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( WristJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( WristEndJoint+'.displayLocalAxis', 1 )
        
    # -- orient the joints
    
    cmds.select( clear=True )
    cmds.joint( ElbowJoint, e=True, oj='xyz', zso=True )
    cmds.joint( WristJoint, e=True, oj='none', zso=True )
    ShldJoint = cmds.parent( ShldJoint, side+prefix+'Shld_Piv' ) # -- temp reparent shoulder under planar space
    cmds.joint( ShldJoint, e=True, oj='none', zso=True ) # -- orient joint
    ShldJoint = cmds.parent( ShldJoint, WingSkelGrp )[0] # -- put shoulder back under clav
    
    # -- duplicate the arm to make the FK and IK arm bones
    ShldJointIK = cmds.duplicate (ShldJoint, name=side+prefix+'Shld_IK' )[0]
    ElbowJointIK = cmds.rename (ShldJointIK+'|'+side+prefix+'Elbow_Jnt', side+prefix+'Elbow_IK' )
    WristJointIK = cmds.rename (ElbowJointIK+'|'+side+prefix+'Wrist_Jnt', side+prefix+'Wrist_IK' )
    #print ShldJointIK, '----', ElbowJointIK, '----', WristJointIK
    ShldJointFK = cmds.duplicate (ShldJoint, name=side+prefix+'Shld_FK' )[0]
    ElbowJointFK = cmds.rename (ShldJointFK+'|'+side+prefix+'Elbow_Jnt', side+prefix+'Elbow_FK' )
    WristJointFK = cmds.rename (ElbowJointFK+'|'+side+prefix+'Wrist_Jnt', side+prefix+'Wrist_FK' )
    #print ShldJointFK, '----', ElbowJointFK, '----', WristJointFK
    
    # -- make the controls and zero nulls
    
    # -- Shoulder FK Control
    ShldFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'ShldFK_Ctrl', pos=(0,0,0) ,radius=2*ctrlRadius, doT=False, axis='-Z' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ShldFKCtrl = cmds.parent( ShldFKCtrl, ShldJointFK, relative=True )
    ShldFKCtrl = cmds.parent( ShldFKCtrl, WingCtrlGrp )
    ShldFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    ShldFKCtrlZero = cmds.listRelatives( ShldFKCtrl, parent=True, fullPath=True )
    cmds.connectAttr( ShldFKCtrl[0]+'.rotate', ShldJointFK+'.rotate' )
    cmds.parentConstraint( WingSkelGrp, ShldFKCtrlZero, mo=True )
    WingCtrlsALL += ShldFKCtrl # add to the controls list
    
    # -- Wing Utility Control
    WingUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(2,2,0), radius=ctrlRadius*0.2, doT=False, Plane='XY' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    WingUtilCtrl = cmds.parent( WingUtilCtrl, ShldFKCtrl, relative=True )
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', lock=False, keyable=True )
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+'Wrist_FK_IK', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+'Wrist_FK_IK', lock=False, keyable=True )
    WingCtrlsALL += WingUtilCtrl # add to the controls list
    
    # -- Elbow IK Controls
    ElbowCtrl = denUt.den_MakePole( nodeName=side+prefix+'Elbow_Ctrl', pos=(0,0,0) , radius=ctrlRadius*0.4, doT=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ElbowPolePos )
    ElbowCtrl = cmds.parent( ElbowCtrl, WingCtrlGrp )
    ElbowCtrl = denUt.den_AddZeroNull()
    WingCtrlsALL += ElbowCtrl # add to the controls list
    
    # -- Elbow FK Controls
    #ElbowFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'ElbowFK_Ctrl', pos=(0,-2,0), radius=ctrlRadius*0.4, doT=True, axis='-Y', flip=False )
    ElbowFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'ElbowFK_Ctrl', pos=(0,0,0) ,radius=1.5*ctrlRadius, doT=False, axis='-Z' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ElbowJointFK, relative=True )
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ShldFKCtrl )
    ElbowFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( ElbowFKCtrl[0]+'.rotate', ElbowJointFK+'.rotate' )
    WingCtrlsALL += ElbowFKCtrl # add to the controls list
    
    # -- Wrist IK Controls
    WristCtrl = denUt.den_MakeBall( nodeName=side+prefix+'Wrist_Ctrl', pos=(0,0,0), radius=ctrlRadius*0.7, doT=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=WristPos )
    WristCtrl = cmds.parent( WristCtrl, WristCtrlSpace )
    WristCtrl = denUt.den_AddZeroNull()
    WristCtrlZero = cmds.listRelatives( WristCtrl, parent=True, fullPath=True )
    WingCtrlsALL += WristCtrl # add to the controls list
    
    # -- Wrist FK Controls
    WristFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'WristFK_Ctrl', pos=(0,0,0), radius=ctrlRadius, doT=False, axis='-Z' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    WristFKCtrl = cmds.parent( WristFKCtrl, WristJointFK, relative=True )
    WristFKCtrl = cmds.parent( WristFKCtrl, ElbowFKCtrl )
    WristFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.setAttr( WristFKCtrl[0]+'.rotateOrder', 1 )
    WristFKCtrlZero = cmds.listRelatives( WristFKCtrl, parent=True, fullPath=True )
    WingCtrlsALL += WristFKCtrl # add to the controls list
    
    # -- set up IK/FK blending for wrist
    cmds.orientConstraint( WristCtrl, WristJointIK, mo=True )
    cmds.orientConstraint( WristFKCtrl, WristJointFK, mo=True )
    
    # -- connect up the IK Wrist control space switcher
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+'HeadSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+'HeadSpace', lock=False, keyable=True )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+'HeadSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Head_SpaceINW0' )
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+'ChestSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+'ChestSpace', lock=False, keyable=True )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+'ChestSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Chest_SpaceINW1' )
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+'PelvisSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', lock=False, keyable=True )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Pelvis_SpaceINW2' )
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+'CogSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Cog_SpaceINW3' )
    cmds.addAttr( WingUtilCtrl, longName=side+prefix+'AllSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( WingUtilCtrl[0]+'.'+side+prefix+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+'AllSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'All_SpaceINW4' )
    
    # -- set up Wing FK_IK blending
    Shld_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Shld_ikFk_pairBlend' )
    cmds.setAttr( Shld_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ShldJointFK+'.rotate', Shld_pairBlend+'.inRotate1' )
    cmds.connectAttr( ShldJointIK+'.rotate', Shld_pairBlend+'.inRotate2' )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Shld_pairBlend+'.weight' )
    cmds.connectAttr( Shld_pairBlend+'.outRotate', ShldJoint+'.rotate' )
    
    Elbow_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Elbow_ikFk_pairBlend' )
    cmds.setAttr( Elbow_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ElbowJointFK+'.rotate', Elbow_pairBlend+'.inRotate1' )
    cmds.connectAttr( ElbowJointIK+'.rotate', Elbow_pairBlend+'.inRotate2' )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Elbow_pairBlend+'.weight' )
    cmds.connectAttr( Elbow_pairBlend+'.outRotate', ElbowJoint+'.rotate' )
    
    Wrist_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Wrist_ikFk_pairBlend' )
    cmds.setAttr( Wrist_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( WristJointFK+'.rotate', Wrist_pairBlend+'.inRotate1' )
    cmds.connectAttr( WristJointIK+'.rotate', Wrist_pairBlend+'.inRotate2' )
    cmds.connectAttr( WingUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Wrist_pairBlend+'.weight' )
    cmds.connectAttr( Wrist_pairBlend+'.outRotate', WristJoint+'.rotate' )
    
    # -- make the ik handles
    #print( ShldJointIK, WristJointIK, ClavJoint, ShldJoint, Scap01Joint, Scap03Joint )
    WingIKhandle = cmds.ikHandle( startJoint=ShldJointIK, endEffector=WristJointIK, solver='ikRPsolver', setupForRPsolver=True, name=ShldJointIK.replace('IK','Ikh') )
    #print( WingIKhandle )
    cmds.rename( WingIKhandle[1], WingIKhandle[0].replace('Ikh','Eff') )
    WingIKhandle = cmds.parent( WingIKhandle[0], WristCtrl )
    cmds.poleVectorConstraint( ElbowCtrl, WingIKhandle )
    # -- add the wrist SpaceOUT
    WristSpaceOUT = denUt.den_makeGrp( nodeName=side+prefix+'Wrist_SpaceOUT', pos=(0,0,0) )
    WristSpaceOUT = cmds.parent( WristSpaceOUT, WristJoint )
    WingSpaceOUTs += WristSpaceOUT
    
    # -- list the joints for binding
    #WingBindJoints = [ ClavJoint, ShldJoint, ElbowJoint, WristJoint, Scap02Joint ]
    WingBindJoints = [ ShldJoint, ElbowJoint, WristJoint ]
    
    
    # -- flip the right side back where it belongs
    if side == 'R_':
        cmds.setAttr( WingRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return WingRigGrp, WingSpaceINs, WingSpaceOUTs, WingBindJoints, WingCtrlsALL, WingGutsALL




def den_makeWingFeatherPivs( side='L_', prefix='', name='FeathLarge', radius=2.0, size=2.2, featherCount=10, dpTime=0.01 ):
    #--------------------- testing variables
    #side='L_'
    #name='FeathLarge'
    #radius=0.2
    #featherCount=17
    #---------------------
    
    # -- makes arm pivots that can then be re-positioned to match a particular character
    FeaPivGrp = denUt.den_makeGrp( nodeName=side+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    for i in range(featherCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        print( i, iStr, iStrPad )
        PivsRet = denSR.den_makeFinPivs(  side=side, name=name+iStrPad, jointCount=2, radius=radius, size=size )
        if side == 'R_':
            cmds.setAttr( PivsRet+'.scaleX', 1 ) # remove the mirroring because the whole thing will get mirrored later
        #denUt.den_ColorShape(22)
        cmds.parent( PivsRet, FeaPivGrp )
        
        denUt.den_DiagPause( dpTime )
    
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( FeaPivGrp+'.scaleX', -1 )
    
    return FeaPivGrp





def den_makeWingFeatherRig( side='L_', prefix='', name='FeathLarge', radius=0.2, ctrlRadius=1, featherCount=17, bindProxy=False, dpTime=0.01 ):
    #--------------------- testing variables
    #side='L_'
    #name='FeathLarge'
    #radius=0.2
    #ctrlRadius=1
    #featherCount=17
    #bindProxy=True
    #---------------------
    
    # -- if doing right side, change the color and flip the pivots to the left for good/easy mirroring
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    
    # -- makes arm pivots that can then be re-positioned to match a particular character
    FeaRigGrp = denUt.den_makeGrp( nodeName=side+name+'Rig_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    # -- set up the return variables
    FeaSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    FeaSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    FeaBindJoints = [] #Set list variable to hold names of all the _Jnt Bind joints
    FeaCtrlsALL = [] #Set list variable to hold names of all the controls
    FeaGutsALL = [] #Set list variable to hold names of all the guts
    FeaBindJointsALL = []
    
    for i in range(featherCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        #print( i, iStr, iStrPad )
        RigRet = denSR.den_makeFinRigFK( side=side, prefix=prefix, name=name+iStrPad, jointCount=2, radius=0.5*ctrlRadius, dpTime=dpTime )
        if side == 'R_':
            cmds.setAttr( RigRet[0]+'.scaleX', 1 ) # remove the mirroring because the whole thing will get mirrored later
        #print( RigRet )
        FeaSpaceINs += RigRet[1]
        FeaBindJoints += RigRet[3]
        FeaCtrlsALL += RigRet[4]
        rootLoc = denUt.den_makeLoc( nodeName=side+name+iStrPad+'Root_Loc', radius=radius )
        aimLoc = denUt.den_makeLoc( nodeName=side+name+iStrPad+'Aim_Loc', pos=(5+5*i/(featherCount-1),0,0), radius=radius )
        upLoc = denUt.den_makeLoc( nodeName=side+name+iStrPad+'Up_Loc', pos=(0,1,0), radius=radius )
        aimLoc = cmds.parent( aimLoc, RigRet[3][0], relative=True )
        upLoc = cmds.parent( upLoc, RigRet[3][0], relative=True )
        rootLoc = cmds.parent( rootLoc, RigRet[3][0], relative=True )
        aimLoc = cmds.parent( aimLoc, RigRet[1][0], relative=False )
        upLoc = cmds.parent( upLoc, RigRet[1][0], relative=False )
        rootLoc = cmds.parent( rootLoc, RigRet[1][0], relative=False )
        firstJnt = cmds.parent( RigRet[3][0], rootLoc )
        firstCtrlZero = cmds.parent( RigRet[4][0]+'Zero', rootLoc )
        aimCon = cmds.aimConstraint( aimLoc, rootLoc, worldUpType='object', worldUpObject=upLoc[0] )
        
        rootJnt = cmds.joint( name=side+name+iStrPad+'Root_Jnt', radius=ctrlRadius )
        #rootJnt = denUt.den_makeJoint( nodeName=side+name+iStrPad+'Root_Jnt', pos=(-0.1*ctrlRadius,0,0), radius=ctrlRadius, leaveSelected=False )
        rootJnt = cmds.parent( rootJnt, rootLoc, relative=True )
        cmds.xform( rootJnt[0], t=(-0.1*ctrlRadius,0,0) )
        rootJnt = cmds.parent( rootJnt, RigRet[1] )
        FeaBindJointsALL += [RigRet[3]+rootJnt]
        
        if i == (0):
            rootCtrlZero = cmds.duplicate( aimLoc, name=side+name+'Root_CtrlZero' )
            cmds.setAttr( rootCtrlZero[0]+'.rotate',0,0,0 )
            rootCtrl = denUt.den_MakeBall( nodeName=side+name+'Root_Ctrl', pos=(0,0,0), radius=0.5*ctrlRadius, doT=False )
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            rootCtrl = cmds.parent( rootCtrl, rootCtrlZero, relative=True )
            FeaCtrlsALL += rootCtrl
        
        if i == (featherCount-1):
            tipCtrlZero = cmds.duplicate( aimLoc, name=side+name+'Tip_CtrlZero' )
            cmds.setAttr( tipCtrlZero[0]+'.rotate',0,0,0 )
            tipCtrl = denUt.den_MakeBall( nodeName=side+name+'Tip_Ctrl', pos=(0,0,0), radius=ctrlRadius, doT=False )
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            tipCtrl = cmds.parent( tipCtrl, tipCtrlZero, relative=True )
            FeaCtrlsALL += tipCtrl
        
        cmds.parent( RigRet[0], FeaRigGrp )
        
        denUt.den_DiagPause( dpTime )
    
    
    featherAims = cmds.ls( side+name+'*Aim_Loc' )
    
    for i in range(featherCount):
        rootWeight = (featherCount-1-i)/(featherCount-1)
        tipWeight = i/(featherCount-1)
        rootCtrl = side+name+'Root_Ctrl'
        tipCtrl = side+name+'Tip_Ctrl'
        print( featherAims[i], rootCtrl, rootWeight, tipCtrl, tipWeight )
        cmds.parentConstraint( rootCtrl, featherAims[i], w=rootWeight, mo=True )
        cmds.parentConstraint( side+name+'Tip_Ctrl', featherAims[i], w=tipWeight, mo=True  )
    
    #cmds.setAttr( 'locator2.rotate',1,0,0 )
    #rootCtrl = cmds.ls( 'L_FeathLargeRoot_Ctrl' ); print( rootCtrl[0] )
    #aimLoc = cmds.ls( 'L_FeathLarge01Aim_Loc' ); print( aimLoc[0] )
    #cmds.parentConstraint( 'L_FeathLargeRoot_Ctrl', 'L_FeathLarge01Aim_Loc' )
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( FeaRigGrp+'.scaleX', -1 )
    
    for i in range(featherCount):
        iStr = str(i+1)
        iStrPad = iStr.rjust(2,'0')
        if bindProxy:
            FeaSkinClust = cmds.skinCluster( side+name+iStrPad+'_Mesh', FeaBindJointsALL[i], tsb=True, name=side+name+iStrPad+'_skinCluster', nw=2 )[0]
    
    
    return FeaRigGrp, FeaSpaceINs, FeaSpaceOUTs, FeaBindJoints, FeaCtrlsALL, FeaGutsALL


def den_addTorsoAdjust( prefix='', Jnts=['Neck01_Jnt','Neck02_Jnt','Neck03_Jnt'], radius=2.2, ctrlDist=-10, dpTime=0.01 ):
    #Jnts = ['Neck01_Jnt','Neck02_Jnt','Neck03_Jnt']
    #radius = 2.1
    #ctrlDist = -14
    
    for jnt in Jnts:
        print( jnt )
        loc = cmds.spaceLocator( name=prefix+jnt.replace('_Jnt','Adj_Loc') )
        cmds.matchTransform( loc, jnt )
        adj = cmds.spaceLocator( name=prefix+jnt.replace('_Jnt','_adj') )
        adj = cmds.parent( adj, loc, relative=True )
        oldJnt = cmds.rename(jnt, jnt.replace('_Jnt','_Jx') )
        newJnt = cmds.joint( name=jnt, radius=radius )
        adjCtrl = denUt.den_MakeCube( nodeName=prefix+jnt.replace('_Jnt','Adj_Ctrl'), radius=0.3*radius )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        cmds.move( 0,-14,0 )
        adjCtrl = cmds.parent( adjCtrl, loc, relative=True )
        adjCtrl = denUt.den_AddZeroNull()
        #upGoal = cmds.spaceLocator( name=jnt.replace('_Jnt','_aim') )
        upGoal = denUt.den_makeGrp ( nodeName=prefix+jnt.replace('_Jnt','_aim'), pos=(5*abs(ctrlDist),0,0) )
        #cmds.move( 5*abs(ctrlDist),0,0 )
        upGoal = cmds.parent( upGoal, loc, relative=True )
        aimCon = cmds.aimConstraint( adjCtrl, adj, aimVector=(0,-1,0), upVector=(1,0,0), worldUpType='object', worldUpObject=upGoal[0], mo=False )[0]
        cmds.parent( loc, oldJnt, relative=False )


#den_addTorsoAdjust( prefix='', Jnts=['Neck01_Jnt','Neck02_Jnt','Neck03_Jnt'], radius=2.2, ctrlDist=-15, dpTime=0.01 )




