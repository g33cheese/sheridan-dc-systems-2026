#
#  copyright 2017, 2023, Den Turner  -  all rights reserved
#
import sys; sys.dont_write_bytecode=True
import importlib
import inspect

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

import den_Utilities_v12 as denUt
importlib.reload(denUt)
print(inspect.getfile(inspect.currentframe()), 'is importing', denUt.__file__)

#import CAAR_utilities_v03 as caarUt
#importlib.reload(caarUt)
#print(caarUt.__file__)



# ---------------------------------------------------------------------------------------
# define Base (cog) pivot creation command

def den_makeBasePiv(name='abcdef', radius=1.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #name = 'Sluggy'
    #radius=1.0
    #---------------------
    
    # -- makes base cog pivot that can then be re-positioned to match a particular character
    RootPivGrp = denUt.den_makeGrp( nodeName=name+'_Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    BasePivGrp = denUt.den_makeGrp( nodeName='BasePiv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    BasePivGrp = cmds.parent( BasePivGrp, RootPivGrp )[0]
    denUt.den_makeLoc( nodeName='Cog_Piv', pos=(0, size, 0), radius=radius )
    denUt.den_ColorShape(20)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.parent( 'Cog_Piv', BasePivGrp )
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    return RootPivGrp


# ---------------------------------------------------------------------------------------
# define Base Rig creation command

def den_makeBaseRig(label='abcdef',ctrlRadius=50.0, dpTime=0.01 ):
    #--------------------- testing variables
    #label = 'Jumpsuit Girl'
    #ctrlRadius = 50.0
    #---------------------
        
    # -- make the master root pivot group for the whole overall rig - later part pivots will be parented under this node
    RootRigGrp = denUt.den_makeGrp( nodeName=label+'_Rig_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    #print RootRigGrp
    
    # -- make the group for the base rig
    BaseRigGrp = denUt.den_makeGrp( nodeName='Base_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    BaseRigGrp = cmds.parent( BaseRigGrp, RootRigGrp )
    
    BaseSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    BaseSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    BaseBindJoints = [] #Set list variable to hold names of all the Jx joints (none for Base rig)
    BaseCtrlsALL = [] #Set list variable to hold names of all the controls
    BaseGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- set variables for pivot positions
    CogPos = cmds.xform( 'Cog_Piv', ws=True, q=True, t=True )
    
    # -- World control
    WorldCtrl = cmds.circle( radius=ctrlRadius, normal=(0,1,0), name='World_Ctrl' )[0]
    denUt.den_ColorShape(11)
    WorldCtrl = cmds.parent( WorldCtrl, BaseRigGrp )
    WorldCtrl = denUt.den_AddZeroNull()
    #denUt.den_LockAttr(False,False,True,False)
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    WorldCtrl = cmds.ls( WorldCtrl )
    BaseCtrlsALL += WorldCtrl
    
    # -- WorldOffset control
    WorldOffsetCtrl = cmds.circle( radius=ctrlRadius*0.9, normal=(0,1,0), name='WorldOffset_Ctrl' )[0]
    denUt.den_ColorShape(10)
    WorldOffsetCtrl = cmds.parent( WorldOffsetCtrl, WorldCtrl, relative=False )
    WorldOffsetCtrl = denUt.den_AddZeroNull()
    #denUt.den_LockAttr(False,False,True,False)
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    WorldOffsetCtrl = cmds.ls( WorldOffsetCtrl )
    BaseCtrlsALL += WorldOffsetCtrl
    
    # -- All control
    AllCtrl = denUt.den_MakeLabel( nodeName='All_Ctrl', pos=(0,0,0), radius=ctrlRadius*0.8, doT=False, label=label, doCircle=True )
    denUt.den_ColorShape(21)
    #denUt.den_LockAttr(False,False,True,False)
    AllCtrl = cmds.parent( AllCtrl, WorldOffsetCtrl )
    AllCtrl = denUt.den_AddZeroNull()
    AllCtrl = cmds.ls( AllCtrl )
    BaseCtrlsALL += AllCtrl
    
    # -- Cog control
    CogCtrl = denUt.den_MakeBall( nodeName='Cog_Ctrl', pos=(0,0,0), radius=ctrlRadius*0.5, doT=False )
    cmds.xform( t=CogPos )
    denUt.den_ColorShape(21)
    CogCtrl = cmds.parent( CogCtrl, AllCtrl )
    CogCtrl = denUt.den_AddZeroNull()
    CogCtrl = cmds.ls( CogCtrl )
    BaseCtrlsALL += CogCtrl
    
    # -- add attributes to control rig part visibility later
    cmds.addAttr( AllCtrl[0], longName='Global_Scale', attributeType='float', defaultValue=1.0 )
    cmds.setAttr ( AllCtrl[0]+'.Global_Scale', lock=False, channelBox=True )
    cmds.connectAttr( AllCtrl[0]+'.Global_Scale', AllCtrl[0]+'.sx' )
    cmds.connectAttr( AllCtrl[0]+'.Global_Scale', AllCtrl[0]+'.sy' )
    cmds.connectAttr( AllCtrl[0]+'.Global_Scale', AllCtrl[0]+'.sz' )
    
    cmds.addAttr( AllCtrl[0], longName='Show_Render_Geo', attributeType='enum', enumName=' off ---: --- on' )
    cmds.setAttr ( AllCtrl[0]+'.Show_Render_Geo', lock=False, channelBox=True )
    cmds.addAttr( AllCtrl[0], longName='Show_Proxy_Geo', attributeType='enum', enumName=' off ---: --- on' )
    cmds.setAttr ( AllCtrl[0]+'.Show_Proxy_Geo', 1, lock=False, channelBox=True )
    cmds.addAttr( AllCtrl[0], longName='Show_Box_Geo', attributeType='enum', enumName=' off ---: --- on' )
    cmds.setAttr ( AllCtrl[0]+'.Show_Box_Geo', 1, lock=False, channelBox=True )
    cmds.addAttr( AllCtrl[0], longName='Show_Controls', attributeType='enum', enumName=' off ---: --- on' )
    cmds.setAttr ( AllCtrl[0]+'.Show_Controls', 1, lock=False, channelBox=True )
    cmds.addAttr( AllCtrl[0], longName='Show_Guts', attributeType='enum', enumName=' off ---: --- on' )
    cmds.setAttr ( AllCtrl[0]+'.Show_Guts', lock=False, channelBox=True )
    cmds.addAttr(  AllCtrl[0], longName='Bone_Draw_Style', attributeType='enum', enumName='Bone:Multi-child as Box:None' )
    cmds.setAttr (  AllCtrl[0]+'.Bone_Draw_Style', lock=False, channelBox=True )
    # Create bend ctl visibility attribute on the All control.
    cmds.addAttr(AllCtrl, ln="Bend_Controls", attributeType='enum', enumName=' off ---: --- on' )
    cmds.setAttr(AllCtrl[0] + ".Bend_Controls", keyable=True)
    
    # Add custom color attributes to the All control.
    cmds.addAttr(AllCtrl, ln="Center_Color", uac=True, at="float3")
    cmds.addAttr(AllCtrl, ln="Center_ColorR", at="float", parent="Center_Color")
    cmds.addAttr(AllCtrl, ln="Center_ColorG", at="float", parent="Center_Color")
    cmds.addAttr(AllCtrl, ln="Center_ColorB", at="float", parent="Center_Color")
    cmds.addAttr(AllCtrl, ln="Left_Color", uac=True, at="float3")
    cmds.addAttr(AllCtrl, ln="Left_ColorR", at="float", parent="Left_Color")
    cmds.addAttr(AllCtrl, ln="Left_ColorG", at="float", parent="Left_Color")
    cmds.addAttr(AllCtrl, ln="Left_ColorB", at="float", parent="Left_Color")
    cmds.addAttr(AllCtrl, ln="Right_Color", uac=True, at="float3")
    cmds.addAttr(AllCtrl, ln="Right_ColorR", at="float", parent="Right_Color")
    cmds.addAttr(AllCtrl, ln="Right_ColorG", at="float", parent="Right_Color")
    cmds.addAttr(AllCtrl, ln="Right_ColorB", at="float", parent="Right_Color")
    
    cmds.setAttr(AllCtrl[0] + ".Center_Color", 0.8, 0.8, 0.05, type="double3")
    cmds.setAttr(AllCtrl[0] + ".Left_Color", 0, 0.3, 0.95, type="double3")
    cmds.setAttr(AllCtrl[0] + ".Right_Color", 1, 0.03, 0.05, type="double3")
    
    # connect Controls visibility to the All_Ctrl
    #print( AllCtrl )
    for i,s in enumerate(BaseCtrlsALL):
        shapes = cmds.listRelatives( s, shapes=True )
        print( shapes )
        for shape in shapes:
            if i != 2:
                cmds.connectAttr( AllCtrl[0]+'.Show_Controls', shape+'.visibility' )
    
    
    
    # -- lock the Scale of the All_Ctrl
    cmds.select( AllCtrl[0] )
    #denUt.den_LockAttr(False,False,True,False)
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    
    # -- add the space output nulls
    CogSpaceOUT = denUt.den_makeGrp( nodeName='CogSpace_OUT', pos=(0,0,0) )
    CogSpaceOUT = cmds.parent( CogSpaceOUT, CogCtrl )[0]
    AllSpaceOUT = denUt.den_makeGrp( nodeName='AllSpace_OUT', pos=(0,0,0) )
    AllSpaceOUT = cmds.parent( AllSpaceOUT, AllCtrl )[0]
    
    BaseSpaceOUTs += [CogSpaceOUT, AllSpaceOUT]
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return RootRigGrp, BaseSpaceINs, BaseSpaceOUTs, BaseBindJoints, BaseCtrlsALL, BaseGutsALL



# ---------------------------------------------------------------------------------------
# define Biped Torso pivot creation command

def den_makeBipedTorsoPivs( prefix='', radius=2.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #radius=2.0
    #---------------------
    
    # -- makes torso pivots that can then be re-positioned to match a particular character
    
    TorsoPivGrp = denUt.den_makeGrp( nodeName=prefix+'TorsoPiv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    PelvisPiv = denUt.den_makeLoc( nodeName=prefix+'Pelvis_Piv', pos=(0, size*0.6, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine01Piv = denUt.den_makeLoc( nodeName=prefix+'Spine01_Piv', pos=(0, size*0.65, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Spine02Piv = denUt.den_makeLoc( nodeName=prefix+'Spine02_Piv', pos=(0, size*0.7, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    ChestPiv = denUt.den_makeLoc( nodeName=prefix+'Chest_Piv', pos=(0, size*0.75, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    Neck01Piv = denUt.den_makeLoc( nodeName=prefix+'Neck01_Piv', pos=(0, size*0.85, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadPiv = denUt.den_makeLoc( nodeName=prefix+'Head_Piv', pos=(0, size*0.9, 0), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    HeadEndPiv = denUt.den_makeLoc( nodeName=prefix+'HeadEnd_Piv', pos=(0, size*1.0, 0), radius=radius/2 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawPiv = denUt.den_makeLoc( nodeName=prefix+'Jaw_Piv', pos=(0, size*0.9, size*0.05), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    JawEndPiv = denUt.den_makeLoc( nodeName=prefix+'JawEnd_Piv', pos=(0, size*0.9, size*0.1), radius=radius/2 )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    
    cmds.parent( PelvisPiv,Spine01Piv,Spine02Piv,ChestPiv,Neck01Piv,HeadPiv,HeadEndPiv,JawPiv,JawEndPiv,TorsoPivGrp )
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    return TorsoPivGrp



# ---------------------------------------------------------------------------------------
def den_makeBipedTorsoRig( prefix='', radius=2.0, ctrlRadius=(18.0,20.0,12.0,2.0), displayLocalAxis=False, dpTime=0.01 ):
    #--------------------- testing variables
    #radius = 2.0
    #ctrlRadius=(18.0,20.0,12.0,2.0)
    #displayLocalAxis=False 
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
    Spine01Pos = cmds.xform( prefix+'Spine01_Piv', ws=True, q=True, t=True )
    Spine02Pos = cmds.xform( prefix+'Spine02_Piv', ws=True, q=True, t=True )
    ChestPos = cmds.xform( prefix+'Chest_Piv', ws=True, q=True, t=True )
    Neck01Pos = cmds.xform( prefix+'Neck01_Piv', ws=True, q=True, t=True )
    HeadPos = cmds.xform( prefix+'Head_Piv', ws=True, q=True, t=True )
    HeadEndPos = cmds.xform( prefix+'HeadEnd_Piv', ws=True, q=True, t=True )
    JawPos = cmds.xform( prefix+'Jaw_Piv', ws=True, q=True, t=True )
    JawEndPos = cmds.xform( prefix+'JawEnd_Piv', ws=True, q=True, t=True )
    
    # make sure the TorsoSpaceIN is selected so the first joint will be parented under it when created
    cmds.select( TorsoSpaceIN )
    # -- make the joints
    PelvisJoint = denUt.den_makeJoint( nodeName=prefix+'Pelvis_Jnt', pos=(PelvisPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( PelvisJoint, PelvisPos )
    Spine01Joint = denUt.den_makeJoint( nodeName=prefix+'Spine01_Jnt', pos=(Spine01Pos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( Spine01Joint, Spine01Pos )
    Spine02Joint = denUt.den_makeJoint( nodeName=prefix+'Spine02_Jnt', pos=(Spine02Pos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( Spine02Joint, Spine02Pos )
    ChestJoint = denUt.den_makeJoint( nodeName=prefix+'Chest_Jnt', pos=(ChestPos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
    #print( ChestJoint, ChestPos )
    Neck01Joint = denUt.den_makeJoint( nodeName=prefix+'Neck01_Jnt', pos=(Neck01Pos), radius=radius, leaveSelected=True ); denUt.den_DiagPause( seconds=dpTime )
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
        cmds.setAttr( HeadJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( JawJoint+'.displayLocalAxis', 1 )
    
    
    # -- orient the joints
    cmds.joint( PelvisJoint, e=True, oj='xyz', secondaryAxisOrient='zdown', ch=True, zso=True )
    cmds.joint( JawJoint, e=True, oj='xyz', secondaryAxisOrient='zdown', ch=True, zso=True )
    
    # -- set up the ik handles for Spine01, Spine02, Neck01
    # -- Pelvis, Cheat, Head will be driven directly by constraints
    cmds.select( Spine01Joint, Spine02Joint )
    Spine01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Spine02Joint, ChestJoint )
    Spine02Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    cmds.select( Neck01Joint, HeadJoint )
    Neck01Handle = denUt.den_AddIKHandle('ikSCsolver',False)
    
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
    JawCtrl = denUt.den_MakeBall(nodeName=prefix+'Jaw_Ctrl',pos=(0,-6,10),radius=ctrlRadius[3],doT=True)
    cmds.xform( t=JawPos )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    
    # make temporary list of controls to add to Controls list
    stuffToAdd = [PelvisCtrl,ChestCtrl,HeadCtrl,JawCtrl]
    # add controls to Controls list
    TorsoCtrlsALL += stuffToAdd
    print( stuffToAdd )
    print( TorsoCtrlsALL )
    
    # - this loop is here in case more than one spine or neck joint are needed
    VertJoints = [Spine02Joint]
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
        denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
        VertControls += Ctrl
        denUt.den_DiagPause( seconds=dpTime )
    
    # add controls to Controls list
    TorsoCtrlsALL += VertControls
    print( VertControls )
    print( TorsoCtrlsALL )
    
    Spine02Ctrl = VertControls[0]
    #Neck02Ctrl = VertControls[0]
    #Neck03Ctrl = VertControls[1]
    #Neck04Ctrl = VertControls[2]
    #Spine02Ctrl = VertControls[3]
    #Spine03Ctrl = VertControls[4]
    #Spine04Ctrl = VertControls[5]
    
    
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
    
    # make temporary list of locators to add to Guts list
    #stuffToAdd = [PelvisLoc,ChestLoc,HeadLoc]
    # add locators to Guts list
    #TorsoGutsALL += stuffToAdd
    #print( stuffToAdd )
    #print( TorsoGutsALL )
    
    # -- reparent some things
    Spine01Handle = cmds.parent( Spine01Handle, Spine02Ctrl ) # make Spine01 ik goal follow Spine02Ctrl
    Spine02Handle = cmds.parent( Spine02Handle, ChestCtrl ) # make Spine02 ik goal follow chest
    Neck01Handle = cmds.parent( Neck01Handle, HeadCtrl ) # make neck ik goal follow head
    
    JawCtrl = cmds.parent( JawCtrl, HeadCtrl )
    HeadCtrl = cmds.parent( HeadCtrl, ChestCtrl )
    ChestCtrl = cmds.parent( ChestCtrl, TorsoSpaceIN )
    PelvisCtrl = cmds.parent( PelvisCtrl, TorsoSpaceIN )
    
    # -- add the main control zero nulls
    cmds.select( PelvisCtrl )
    PelvisCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
    cmds.select( ChestCtrl )
    ChestCtrl = denUt.den_AddZeroNull()
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
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
    
    # distribute influence of pelvis and chest controls to the Vertebrae controls of the spine
    cmds.parentConstraint( PelvisCtrl, ChestCtrl, prefix+'Spine02_CtrlZero', mo=True )
    # spreads the twist forward one joint to avoid last spine joint having no twist
    sc1 = cmds.orientConstraint( PelvisCtrl, prefix+'Spine02_Ctrl', Spine01Handle )
    sc2 = cmds.orientConstraint( prefix+'Spine02_Ctrl', ChestCtrl, Spine02Handle )
    # spreads the twist forward one joint to avoid last neck joint having no twist
    nc1 = cmds.orientConstraint( ChestLoc, HeadLoc, Neck01Handle, mo=True ) # neck x-rot split between head and chest
    
    for con in [ sc1, sc2, nc1 ]:
        print( con )
        cmds.setAttr( con[0]+'.interpType', 2 )
    
    
    # -- list the jx joints for binding or proxy
    TorsoBindJoints += [ PelvisJoint, Spine01Joint, Spine02Joint, ChestJoint, Neck01Joint, HeadJoint, JawJoint ]
    
    # -- add the space output nulls
    TorsoSpaceOUTs += denUt.den_AddSpaceOUTs(TorsoBindJoints)
    print( TorsoSpaceOUTs )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return TorsoRigGrp, TorsoSpaceINs, TorsoSpaceOUTs, TorsoBindJoints, TorsoCtrlsALL, TorsoGutsALL




# ---------------------------------------------------------------------------------------
# define Biped Arm pivots creation command

def den_makeBipedArmPivs( side='L_', prefix='', name='Arm', radius=2.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #side='L_'
    #name='Arm'
    #prefix = ''  # - this is here to add a unique identifier to the node names in case there is more than one Arm
    #radius=2.0
    #elbowDist=20.0
    #---------------------
    
    # -- makes arm pivots that can then be re-positioned to match a particular character
    ArmPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    ClavPiv = denUt.den_makeLoc( nodeName=side+prefix+'Clav_Piv', pos=(size*0.01, size*0.8, size*0.05), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    ShldPiv = denUt.den_makeLoc( nodeName=side+prefix+'Shld_Piv', pos=(size*0.1, size*0.8, size*0.01), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    
    ElbowPiv = denUt.den_makeLoc( nodeName=side+prefix+'Elbow_Piv', pos=(size*0.2, size*0.7, size*0.01), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    WristPiv = denUt.den_makeLoc( nodeName=side+prefix+'Wrist_Piv', pos=(size*0.3, size*0.6, size*0.1), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    
    Scap01Piv = denUt.den_makeLoc( nodeName=side+prefix+'Scap01_Piv', pos=(-size*0.01, size*0.8, size*0.05), radius=radius*0.7 ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    
    Scap02Piv = denUt.den_makeLoc( nodeName=side+prefix+'Scap02_Piv', pos=(size*0.02, size*0.8, -size*0.02), radius=radius*0.7 ); denUt.den_DiagPause( seconds=dpTime )
    denUt.den_ColorShape(20)
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    ElbowMidLoc = denUt.den_makeLoc( nodeName=side+prefix+'ElbowMid_Loc', radius=radius/2 )
    denUt.den_ColorShape(2)
    
    ElbowPoleLoc = denUt.den_makeLoc( nodeName=side+prefix+'ElbowPole_Loc', pos=(0, size*0.1, 0), radius=radius )
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
    #denUt.den_LockAttr( denT=False )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    # aim Scap01_Piv at scap02, use shoulder to keep up on the triangle plane
    cmds.aimConstraint( Scap02Piv,Scap01Piv, maintainOffset=False, worldUpType='object', worldUpObject=ShldPiv[0] )
    # lock Scap01_Piv rotate so user cannot mess up the ain constraint
    cmds.select(Scap01Piv)
    #denUt.den_LockAttr( denT=False )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    # ain Wrist_Piv at the elbow, use L_ArmMid_Loc to keep up on the triangle plane, use aimvector to flip
    cmds.aimConstraint( ElbowPiv,WristPiv, maintainOffset=False, worldUpType='object', worldUpObject=ElbowMidLoc[0], aimVector=(-1,0,0) )
    # lock Wrist_Piv rotate so user cannot mess up the ain constraint
    cmds.select(WristPiv)
    #denUt.den_LockAttr( denT=False )
    denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.parent( ClavPiv,ShldPiv,ElbowPiv,WristPiv,Scap01Piv,Scap02Piv,ElbowMidLoc,ArmPivGrp )
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( ArmPivGrp+'.scaleX', -1 )
    
    return ArmPivGrp






# ---------------------------------------------------------------------------------------
# define Twist rig creation command

def den_makeTwists( side='L_', prefix='', name='Arm', radius=2.0, Joints=['Shld','Elbow','Wrist'], ctrlPos=(-10,0,-10), ctrlUpVec=(0,0,-1), displayLocalAxis=True, dpTime = 0.01 ):
    #--------------------- testing variables
    #side='R_'
    #name='Arm'
    #radius=2.0
    #Joints=['Shld_Jnt','Elbow_Jnt','Wrist_Jnt']
    #ctrlPos=(-10,0,-10)
    #ctrlUpVec=(0,0,-1)
    #displayLocalAxis=True
    #---------------------
    
    sideColor = 6
    
    if side == 'R_':
        sideColor = 13
    
    # -- make the Twist rig top group - coming soon
    #TwistRigGrp = denUt.den_makeGrp( nodeName=side+name+'Twist_Grp', pos=(0,0,0) )
    TwistRigGrp = ''
    
    # -- set up the return variables
    TwistSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    TwistSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    TwistBindJoints = [] #Set list variable to hold names of all the _Jnt bind joints
    TwistCtrlsALL = [] #Set list variable to hold names of all the controls
    TwistGutsALL = [] #Set list variable to hold names of all the guts
    
    FirstName = side+prefix+Joints[0]
    SecondName = side+prefix+Joints[1]
    ThirdName = side+prefix+Joints[2]
    
    FirstJoint = cmds.ls( FirstName+'_Jnt' )[0]
    FirstParent = cmds.listRelatives( FirstJoint, parent=True, fullPath=True )[0]
    SecondJoint = cmds.ls( SecondName+'_Jnt' )[0]
    ThirdJoint = cmds.ls( ThirdName+'_Jnt' )[0]
    #print( FirstParent, FirstJoint, SecondJoint, ThirdJoint )
    
    print( '\nden_makeTwists -- WARNING -- Twist does not build a separate rig part, but modifies the existing limb.' )
    print( '                             If it fails, you will likely need to bebuild the limb before trying again.' )
    
    # - these variables are for future upgrades - currently they are redundant
    FirstIN = FirstJoint
    SecondIN = SecondJoint
    ThirdIN = ThirdJoint
    
    FirstTwist01Joint = cmds.joint( n=FirstName+'Twist01_Jnt', radius=radius )
    FirstTwist01Joint = cmds.parent( FirstTwist01Joint, FirstIN, relative=True )[0]
    FirstTwist01Joint = cmds.parent( FirstTwist01Joint, FirstParent )[0]
    FirstTwist02Joint = cmds.joint( n=FirstName+'Twist02_Jnt', radius=radius )
    FirstTwist02Joint = cmds.parent( FirstTwist02Joint, FirstIN, relative=True )[0]
    FirstTwist03Joint = cmds.joint( n=FirstName+'Twist03_Jnt', radius=radius )
    FirstTwist03Joint = cmds.parent( FirstTwist03Joint, FirstIN, relative=True )[0]
    SecondTwist01Joint = cmds.joint( n=SecondName+'Twist01_Jnt', radius=radius )
    SecondTwist01Joint = cmds.parent( SecondTwist01Joint, SecondIN, relative=True )[0]
    SecondTwist01Joint = cmds.parent( SecondTwist01Joint, FirstIN )[0]
    SecondTwist02Joint = cmds.joint( n=SecondName+'Twist02_Jnt', radius=radius )
    SecondTwist02Joint = cmds.parent( SecondTwist02Joint, SecondIN, relative=True )[0]
    SecondTwist03Joint = cmds.joint( n=SecondName+'Twist03_Jnt', radius=radius )
    SecondTwist03Joint = cmds.parent( SecondTwist03Joint, SecondIN, relative=True )[0]
    
    FirstRestJoint = cmds.duplicate( FirstTwist01Joint, n=FirstName+'Rest_Jx' )[0]
    FirstUpCarJoint = cmds.duplicate( FirstRestJoint, n=FirstName+'UpCar_Jx' )[0]
    FirstTwist01UpCtrl = denUt.den_MakePole( nodeName=FirstName+'Twist01Up_Ctrl', radius=radius/2 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ctrlPos, relative=True, ws=True )
    FirstTwist01UpCtrl = cmds.parent( FirstTwist01UpCtrl, FirstUpCarJoint, relative=True )[0]
    FirstTwist01UpCtrl = denUt.den_AddZeroNull()
    FirstTwist01UpCtrlZero = cmds.listRelatives( FirstTwist01UpCtrl, parent=True, fullPath=True )[0]
    
    if ( displayLocalAxis ):
        cmds.setAttr( FirstTwist01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( FirstTwist02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( FirstTwist03Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( SecondTwist01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( SecondTwist02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( SecondTwist03Joint+'.displayLocalAxis', 1 )
    
    # -- make the constraints
    
    # - set up a carrier for the shoulder up that stays mostly out of the way, rotates in y only
    FirstUpCarJointOriCon = cmds.orientConstraint( FirstIN, FirstRestJoint, FirstUpCarJoint )[0]
    cmds.setAttr( FirstUpCarJointOriCon+'.interpType', 2 )
    cmds.disconnectAttr( FirstUpCarJointOriCon+'.constraintRotateX', FirstUpCarJoint+'.rotateX' )
    cmds.disconnectAttr( FirstUpCarJointOriCon+'.constraintRotateZ', FirstUpCarJoint+'.rotateZ' )
    # - set up the First Twist01 so it does not twist with the Second
    cmds.aimConstraint( SecondIN, FirstTwist01Joint, upVector=ctrlUpVec, maintainOffset=False, worldUpType='object', worldUpObject=FirstTwist01UpCtrl[0] )
    # - connect Second twist03 rotateX to the Third rotateX
    cmds.connectAttr( ThirdIN+'.rotateX', SecondTwist03Joint+'.rotateX' )
    # set up First twist02 so it splits the difference between First twist01 and First twist03
    FirstTwist02t_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=FirstName+'Twist02t_unitConversion' )
    FirstTwist03t_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=FirstName+'Twist03t_unitConversion' )
    cmds.setAttr( FirstTwist02t_unitConversion+'.conversionFactor', 0.33 )
    cmds.setAttr( FirstTwist03t_unitConversion+'.conversionFactor', 0.66 )
    cmds.connectAttr( SecondIN+'.translate', FirstTwist02t_unitConversion+'.input' )
    cmds.connectAttr( FirstTwist02t_unitConversion+'.output', FirstTwist02Joint+'.translate' )
    cmds.connectAttr( SecondIN+'.translate', FirstTwist03t_unitConversion+'.input' )
    cmds.connectAttr( FirstTwist03t_unitConversion+'.output', FirstTwist03Joint+'.translate' )
    FirstTwist02OriCon = cmds.orientConstraint( FirstTwist01Joint, FirstTwist03Joint, FirstTwist02Joint )
    cmds.setAttr( FirstTwist02OriCon[0]+'.interpType', 2 )
    # set up First twist02 so it splits the difference between First twist01 and First twist03
    SecondTwist02t_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=SecondName+'Twist02t_unitConversion' )
    SecondTwist03t_unitConversion = cmds.shadingNode( 'unitConversion', asUtility=True, n=SecondName+'Twist03t_unitConversion' )
    cmds.setAttr( SecondTwist02t_unitConversion+'.conversionFactor', 0.33 )
    cmds.setAttr( SecondTwist03t_unitConversion+'.conversionFactor', 0.66 )
    cmds.connectAttr( ThirdIN+'.translate', SecondTwist02t_unitConversion+'.input' )
    cmds.connectAttr( SecondTwist02t_unitConversion+'.output', SecondTwist02Joint+'.translate' )
    cmds.connectAttr( ThirdIN+'.translate', SecondTwist03t_unitConversion+'.input' )
    cmds.connectAttr( SecondTwist03t_unitConversion+'.output', SecondTwist03Joint+'.translate' )
    cmds.connectAttr( SecondIN+'.rotate', SecondTwist01Joint+'.rotate' )
    SecondTwist02OriCon = cmds.orientConstraint( SecondTwist01Joint, SecondTwist03Joint, SecondTwist02Joint )
    cmds.setAttr( SecondTwist02OriCon[0]+'.interpType', 2 )
    
    
    # -- rename no-longer-needed bind joints and hide no-longer-needed proxy geo
    																											 
    NewFirstJointName = FirstJoint.replace('Jnt','Jx')
    FirstBindJoint = cmds.ls( FirstJoint )
    if FirstBindJoint != []:
        FirstBindJoint = cmds.rename( FirstBindJoint, NewFirstJointName )
        print( 'den_makeTwists ---------', FirstBindJoint, 'renamed to', NewFirstJointName )
    FirstProxy = cmds.ls( FirstJoint.replace('_Jnt','_Mesh' ))
    if FirstProxy != []:
        cmds.setAttr( FirstProxy[0]+'.visibility', 0 )
        print( 'den_makeTwists ---------', FirstProxy[0], 'visibility set to 0' )
    
    NewSecondJointName = SecondJoint.replace('Jnt','Jx')
    SecondBindJoint = cmds.ls( SecondJoint )
    if SecondBindJoint != []:
        SecondBindJoint = cmds.rename( SecondBindJoint, NewSecondJointName )
        print( 'den_makeTwists ---------', SecondBindJoint, 'renamed to', NewSecondJointName )
    SecondProxy = cmds.ls( SecondJoint.replace('_Jnt','_Mesh' ))
    if SecondProxy != []:
        cmds.setAttr( SecondProxy[0]+'.visibility', 0 )
        print( 'den_makeTwists ---------', SecondProxy[0], 'visibility set to 0' )
    
        
    TwistBindJoints += [ FirstTwist01Joint, FirstTwist02Joint, FirstTwist03Joint, SecondTwist01Joint, SecondTwist02Joint, SecondTwist03Joint ]
    TwistCtrlsALL += FirstTwist01UpCtrl
    
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return TwistRigGrp, TwistSpaceINs, TwistSpaceOUTs, TwistBindJoints, TwistCtrlsALL, TwistGutsALL


# ---------------------------------------------------------------------------------------
# define Stretchy rig creation command

def den_makeStretchy( side='L_', prefix='', name='Arm', Joints=['Shld','Elbow','Wrist'], dpTime = 0.01 ):
    #--------------------- testing variables
    #side = 'L_'
    #prefix = ''
    #name = 'Arm'
    #radius=2.0
    #Joints=['Shld','Elbow','Wrist']
    #dpTime = 0.01
    #---------------------
    
    print( '\nden_makeStretchy -- WARNING -- Stretchy does not build a separate rig part, but modifies the existing limb.' )
    print( '                             If it fails, you will likely need to bebuild the limb before trying again.' )
        
    # - find rest x trans of elbow and wrist joint
    FirstRestLen = cmds.getAttr( side+prefix+Joints[1]+'_Jnt'+'.translateX' )
    FirstRestLenAttr = side+prefix+name+Joints[0]+'_RestLength'
    SecondRestLen = cmds.getAttr( side+prefix+Joints[2]+'_Jnt'+'.translateX' )
    SecondRestLenAttr = side+prefix+name+Joints[1]+'_RestLength'
    LimbRestLen = FirstRestLen+SecondRestLen; print( LimbRestLen )
    LimbRestLenAttr = side+prefix+name+'_RestLength'
    
    # - add the rest length value as attr to the Ctrl
    #cmds.select( side+prefix+Joints[2]+'_Ctrl' )
    cmds.addAttr( side+prefix+Joints[2]+'_Ctrl', longName=FirstRestLenAttr, attributeType='float', defaultValue=FirstRestLen )
    cmds.setAttr ( side+prefix+Joints[2]+'_Ctrl'+'.'+FirstRestLenAttr, lock=True, channelBox=True )
    cmds.addAttr( side+prefix+Joints[2]+'_Ctrl', longName=SecondRestLenAttr, attributeType='float', defaultValue=SecondRestLen )
    cmds.setAttr ( side+prefix+Joints[2]+'_Ctrl'+'.'+SecondRestLenAttr, lock=True, channelBox=True )
    cmds.addAttr( side+prefix+Joints[2]+'_Ctrl', longName=LimbRestLenAttr, attributeType='float', defaultValue=LimbRestLen )
    cmds.setAttr ( side+prefix+Joints[2]+'_Ctrl'+'.'+LimbRestLenAttr, lock=True, channelBox=True )
    
    # - make a distanceBetween node and connect the First joint and the Ctrl world matrix outs to it
    # -- this will output the distance between them
    
    distNode = cmds.shadingNode( 'distanceBetween', asUtility=True, n=side+prefix+name+Joints[0]+'2'+Joints[2]+'_distanceBetween' ); print( distNode )
    cmds.connectAttr( side+prefix+Joints[0]+'_Jnt.worldMatrix', distNode+'.inMatrix1' )
    cmds.connectAttr( side+prefix+Joints[2]+'_Ctrl.worldMatrix', distNode+'.inMatrix2' )
    
    # - use multiplyDivide to divide distance by rest distance
    divNode = cmds.shadingNode( 'multiplyDivide', asUtility=True, n=side+prefix+name+'_HyperExtendAmount_multiplyDivide' ); print( divNode )
    cmds.connectAttr( distNode+'.distance', divNode+'.input1X' )
    cmds.connectAttr( side+prefix+Joints[2]+'_Ctrl.'+LimbRestLenAttr, divNode+'.input2X' )
    cmds.setAttr( divNode+'.operation', 2 )
    
    # - use clamp to limit results between 1 and whatever upper limit you want (I chose 10)
    clampNode = cmds.shadingNode( 'clamp', asUtility=True, n=side+prefix+name+'_clamp' ); print( divNode )
    cmds.connectAttr( divNode+'.outputX', clampNode+'.inputR' )
    cmds.setAttr( clampNode+'.minR', 1 )
    cmds.setAttr( clampNode+'.maxR', 10 )
    
    # - multiply clamp result by rest distance for elbow and wrist to find stretched distance
    multNode = cmds.shadingNode( 'multiplyDivide', asUtility=True, n=side+prefix+name+'_StretchedLength_multiplyDivide' ); print( multNode )
    cmds.connectAttr( side+prefix+Joints[2]+'_Ctrl'+'.'+FirstRestLenAttr,  multNode+'.input1X' )
    cmds.connectAttr( side+prefix+Joints[2]+'_Ctrl'+'.'+SecondRestLenAttr,  multNode+'.input1Y' )
    cmds.connectAttr( clampNode+'.outputR',  multNode+'.input2X' )
    cmds.connectAttr( clampNode+'.outputR',  multNode+'.input2Y' )
    
    # - connect stretched distance to x trans of elbow joint
    cmds.select( side+prefix+Joints[1]+'_Jnt' )
    denUt.den_Lock(  0,1,1 , 0,0,0 , 1,1,1 , 0 )
    cmds.select( side+prefix+Joints[2]+'_Jnt' )
    denUt.den_Lock(  0,1,1 , 0,0,0 , 1,1,1 , 0 )
    cmds.connectAttr( multNode+'.outputX', side+prefix+Joints[1]+'_Jnt'+'.translateX', f=True )
    cmds.connectAttr( multNode+'.outputY', side+prefix+Joints[2]+'_Jnt'+'.translateX', f=True )
    cmds.select( side+prefix+Joints[1]+'_Jnt' )
    denUt.den_Lock(  1,1,1 , 0,0,0 , 1,1,1 , 0 )
    cmds.select( side+prefix+Joints[2]+'_Jnt' )
    denUt.den_Lock(  1,1,1 , 0,0,0 , 1,1,1 , 0 )





# ---------------------------------------------------------------
# - define ribbon builder for use in ribbon-based twist setup
'''
def CAAR_rigRibbon_v03(count, name, size, dpTime = 0.01 ):
    # Clear selection.
    cmds.select(clear=True)

    # Set count to minimum of five.
    count = max(count, 5)

    # Create basename.
    base = name + 'Ribbon'

    # Create the ribbon geo.
    cmds.polyPlane(w=(0.05*size), h=size, sx=1, sy=(count - 1), ax=[0,0,1], cuv=1, ch=0, n=(base + '_geo'))

    # Create controls.
    parts = ['Root', 'Mid', 'End']

    for i in range(3):
        cmds.select(clear=True)
        cmds.joint(n=(base + parts[i] + '_Jx'), rad=(0.1*size))
        cmds.circle(c=[0,0,0], nr=[0,1,0], sw=360, r=(0.1*size), d=3, ut=0, tol=0.01, s=8, ch=0, n=(base + parts[i] + '_Ctrl'))
        cmds.parent((base + parts[i] + '_Jx'), (base + parts[i] + '_Ctrl'))
        cmds.group(n=(base + parts[i] + '_Grp'), em=True)
        cmds.parent((base + parts[i] + '_Ctrl'), (base + parts[i] + '_Grp'))
        cmds.move(0, (0.5*(-1+1*i)*size), 0, (base + parts[i] + '_Grp'))
        #cmds.makeIdentity((base + parts[i] + '_Grp'), apply=True, t=1, r=1, s=1, n=0, pn=1)

    # Bind the ribbon geo to the control joints.
    cmds.skinCluster((base + '*_Jx'), (base + '_geo'), bm=0, dr=2.2, mi=2, nw=1, omi=True, sm=0, wd=0, n=(base + 'SkinCluster'))

    # Create and group follicles on ribbon.
    zeroConstant = cmds.createNode('floatConstant', n=(base + '_floatConstant'))
    Uval = (0.5)
    cmds.setAttr((zeroConstant+'.inFloat'), Uval)
    uvPin = cmds.createNode('uvPin', n=(base + '_uvPin'))
    cmds.connectAttr((base + '_geoShapeOrig.outMesh'), (uvPin+'.originalGeometry'))
    cmds.connectAttr((base + '_geoShape.outMesh'), (uvPin+'.deformedGeometry'))

    for i in range(count):
        nnum = '{:02d}'.format(i+1) # creates a 2 digit zero-padded string
        Vval = float(i)/(count-1)
        pin = cmds.spaceLocator(n=(base+nnum+'_pin'), r=True )
        cmds.setAttr( pin[0]+'.localScaleX', (0.05*size) )
        cmds.setAttr( pin[0]+'.localScaleY', (0.05*size) )
        cmds.setAttr( pin[0]+'.localScaleZ', (0.05*size) )
        cmds.connectAttr((zeroConstant+'.inFloat'), (uvPin+'.coordinate[{}].coordinateU'.format(i)))
        cmds.setAttr((uvPin+'.coordinate[{}].coordinateV'.format(i)), Vval)
        cmds.connectAttr((uvPin+'.outputMatrix[{}]'.format(i)), (pin[0]+'.offsetParentMatrix'))
        if (i==(count-1)):
            cmds.joint(n=(base+nnum+'_End'), rad=(size / 30))
        else:
            cmds.joint(n=(base+nnum+'_Jnt'), rad=(size / 20))
    # group -n ($base + 'Follicles_Grp') ($base + '_fol*');
    cmds.group(n=(base + 'Pins_Grp'), em=True)
    cmds.parent((base + '*_pin'), (base + 'Pins_Grp'))

    # Group everything together and turn off inherit transformations.
    cmds.group((base + '_geo'), (base + 'Root_Grp'), (base + 'Mid_Grp'), (base + 'End_Grp'), (base + 'Pins_Grp'), n=(base + '_Grp'))
    cmds.setAttr((base + 'Pins_Grp.inheritsTransform'), 0)
    cmds.setAttr((base + '_geo.inheritsTransform'), 0)
    cmds.move(0, (-0.5*size), 0, (base + '_Grp.sp'), (base + '_Grp.rp'))

    # Clear selection.
    cmds.select(clear=True)
'''
'''
def CAAR_rigRibbon_v03(count, name, size):
    # Clear selection.
    cmds.select(clear=True)

    # Set count to minimum of five.
    count = max(count, 5)

    # Create basename.
    base = name + 'Ribbon'

    # Create the ribbon geo.
    cmds.polyPlane(w=(0.05*size), h=size, sx=1, sy=(count - 1), ax=[0,0,1], cuv=1, ch=0, n=(base + '_geo'))
    cmds.addAttr( base+'_geo', longName='Uval', attributeType='float', defaultValue=0.5 )

    # Create controls.
    parts = ['Root', 'Mid', 'End']

    for i in range(3):
        cmds.select(clear=True)
        cmds.joint(n=(base + parts[i] + '_Jx'), rad=(0.1*size))
        cmds.circle(c=[0,0,0], nr=[0,1,0], sw=360, r=(0.1*size), d=3, ut=0, tol=0.01, s=8, ch=0, n=(base + parts[i] + '_Ctrl'))
        cmds.parent((base + parts[i] + '_Jx'), (base + parts[i] + '_Ctrl'))
        cmds.group(n=(base + parts[i] + '_Grp'), em=True)
        cmds.parent((base + parts[i] + '_Ctrl'), (base + parts[i] + '_Grp'))
        cmds.move(0, (0.5*(-1+1*i)*size), 0, (base + parts[i] + '_Grp'))
        #cmds.makeIdentity((base + parts[i] + '_Grp'), apply=True, t=1, r=1, s=1, n=0, pn=1)

    # Bind the ribbon geo to the control joints.
    cmds.skinCluster((base + '*_Jx'), (base + '_geo'), bm=0, dr=2.2, mi=2, nw=1, omi=True, sm=0, wd=0, n=(base + 'SkinCluster'))

    # Create and group follicles on ribbon.
    
    #zeroConstant = cmds.createNode('floatConstant', n=(base + '_floatConstant'))
    #Uval = (0.5)
    #cmds.setAttr((zeroConstant+'.inFloat'), Uval)
    uvPin = cmds.createNode('uvPin', n=(base + '_uvPin'))
    cmds.connectAttr((base + '_geoShapeOrig.outMesh'), (uvPin+'.originalGeometry'))
    cmds.connectAttr((base + '_geoShape.outMesh'), (uvPin+'.deformedGeometry'))

    for i in range(count):
        nnum = '{:02d}'.format(i+1) # creates a 2 digit zero-padded string
        Vval = float(i)/(count-1)
        pin = cmds.spaceLocator(n=(base+nnum+'_Pin'), r=True )
        cmds.setAttr( pin[0]+'.localScaleX', (0.05*size) )
        cmds.setAttr( pin[0]+'.localScaleY', (0.05*size) )
        cmds.setAttr( pin[0]+'.localScaleZ', (0.05*size) )
        cmds.connectAttr((base+'_geo.Uval'), (uvPin+'.coordinate[{}].coordinateU'.format(i)))
        cmds.setAttr((uvPin+'.coordinate[{}].coordinateV'.format(i)), Vval)
        cmds.connectAttr((uvPin+'.outputMatrix[{}]'.format(i)), (pin[0]+'.offsetParentMatrix'))
        if (i==(count-1)):
            cmds.joint(n=(base+nnum+'_Jnt'), rad=(size / 30))
        else:
            cmds.joint(n=(base+nnum+'_Jnt'), rad=(size / 20))
    # group -n ($base + 'Follicles_Grp') ($base + '_fol*');
    cmds.group(n=(base + 'Pins_Grp'), em=True)
    cmds.parent((base + '*_Pin'), (base + 'Pins_Grp'))

    # Group everything together and turn off inherit transformations.
    cmds.group((base + '_geo'), (base + 'Root_Grp'), (base + 'Mid_Grp'), (base + 'End_Grp'), (base + 'Pins_Grp'), n=(base + '_Grp'))
    cmds.setAttr((base + 'Pins_Grp.inheritsTransform'), 0)
    cmds.setAttr((base + '_geo.inheritsTransform'), 0)
    cmds.move(0, (-0.5*size), 0, (base + '_Grp.sp'), (base + '_Grp.rp'))

    # Clear selection.
    cmds.select(clear=True)
'''
#CAAR_rigRibbon_v03(6, 'L_Shld', 30)


# ---------------------------------------------------------------------------------------
# define Ribbon rig creation command

def den_makeRibbons( side='L_', prefix='', name='Arm', radius=2.0, Joints=['Shld','Elbow','Wrist'], ctrlPos=(-10,0,-10), ctrlUpVec=(0,0,-1), count=7, displayLocalAxis=True, dpTime = 0.01 ):
    #--------------------- testing variables
    #side='L_'
    #name='Arm'
    #radius=2.0
    #Joints=['Shld','Elbow','Wrist']
    #ctrlPos=(-10,0,-10)
    #ctrlUpVec=(0,0,-1)
    #displayLocalAxis=True
    #---------------------
    
    sideColor = 6
    
    if side == 'R_':
        sideColor = 13
    
    # -- make the Twist rig top group - coming soon
    #TwistRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Twist_Grp', pos=(0,0,0) )
    TwistRigGrp = ''
    
    # -- set up the return variables
    TwistSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    TwistSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    TwistBindJoints = [] #Set list variable to hold names of all the Jx joints
    TwistCtrlsALL = [] #Set list variable to hold names of all the controls
    TwistGutsALL = [] #Set list variable to hold names of all the guts
    
    FirstName = side+prefix+Joints[0]
    SecondName = side+prefix+Joints[1]
    ThirdName = side+prefix+Joints[2]
    
    FirstJoint = cmds.ls( FirstName+'_Jnt' )[0]
    FirstParent = cmds.listRelatives( FirstJoint, parent=True, fullPath=True )[0]
    SecondJoint = cmds.ls( SecondName+'_Jnt' )[0]
    ThirdJoint = cmds.ls( ThirdName+'_Jnt' )[0]
    #print( FirstParent, FirstJoint, SecondJoint, ThirdJoint )
    
    print( '\nden_makeRibbons -- WARNING -- den_makeRibbons does not build a separate rig part, but modifies the existing limb.' )
    print( '                             If it fails, you will likely need to bebuild the limb before trying again.' )
    
    # - these variables are for future upgrades - currently they are redundant
    FirstIN = FirstJoint
    SecondIN = SecondJoint
    ThirdIN = ThirdJoint
    
    FirstTwist01Joint = cmds.joint( n=FirstName+'Twist01_Jx', radius=radius )
    FirstTwist01Joint = cmds.parent( FirstTwist01Joint, FirstIN, relative=True )[0]
    FirstTwist01Joint = cmds.parent( FirstTwist01Joint, FirstParent )[0]
    
    
    FirstRestJoint = cmds.duplicate( FirstTwist01Joint, n=FirstName+'Rest_Jx' )[0]
    FirstUpCarJoint = cmds.duplicate( FirstRestJoint, n=FirstName+'UpCar_Jx' )[0]
    FirstTwist01UpCtrl = denUt.den_MakePole( nodeName=FirstName+'Twist01Up_Ctrl' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ctrlPos, relative=True, ws=True )
    FirstTwist01UpCtrl = cmds.parent( FirstTwist01UpCtrl, FirstUpCarJoint, relative=True )[0]
    FirstTwist01UpCtrl = denUt.den_AddZeroNull()
    FirstTwist01UpCtrlZero = cmds.listRelatives( FirstTwist01UpCtrl, parent=True, fullPath=True )[0]
    
    if ( displayLocalAxis ):
        cmds.setAttr( FirstTwist01Joint+'.displayLocalAxis', 1 )
    
    
    # -- make the constraints
    
    # - set up a carrier for the shoulder up that stays mostly out of the way, rotates in y only
    FirstUpCarJointOriCon = cmds.orientConstraint( FirstIN, FirstRestJoint, FirstUpCarJoint )[0]
    cmds.setAttr( FirstUpCarJointOriCon+'.interpType', 2 )
    cmds.disconnectAttr( FirstUpCarJointOriCon+'.constraintRotateX', FirstUpCarJoint+'.rotateX' )
    cmds.disconnectAttr( FirstUpCarJointOriCon+'.constraintRotateZ', FirstUpCarJoint+'.rotateZ' )
    # - set up the First Twist01 so it does not twist with the Second
    cmds.aimConstraint( SecondIN, FirstTwist01Joint, upVector=ctrlUpVec, maintainOffset=False, worldUpType='object', worldUpObject=FirstTwist01UpCtrl[0] )
    
    
    FirstSize = cmds.getAttr( SecondJoint+'.translateX' )
    #print( size )
    caarUt.CAAR_rigRibbon_v03(count, FirstName, FirstSize)
    
    cmds.parent( FirstName+'Ribbon_Grp', side+prefix+name+'_Grp' )
    cmds.parent( FirstName+'RibbonRoot_Grp', FirstTwist01Joint, relative=True )
    cmds.parent( FirstName+'RibbonMid_Grp', FirstTwist01Joint, relative=True )
    cmds.parent( FirstName+'RibbonEnd_Grp', FirstJoint, relative=True )
    cmds.xform( FirstName+'RibbonRoot_Grp', t=( 0, 0, 0 ), ro=( 0.0, 0.0, -90.0 ), s=( 1.0, 1.0, 1.0 ) )
    cmds.xform( FirstName+'RibbonEnd_Grp', t=( 0, 0, 0 ), ro=( 0.0, 0.0, -90.0 ), s=( 1.0, 1.0, 1.0 ) )
    cmds.connectAttr( SecondJoint+'.translateX', FirstName+'RibbonEnd_Grp.translateX' )
    cmds.parentConstraint( FirstName+'RibbonRoot_Grp', FirstName+'RibbonEnd_Grp', FirstName+'RibbonMid_Grp', mo=False )
    
    TwistBindJoints += [ FirstName+'Ribbon01_Jnt', FirstName+'Ribbon02_Jnt', FirstName+'Ribbon03_Jnt', FirstName+'Ribbon04_Jnt', FirstName+'Ribbon05_Jnt' ]
    
    
    SecondSize = cmds.getAttr( ThirdJoint+'.translateX' )
    #print( size )
    caarUt.CAAR_rigRibbon_v03(count, SecondName, SecondSize)
    
    cmds.parent( SecondName+'Ribbon_Grp', side+prefix+name+'_Grp' )
    cmds.parent( SecondName+'RibbonRoot_Grp', SecondJoint, relative=True )
    cmds.parent( SecondName+'RibbonMid_Grp', SecondJoint, relative=True )
    cmds.parent( SecondName+'RibbonEnd_Grp', SecondJoint, relative=True )
    cmds.xform( SecondName+'RibbonRoot_Grp', t=( 0, 0, 0 ), ro=( 0.0, 0.0, -90.0 ), s=( 1.0, 1.0, 1.0 ) )
    cmds.xform( SecondName+'RibbonEnd_Grp', t=( 0, 0, 0 ), ro=( 0.0, 0.0, -90.0 ), s=( 1.0, 1.0, 1.0 ) )
    cmds.connectAttr( ThirdJoint+'.translateX', SecondName+'RibbonEnd_Grp.translateX' )
    cmds.connectAttr( ThirdJoint+'.rotateX', SecondName+'RibbonEnd_Grp.rotateY' )
    cmds.parentConstraint( SecondName+'RibbonRoot_Grp', SecondName+'RibbonEnd_Grp', SecondName+'RibbonMid_Grp', mo=False )
    
    TwistBindJoints += [ SecondName+'Ribbon01_Jnt', SecondName+'Ribbon02_Jnt', SecondName+'Ribbon03_Jnt', SecondName+'Ribbon04_Jnt', SecondName+'Ribbon05_Jnt' ]
    
    
    
    # -- rename no-longer-needed bind joints and hide no-longer-needed proxy geo
    																											 
    #FirstBindJointName = FirstJoint.replace('Jx','Jnt')
    NewFirstJointName = FirstJoint.replace('Jnt','Jx')
    FirstBindJoint = cmds.ls( FirstJoint )
    if FirstBindJoint != []:
        FirstBindJoint = cmds.rename( FirstBindJoint, NewFirstJointName )
        print( 'den_makeTwists ---------', FirstBindJoint, 'renamed to', NewFirstJointName )
    FirstProxy = cmds.ls( FirstJoint.replace('_Jnt','_Mesh' ))
    if FirstProxy != []:
        cmds.setAttr( FirstProxy[0]+'.visibility', 0 )
        print( 'den_makeTwists ---------', FirstProxy[0], 'visibility set to 0' )
    
    #SecondBindJointName = SecondJoint.replace('Jx','Jnt')
    NewSecondJointName = SecondJoint.replace('Jnt','Jx')
    SecondBindJoint = cmds.ls( SecondJoint )
    if SecondBindJoint != []:
        SecondBindJoint = cmds.rename( SecondBindJoint, NewSecondJointName )
        print( 'den_makeTwists ---------', SecondBindJoint, 'renamed to', NewSecondJointName )
    SecondProxy = cmds.ls( SecondJoint.replace('_Jnt','_Mesh' ))
    if SecondProxy != []:
        cmds.setAttr( SecondProxy[0]+'.visibility', 0 )
        print( 'den_makeTwists ---------', SecondProxy[0], 'visibility set to 0' )
    
        
    TwistCtrlsALL += FirstTwist01UpCtrl
    
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return TwistRigGrp, TwistSpaceINs, TwistSpaceOUTs, TwistBindJoints, TwistCtrlsALL, TwistGutsALL




# ---------------------------------------------------------------------------------------
# define Biped Arm rig creation command

def den_makeBipedArmRig( side='L_', prefix='', name='Arm', radius=2.0, ctrlRadius=10.0, displayLocalAxis=False, twistType='none', dpTime=0.01, size=100 ):
    #--------------------- testing variables    
    #side = 'L_'
    #prefix=''
    #name='Arm'
    #radius=2.0
    #ctrlRadius=10.0
    #displayLocalAxis=False
    #twistType='none'
    #dpTime=0.01
    #size=100
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
    
    
    # -- make the Arm rig top group
    ArmRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp', pos=(0,0,0) )
    
    # -- set up the return variables
    ArmSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    ArmSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    ArmBindJoints = [] #Set list variable to hold names of all the _Jnt Bind joints
    ArmCtrlsALL = [] #Set list variable to hold names of all the controls
    ArmGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Arm SpaceINs
    HeadSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Head_SpaceIN', pos=(0,0,0) )
    HeadSpaceIN = cmds.parent( HeadSpaceIN, ArmRigGrp )[0]
    ChestSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Chest_SpaceIN', pos=(0,0,0) )
    ChestSpaceIN = cmds.parent( ChestSpaceIN, ArmRigGrp )[0]
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Pelvis_SpaceIN', pos=(0,0,0) )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, ArmRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Cog_SpaceIN', pos=(0,0,0) )
    CogSpaceIN = cmds.parent( CogSpaceIN, ArmRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'All_SpaceIN', pos=(0,0,0) )
    AllSpaceIN = cmds.parent( AllSpaceIN, ArmRigGrp )[0]
    # add all the SpaceINs to the list
    ArmSpaceINs += [ HeadSpaceIN, ChestSpaceIN, PelvisSpaceIN, CogSpaceIN, AllSpaceIN ]
    
    # -- make groups to hold the skeleton and the controls
    ArmSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp', pos=(0,0,0) )
    ArmSkelGrp = cmds.parent( ArmSkelGrp, ChestSpaceIN )
    ArmCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp', pos=(0,0,0) )
    ArmCtrlGrp = cmds.parent( ArmCtrlGrp, ChestSpaceIN )
    
    # -- make Wrist control space switcher
    WristCtrlSpace = denUt.den_makeGrp( nodeName=side+prefix+'WristCtrl_Space', pos=(0,0,0) )
    WristCtrlSpace = cmds.parent( WristCtrlSpace, ArmCtrlGrp )
    WristCtrlSpaceConstraint = cmds.parentConstraint( HeadSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( ChestSpaceIN, WristCtrlSpace, weight=1 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( PelvisSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( CogSpaceIN, WristCtrlSpace, weight=0 )
    WristCtrlSpaceConstraint = cmds.parentConstraint( AllSpaceIN, WristCtrlSpace, weight=0 )
    
        
    # -- set variables for pivot positions
    
    ClavPos = cmds.xform( side+prefix+'Clav_Piv', ws=True, q=True, t=True )
    ShldPos = cmds.xform( side+prefix+'Shld_Piv', ws=True, q=True, t=True )
    ElbowPos = cmds.xform( side+prefix+'Elbow_Piv', ws=True, q=True, t=True )
    WristPos = cmds.xform( side+prefix+'Wrist_Piv', ws=True, q=True, t=True )
    ElbowPolePos = cmds.xform( side+prefix+'ElbowPole_Loc', ws=True, q=True, t=True )
    Scap01Pos = cmds.xform( side+prefix+'Scap01_Piv', ws=True, q=True, t=True )
    Scap02Pos = cmds.xform( side+prefix+'Scap02_Piv', ws=True, q=True, t=True )
    
    # -- make the joints
    cmds.select( clear=True )
    ClavJoint = cmds.joint( n=side+prefix+'Clav_Jnt', p=(ClavPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    ClavJoint = cmds.parent( ClavJoint, ArmSkelGrp )[0]
    ShldJoint = cmds.joint( n=side+prefix+'Shld_Jnt', p=(ShldPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    ElbowJoint = cmds.joint( n=side+prefix+'Elbow_Jnt', p=(ElbowPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    WristJoint = cmds.joint( n=side+prefix+'Wrist_Jnt', p=(WristPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    
    if ( displayLocalAxis ):
        cmds.setAttr( ClavJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ShldJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ElbowJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( WristJoint+'.displayLocalAxis', 1 )
    
    cmds.select( clear=True )
    Scap01Joint = cmds.joint( n=side+prefix+'Scap01_Jx', p=(Scap01Pos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    Scap01Joint = cmds.parent( Scap01Joint, ArmSkelGrp )[0]
    Scap02Joint = cmds.joint( n=side+prefix+'Scap02_Jnt', p=(Scap02Pos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    Scap03Joint = cmds.joint( n=side+prefix+'Scap02_end', p=(ShldPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    
    if ( displayLocalAxis ):
        cmds.setAttr( Scap01Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Scap02Joint+'.displayLocalAxis', 1 )
        cmds.setAttr( Scap03Joint+'.displayLocalAxis', 1 )
    
    # -- orient the joints
    
    cmds.select( clear=True )
    cmds.joint( ClavJoint, e=True, oj='xyz', secondaryAxisOrient='yup', zso=True )
    
    cmds.select( clear=True )
    #cmds.joint( ElbowJoint, e=True, oj='xyz', zso=True )
    cmds.joint( ElbowJoint, e=True, oj='xzy', secondaryAxisOrient='ydown', aos=True, ch=False, zso=True )
    cmds.joint( WristJoint, e=True, oj='none', zso=True )
    ShldJoint = cmds.parent( ShldJoint, side+prefix+'Shld_Piv' ) # -- temp reparent shoulder under planar space
    cmds.joint( ShldJoint, e=True, oj='none', zso=True ) # -- orient joint
    ShldJoint = cmds.parent( ShldJoint, ClavJoint )[0] # -- put shoulder back under clav
    
    cmds.select( clear=True )
    #cmds.joint( Scap02Joint, e=True, oj='xyz', zso=True )
    cmds.joint( Scap02Joint, e=True, oj='xzy', secondaryAxisOrient='ydown', aos=True, ch=False, zso=True )
    cmds.joint( Scap03Joint, e=True, oj='none', zso=True )
    Scap01Joint = cmds.parent( Scap01Joint, side+prefix+'Scap01_Piv' ) # -- temp reparent scap under planar space
    cmds.joint( Scap01Joint, e=True, oj='none', zso=True )
    Scap01Joint = cmds.parent( Scap01Joint, ArmSkelGrp )[0] # -- put scap back
    
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
    
    # -- Shoulder IK Control
    ShldCtrl = denUt.den_MakeCube( nodeName=side+prefix+'Shld_Ctrl', pos=(0,0,0) ,radius=0.8*ctrlRadius, doT=False)
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ShldPos )
    ShldCtrl = cmds.parent( ShldCtrl, ArmCtrlGrp )
    ShldCtrl = denUt.den_AddZeroNull()
    ShldCtrlZero = cmds.listRelatives( ShldCtrl, parent=True, fullPath=True )
    ArmCtrlsALL += ShldCtrl # add to the controls list
    
    # -- Shoulder FK Control
    ShldFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'ShldFK_Ctrl', pos=(0,0,0) ,radius=ctrlRadius, doT=False, axis='-Z' )
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
    ArmUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(4,12,0), radius=ctrlRadius*0.2, doT=False, Plane='XY' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ArmUtilCtrl = cmds.parent( ArmUtilCtrl, ShldCtrl, relative=True )
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+name+'_FK_IK', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', lock=False, keyable=True )
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+'Wrist_FK_IK', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+'Wrist_FK_IK', lock=False, keyable=True )
    ArmCtrlsALL += ArmUtilCtrl # add to the controls list
    
    # -- Elbow IK Controls
    ElbowCtrl = denUt.den_MakePole( nodeName=side+prefix+'Elbow_Ctrl', pos=(0,0,0) , radius=ctrlRadius*0.4, doT=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=ElbowPolePos )
    ElbowCtrl = cmds.parent( ElbowCtrl, ArmCtrlGrp )
    ElbowCtrl = denUt.den_AddZeroNull()
    ArmCtrlsALL += ElbowCtrl # add to the controls list
    
    # -- Elbow FK Controls
    ElbowFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'ElbowFK_Ctrl', pos=(0,-4,0), radius=ctrlRadius*0.4, doT=True, axis='-Y', flip=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ElbowJointFK, relative=True )
    ElbowFKCtrl = cmds.parent( ElbowFKCtrl, ShldFKCtrl )
    ElbowFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( ElbowFKCtrl[0]+'.rotate', ElbowJointFK+'.rotate' )
    ArmCtrlsALL += ElbowFKCtrl # add to the controls list
    
    # -- Wrist IK Controls
    WristCtrl = denUt.den_MakeBall( nodeName=side+prefix+'Wrist_Ctrl', pos=(0,0,0), radius=ctrlRadius*0.7, doT=False )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=WristPos )
    WristCtrl = cmds.parent( WristCtrl, WristCtrlSpace )
    WristCtrl = denUt.den_AddZeroNull()
    WristCtrlZero = cmds.listRelatives( WristCtrl, parent=True, fullPath=True )
    ArmCtrlsALL += WristCtrl # add to the controls list
    
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
    ArmCtrlsALL += WristFKCtrl # add to the controls list
    
    # -- set up IK/FK blending for wrist
    WristCtrlZeroDupA = cmds.duplicate( WristFKCtrlZero, name=side+prefix+'WristFK_CtrlZeroA', parentOnly=True )[0]
    WristCtrlZeroDupA = cmds.parent( WristCtrlZeroDupA, ElbowJoint )
    WristCtrlZeroDupB = cmds.duplicate( WristFKCtrlZero, name=side+prefix+'WristFK_CtrlZeroB', parentOnly=True )[0]
    WristCtrlZeroDupB = cmds.parent( WristCtrlZeroDupB, WristCtrl )
    cmds.setAttr( WristCtrlZeroDupB[0]+'.rotate', 90,0,-90 )
    cmds.pointConstraint( WristCtrlZeroDupA, WristFKCtrlZero )
    WristFKCtrlZeroOriCon = cmds.orientConstraint( WristCtrlZeroDupA, WristFKCtrlZero, weight=1 )
    WristFKCtrlZeroOriCon = cmds.orientConstraint( WristCtrlZeroDupB, WristFKCtrlZero, weight=0 )
    cmds.setAttr( WristFKCtrlZeroOriCon[0]+'.interpType', 2 )
    cmds.setAttr( WristJoint+'.rotateOrder', 1 )
    cmds.orientConstraint( WristFKCtrl, WristJoint )
    
    # -- connect up the IK Wrist control space switcher
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+'HeadSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+'HeadSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+'HeadSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Head_SpaceINW0' )
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+'ChestSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+'ChestSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+'ChestSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Chest_SpaceINW1' )
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+'PelvisSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Pelvis_SpaceINW2' )
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+'CogSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'Cog_SpaceINW3' )
    cmds.addAttr( ArmUtilCtrl, longName=side+prefix+'AllSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( ArmUtilCtrl[0]+'.'+side+prefix+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+'AllSpace', WristCtrlSpaceConstraint[0]+'.'+side+prefix+'All_SpaceINW4' )
    
    # -- set up Arm FK_IK blending
    Shld_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Shld_ikFk_pairBlend' )
    cmds.setAttr( Shld_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ShldJointFK+'.rotate', Shld_pairBlend+'.inRotate1' )
    cmds.connectAttr( ShldJointIK+'.rotate', Shld_pairBlend+'.inRotate2' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Shld_pairBlend+'.weight' )
    cmds.connectAttr( Shld_pairBlend+'.outRotate', ShldJoint+'.rotate' )
    
    Elbow_pairBlend = cmds.shadingNode ('pairBlend', asUtility=True, n=side+prefix+'Elbow_ikFk_pairBlend' )
    cmds.setAttr( Elbow_pairBlend+'.rotInterpolation', 1 ) # -- set rotation interp to quaternion
    cmds.connectAttr( ElbowJointFK+'.rotate', Elbow_pairBlend+'.inRotate1' )
    cmds.connectAttr( ElbowJointIK+'.rotate', Elbow_pairBlend+'.inRotate2' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Elbow_pairBlend+'.weight' )
    cmds.connectAttr( Elbow_pairBlend+'.outRotate', ElbowJoint+'.rotate' )
    
    # -- set up Wrist FK_IK blending
    WristFKCtrlZeroOC = cmds.listRelatives( WristFKCtrlZero, type='orientConstraint', fullPath=True)
    Wrist_multiplyDivide = cmds.shadingNode ('multiplyDivide', asUtility=True, n=side+prefix+'Wrist_ikFk_multiplyDivide' )
    Wrist_reverse = cmds.shadingNode ('reverse', asUtility=True, n=side+prefix+'Wrist_ikFk_reverse' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+name+'_FK_IK', Wrist_multiplyDivide+'.input1X' )
    cmds.connectAttr( ArmUtilCtrl[0]+'.'+side+prefix+'Wrist_FK_IK', Wrist_multiplyDivide+'.input2X' )
    cmds.connectAttr( Wrist_multiplyDivide+'.outputX', Wrist_reverse+'.inputX' )
    cmds.connectAttr( Wrist_multiplyDivide+'.outputX', WristFKCtrlZeroOC[0]+'.'+side+prefix+'WristFK_CtrlZeroBW1' )
    cmds.connectAttr( Wrist_reverse+'.outputX', WristFKCtrlZeroOC[0]+'.'+side+prefix+'WristFK_CtrlZeroAW0' )
    
    # -- make the ik handles
    #print( ShldJointIK, WristJointIK, ClavJoint, ShldJoint, Scap01Joint, Scap03Joint )
    ArmIKhandle = cmds.ikHandle( startJoint=ShldJointIK, endEffector=WristJointIK, solver='ikRPsolver', setupForRPsolver=True, name=ShldJointIK.replace('IK','Ikh') )
    #print( ArmIKhandle )
    cmds.rename( ArmIKhandle[1], ArmIKhandle[0].replace('Ikh','Eff') )
    ArmIKhandle = cmds.parent( ArmIKhandle[0], WristCtrl )
    cmds.poleVectorConstraint( ElbowCtrl, ArmIKhandle )
    
    ClavIKhandle = cmds.ikHandle( startJoint=ClavJoint, endEffector=ShldJoint, solver='ikSCsolver', name=ClavJoint.replace('Jnt','Ikh') )
    #print( ClavIKhandle )
    cmds.rename( ClavIKhandle[1], ClavIKhandle[0].replace('Ikh','Eff') )
    ClavIKhandle = cmds.parent( ClavIKhandle[0], ShldCtrl )
    
    ScapIKhandle = cmds.ikHandle( startJoint=Scap01Joint, endEffector=Scap03Joint, solver='ikSCsolver', name=Scap01Joint.replace('Jx','Ikh') )
    #print( ScapIKhandle )
    cmds.rename( ScapIKhandle[1], ScapIKhandle[0].replace('Ikh','Eff') )
    ScapIKhandle = cmds.parent( ScapIKhandle[0], ClavJoint )
    
    # -- add the wrist SpaceOUT
    WristSpaceOUT = denUt.den_makeGrp( nodeName=side+prefix+'Wrist_SpaceOUT', pos=(0,0,0) )
    WristSpaceOUT = cmds.parent( WristSpaceOUT, WristJoint )
    ArmSpaceOUTs += WristSpaceOUT
    
    # -- list the joints for binding
    ArmBindJoints = [ ClavJoint, ShldJoint, ElbowJoint, WristJoint, Scap02Joint ]
    
    # --- deal with twist options
    if twistType == 'none':
        print( 'no twist joints added' )
        ArmBindJoints = [ ClavJoint, ShldJoint, ElbowJoint, WristJoint, Scap02Joint ]
        
    if twistType == 'twist':
        ArmTwistRigRet = den_makeTwists( side=side, prefix=prefix, name=name, radius=radius, Joints=['Shld','Elbow','Wrist'], ctrlPos=(-10,0,-10), ctrlUpVec=(0,0,-1), displayLocalAxis=False )
        print( ArmTwistRigRet )
        ArmTwistBindJoints = ArmTwistRigRet[3]; print( ArmTwistBindJoints )
        ArmTwistCtrlsALL = ArmTwistRigRet[4]; print( ArmTwistCtrlsALL )
        ArmBindJoints = [ ClavJoint, WristJoint, Scap02Joint ] + ArmTwistBindJoints
        ArmCtrlsALL += ArmTwistCtrlsALL        
    
    if twistType == 'ribbon':
        ArmRibbonRigRet = den_makeRibbons( side=side, prefix=prefix, name=name, radius=radius, Joints=['Shld','Elbow','Wrist'], ctrlPos=(-10,0,-10), ctrlUpVec=(0,0,-1), displayLocalAxis=False )
        print( ArmRibbonRigRet )
        ArmRibbonBindJoints = ArmRibbonRigRet[3]; print( ArmRibbonBindJoints )
        ArmRibbonCtrlsALL = ArmRibbonRigRet[4]; print( ArmRibbonCtrlsALL )
        ArmBindJoints = [ ClavJoint, WristJoint, Scap02Joint ] + ArmRibbonBindJoints
        ArmCtrlsALL += ArmRibbonCtrlsALL
        
    
    # -- flip the right side back where it belongs
    if side == 'R_':
        cmds.setAttr( ArmRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return ArmRigGrp, ArmSpaceINs, ArmSpaceOUTs, ArmBindJoints, ArmCtrlsALL, ArmGutsALL



# ---------------------------------------------------------------------------------------
# define Biped Hand pivots creation command

def den_makeBipedHandPivs( side='L_', prefix='', name='Hand', radius=1.0, knuckleUpDist=5.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #side='L_'
    #name='Hand'
    #radius=1.0
    #knuckleUpDist=5.0
    #---------------------
    
    HandPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    fingList = [side+prefix+'Thumb',side+prefix+'Index',side+prefix+'Middle',side+prefix+'Ring',side+prefix+'Pinky']
    
    for i,fing in enumerate(fingList):
        
        if fing!=side+prefix+'Thumb':
            denUt.den_makeLoc( nodeName=fing+'00_Piv', pos=(50, 100, -i*5+10), rot=(0,0,0), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
            denUt.den_ColorShape(20)
            cmds.parent( fing+'00_Piv', HandPivGrp )
            denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
            
            denUt.den_makeLoc( nodeName=fing+'01_Piv', pos=(10, 0, 0), rot=(0,0,0), radius=2*radius ); denUt.den_DiagPause( seconds=dpTime )
            denUt.den_ColorShape(20)
            cmds.parent( fing+'01_Piv', fing+'00_Piv', relative=True )
            denUt.den_Lock(  0,1,1 , 0,0,0 , 1,1,1 , 0 )
        else:
            denUt.den_makeLoc( nodeName=fing+'01_Piv', pos=(55, 100, -i*5+10), rot=(60,-45,-15), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
            denUt.den_ColorShape(20)
            cmds.parent( fing+'01_Piv', HandPivGrp )
            denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'02_Piv', pos=(5, 0, 0), rot=(0,0,-10), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(20)
        cmds.parent( fing+'02_Piv', fing+'01_Piv', relative=True )
        denUt.den_Lock(  0,1,1 , 1,1,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'03_Piv', pos=(5, 0, 0), rot=(0,0,-10), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(20)
        cmds.parent( fing+'03_Piv', fing+'02_Piv', relative=True )
        denUt.den_Lock(  0,1,1 , 1,1,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'End_Piv', pos=(5, 0, 0), rot=(0,0,0), radius=0.5*radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(20)
        cmds.parent( fing+'End_Piv', fing+'03_Piv', relative=True )
        denUt.den_Lock(  0,1,1 , 1,1,1 , 1,1,1 , 0 )
    
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( HandPivGrp+'.scaleX', -1 )
    
    print( 'den_makeHandPivs -- done\n' )
    
    return HandPivGrp





# ---------------------------------------------------------------------------------------
# define Biped Hand rig creation command

def den_makeBipedHandRig( side='L_', prefix='', name='Hand', radius=1.0, displayLocalAxis=False, dpTime=0.01, size=100 ):
    #--------------------- testing variables    
    #side = 'L_'
    #name='Hand'
    #radius=1.0
    #displayLocalAxis=True
    #---------------------
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    # -- set up the return variables
    HandSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    HandSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    HandBindJoints = [] #Set list variable to hold names of all the Jx joints
    HandCtrlsALL = [] #Set list variable to hold names of all the controls
    HandGutsALL = [] #Set list variable to hold names of all the guts
    
    
    fingList = [side+prefix+'Thumb',side+prefix+'Index',side+prefix+'Middle',side+prefix+'Ring',side+prefix+'Pinky']
    HandRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp' )
    WristSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Wrist_SpaceIN' )
    WristSpaceIN = cmds.parent( WristSpaceIN, HandRigGrp )
    HandSpaceINs += WristSpaceIN
    HandSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp' )
    HandSkelGrp = cmds.parent( HandSkelGrp, WristSpaceIN )
    HandCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp' )
    HandCtrlGrp = cmds.parent( HandCtrlGrp, WristSpaceIN )
    #print( HandRigGrp, WristSpaceIN, HandSkelGrp, HandCtrlGrp )
    for fing in fingList:
        
        #fing = side+prefix+'Pinky'
        # -- do the palm joints
        if fing==side+prefix+'Thumb':
            fingSkelParent = HandSkelGrp
            fingCtrlParent = HandCtrlGrp
            #print 'thumb'
        else:
            # -- make the palm joints for not-thumbs
            fing00Pos = cmds.xform( fing+'00_Piv', ws=True, q=True, t=True )
            cmds.select( clear=True )
            fing00Joint = cmds.joint( n=fing+'00_Jnt', radius=radius )
            if( displayLocalAxis ):
                cmds.setAttr( fing00Joint+'.displayLocalAxis', 1 )
            fing00Joint = cmds.parent( fing00Joint, fing+'00_Piv', relative=True ) # -- temp reparent finger under planar space
            cmds.joint( fing00Joint, e=True, oj='none', zso=True )
            fing00Joint = cmds.parent( fing00Joint, HandSkelGrp )[0] # -- put finger back
            fing00Ctrl = denUt.den_MakeSpike( nodeName=fing+'00_Ctrl', radius=3*radius, axis='-Y' )
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
            fing00Ctrl = cmds.parent( fing00Ctrl, fing00Joint, relative=True )
            fing00Ctrl = cmds.parent( fing00Ctrl, HandCtrlGrp )
            fing00Ctrl = denUt.den_AddZeroNull()
            denUt.den_LockAttr(True,False,True,False)# relock after parenting
            cmds.connectAttr( fing00Ctrl[0]+'.rotate', fing00Joint+'.rotate' )
            fingSkelParent = fing00Joint
            fingCtrlParent = fing00Ctrl
            #print 'not thumb'
            
        # -- get joint positions
        fing01Pos = cmds.xform( fing+'01_Piv', ws=True, q=True, t=True )
        fing02Pos = cmds.xform( fing+'02_Piv', ws=True, q=True, t=True )
        fing03Pos = cmds.xform( fing+'03_Piv', ws=True, q=True, t=True )
        fingEndPos = cmds.xform( fing+'End_Piv', ws=True, q=True, t=True )
        
        # -- make the joints
        cmds.select( clear=True )
        fing01Joint = cmds.joint( n=fing+'01_Jnt', radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        fing01Joint = cmds.parent( fing01Joint, fing+'01_Piv', relative=True ) # -- temp reparent finger under planar space
        cmds.joint( fing01Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        fing02Joint = cmds.joint( n=fing+'02_Jnt', p=(fing02Pos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        fing03Joint = cmds.joint( n=fing+'03_Jnt', p=(fing03Pos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        fingEndJoint = cmds.joint( n=fing+'_end', p=(fingEndPos), radius=radius*0.5 ); denUt.den_DiagPause( seconds=dpTime )
        cmds.joint( fing02Joint, e=True, oj='xyz', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        cmds.joint( fing03Joint, e=True, oj='xyz', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        cmds.joint( fingEndJoint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        fing01Joint = cmds.parent( fing01Joint, fingSkelParent )[0] # -- put finger back
        
        if( displayLocalAxis ):
            cmds.setAttr( fing01Joint+'.displayLocalAxis', 1 )
            cmds.setAttr( fing02Joint+'.displayLocalAxis', 1 )
            cmds.setAttr( fing03Joint+'.displayLocalAxis', 1 )
            cmds.setAttr( fingEndJoint+'.displayLocalAxis', 1 )
        
        # -- orient the joints
        #cmds.select( clear=True )
        #fing01Joint = cmds.parent( fing01Joint, fing+'01_Piv' ) # -- temp reparent finger under planar space
        #cmds.joint( fing01Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( 0.2 )
        
        # -- do the controls
        fing01Ctrl = denUt.den_MakeSpike( nodeName=fing+'01_Ctrl', radius=3*radius, axis='-Y' )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        fing01Ctrl = cmds.parent( fing01Ctrl, fing01Joint, relative=True )
        fing01Ctrl = cmds.parent( fing01Ctrl, fingCtrlParent )
        fing01Ctrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_DiagPause( seconds=dpTime )
        
        fing02Ctrl = denUt.den_MakeSpike( nodeName=fing+'02_Ctrl', radius=3*radius, axis='-Y' )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        fing02Ctrl = cmds.parent( fing02Ctrl, fing02Joint, relative=True )
        fing02Ctrl = cmds.parent( fing02Ctrl, fing01Ctrl )
        fing02Ctrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_DiagPause( seconds=dpTime )
        
        fing03Ctrl = denUt.den_MakeSpike( nodeName=fing+'03_Ctrl', radius=3*radius, axis='-Y' )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        fing03Ctrl = cmds.parent( fing03Ctrl, fing03Joint, relative=True )
        fing03Ctrl = cmds.parent( fing03Ctrl, fing02Ctrl )
        fing03Ctrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_DiagPause( seconds=dpTime )
        
        cmds.connectAttr( fing01Ctrl[0]+'.rotate', fing01Joint+'.rotate' )
        cmds.connectAttr( fing02Ctrl[0]+'.rotate', fing02Joint+'.rotate' )
        cmds.connectAttr( fing03Ctrl[0]+'.rotate', fing03Joint+'.rotate' )
        
        # -- list the joints for binding
        if fing==side+prefix+'Thumb':
            HandBindJoints += [ fing01Joint, fing02Joint, fing03Joint ]
            HandCtrlsALL += [ fing01Ctrl[0], fing02Ctrl[0], fing03Ctrl[0] ]
        else:
            HandBindJoints += [ fing00Joint, fing01Joint, fing02Joint, fing03Joint ]
            HandCtrlsALL += [ fing00Ctrl[0], fing01Ctrl[0], fing02Ctrl[0], fing03Ctrl[0] ]
        #HandJxJoints += JxJnts
    
    
    if side == 'R_':
        cmds.setAttr( HandRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    #print '=========', HandBindJoints
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return HandRigGrp, HandSpaceINs, HandSpaceOUTs, HandBindJoints, HandCtrlsALL, HandGutsALL


# ---------------------------------------------------------------------------------------
# define Biped Hand pivots creation command

def den_makeBipedHandPivs2( side='L_', prefix='', name='Hand', radius=1.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables
    #side='L_'
    #prefix=''
    #name='Hand'
    #radius=1.0
    #dpTime=0.01
    #---------------------
    
    HandPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    fingList = [side+prefix+'Thumb',side+prefix+'Index',side+prefix+'Middle',side+prefix+'Ring',side+prefix+'Pinky']
    
    # build and set a good starting position the hand pivots
    for i,fing in enumerate(fingList):
        
        if fing!=side+prefix+'Thumb':
            denUt.den_makeLoc( nodeName=fing+'00_Piv', pos=(size*0.25, size*0.5, -i*size*0.025+size*0.050), rot=(0,0,0), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            cmds.parent( fing+'00_Piv', HandPivGrp )
            #denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
            
            denUt.den_makeLoc( nodeName=fing+'01_Piv', pos=(size*0.050, 0, 0), rot=(0,0,0), radius=2*radius ); denUt.den_DiagPause( seconds=dpTime )
            denUt.den_ColorShape(20)
            cmds.parent( fing+'01_Piv', fing+'00_Piv', relative=True )
            cmds.parent( fing+'01_Piv', HandPivGrp, relative=False )
            #denUt.den_Lock(  0,1,1 , 0,0,0 , 1,1,1 , 0 )
        else:
            denUt.den_makeLoc( nodeName=fing+'01_Piv', pos=(size*0.275, size*0.5, -i*size*0.025+size*0.050), rot=(60,-45,-15), radius=2*radius ); denUt.den_DiagPause( seconds=dpTime )
            denUt.den_ColorShape(20)
            cmds.parent( fing+'01_Piv', HandPivGrp )
            #denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'Up_Piv', pos=(0, -size*0.025, 0), rot=(0,0,0), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(23)
        cmds.parent( fing+'Up_Piv', fing+'01_Piv', relative=True )
        cmds.parent( fing+'Up_Piv', HandPivGrp, relative=False )
        #denUt.den_Lock(  0,1,1 , 1,1,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'02_Piv', pos=(size*0.030, 0, 0), rot=(0,0,-10), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(21)
        cmds.parent( fing+'02_Piv', fing+'01_Piv', relative=True )
        cmds.parent( fing+'02_Piv', HandPivGrp, relative=False )
        #denUt.den_Lock(  0,1,1 , 1,1,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'03_Piv', pos=(size*0.025, 0, 0), rot=(0,0,-10), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(25)
        cmds.parent( fing+'03_Piv', fing+'02_Piv', relative=True )
        cmds.parent( fing+'03_Piv', HandPivGrp, relative=False )
        #denUt.den_Lock(  0,1,1 , 1,1,0 , 1,1,1 , 0 )
        
        denUt.den_makeLoc( nodeName=fing+'End_Piv', pos=(size*0.020, 0, 0), rot=(0,0,0), radius=0.5*radius ); denUt.den_DiagPause( seconds=dpTime )
        denUt.den_ColorShape(26)
        cmds.parent( fing+'End_Piv', fing+'03_Piv', relative=True )
        cmds.parent( fing+'End_Piv', HandPivGrp, relative=False )
        #denUt.den_Lock(  0,1,1 , 1,1,1 , 1,1,1 , 0 )
        
        # - constrains pivot locators so they provide orientation for the hand joints
        if fing!=side+prefix+'Thumb':
            cmds.aimConstraint( fing+'01_Piv',fing+'00_Piv', worldUpType='object', worldUpObject=fing+'Up_Piv', upVector=(0,1,0) )
        cmds.aimConstraint( fing+'02_Piv',fing+'01_Piv', worldUpType='object', worldUpObject=fing+'Up_Piv', upVector=(0,1,0) )
        cmds.aimConstraint( fing+'03_Piv',fing+'02_Piv', worldUpType='object', worldUpObject=fing+'Up_Piv', upVector=(0,1,0) )
        cmds.aimConstraint( fing+'End_Piv',fing+'03_Piv', worldUpType='object', worldUpObject=fing+'Up_Piv', upVector=(0,1,0) )
        cmds.orientConstraint( fing+'03_Piv', fing+'End_Piv', mo=False )
        
        # - lock the rotate and scale of the pivots so the user can only translate them.  Scale should not be touched, and rotates are driven by constraints
        pivs = cmds.ls( fing+'*_Piv' )
        for piv in pivs:
            cmds.select( piv )
            denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 0 )
    
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( HandPivGrp+'.scaleX', -1 )
    
    print( 'den_makeHandPivs -- done\n' )
    
    return HandPivGrp

#den_makeBipedHandPivs2( side='L_', prefix='', name='Hand', radius=1.0, dpTime = 0.01 )



# ---------------------------------------------------------------------------------------
# define Biped Hand rig creation command

def den_makeBipedHandRig2( side='L_', prefix='', name='Hand', radius=1.0, displayLocalAxis=False, dpTime=0.01, size=100 ):
    #--------------------- testing variables    
    #side = 'L_'
    #name='Hand'
    #radius=1.0
    #displayLocalAxis=True
    #---------------------
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    # -- set up the return variables
    HandSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    HandSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    HandBindJoints = [] #Set list variable to hold names of all the Jx joints
    HandCtrlsALL = [] #Set list variable to hold names of all the controls
    HandGutsALL = [] #Set list variable to hold names of all the guts
    
    
    fingList = [side+prefix+'Thumb',side+prefix+'Index',side+prefix+'Middle',side+prefix+'Ring',side+prefix+'Pinky']
    
    HandRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp' )
    WristSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'Wrist_SpaceIN' )
    WristSpaceIN = cmds.parent( WristSpaceIN, HandRigGrp )
    HandSpaceINs += WristSpaceIN
    HandSkelGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Skel_Grp' )
    HandSkelGrp = cmds.parent( HandSkelGrp, WristSpaceIN )
    HandCtrlGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Ctrl_Grp' )
    HandCtrlGrp = cmds.parent( HandCtrlGrp, WristSpaceIN )
    #print( HandRigGrp, WristSpaceIN, HandSkelGrp, HandCtrlGrp )
    for fing in fingList:
        
        #fing = side+prefix+'Pinky'
        # -- do the palm joints
        if fing==side+prefix+'Thumb':
            fingSkelParent = HandSkelGrp
            fingCtrlParent = HandCtrlGrp
            #print 'thumb'
        else:
            # -- make the palm joints for not-thumbs
            fing00Pos = cmds.xform( fing+'00_Piv', ws=True, q=True, t=True )
            cmds.select( clear=True )
            fing00Joint = cmds.joint( n=fing+'00_Jnt', radius=radius )
            if( displayLocalAxis ):
                cmds.setAttr( fing00Joint+'.displayLocalAxis', 1 )
            fing00Joint = cmds.parent( fing00Joint, fing+'00_Piv', relative=True ) # -- temp reparent finger under planar space
            cmds.joint( fing00Joint, e=True, oj='none', zso=True )
            fing00Joint = cmds.parent( fing00Joint, HandSkelGrp )[0] # -- put finger back
            fing00Ctrl = denUt.den_MakeSpike( nodeName=fing+'00_Ctrl', radius=3*radius, axis='-Y' )
            denUt.den_ColorShapeRGB(rgb=(1,0,1))
            denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
            fing00Ctrl = cmds.parent( fing00Ctrl, fing00Joint, relative=True )
            fing00Ctrl = cmds.parent( fing00Ctrl, HandCtrlGrp )
            fing00Ctrl = denUt.den_AddZeroNull()
            denUt.den_LockAttr(True,False,True,False)# relock after parenting
            cmds.connectAttr( fing00Ctrl[0]+'.rotate', fing00Joint+'.rotate' )
            fingSkelParent = fing00Joint
            fingCtrlParent = fing00Ctrl
            #print 'not thumb'
            
        # -- get joint positions
        fing01Pos = cmds.xform( fing+'01_Piv', ws=True, q=True, t=True )
        fing02Pos = cmds.xform( fing+'02_Piv', ws=True, q=True, t=True )
        fing03Pos = cmds.xform( fing+'03_Piv', ws=True, q=True, t=True )
        fingEndPos = cmds.xform( fing+'End_Piv', ws=True, q=True, t=True )
        
        # -- make the joints
        cmds.select( clear=True )
        fing01Joint = cmds.joint( n=fing+'01_Jnt', radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        fing01Joint = cmds.parent( fing01Joint, fing+'01_Piv', relative=True ) # -- temp reparent finger under planar space
        cmds.joint( fing01Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        fing01Joint = cmds.parent( fing01Joint, fingSkelParent )[0] # -- put finger back
        
        cmds.select( clear=True )
        fing02Joint = cmds.joint( n=fing+'02_Jnt', radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        fing02Joint = cmds.parent( fing02Joint, fing+'02_Piv', relative=True ) # -- temp reparent finger under planar space
        cmds.joint( fing02Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        fing02Joint = cmds.parent( fing02Joint, fing01Joint )[0] # -- put finger back
        
        cmds.select( clear=True )
        fing03Joint = cmds.joint( n=fing+'03_Jnt', radius=radius ); denUt.den_DiagPause( seconds=dpTime )
        fing03Joint = cmds.parent( fing03Joint, fing+'03_Piv', relative=True ) # -- temp reparent finger under planar space
        cmds.joint( fing03Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        fing03Joint = cmds.parent( fing03Joint, fing02Joint )[0] # -- put finger back
        
        cmds.select( clear=True )
        fingEndJoint = cmds.joint( n=fing+'_end', radius=radius*0.5 ); denUt.den_DiagPause( seconds=dpTime )
        fingEndJoint = cmds.parent( fingEndJoint, fing+'End_Piv', relative=True ) # -- temp reparent finger under planar space
        cmds.joint( fing02Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        fingEndJoint = cmds.parent( fingEndJoint, fing03Joint )[0] # -- put finger back
        
        #cmds.joint( fing02Joint, e=True, oj='xyz', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        #cmds.joint( fing03Joint, e=True, oj='xyz', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        #cmds.joint( fingEndJoint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
        
        if( displayLocalAxis ):
            cmds.setAttr( fing01Joint+'.displayLocalAxis', 1 )
            cmds.setAttr( fing02Joint+'.displayLocalAxis', 1 )
            cmds.setAttr( fing03Joint+'.displayLocalAxis', 1 )
            cmds.setAttr( fingEndJoint+'.displayLocalAxis', 1 )
        
        # -- orient the joints
        #cmds.select( clear=True )
        #fing01Joint = cmds.parent( fing01Joint, fing+'01_Piv' ) # -- temp reparent finger under planar space
        #cmds.joint( fing01Joint, e=True, oj='none', zso=True ); denUt.den_DiagPause( 0.2 )
        
        # -- do the controls
        fing01Ctrl = denUt.den_MakeSpike( nodeName=fing+'01_Ctrl', radius=3*radius, axis='-Y' )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        fing01Ctrl = cmds.parent( fing01Ctrl, fing01Joint, relative=True )
        fing01Ctrl = cmds.parent( fing01Ctrl, fingCtrlParent )
        fing01Ctrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_DiagPause( seconds=dpTime )
        
        fing02Ctrl = denUt.den_MakeSpike( nodeName=fing+'02_Ctrl', radius=3*radius, axis='-Y' )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        fing02Ctrl = cmds.parent( fing02Ctrl, fing02Joint, relative=True )
        fing02Ctrl = cmds.parent( fing02Ctrl, fing01Ctrl )
        fing02Ctrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_DiagPause( seconds=dpTime )
        
        fing03Ctrl = denUt.den_MakeSpike( nodeName=fing+'03_Ctrl', radius=3*radius, axis='-Y' )
        denUt.den_ColorShapeRGB(rgb=(1,0,1))
        denUt.den_UnLockAttr(True,True,True,True)# unloc before reparenting
        fing03Ctrl = cmds.parent( fing03Ctrl, fing03Joint, relative=True )
        fing03Ctrl = cmds.parent( fing03Ctrl, fing02Ctrl )
        fing03Ctrl = denUt.den_AddZeroNull()
        denUt.den_LockAttr(True,False,True,False)# relock after parenting
        denUt.den_DiagPause( seconds=dpTime )
        
        cmds.connectAttr( fing01Ctrl[0]+'.rotate', fing01Joint+'.rotate' )
        cmds.connectAttr( fing02Ctrl[0]+'.rotate', fing02Joint+'.rotate' )
        cmds.connectAttr( fing03Ctrl[0]+'.rotate', fing03Joint+'.rotate' )
        
        # -- list the joints for binding
        if fing==side+prefix+'Thumb':
            HandBindJoints += [ fing01Joint, fing02Joint, fing03Joint ]
            HandCtrlsALL += [ fing01Ctrl[0], fing02Ctrl[0], fing03Ctrl[0] ]
        else:
            HandBindJoints += [ fing00Joint, fing01Joint, fing02Joint, fing03Joint ]
            HandCtrlsALL += [ fing00Ctrl[0], fing01Ctrl[0], fing02Ctrl[0], fing03Ctrl[0] ]
        #HandJxJoints += JxJnts
    
    
    if side == 'R_':
        cmds.setAttr( HandRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    #print '=========', HandBindJoints
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return HandRigGrp, HandSpaceINs, HandSpaceOUTs, HandBindJoints, HandCtrlsALL, HandGutsALL

#den_makeBipedHandRig2( side='L_', prefix='', name='Hand', radius=1.03, displayLocalAxis=False )



# ---------------------------------------------------------------------------------------
# define Biped Leg pivots creation command

def den_makeBipedLegPivs( side='L_', prefix='', name='Leg', radius=2.0, kneeDist=20.0, footUpDist=10.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables    
    #side='L_'
    #prefix=''
    #name='Leg'
    #radius=2.0
    #kneeDist=20.0
    #footUpDist=10.0
    #dpTime=0.01
    #---------------------
    
    LegPivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp' )
    
    denUt.den_makeLoc( nodeName='Hip_Piv', pos=(size*0.043, size*0.520, size*0.007), radius=radius ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Knee_Piv', pos=(size*0.056, size*0.282, -size*0.004), radius=radius ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ankle_Piv', pos=(size*0.064, size*0.067, -size*0.037), radius=radius ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Ball_Piv', pos=(size*0.064, size*0.018, size*0.025), radius=radius ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeGrp ( 'BallSole_Piv', pos=(size*0.064, 0, size*0.025) ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    #denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='Toe_Piv', pos=(size*0.064, 0, size*0.081), radius=radius ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    #cmds.polyPlane( name='Heel_Piv', w=7*radius, h=14*radius, sx=1, sy=1, ax=(0,1,0), cuv=2, ch=1 ); cmds.move(12.1,0,-12,'Heel_Piv', r=True); cmds.move(0,0,7*radius,'Heel_Piv.vtx[*]', r=True); cmds.setAttr( 'Heel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    cmds.curve( name='Heel_Piv', degree=1, p=[( -1,0,0 ),( 1,0,0 ),( 1,0,2 ),( -1,0,2 ),( -1,0,0 )] ); cmds.move(size*0.064,0,-size*0.063,'Heel_Piv', r=True); cmds.scale(3.5*radius,0,7*radius,'Heel_Piv.cv[*]'); cmds.setAttr( 'Heel_Piv.displayLocalAxis', 1); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleLF_Piv', pos=(size*0.097, 0, size*0.022), radius=radius/2 ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleLB_Piv', pos=(size*0.085, 0, -size*0.049), radius=radius/2 ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleRF_Piv', pos=(size*0.041, 0, size*0.041), radius=radius/2 ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    denUt.den_makeLoc( nodeName='SoleRB_Piv', pos=(size*0.045, 0, -size*0.047), radius=radius/2 ); denUt.den_DiagPause( seconds=dpTime ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(20)
    # -- connect the y translate attrs to the xxx to maintain a flat sole, then lock attrs
    cmds.connectAttr( 'Ball_Piv.translateX', 'BallSole_Piv.translateX' )
    cmds.connectAttr( 'Ball_Piv.translateZ', 'BallSole_Piv.translateZ' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'BallSole_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'Toe_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleLF_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleRF_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleLB_Piv.translateY' )
    #cmds.connectAttr( 'Heel_Piv.translateY', 'SoleRB_Piv.translateY' )
    
    
    # - make a second set of pivots for the triangle of the top two leg bones
    denUt.den_makeLoc( nodeName='KneeMid_Loc', radius=radius/2) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(2)
    
    denUt.den_makeLoc( nodeName='KneePole_Loc', radius=radius, pos=(0, kneeDist, 0) ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(9)
    cmds.parent( 'KneePole_Loc', 'KneeMid_Loc' )
    
    # - make a locator that sets the up of the foot based on foot plane to aid pivot placement
    denUt.den_makeLoc( nodeName='FootUp_Piv', radius=radius, pos=(0, footUpDist, 2*footUpDist) ) # leave off the L_ so constraint attrs are not confusing when mirrored
    denUt.den_ColorShape(14)
    #cmds.parent( 'FootUp_Piv', 'Ankle_Piv', relative=True )
    cmds.parent( 'FootUp_Piv', 'Heel_Piv', relative=True )
    
    LegMidLocPtCon = cmds.pointConstraint( 'Hip_Piv','Ankle_Piv','KneeMid_Loc', mo=False  )[0]
    LegMidLocAimCon = cmds.aimConstraint( 'Ankle_Piv','KneeMid_Loc', worldUpType='object', worldUpObject='Knee_Piv', mo=False  )[0]
    HipPivAimCon = cmds.aimConstraint( 'Knee_Piv','Hip_Piv', worldUpType='object', worldUpObject='Ankle_Piv', mo=False  )[0]
    AnklePivAimCon = cmds.aimConstraint( 'Ball_Piv','Ankle_Piv', worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    SoleLFPivAimCon = cmds.aimConstraint( 'SoleLB_Piv','SoleLF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    SoleRFPivAimCon = cmds.aimConstraint( 'SoleRB_Piv','SoleRF_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    ToePivAimCon = cmds.aimConstraint( 'Ball_Piv','Toe_Piv', aimVector=(0,0,-1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    HeelPivAimCon = cmds.aimConstraint( 'Toe_Piv','Ball_Piv', aimVector=(0,0,1), worldUpType='object', worldUpObject='FootUp_Piv', mo=False )[0]
    
    # - lock down channels the user is not supposed to touch
    cmds.select( LegPivGrp ); denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    cmds.select( 'Hip_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Knee_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'Hock_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'Hock_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ankle_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Ball_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'BallSole_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Toe_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'Heel_Piv' ); denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 1 )
    cmds.select( 'KneeMid_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'LegMid2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'KneePole_Loc' ); denUt.den_Lock(  0,0,1 , 1,1,1 , 1,1,1 , 1 )
    #cmds.select( 'KneePole2_Loc' ); denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'FootUp_Piv' ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleLF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleRF_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleLB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( 'SoleRB_Piv' ); denUt.den_Lock(  0,1,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.parent( 'Heel_Piv', 'Hip_Piv', 'Knee_Piv', 'KneeMid_Loc', LegPivGrp )
    cmds.parent( 'Ankle_Piv', 'Ball_Piv', 'BallSole_Piv', 'Toe_Piv', 'SoleLF_Piv', 'SoleLB_Piv', 'SoleRF_Piv', 'SoleRB_Piv', 'Heel_Piv' )
    
    # -- put the L_ back into the node names
    cmds.rename( 'Hip_Piv', side+prefix+'Hip_Piv' )
    cmds.rename( 'Knee_Piv', side+prefix+'Knee_Piv' )
    cmds.rename( 'Ankle_Piv', side+prefix+'Ankle_Piv' )
    cmds.rename( 'Ball_Piv', side+prefix+'Ball_Piv' )
    cmds.rename( 'BallSole_Piv', side+prefix+'BallSole_Piv' )
    cmds.rename( 'Toe_Piv', side+prefix+'Toe_Piv' )
    cmds.rename( 'Heel_Piv', side+prefix+'Heel_Piv' )
    cmds.rename( 'KneeMid_Loc', side+prefix+'KneeMid_Loc' )
    cmds.rename( 'KneePole_Loc', side+prefix+'KneePole_Loc' )
    cmds.rename( 'FootUp_Piv', side+prefix+'FootUp_Piv' )
    cmds.rename( 'SoleLF_Piv', side+prefix+'SoleLF_Piv' )
    cmds.rename( 'SoleRF_Piv', side+prefix+'SoleRF_Piv' )
    cmds.rename( 'SoleLB_Piv', side+prefix+'SoleLB_Piv' )
    cmds.rename( 'SoleRB_Piv', side+prefix+'SoleRB_Piv' )
    cmds.rename( LegMidLocPtCon, side+prefix+LegMidLocPtCon )
    cmds.rename( LegMidLocAimCon, side+prefix+LegMidLocAimCon )
    cmds.rename( HipPivAimCon, side+prefix+HipPivAimCon )
    cmds.rename( AnklePivAimCon, side+prefix+AnklePivAimCon )
    cmds.rename( SoleLFPivAimCon, side+prefix+SoleLFPivAimCon )
    cmds.rename( SoleRFPivAimCon, side+prefix+SoleRFPivAimCon )
    cmds.rename( ToePivAimCon, side+prefix+ToePivAimCon )
    
    cmds.select(clear=True) # clear selection to avoid accidents
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( LegPivGrp+'.scaleX', -1 )
    
    return LegPivGrp








# ---------------------------------------------------------------------------------------
# define Biped Leg rig creation command

def den_makeBipedLegRig( side='L_', prefix='', name='Leg', radius=2.0, ctrlRadius=15.0, displayLocalAxis=False, twistType='none', revKnee=False, dpTime=0.01 ):
    #--------------------- testing variables
    #side = 'L_'
    #prefix=''
    #name='Leg'
    #radius=2.0
    #ctrlRadius=15.0
    #displayLocalAxis=True
    #twistType='none'
    #dpTime = 0.01
    #---------------------
    
    if( twistType == 'none' ) or ( twistType == 'ribbon' ) or ( twistType == 'twist' ):
        print( 'doing twistType \''+twistType+'\'' )
    else:
        print( 'ERROR - twistType must be  \'none\' or \'ribon\' or \'upcar\' - nothing else will work' )
    
    # -- if doing right side, change the color and flip the pivots to the left for good/easy mirroring
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let any pivot constraints re-evaluate
    # == set up top groups
    LegRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp' )
    
    # -- set up the return variables
    LegSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    LegSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    LegBindJoints = [] #Set list variable to hold names of all the Jx joints
    LegCtrlsALL = [] #Set list variable to hold names of all the controls
    LegGutsALL = [] #Set list variable to hold names of all the guts
    
    PelvisSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'PelvisSpace_IN' )
    PelvisSpaceIN = cmds.parent( PelvisSpaceIN, LegRigGrp )[0]
    CogSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'CogSpace_IN' )
    CogSpaceIN = cmds.parent( CogSpaceIN, LegRigGrp )[0]
    AllSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+'AllSpace_IN' )
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
    KneePos = cmds.xform( side+prefix+'Knee_Piv', ws=True, q=True, t=True )
    AnklePos = cmds.xform( side+prefix+'Ankle_Piv', ws=True, q=True, t=True )
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
    
    
    # -- make the joints
    cmds.select( clear=True )
    
    HipJoint = cmds.joint( n=side+prefix+'Hip_Jnt', p=(HipPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    KneeJoint = cmds.joint( n=side+prefix+'Knee_Jnt', p=(KneePos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    AnkleJoint = cmds.joint( n=side+prefix+'Ankle_Jnt', p=(AnklePos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    BallJoint = cmds.joint( n=side+prefix+'Ball_Jnt', p=(BallPos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    ToeJoint = cmds.joint( n=side+prefix+'Toe_Jx', p=(ToePos), radius=radius ); denUt.den_DiagPause( seconds=dpTime )
    
    #print HipJoint, HipPos
    #print KneeJoint, KneePos
    #print AnkleJoint, AnklePos
    #print BallJoint, BallPos
    #print ToeJoint, ToePos
    
    if ( displayLocalAxis ):
        cmds.setAttr( HipJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( KneeJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( AnkleJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( BallJoint+'.displayLocalAxis', 1 )
        cmds.setAttr( ToeJoint+'.displayLocalAxis', 1 )
    
    
    
    # -- orient the joints
    
    cmds.select( clear=True ); denUt.den_DiagPause( seconds=dpTime )
    #cmds.joint( KneeJoint, e=True, oj='xyz', zso=True ); denUt.den_DiagPause( seconds=dpTime )
    cmds.joint( KneeJoint, e=True, oj='xzy', secondaryAxisOrient='xup', aos=True, ch=False, zso=True ); denUt.den_DiagPause( seconds=dpTime )
    cmds.joint( AnkleJoint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
    if revKnee:
        cmds.setAttr( side+prefix+'Hip_Piv_aimConstraint1.upVectorY', -1 ); denUt.den_DiagPause( seconds=dpTime )
    HipJoint = cmds.parent( HipJoint, side+prefix+'Hip_Piv' )[0] # -- temp reparent hip under planar space
    cmds.joint( HipJoint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
    HipJoint = cmds.parent( HipJoint, LegSkelGrp )[0] # -- put hip back under leg skel grp
    AnkleJoint = cmds.parent( AnkleJoint, side+prefix+'Ankle_Piv' )[0] # -- temp reparent ankle under planar space
    #cmds.joint( BallJoint, e=True, oj='xyz', zso=True ); denUt.den_DiagPause( seconds=dpTime )
    cmds.joint( BallJoint, e=True, oj='xzy', secondaryAxisOrient='xup', aos=True, ch=False, zso=True ); denUt.den_DiagPause( seconds=dpTime )
    cmds.joint( ToeJoint, e=True, oj='none', zso=True ); denUt.den_DiagPause( seconds=dpTime )
    AnkleJoint = cmds.parent( AnkleJoint, KneeJoint )[0] # -- put ankle back under knee jnt
    
    # -- duplicate the leg to make the FK and IK leg bones
    HipJointIK = cmds.duplicate (HipJoint, name=side+prefix+'Hip_IK' )[0]
    KneeJointIK = cmds.rename (HipJointIK+'|'+side+prefix+'Knee_Jnt', side+prefix+'Knee_IK' )
    AnkleJointIK = cmds.rename (KneeJointIK+'|'+side+prefix+'Ankle_Jnt', side+prefix+'Ankle_IK' )
    BallJointIK = cmds.rename (AnkleJointIK+'|'+side+prefix+'Ball_Jnt', side+prefix+'Ball_IK' )
    ToeJointIK = cmds.rename (BallJointIK+'|'+side+prefix+'Toe_Jx', side+prefix+'Toe_IK' )
    #print HipJointIK, '----', KneeJointIK, '----', AnkleJointIK, '----', BallJointIK, '----', ToeJointIK
    HipJointFK = cmds.duplicate (HipJoint, name=side+prefix+'Hip_FK' )[0]
    KneeJointFK = cmds.rename (HipJointFK+'|'+side+prefix+'Knee_Jnt', side+prefix+'Knee_FK' )
    AnkleJointFK = cmds.rename (KneeJointFK+'|'+side+prefix+'Ankle_Jnt', side+prefix+'Ankle_FK' )
    BallJointFK = cmds.rename (AnkleJointFK+'|'+side+prefix+'Ball_Jnt', side+prefix+'Ball_FK' )
    ToeJointFK = cmds.rename (BallJointFK+'|'+side+prefix+'Toe_Jx', side+prefix+'Toe_FK' )
    #print HipJointFK, '----', KneeJointFK, '----', AnkleJointFK, '----', BallJointFK, '----', ToeJointFK
    
    # -- make the controls and zero nulls
    
    # -- Hip FK
    HipFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'HipFK_Ctrl', radius=ctrlRadius, axis='+Z')
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
    LegUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+name+'Util_Ctrl', pos=(ctrlRadius*0.5,0,ctrlRadius), radius=ctrlRadius*0.2, Plane='ZX')
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
    #KneeCtrl = cmds.rename( KneeCtrl, side+prefix+'Knee_Ctrl' )
    KneeCtrl = cmds.parent( KneeCtrl, LegCtrlGrp )
    KneeCtrl = denUt.den_AddZeroNull()
    if revKnee:
        KneeFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'KneeFK_Ctrl', pos=(0,ctrlRadius*0.5,0), radius=ctrlRadius*0.3, doT=True, axis='+Y' )
    else:
        KneeFKCtrl = denUt.den_MakeArrowR( nodeName=side+prefix+'KneeFK_Ctrl', pos=(0,-ctrlRadius*0.5,0), radius=ctrlRadius*0.3, doT=True, axis='-Y' )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    KneeFKCtrl = cmds.parent( KneeFKCtrl, KneeJointFK, relative=True )
    KneeFKCtrl = cmds.parent( KneeFKCtrl, HipFKCtrl )
    KneeFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( KneeFKCtrl[0]+'.rotate', KneeJointFK+'.rotate' )
    #print KneeFKCtrl
    # -- Ankle Controls
    AnkleCtrl = denUt.den_MakeBall( nodeName=side+prefix+'Ankle_Ctrl', radius=ctrlRadius*0.7 )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    cmds.xform( t=AnklePos )
    AnkleCtrl = cmds.parent( AnkleCtrl, AnkleCtrlSpace )
    AnkleCtrl = denUt.den_AddZeroNull()
    cmds.setAttr( AnkleCtrl[0]+'.rotateOrder', 1 )
    AnkleCtrlZero = cmds.listRelatives( AnkleCtrl, parent=True, fullPath=True )[0]
    
    AnkleFKCtrl = denUt.den_MakeSpike( nodeName=side+prefix+'AnkleFK_Ctrl', radius=ctrlRadius*0.7, axis='+Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    AnkleFKCtrl = cmds.parent( AnkleFKCtrl, AnkleJointFK, relative=True )
    AnkleFKCtrl = cmds.parent( AnkleFKCtrl, KneeFKCtrl )
    AnkleFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( AnkleFKCtrl[0]+'.rotate', AnkleJointFK+'.rotate' )
    AnkleFKCtrlZero = cmds.listRelatives( AnkleFKCtrl, parent=True, fullPath=True )[0]
    
    #print AnkleCtrlZero
    BallFKCtrl = denUt.den_MakeSpike(nodeName=side+prefix+'BallFK_Ctrl', radius=ctrlRadius*0.7, axis='-Z')
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    denUt.den_UnLockAttr(True,True,True,True)# lock before parenting
    BallFKCtrl = cmds.parent( BallFKCtrl, BallJointFK, relative=True )
    BallFKCtrl = cmds.parent( BallFKCtrl, AnkleFKCtrl )
    BallFKCtrl = denUt.den_AddZeroNull()
    denUt.den_LockAttr(True,False,True,False)# relock after parenting
    cmds.connectAttr( BallFKCtrl[0]+'.rotate', BallJointFK+'.rotate' )
    BallFKCtrlZero = cmds.listRelatives( BallFKCtrl, parent=True, fullPath=True )[0]
    # -- Foot Utility
    FootUtilCtrl = denUt.den_MakeGear( nodeName=side+prefix+'FootUtil_Ctrl', pos=(ctrlRadius*0.5,ctrlRadius*0.5,0), radius=ctrlRadius*0.2, Plane='XY')
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
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'PelvisSpace', AnkleCtrlSpaceConstraint[0]+'.'+side+prefix+'PelvisSpace_INW0' )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'CogSpace', defaultValue=0.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'CogSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'CogSpace', AnkleCtrlSpaceConstraint[0]+'.'+side+prefix+'CogSpace_INW1' )
    cmds.addAttr( LegUtilCtrl, longName=side+prefix+'AllSpace', defaultValue=1.0, minValue=0.0, maxValue=1.0 )
    cmds.setAttr( LegUtilCtrl[0]+'.'+side+prefix+'AllSpace', lock=False, keyable=True )
    cmds.connectAttr( LegUtilCtrl[0]+'.'+side+prefix+'AllSpace', AnkleCtrlSpaceConstraint[0]+'.'+side+prefix+'AllSpace_INW2' )
    
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
    for number,footPiv in enumerate(footPivs):
        prevNum = number-1
        nameRoot = footPiv.replace('_Piv','')
        #print 'nameRoot', nameRoot, number
        footJnt = cmds.joint( n=side+prefix+nameRoot+'Rev_Jx', radius=radius*0.7 )
        footPiv = side+prefix+footPivs[number]
        footJnt = cmds.parent( footJnt, footPiv, relative=True )
        cmds.joint( footJnt, e=True, oj='none', zso=True, radius=radius*0.7 ); denUt.den_DiagPause( seconds=dpTime )
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
    #RevToeBendLoc = cmds.spaceLocator( name=side+prefix+'RevToeBend_Loc' )
    #RevToeBendLoc = cmds.parent( RevToeBendLoc, RevToeJoint, relative=True )
    
    # -- make the ik handles
    cmds.select( HipJointIK, AnkleJointIK )
    LegIKhandle = denUt.den_AddIKHandle( handleType='ikRPsolver' )
    LegIKhandle = cmds.parent( LegIKhandle, RevAnkleJoint )[0]
    cmds.poleVectorConstraint( KneeCtrl, LegIKhandle )
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
    
    # -- list the joints for binding
    LegBindJoints += [ HipJoint, KneeJoint, AnkleJoint, BallJoint ]
    LegCtrlsALL += [ HipFKCtrl[0], KneeFKCtrl[0], AnkleFKCtrl[0], BallFKCtrl[0], KneeCtrl[0], AnkleCtrl[0], LegUtilCtrl[0], FootUtilCtrl[0] ]
    
    
    # --- deal with twist options
    if twistType == 'none':
        print( 'no twist joints added' )
        LegBindJoints = [ HipJoint, KneeJoint, AnkleJoint, BallJoint ]
        
    if twistType == 'twist':
        LegTwistRigRet = den_makeTwists( side=side, prefix=prefix, radius=radius, Joints=['Hip','Knee','Ankle'], ctrlPos=(-10,0,-10), ctrlUpVec=(0,0,-1), displayLocalAxis=False )
        print( LegTwistRigRet )
        LegTwistBindJoints = LegTwistRigRet[3]; print( LegTwistBindJoints )
        LegTwistCtrlsALL = LegTwistRigRet[4]; print( LegTwistCtrlsALL )
        LegBindJoints = [ AnkleJoint, BallJoint ] + LegTwistBindJoints
        LegCtrlsALL += LegTwistCtrlsALL        
    
    if twistType == 'ribbon':
        LegRibbonRigRet = den_makeRibbons( side=side, prefix=prefix, radius=radius, Joints=['Hip','Knee','Ankle'], ctrlPos=(-10,0,-10), ctrlUpVec=(0,0,-1), displayLocalAxis=False )
        print( LegRibbonRigRet )
        LegRibbonBindJoints = LegRibbonRigRet[3]; print( LegRibbonBindJoints )
        LegRibbonCtrlsALL = LegRibbonRigRet[4]; print( LegRibbonCtrlsALL )
        LegBindJoints = [ AnkleJoint, BallJoint ] + LegRibbonBindJoints
        LegCtrlsALL += LegRibbonCtrlsALL
        
    
    # -- flip the right side back where it belongs
    if side == 'R_':
        cmds.setAttr( LegRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return LegRigGrp, LegSpaceINs, LegSpaceOUTs, LegBindJoints, LegCtrlsALL, LegGutsALL





# ---------------------------------------------------------------------------------------
#     FACE
# ---------------------------------------------------------------------------------------



def den_makeEyePiv( side='L_', prefix='', radius=1.0, dpTime=0.01, size=100 ):
    #--------------------- testing variables    
    #---------------------

    EyePivGrp = denUt.den_makeGrp( nodeName=side+prefix+'EyePiv_Grp' )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    EyeCenterPiv = denUt.den_makeLoc( nodeName=side+prefix+'Eye_Piv', pos=(size*0.02,size*0.9,size*0.05), rot=(8,0,2), radius=10*radius )
    cmds.parent( EyeCenterPiv, EyePivGrp )
    
    if side == 'R_':
        cmds.setAttr( EyePivGrp+'.scaleX', -1 )
    
    return EyePivGrp


def den_makeEyeRig( side='L_', prefix='', name='Eye', radius=1.0, ctrlRadius=6.0, displayLocalAxis=False, dpTime=0.01 ):
    #--------------------- testing variables    
    #---------------------
    
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    EyeRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Rig_Grp' )
    
    # -- set up the return variables
    EyeSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    EyeSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    EyeJoints = [] #Set list variable to hold names of all the Jx joints
    EyeCtrlsALL = [] #Set list variable to hold names of all the controls
    EyeGutsALL = [] #Set list variable to hold names of all the guts
    
    EyeSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'Space_IN' )
    EyeSpaceIN = cmds.parent( EyeSpaceIN, EyeRigGrp )
    EyeSpaceINs += EyeSpaceIN
    
    EyePos = cmds.xform( side+prefix+name+'_Piv', ws=True, q=True, t=True )
    EyeRot = cmds.xform( side+prefix+name+'_Piv', ws=True, q=True, ro=True )
    #print EyeRot
    EyeLoc = denUt.den_makeLoc( nodeName=side+prefix+name+'_Loc', pos=EyePos, rot=EyeRot, radius=radius )
    EyeLoc = cmds.parent( EyeLoc, EyeSpaceIN )
    
    EyeJnt = cmds.joint( n=side+prefix+name+'_Jnt', radius=radius )
    EyeJoints += [EyeJnt]
    
    if ( displayLocalAxis ):
        cmds.setAttr( EyeJnt+'.displayLocalAxis', 1 )
        
    EyeCtrl = denUt.den_MakeSpike( nodeName=side+prefix+name+'_Ctrl', pos=(0,0,ctrlRadius), radius=ctrlRadius*0.3, axis='+Z' )
    EyeCtrl = cmds.parent( EyeCtrl, EyeLoc, relative=True )
    denUt.den_ColorShapeRGB(rgb=(1,0,1))
    EyeCtrlsALL += EyeCtrl
    cmds.connectAttr( EyeCtrl[0]+'.rotate', EyeJnt+'.rotate' )
    
    if side == 'R_':
        cmds.setAttr( EyeRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return EyeRigGrp, EyeSpaceINs, EyeSpaceOUTs, EyeJoints, EyeCtrlsALL, EyeGutsALL




'''
def den_makeHalfMuscle( name='foo', radius=1.0, Root='hip', Tip='knee', rootOffset=(0,0,0), tipOffset=(0,0,0), dpTime = 0.01 ):
    #name = 'R_Thigh01'
    #radius=1.0
    #Root= 'R_HipRest_Jnt'
    #Tip = 'R_HipTwist03_Jnt'
    #rootOffset=(-10,-10,1)
    #tipOffset=(0,-6,0)
    
    RootParent = cmds.listRelatives( Root, parent=True )
    
    RootLoc = denUt.den_makeLoc ( nodeName=name+'_RLoc', radius=radius )
    TipLoc = denUt.den_makeLoc ( nodeName=name+'_TLoc', radius=radius )
    
    cmds.select( clear=True )
    Joint = denUt.den_makeJoint( nodeName=name+'_Jnt', pos=(0,0,0), radius=radius, leaveSelected=True )
    EndJoint = denUt.den_makeJoint( nodeName=name+'_end', pos=(radius*10,0,0), radius=radius*0.1, leaveSelected=False )
    
    Joint = cmds.parent( Joint, RootLoc, relative=True )[0]
    
    
    cmds.setAttr( RootLoc[0]+'.t', rootOffset[0], rootOffset[1], rootOffset[2] )
    cmds.setAttr( TipLoc[0]+'.t', tipOffset[0], tipOffset[1], tipOffset[2] )
    RootLoc = cmds.parent( RootLoc, Root, relative=True )
    TipLoc = cmds.parent( TipLoc, Tip, relative=True )
    
    RootPos = cmds.xform( RootLoc, ws=True, q=True, t=True ); print( 'RootPos =', RootPos ) 
    RootPosVec = om.MVector(RootPos[0],RootPos[1],RootPos[2])
    TipPos = cmds.xform( TipLoc, ws=True, q=True, t=True ); print( 'TipPos =', TipPos ) 
    TipPosVec = om.MVector(TipPos[0],TipPos[1],TipPos[2])
    
    vecA = RootPosVec - TipPosVec
    lenA = om.MVector.length(vecA)
    print( lenA )
    cmds.setAttr( EndJoint+'.translateX', lenA )
    
    cmds.addAttr( RootLoc[0], longName='RestDistance', attributeType='float', defaultValue=lenA )
    cmds.setAttr ( RootLoc[0]+'.RestDistance', lock=False, keyable=True )
    
    DistNode = cmds.shadingNode( 'distanceBetween', name=name+'_distanceBetween', asUtility=True )
    MatrixNode = cmds.shadingNode( 'decomposeMatrix', name=name+'_decomposeMatrix', asUtility=True )
    print( RootLoc, DistNode )
    cmds.connectAttr( RootLoc[0]+'.worldMatrix[0]', DistNode+'.inMatrix1' )
    cmds.connectAttr( TipLoc[0]+'.worldMatrix[0]', DistNode+'.inMatrix2' )
    cmds.connectAttr( RootLoc[0]+'.worldMatrix[0]', MatrixNode+'.inputMatrix' )
    DivNode = cmds.shadingNode( 'multiplyDivide', name=name+'_multiplyDivide', asUtility=True )
    DivNode4scale = cmds.shadingNode( 'multiplyDivide', name=name+'4scale_multiplyDivide', asUtility=True )
    cmds.setAttr( DivNode+'.operation', 2 )
    cmds.connectAttr( DistNode+'.distance', DivNode+'.input1X' )
    cmds.connectAttr( MatrixNode+'.outputScaleX', DivNode4scale+'.input1X' )
    cmds.connectAttr( RootLoc[0]+'.RestDistance', DivNode4scale+'.input2X' )
    cmds.connectAttr( DivNode4scale+'.outputX', DivNode+'.input2X' )
    cmds.connectAttr( DivNode+'.outputX', Joint+'.scaleX' )
    
    cmds.aimConstraint( TipLoc, Joint, worldUpType='none' )
    
    # needs a parented duplicate of the proxy Mesh for stretchiness to display properly
    Mesh = cmds.ls( name+'_Mesh' )
    DispMesh = cmds.duplicate( Mesh, name=name+'_DispMesh' )
    DispMesh = cmds.parent( DispMesh, Joint )
    cmds.connectAttr( 'All_Ctrl.Show_Proxy_Geo', DispMesh[0]+'Shape.visibility' )
    cmds.setAttr( Mesh[0]+'.visibility', 0 )
    
    print( Joint )
    
    return Joint
'''




# ---------------------------------------------------------------------------------------
# define Biped Torso pivot creation command

def den_makeHalfMusclePivs( side='L_', prefix='', name='Foo', radius=1.0, dpTime=0.01 ):
    #--------------------- testing variables
    #radius=2.0
    #---------------------
    
    # -- makes torso pivots that can then be re-positioned to match a particular character
    
    MusclePivGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'Piv_Grp', pos=(0,0,0) )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 0,1,1 , 0 )
    
    RootPiv = denUt.den_makeLoc( nodeName=side+prefix+name+'Root_Piv', pos=(2*radius, 0, 2*radius), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    #denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    RootUpPiv = denUt.den_makeLoc( nodeName=side+prefix+name+'RootUp_Piv', pos=(2*radius, 2*radius, 2*radius), radius=0.5*radius )
    denUt.den_ColorShape(23); denUt.den_DiagPause( seconds=dpTime )
    #denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    TipPiv = denUt.den_makeLoc( nodeName=side+prefix+name+'Tip_Piv', pos=(6*radius, 0, 6*radius), radius=radius )
    denUt.den_ColorShape(20); denUt.den_DiagPause( seconds=dpTime )
    #denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.aimConstraint( TipPiv,RootPiv, maintainOffset=False, worldUpType='object', worldUpObject=RootUpPiv[0] )
    cmds.orientConstraint( RootPiv,TipPiv, maintainOffset=False )
    
    cmds.select( RootPiv ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( RootUpPiv ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( TipPiv ); denUt.den_Lock(  0,0,0 , 1,1,1 , 1,1,1 , 1 )
    
    cmds.parent( RootPiv,RootUpPiv,TipPiv,MusclePivGrp )
    
    denUt.den_DiagPause( seconds=dpTime ) # quick refresh to let scene re-evaluate
    
    if side == 'R_':
        cmds.setAttr( MusclePivGrp+'.scaleX', -1 )
    
    return MusclePivGrp



def den_makeHalfMuscleRig( side='L_', prefix='', name='foo', radius=1.0, dpTime=0.01 ):
    #prefix=''
    #side='L_'
    #name = 'Thigh01'
    #radius=1.0
    #dpTime=0.01
    
    # -- if doing right side, change the color and flip the pivots to the left for good/easy mirroring
    sideColor = 6
    if side == 'R_':
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', 1 )
        sideColor = 13
    
    denUt.den_DiagPause( seconds=0.1 ) # quick refresh to let scene re-evaluate
    
    # -- make the Arm rig top group
    MuscleRigGrp = denUt.den_makeGrp( nodeName=side+prefix+name+'_Grp', pos=(0,0,0) )
    
    # -- set up the return variables
    MuscleSpaceINs = [] #Set list variable to hold names of all the SpaceINs
    MuscleSpaceOUTs = [] #Set list variable to hold names of all the SpaceOUTs
    MuscleBindJoints = [] #Set list variable to hold names of all the _Jnt Bind joints
    MuscleCtrlsALL = [] #Set list variable to hold names of all the controls
    MuscleGutsALL = [] #Set list variable to hold names of all the guts
    
    # -- make the Muscle SpaceINs
    RootSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'Root_SpaceIN', pos=(0,0,0) )
    RootSpaceIN = cmds.parent( RootSpaceIN, MuscleRigGrp )[0]
    TipSpaceIN = denUt.den_makeGrp( nodeName=side+prefix+name+'Tip_SpaceIN', pos=(0,0,0) )
    TipSpaceIN = cmds.parent( TipSpaceIN, MuscleRigGrp )[0]
    
    # add all the SpaceINs to the list
    MuscleSpaceINs += [ RootSpaceIN, TipSpaceIN ]
    
    # -- set variables for pivot positions
    
    RootPos = cmds.xform( side+prefix+name+'Root_Piv', ws=True, q=True, t=True )
    RootRot = cmds.xform( side+prefix+name+'Root_Piv', ws=True, q=True, ro=True )
    TipPos = cmds.xform( side+prefix+name+'Tip_Piv', ws=True, q=True, t=True )
    TipRot = cmds.xform( side+prefix+name+'Tip_Piv', ws=True, q=True, ro=True )
    
    
    #RootParent = cmds.listRelatives( Root, parent=True )
    
    RootLoc = denUt.den_makeLoc ( nodeName=side+prefix+name+'_RLoc', radius=radius )
    TipLoc = denUt.den_makeLoc ( nodeName=side+prefix+name+'_TLoc', radius=radius )
    
    cmds.select( clear=True )
    Joint = denUt.den_makeJoint( nodeName=side+prefix+name+'_Jnt', pos=(0,0,0), radius=radius, leaveSelected=True )
    EndJoint = denUt.den_makeJoint( nodeName=side+prefix+name+'_end', pos=(radius*10,0,0), radius=radius*0.1, leaveSelected=False )
    
    Joint = cmds.parent( Joint, RootLoc, relative=True )[0]
    MuscleBindJoints += [ Joint ]
    cmds.xform( RootLoc, t=RootPos, ro=RootRot )
    #cmds.setAttr( RootLoc[0]+'.t', rootOffset[0], rootOffset[1], rootOffset[2] )
    cmds.xform( TipLoc, t=TipPos, ro=TipRot )
    #cmds.setAttr( TipLoc[0]+'.t', tipOffset[0], tipOffset[1], tipOffset[2] )
    RootLoc = cmds.parent( RootLoc, RootSpaceIN, relative=True )
    TipLoc = cmds.parent( TipLoc, TipSpaceIN, relative=True )
    
    #RootPos = cmds.xform( RootLoc, ws=True, q=True, t=True ); print( 'RootPos =', RootPos ) 
    RootPosVec = om.MVector(RootPos[0],RootPos[1],RootPos[2])
    #TipPos = cmds.xform( TipLoc, ws=True, q=True, t=True ); print( 'TipPos =', TipPos ) 
    TipPosVec = om.MVector(TipPos[0],TipPos[1],TipPos[2])
    
    vecA = RootPosVec - TipPosVec
    lenA = om.MVector.length(vecA)
    print( lenA )
    cmds.setAttr( EndJoint+'.translateX', lenA )
    
    cmds.addAttr( RootLoc[0], longName='RestDistance', attributeType='float', defaultValue=lenA )
    cmds.setAttr ( RootLoc[0]+'.RestDistance', lock=False, keyable=True )
    
    DistNode = cmds.shadingNode( 'distanceBetween', name=side+prefix+name+'_distanceBetween', asUtility=True )
    MatrixNode = cmds.shadingNode( 'decomposeMatrix', name=side+prefix+name+'_decomposeMatrix', asUtility=True )
    print( RootLoc, DistNode )
    cmds.connectAttr( RootLoc[0]+'.worldMatrix[0]', DistNode+'.inMatrix1' )
    cmds.connectAttr( TipLoc[0]+'.worldMatrix[0]', DistNode+'.inMatrix2' )
    cmds.connectAttr( RootLoc[0]+'.worldMatrix[0]', MatrixNode+'.inputMatrix' )
    DivNode = cmds.shadingNode( 'multiplyDivide', name=side+prefix+name+'_multiplyDivide', asUtility=True )
    DivNode4scale = cmds.shadingNode( 'multiplyDivide', name=side+prefix+name+'4scale_multiplyDivide', asUtility=True )
    cmds.setAttr( DivNode+'.operation', 2 )
    cmds.connectAttr( DistNode+'.distance', DivNode+'.input1X' )
    cmds.connectAttr( MatrixNode+'.outputScaleX', DivNode4scale+'.input1X' )
    cmds.connectAttr( RootLoc[0]+'.RestDistance', DivNode4scale+'.input2X' )
    cmds.connectAttr( DivNode4scale+'.outputX', DivNode+'.input2X' )
    cmds.connectAttr( DivNode+'.outputX', Joint+'.scaleX' )
    
    cmds.aimConstraint( TipLoc, Joint, worldUpType='none' )
    
    # needs a parented duplicate of the proxy Mesh for stretchiness to display properly
    Mesh = cmds.ls( side+prefix+name+'_Mesh' )
    DispMesh = cmds.duplicate( Mesh, name=side+prefix+name+'_DispMesh' )
    if side == 'R_':
        cmds.xform( DispMesh, s=( -1.0, 1.0, 1.0 ) )
        cmds.makeIdentity( DispMesh, apply=True, preserveNormals=True )
    
    DispMesh = cmds.parent( DispMesh, Joint )
    cmds.connectAttr( 'All_Ctrl.Show_Proxy_Geo', DispMesh[0]+'Shape.visibility' )
    cmds.setAttr( Mesh[0]+'.visibility', 0 )
    
    # -- flip the right side back where it belongs
    if side == 'R_':
        cmds.setAttr( MuscleRigGrp+'.scaleX', -1 )
        cmds.setAttr( side+prefix+name+'Piv_Grp.scaleX', -1 )
    
    # -- return the top level group node and SpaceINs, SpaceOUTs, BindJoints, CtrlsALL, GutsALL lists in order
    return MuscleRigGrp, MuscleSpaceINs, MuscleSpaceOUTs, MuscleBindJoints, MuscleCtrlsALL, MuscleGutsALL




# -------------------------------------------------------------------------------------------
# make ass helper

def den_makeAngleSplitter( name='L_Seat02', firstJnt='L_HipRest_Jx', secondJnt='L_HipTwist01_Jnt', radius=1.0 ):
    #name='L_Seat02'
    #firstJnt='L_HipRest_Jx'
    #secondJnt='L_HipTwist01_Jnt'
    #radius=2.0
    
    firstJnt = cmds.ls( firstJnt )
    firstJntParent = cmds.listRelatives( firstJnt, parent=True )
    secondJnt = cmds.ls( secondJnt )
    print(firstJnt)
    print(firstJntParent)
    print(secondJnt)
    
    SplitLoc = denUt.den_makeLoc( nodeName=name+'_Loc', radius=radius )
    SplitJnt = cmds.joint( name=name+'_Jnt', radius=radius )
    
    cmds.select( SplitLoc, SplitJnt )
    denUt.den_Lock(  0,0,0 , 0,0,0 , 1,1,1 , 1 )
    
    cmds.setAttr( SplitJnt+'.t', 0, radius, 0 ) # add an offset so that Seat02 is not in the same place as HipTwist01 so that wieght transfer doesn't fuck up
    SplitLoc = cmds.parent( SplitLoc, firstJnt, relative=True )
    SplitLoc = cmds.parent( SplitLoc, firstJntParent, relative=False )
    cmds.orientConstraint( firstJnt, secondJnt, SplitLoc )
    cmds.select( SplitLoc, SplitJnt )
    denUt.den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    cmds.select( clear=True )
    
    return SplitJnt



