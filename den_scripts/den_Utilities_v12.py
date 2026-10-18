#
#  copyright 2017, 2023, Den Turner  -  all rights reserved
#
import sys; sys.dont_write_bytecode=True
import maya.cmds as cmds
import maya.mel as mel
import re
import time
#import pymel.core as pm 


#-------------------------------------------------------------------------
# - snap an object to the position and orientation of another object

def den_ObjSnap():
    den_tempCon = cmds.parentConstraint ( weight=1 )
    cmds.delete ( den_tempCon )
    

#-------------------------------------------------------------------------
# - show or hide the local axis of selected objects

def den_ShowLocalAxis(yn):
    den_objects = cmds.ls (selection=True, long=True)
    for obj in den_objects:
        #print( 'doing object '+obj )
        cmds.setAttr (obj+'.displayLocalAxis', yn)
        #print( '-' )
    #print '----- done'        
    return True


#-------------------------------------------------------------------------
# - sets the index-display color of selected object shape nodes

def den_ColorShape(den_color=0, override=True):
    den_objects = cmds.ls (selection=True, long=True)
    for obj in den_objects:
        #print 'coloring object '+obj
        den_objShapes = cmds.listRelatives (obj, children=True, shapes=True, fullPath=True)
        for objShape in den_objShapes:
            #print '--- coloring shape '+objShape
            cmds.setAttr (objShape+'.overrideEnabled', override)
            cmds.setAttr (objShape+'.overrideColor', den_color)
        #print '-'
    #print '----- done'        
    return True


#-------------------------------------------------------------------------
# - sets the rgb-display color of selected object shape nodes

def den_ColorShapeRGB(rgb=(1,0,1), override=True):
    den_objects = cmds.ls (selection=True, long=True)
    for obj in den_objects:
        #print( 'coloring object '+obj )
        cmds.addAttr(obj, ln="Ctrl_Color", uac=True, at="float3")
        cmds.addAttr(obj, ln="Ctrl_ColorR", at="float", parent="Ctrl_Color")
        cmds.addAttr(obj, ln="Ctrl_ColorG", at="float", parent="Ctrl_Color")
        cmds.addAttr(obj, ln="Ctrl_ColorB", at="float", parent="Ctrl_Color")
        cmds.setAttr(obj + ".Ctrl_Color", rgb[0], rgb[1], rgb[2], type="double3")
        den_objShapes = cmds.listRelatives (obj, children=True, shapes=True, fullPath=True)
        for objShape in den_objShapes:
            #print '--- coloring shape '+objShape
            cmds.setAttr(objShape+'.overrideEnabled', override)
            cmds.setAttr(objShape+".overrideRGBColors", 1)
            cmds.connectAttr(obj+'.Ctrl_Color', objShape+'.drawOverride.overrideColorRGB')
        #print '-'
    #print '----- done'        
    return True

#den_ColorShapeRGB(rgb=(0,1,1), override=True)
#cmds.setAttr('Cog_PivShape.drawOverride.overrideColorRGB', 0, 0.9, 1, lock=False )

#-------------------------------------------------------------------------
# - sets the index-display color of selected objects

def den_ColorObject(den_color=0, override=True):
    den_objects = cmds.ls (selection=True, long=True)
    for obj in den_objects:
        #print 'coloring object '+obj
        cmds.setAttr (obj+'.overrideEnabled', override)
        cmds.setAttr (obj+'.overrideColor', den_color)
        #print '-'
    #print '----- done'        
    return True


#-------------------------------------------------------------------------
# - copy the shape of one node (last selected) into all other selected nodes

def den_CopyShapesIntoManyNodes():
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- find the last selected node, which will be our Ctrl object
      
    den_CtrlNode = cmds.ls( long=True, selection=True, tail=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the long name of the node again, as the for loop seems to mess with this somehow and it messes up the 'if' comparison  
        den_node = cmds.ls(den_node, long=True)
        
        #----- if the node is not the last-selected Ctrl object then duplicat and reparent shape nodes, otherwise do other stuff
        if (den_node != den_CtrlNode):
            tempDupe = cmds.duplicate(den_CtrlNode)
            #print( '-- makeing temporary duplicate of',den_node )
            den_ShapeNodes = cmds.listRelatives( tempDupe, children=True, shapes=True, fullPath=True )
            den_origShapeNodes = cmds.listRelatives( den_node, children=True, shapes=True, fullPath=True )
            #print( '-- moving shape nodes(s) from temporary duplicate to/n',den_node )
            cmds.parent(den_origShapeNodes, tempDupe, shape=True, relative=True )
            cmds.parent(den_ShapeNodes, den_node, shape=True, relative=True )
            #print( '---- deleting temp node leftover transform' )
            cmds.delete(tempDupe)
        else:
            print( 'Geometry from ',den_CtrlNode, 'copied into selected nodes' )




#-------------------------------------------------------------------------
# - copies all the shape nodes of selected nodes into the last node selected

def den_CombineShapesIntoOneNode(worldSpace=False):
    #worldSpace=False
    
    #----- make a list of all selected nodes
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- find the last selected node, which will be our Ctrl object
    den_CtrlNode = cmds.ls( long=True, selection=True, tail=True )[0]
    
    #----- loop through all selected objects
    for den_node in den_SelectedNodes:
        
        #----- if the node is not the last-selected Ctrl object then duplicat and reparent shape nodes, otherwise do other stuff
        if (den_node != den_CtrlNode):
            #----- find the original shape nodes in the seleced node
            origShapeNodes = cmds.listRelatives( den_node, children=True, shapes=True, fullPath=True )
            #print( origShapeNodes )
            #----- make a temporary group to hold original shape
            tempGrp = cmds.group( empty=True, name='temp_Grp' )
            #----- give temp group same transforms as original
            tempConstraint = cmds.parentConstraint( den_node, tempGrp )
            cmds.delete( tempConstraint )
            #----- move the original shape nodes under the temp group
            origShapeNodes = cmds.parent( origShapeNodes, tempGrp, shape=True, relative=True )
            #----- get the new path of the original shape
            origShapeNodes = cmds.listRelatives( tempGrp, children=True, shapes=True, fullPath=True )
            #print( origShapeNodes )
            #----- duplicate the temp group and original shape
            tempDupe = cmds.duplicate( tempGrp, name='dup_Grp' )
            #----- get the path of the duplicate shape
            newShapeNodes = cmds.listRelatives( tempDupe, children=True, shapes=True, fullPath=True )
            #print( newShapeNodes )
            #----- put the roiginal shape back where it came from
            cmds.parent( origShapeNodes, den_node, shape=True, relative=True )
            #----- put the duplicate shape under the Ctrl object
            if worldSpace:
                cmds.makeIdentity( tempDupe, apply=True )
                cmds.parent( newShapeNodes, den_CtrlNode, shape=True, relative=True )
            else:
                cmds.parent( newShapeNodes, den_CtrlNode, shape=True, relative=True )
                #---- clean up the empy temp nodes
            cmds.delete( tempGrp, tempDupe )
        else:
            print( den_node, 'IS', den_CtrlNode )




#-------------------------------------------------------------------------
# Lock
#
# - locks transform attrs on all selected nodes - does locking only, not unlocking

def den_LockAttr(denT=True,denR=True,denS=True,denV=True):
    #denT=True
    #denR=True
    #denS=True
    #denV=True
    objs = cmds.ls (sl=True)
    #print( objs )
    for obj in objs:
        if denT:
            cmds.setAttr (obj+'.tx', lock=True, keyable=False, channelBox=False)
            cmds.setAttr (obj+'.ty', lock=True, keyable=False, channelBox=False)
            cmds.setAttr (obj+'.tz', lock=True, keyable=False, channelBox=False)
        if denR:
            cmds.setAttr (obj+'.rx', lock=True, keyable=False, channelBox=False)
            cmds.setAttr (obj+'.ry', lock=True, keyable=False, channelBox=False)
            cmds.setAttr (obj+'.rz', lock=True, keyable=False, channelBox=False)
        if denS:
            cmds.setAttr (obj+'.sx', lock=True, keyable=False, channelBox=False)
            cmds.setAttr (obj+'.sy', lock=True, keyable=False, channelBox=False)
            cmds.setAttr (obj+'.sz', lock=True, keyable=False, channelBox=False)
        if denV:
            cmds.setAttr (obj+'.v', lock=True, keyable=False, channelBox=False)

#-------------------------------------------------------------------------
# Unlock
#
# - unlocks transform attrs on all selected nodes - does unlocking only, not locking

def den_UnLockAttr(denT=True,denR=True,denS=True,denV=True):
    #denT=True
    #denR=True
    #denS=True
    #denV=True
    objs = cmds.ls (sl=True)
    #print( objs )
    for obj in objs:
        if denT:
            cmds.setAttr (obj+'.tx', lock=False, keyable=True )
            cmds.setAttr (obj+'.ty', lock=False, keyable=True )
            cmds.setAttr (obj+'.tz', lock=False, keyable=True )
            #cmds.setAttr (obj+'.tx', keyable=True)
            #cmds.setAttr (obj+'.ty', keyable=True)
            #cmds.setAttr (obj+'.tz', keyable=True)
        if denR:
            cmds.setAttr (obj+'.rx', lock=False, keyable=True )
            cmds.setAttr (obj+'.ry', lock=False, keyable=True )
            cmds.setAttr (obj+'.rz', lock=False, keyable=True )
            #cmds.setAttr (obj+'.rx', keyable=True)
            #cmds.setAttr (obj+'.ry', keyable=True)
            #cmds.setAttr (obj+'.rz', keyable=True)
        if denS:
            cmds.setAttr (obj+'.sx', lock=False, keyable=True )
            cmds.setAttr (obj+'.sy', lock=False, keyable=True )
            cmds.setAttr (obj+'.sz', lock=False, keyable=True )
            #cmds.setAttr (obj+'.sx', keyable=True)
            #cmds.setAttr (obj+'.sy', keyable=True)
            #cmds.setAttr (obj+'.sz', keyable=True)
        if denV:
            cmds.setAttr (obj+'.v', lock=False, keyable=True )
            #cmds.setAttr (obj+'.v', keyable=True)




#-------------------------------------------------------------------------
# Lock Set - does individual channels
#
# - sets the lock state of individual transform channels ( 1 = locked, 0 = unlocked )
# - I am using this one more than the den_LockAttr or den_UnLockAttr lately

def den_Lock(  tx,ty,tz , rx,ry,rz , sx,sy,sz , v ):
    #denT=(0,0,0)
    #denR=(0,0,0)
    #denS=(0,0,0)
    #denV=(0)
    objs = cmds.ls (sl=True)
    #print( objs )
    for obj in objs:
        cmds.setAttr ( obj+'.tx', lock=tx, keyable=1-tx )
        cmds.setAttr ( obj+'.ty', lock=ty, keyable=1-ty )
        cmds.setAttr ( obj+'.tz', lock=tz, keyable=1-tz )
        cmds.setAttr ( obj+'.rx', lock=rx, keyable=1-rx )
        cmds.setAttr ( obj+'.ry', lock=ry, keyable=1-ry )
        cmds.setAttr ( obj+'.rz', lock=rz, keyable=1-rz )
        cmds.setAttr ( obj+'.sx', lock=sx, keyable=1-sx )
        cmds.setAttr ( obj+'.sy', lock=sy, keyable=1-sy )
        cmds.setAttr ( obj+'.sz', lock=sz, keyable=1-sz )
        cmds.setAttr ( obj+'.v', lock=v, keyable=1-v )




#-------------------------------------------------------------------------
# Add Zero Nulls to selected Controllers
#
# - adds a group above a controller to zero out the controller's transform

def den_AddZeroNull():
    #----- make a list of all selected nodes
    den_SelectedNodes = cmds.ls( uuid=True, selection=True )
    #print( 'den_SelectedNodes =', den_SelectedNodes )
    for den_node in den_SelectedNodes:
        #print( '== 1 ==', den_node )
        den_node = cmds.ls(den_node, long=True)[0]
        #print( '== 2 ==', den_node )
        m = re.compile("[^|]*$").search(den_node)
        den_shortname = m.group(0)
        #print( 'den_shortname =', den_shortname )
        den_parent = cmds.listRelatives( den_node, parent=True )
        #print( 'den_parent =', den_parent )
        den_Zero = cmds.createNode( 'transform', parent=den_node, name=den_shortname+'Zero' )
        if (den_parent == None): #just in case it has no parent
            den_Zero = cmds.parent( den_Zero, world=True, absolute=True )
        else:
            den_Zero = cmds.parent( den_Zero, den_parent, absolute=True )
            
        lastOne = cmds.parent( den_node, den_Zero, absolute=True )
        lastOne = cmds.ls( lastOne )
    return lastOne


#-------------------------------------------------------------------------
# Add Mocap Nulls to selected Controllers
#
# - adds a group above a controller to carry mocap animation leaving the controller free 
#   to make modification to the mocap without changing the mocap curves

def den_AddMocapNull():
    #----- make a list of all selected nodes
    den_SelectedNodes = cmds.ls( uuid=True, selection=True )
    #print 'den_SelectedNodes =', den_SelectedNodes )
    for den_node in den_SelectedNodes:
        #print( '== 1 ==', den_node )
        den_node = cmds.ls(den_node, long=True)[0]
        #print( '== 2 ==', den_node )
        m = re.compile("[^|]*$").search(den_node)
        den_shortname = m.group(0)
        #print( 'den_shortname =', den_shortname )
        den_parent = cmds.listRelatives( den_node, parent=True )
        #print( 'den_parent =', den_parent )
        den_Zero = cmds.createNode( 'transform', parent=den_node, name=den_shortname+'Mocap' )
        if (den_parent == None): #just in case it has no parent
            den_Zero = cmds.parent( den_Zero, world=True, absolute=True )
        else:
            den_Zero = cmds.parent( den_Zero, den_parent, absolute=True )
            
        lastOne = cmds.parent( den_node, den_Zero, absolute=True )
        lastOne = cmds.ls( lastOne )
    return lastOne


#-------------------------------------------------------------------------
# Add "Whatever" Nulls to selected Controllers
#
# - adds a group above a node that zeros transforms but can be named whatever

def den_AddNullAbove(addName='Connect'):
    #----- make a list of all selected nodes
    den_SelectedNodes = cmds.ls( uuid=True, selection=True )
    #print 'den_SelectedNodes =', den_SelectedNodes )
    for den_node in den_SelectedNodes:
        #print( '== 1 ==', den_node )
        den_node = cmds.ls(den_node, long=True)[0]
        #print( '== 2 ==', den_node )
        m = re.compile("[^|]*$").search(den_node)
        den_shortname = m.group(0)
        #print( 'den_shortname =', den_shortname )
        den_parent = cmds.listRelatives( den_node, parent=True )
        #print( 'den_parent =', den_parent )
        den_Zero = cmds.createNode( 'transform', parent=den_node, name=den_shortname+addName )
        if (den_parent == None): #just in case it has no parent
            den_Zero = cmds.parent( den_Zero, world=True, absolute=True )
        else:
            den_Zero = cmds.parent( den_Zero, den_parent, absolute=True )
            
        lastOne = cmds.parent( den_node, den_Zero, absolute=True )
        lastOne = cmds.ls( lastOne )
    return lastOne

#den_AddNullAbove(addName='Connect')

#-------------------------------------------------------------------------
# Add IK handle between first and second selection 
#
# - I made my own so I can control names of effector and handle

def den_AddIKHandle(handleType='ikSCsolver', makeUp=False, upPos=(0,-10,0)):
    
    #----- get the first joint
    den_firstNode = cmds.ls( long=True, selection=True, head=True )
    den_firstNodeName = cmds.ls( long=False, selection=True, head=True )
    print( 'den_firstNodeName = ', den_firstNodeName )
    #print( '----- get the ascii string of the short name of the controller node - regex voodoo' )
    den_firstNodeShortName = den_firstNodeName[0]
    print( 'den_firstNodeShortName = ', den_firstNodeShortName )
    #----- get the last joint
    den_lastNode = cmds.ls( long=True, selection=True, tail=True )
    den_lastNodeName = den_lastNode[0].encode('ascii','ignore')
    den_handle = cmds.ikHandle (sj=den_firstNodeName[0], ee=den_lastNodeName, sol=handleType, srp=True, n=den_firstNodeShortName+'Ikh' )
    #print( den_handle )
    #print( den_handle[0] )
    den_handleName = cmds.ls( den_handle )
    #print( den_handleName )
    #print( den_handleName[0] )
    if (makeUp and handleType == 'ikSCsolver'):
        print( 'WARNING - ikSCsolver does not support up opjects - no up object will be created' )
    if (makeUp and handleType == 'ikRPsolver'):
        den_Up = cmds.spaceLocator (n=den_firstNodeShortName+'Up')
        cmds.xform ( t=upPos )
        cmds.parent( den_Up, den_firstNode, relative=True )
        cmds.parent( den_Up, world=True )
        den_P1 = cmds.xform(den_firstNode,q=True,ws=True,t=True)
        cmds.poleVectorConstraint( den_Up, den_handleName[0] )
    cmds.rename(den_handle[1].encode('ascii','ignore'),den_firstNodeShortName+'Eff')
    #print( 'DONE' )
    return den_handleName[0]




#=========================================================================
# Control Objects


#-------------------------------------------------------------------------
# Ball Control
#
# - ball control used for controls that can be translated and rotated

def den_MakeBall (nodeName='Ball_Ctrl',pos=(0,0,0),radius=1,doT=False):
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    den_Shape1 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
    den_Shape2 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
    den_Shape3 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
    den_Geo1 = cmds.createNode( 'makeNurbCircle' )
    den_Geo2 = cmds.createNode( 'makeNurbCircle' )
    den_Geo3 = cmds.createNode( 'makeNurbCircle' )
    
    # .cc is short for .outputCurve
    # .cr is short for .create
    # .nr is short for .normal
    # .c  is short for .center
    # .r  is short for .radius
    cmds.connectAttr( str(den_Geo1)+'.oc', str(den_Shape1)+'.cr' )
    cmds.setAttr( str(den_Geo1)+'.nr',1,0,0)
    cmds.setAttr( str(den_Geo1)+'.c',pos[0],pos[1],pos[2])
    cmds.setAttr( str(den_Geo1)+'.r',radius)
    cmds.connectAttr( str(den_Geo2)+'.oc', str(den_Shape2)+'.cr' )
    cmds.setAttr( str(den_Geo2)+'.nr',0,1,0)
    cmds.setAttr( str(den_Geo2)+'.c',pos[0],pos[1],pos[2])
    cmds.setAttr( str(den_Geo2)+'.r',radius)
    cmds.connectAttr( str(den_Geo3)+'.oc', str(den_Shape3)+'.cr' )
    cmds.setAttr( str(den_Geo3)+'.nr',0,0,1)
    cmds.setAttr( str(den_Geo3)+'.c',pos[0],pos[1],pos[2])
    cmds.setAttr( str(den_Geo3)+'.r',radius)
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Pole Control
#
# - pole control used for control of pole vectors on rotatePlane ik solvers

def den_MakePole (nodeName='Pole_Ctrl',pos=(0,0,0),radius=1,doT=False):
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,True,True,False)
    den_Shape1 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
    den_Shape2 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
    den_Shape3 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
    den_Geo1 = cmds.createNode( 'makeNurbCircle' )
    den_Geo2 = cmds.createNode( 'makeNurbCircle' )
    den_Geo3 = cmds.createNode( 'makeNurbCircle' )
    
    # .cc is short for .outputCurve
    # .cr is short for .create
    # .nr is short for .normal
    # .c  is short for .center
    # .r  is short for .radius
    cmds.connectAttr( str(den_Geo1)+'.oc', str(den_Shape1)+'.cr' )
    cmds.setAttr( str(den_Geo1)+'.nr',1,0,0)
    cmds.setAttr( str(den_Geo1)+'.c',pos[0],pos[1],pos[2])
    cmds.setAttr( str(den_Geo1)+'.r',radius)
    cmds.setAttr( str(den_Geo1)+'.degree',1)
    cmds.setAttr( str(den_Geo1)+'.sections',4)
    cmds.connectAttr( str(den_Geo2)+'.oc', str(den_Shape2)+'.cr' )
    cmds.setAttr( str(den_Geo2)+'.nr',0,1,0)
    cmds.setAttr( str(den_Geo2)+'.c',pos[0],pos[1],pos[2])
    cmds.setAttr( str(den_Geo2)+'.r',radius)
    cmds.setAttr( str(den_Geo2)+'.degree',1)
    cmds.setAttr( str(den_Geo2)+'.sections',4)
    cmds.connectAttr( str(den_Geo3)+'.oc', str(den_Shape3)+'.cr' )
    cmds.setAttr( str(den_Geo3)+'.nr',0,0,1)
    cmds.setAttr( str(den_Geo3)+'.c',pos[0],pos[1],pos[2])
    cmds.setAttr( str(den_Geo3)+'.r',radius)
    cmds.setAttr( str(den_Geo3)+'.degree',1)
    cmds.setAttr( str(den_Geo3)+'.sections',4)
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Cube Control
#
# - cube control used for controls that can be translated only

def den_MakeCube (nodeName='Cube_Ctrl',pos=(0,0,0),radius=1,doT=False):
    #nodeName='Cube_Ctrl'
    #pos=(0,5,1)
    #radius=2.3
    #doT=True
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,True,True,False)
    
    tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[
    ( -0.75,0.75,0.75 ),
    ( -0.75,-0.75,0.75 ),
    ( 0.75,-0.75,0.75 ),
    ( 0.75,0.75,0.75 ),
    ( 0.75,0.75,-0.75 ),
    ( 0.75,-0.75,-0.75 ),
    ( -0.75,-0.75,-0.75 ),
    ( -0.75,0.75,-0.75 ),
    ( -0.75,0.75,0.75 ),
    ( 0.75,0.75,0.75 ),
    ( 0.75,0.75,-0.75 ),
    ( -0.75,0.75,-0.75 ),
    ( -0.75,-0.75,-0.75 ),
    ( -0.75,-0.75,0.75 ),
    ( 0.75,-0.75,0.75 ),
    ( 0.75,-0.75,-0.75 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    cmds.move(pos[0],pos[1],pos[2], relative=True )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    
    return den_Ctrl



#-------------------------------------------------------------------------
# Spike Control
#
# - spike control used for controls that can be rotated only

def den_MakeSpike (nodeName='Spike_Ctrl',pos=(0,0,0),radius=1,doT=False,axis='+Y'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,False,True,False)
    
    tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[
    ( -0.1,1.0,0.0 ),
    ( 0.0,1.0,-0.1 ),
    ( 0.1,1.0,0.0 ),
    ( 0.0,1.0,0.1 ),
    ( -0.1,1.0,0.0 ),
    ( 0.0,0.0,0.0 ),
    ( 0.1,1.0,0.0 ),
    ( 0.0,1.0,0.1 ),
    ( 0.0,0.0,0.0 ),
    ( 0.0,1.0,-0.1 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if axis == '+X': cmds.rotate(0,0,-90)
    if axis == '-X': cmds.rotate(0,0,90)
    if axis == '+Y': cmds.rotate(0,0,0)
    if axis == '-Y': cmds.rotate(0,0,180)
    if axis == '+Z': cmds.rotate(90,0,0)
    if axis == '-Z': cmds.rotate(-90,0,0)
    cmds.move(pos[0],pos[1],pos[2], relative=True )
 
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# ArrowT Control
#
# - ArrowT control used for controls that can be translated along a singe axis only - a slider

def den_MakeArrowT (nodeName='ArrowT_Ctrl',pos=(0,0,0),radius=1,doT=False,axis='+Y',flip=False):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[
    ( 0.0,0.2,0.0 ),
    ( -0.2,0.2,0.0 ),
    ( -0.4,0.2,0.0 ),
    ( -0.6,0.2,0.0 ),
    ( -0.6,0.4,0.0 ),
    ( -1.0,0.0,0.0 ),
    ( -0.6,-0.4,0.0 ),
    ( -0.6,-0.2,0.0 ),
    ( -0.4,-0.2,0.0 ),
    ( -0.2,-0.2,0.0 ),
    ( 0.0,-0.2,0.0 ),
    ( 0.2,-0.2,0.0 ),
    ( 0.4,-0.2,0.0 ),
    ( 0.6,-0.2,0.0 ),
    ( 0.6,-0.4,0.0 ),
    ( 1.0,0.0,0.0 ),
    ( 0.6,0.4,0.0 ),
    ( 0.6,0.2,0.0 ),
    ( 0.4,0.2,0.0 ),
    ( 0.2,0.2,0.0 ),
    ( 0.0,0.2,0.0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.move(0,0.5,0, relative=True )
    cmds.scale(radius,radius,radius, relative=True )
    if flip == True: cmds.rotate(0,90,0)
    if axis == '+X': cmds.rotate(0,0,-90)
    if axis == '-X': cmds.rotate(0,0,90)
    if axis == '+Y': cmds.rotate(0,0,0)
    if axis == '-Y': cmds.rotate(0,0,180)
    if axis == '+Z': cmds.rotate(90,0,0)
    if axis == '-Z': cmds.rotate(-90,0,0)
    cmds.move(pos[0],pos[1],pos[2], relative=True )
     
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# ArrowR Control
#
# - ArrowR control used for controls that should be rotated on a singe axis only - elbows, knees, knuckes

def den_MakeArrowR (nodeName='ArrowR_Ctrl',pos=(0,0,0),radius=1,doT=False,axis='+Y',flip=False):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[
    ( 0.0,0.2,0.0 ),
    ( -0.24640014468658333,0.16974586642824568,0.0 ),
    ( -0.47816201468635794,0.08078081984277874,0.0 ),
    ( -0.6815169739488035,-0.06160985556511385,0.0 ),
    ( -0.8153430952205751,0.0870191095303648,0.0 ),
    ( -0.8289715623111973,-0.49426493424844165,0.0 ),
    ( -0.2800386101334885,-0.5074967508515505,0.0 ),
    ( -0.4138647314052601,-0.3588677857560718,0.0 ),
    ( -0.2903733895720016,-0.272398217300792,0.0 ),
    ( -0.1496313864467162,-0.21837242408215293,0.0 ),
    ( 0.0,-0.2,0.0 ),
    ( 0.14963138644671622,-0.21837242408215293,0.0 ),
    ( 0.2903733895720016,-0.2723982173007921,0.0 ),
    ( 0.41386473140526014,-0.3588677857560717,0.0 ),
    ( 0.28003861013348846,-0.5074967508515507,0.0 ),
    ( 0.8289715623111974,-0.49426493424844176,0.0 ),
    ( 0.8153430952205751,0.0870191095303649,0.0 ),
    ( 0.6815169739488036,-0.06160985556511405,0.0 ),
    ( 0.47816201468635794,0.08078081984277885,0.0 ),
    ( 0.24640014468658333,0.16974586642824582,0.0 ),
    ( 0.0,0.2,0.0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.move(0,1,0, relative=True )
    cmds.scale(radius,radius,radius, relative=True )
    if flip == True: cmds.rotate(0,90,0)
    if axis == '+X': cmds.rotate(0,0,-90)
    if axis == '-X': cmds.rotate(0,0,90)
    if axis == '+Y': cmds.rotate(0,0,0)
    if axis == '-Y': cmds.rotate(0,0,180)
    if axis == '+Z': cmds.rotate(90,0,0)
    if axis == '-Z': cmds.rotate(-90,0,0)
    cmds.move(pos[0],pos[1],pos[2], relative=True )
     
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Gear Control
#
# - Gear control used for non-transform attrs like FK/IK, space switching, special foot control attrs, etc.

def den_MakeGear (nodeName='Gear_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[
    ( 0.0,1.0,0.0 ),
    ( -0.13052619222005152,0.9914448613738104,0.0 ),
    ( -0.1393530731647401,0.700575208070201,0.0 ),
    ( -0.27335088587786305,0.6599274159730372,0.0 ),
    ( -0.3968439773436426,0.5939189833715884,0.0 ),
    ( -0.6087614290087205,0.7933533402912349,0.0 ),
    ( -0.7071067811865474,0.7071067811865472,0.0 ),
    ( -0.7933533402912349,0.6087614290087203,0.0 ),
    ( -0.5939189833715881,0.3968439773436425,0.0 ),
    ( -0.6599274159730366,0.27335088587786305,0.0 ),
    ( -0.7005752080702001,0.1393530731647401,0.0 ),
    ( -0.9914448613738097,0.13052619222005146,0.0 ),
    ( -1.0,0.0,0.0 ),
    #( -1.0,0.0,0.0 ),
    ( -0.9914448613738104,-0.13052619222005152,0.0 ),
    ( -0.700575208070201,-0.1393530731647401,0.0 ),
    ( -0.6599274159730372,-0.27335088587786305,0.0 ),
    ( -0.5939189833715884,-0.3968439773436426,0.0 ),
    ( -0.7933533402912349,-0.6087614290087205,0.0 ),
    ( -0.7071067811865472,-0.7071067811865474,0.0 ),
    ( -0.6087614290087203,-0.7933533402912349,0.0 ),
    ( -0.3968439773436425,-0.5939189833715881,0.0 ),
    ( -0.27335088587786305,-0.6599274159730366,0.0 ),
    ( -0.1393530731647401,-0.7005752080702001,0.0 ),
    ( -0.13052619222005146,-0.9914448613738097,0.0 ),
    ( 0.0,-1.0,0.0 ),
    #( 0.0,-1.0,0.0 ),
    ( 0.1305261922200514,-0.9914448613738104,0.0 ),
    ( 0.13935307316474002,-0.700575208070201,0.0 ),
    ( 0.273350885877863,-0.6599274159730372,0.0 ),
    ( 0.3968439773436425,-0.5939189833715884,0.0 ),
    ( 0.6087614290087204,-0.793353340291235,0.0 ),
    ( 0.7071067811865472,-0.7071067811865474,0.0 ),
    ( 0.7933533402912348,-0.6087614290087204,0.0 ),
    ( 0.5939189833715881,-0.3968439773436426,0.0 ),
    ( 0.6599274159730366,-0.2733508858778631,0.0 ),
    ( 0.7005752080702001,-0.1393530731647402,0.0 ),
    ( 0.9914448613738097,-0.13052619222005157,0.0 ),
    ( 1.0,0.0,0.0 ),
    #( 1.0,0.0,0.0 ),
    ( 0.9914448613738104,0.1305261922200513,0.0 ),
    ( 0.700575208070201,0.13935307316473994,0.0 ),
    ( 0.6599274159730373,0.2733508858778629,0.0 ),
    ( 0.5939189833715885,0.39684397734364246,0.0 ),
    ( 0.793353340291235,0.6087614290087203,0.0 ),
    ( 0.7071067811865474,0.7071067811865472,0.0 ),
    ( 0.6087614290087205,0.7933533402912348,0.0 ),
    ( 0.39684397734364263,0.593918983371588,0.0 ),
    ( 0.2733508858778632,0.6599274159730365,0.0 ),
    ( 0.13935307316474027,0.7005752080702001,0.0 ),
    ( 0.13052619222005168,0.9914448613738097,0.0 ),
    ( 0.0,1.0,0.0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Circle Control
#
# - Circle control used by CAAR for ribbons, etc.

def den_MakeCircle (nodeName='Circle_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
    ( -1.1100856969603225e-16,-1.1081941875543884,0.0 ),
    ( 0.7836116248912245,-0.7836116248912244,0.0 ),
    ( 1.1081941875543881,-1.511240500779959e-16,0.0 ),
    ( 0.7836116248912245,0.7836116248912246,0.0 ),
    ( 6.785732323110912e-17,1.1081941875543877,0.0 ),
    ( -0.7836116248912245,0.7836116248912244,0.0 ),
    ( -1.1081941875543881,5.74489823752483e-17,0.0 ),
    ( -0.7836116248912245,-0.7836116248912245,0.0 ),
    ( -1.1100856969603225e-16,-1.1081941875543884,0.0 ),
    ( 0.7836116248912245,-0.7836116248912244,0.0 ),
    ( 1.1081941875543881,-1.511240500779959e-16,0.0 ),
    ] )
    
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl

#den_MakeCircle (nodeName='Gear_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY')



#-------------------------------------------------------------------------
# CAAR Shoulder Control
#
# - Shoulder control used by CAAR for shoulders.

def den_MakeShld (nodeName='Shld_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
    ( -1.1100856969603225e-16,-1.1081941875543884,0.0 ),
    ( 0.5413315306977202,-0.5413315306977201,0.0 ),
    ( 1.1081941875543881,-1.511240500779959e-16,0.0 ),
    ( 0.5413315306977202,0.5413315306977203,0.0 ),
    ( 6.785732323110912e-17,1.1081941875543877,0.0 ),
    ( -0.5413315306977202,0.5413315306977201,0.0 ),
    ( -1.1081941875543881,5.74489823752483e-17,0.0 ),
    ( -0.5413315306977202,-0.5413315306977202,0.0 ),
    ( -1.1100856969603225e-16,-1.1081941875543884,0.0 ),
    ( 0.5413315306977202,-0.5413315306977201,0.0 ),
    ( 1.1081941875543881,-1.511240500779959e-16,0.0 ),
    ] )
    
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl

#den_MakeShld (nodeName='Gear_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='YZ')



#-------------------------------------------------------------------------
# Label Control
#
# - Label control used for start circle in base rig.

def den_MakeLabel (nodeName='Label_Ctrl',pos=(0,0,0),radius=1,doT=False,label='abcdef',doCircle=True):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,False,False)
    if doCircle == True:
        den_Shape1 = cmds.createNode( 'nurbsCurve', parent=den_Ctrl )
        den_Geo1 = cmds.createNode( 'makeNurbCircle' )
        
        cmds.connectAttr( str(den_Geo1)+'.oc', str(den_Shape1)+'.cr' )
        cmds.setAttr( str(den_Geo1)+'.nr',0,1,0)
        cmds.setAttr( str(den_Geo1)+'.r',radius)
    
    textNode = cmds.textCurves( font='Arial', text=label, object=True )
    #print( 'textNode', textNode )
    cmds.xform( s=(radius*0.25,radius*0.25,radius*0.25) )
    bbx = cmds.xform(textNode[0], q=True, bb=True, ws=True)
    #print( bbx )
    if doT:
        cmds.xform( t=(bbx[3]*0.05+pos[0],-bbx[4]*0.5+pos[1],0+pos[2]) )
    else:
        cmds.xform( t=(-bbx[3]*0.5+pos[0],-bbx[4]*1.5+pos[1],0+pos[2]) )
    textShapes = cmds.listRelatives( textNode[0], ad=True, type='nurbsCurve', fullPath=True)
    textNulls = cmds.listRelatives( textNode[0], children=True, fullPath=True)
    cmds.delete( textNode[1] )
    cmds.makeIdentity( textNode[0], apply=True )
    cmds.parent( textShapes, den_Ctrl, shape=True, relative=True )
    cmds.delete( textNode[0] )
    #print( textShapes )
    #print( textNulls )
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Hand Control
#
# - Hand control used as alternative hand-specific control icon.

def den_MakeHand (nodeName='Hand_Ctrl',pos=(0,0,0),length=10.0,width=6.0,doT=False,flipSide=0,Plane='ZX'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, p=[
    ( 0.132896512746811,0.0,-0.979345679283142 ),
    ( -0.164490967988968,0.0,-1.00268518924713 ),
    ( -0.462559789419174,0.0,-0.899686813354492 ),
    ( -0.701837241649628,0.0,-0.679595828056335 ),
    ( -0.892876982688904,0.0,-0.303486317396164 ),
    ( -1.20326960086823,0.0,-0.0497146807610989 ),
    ( -0.980591356754303,0.0,0.0447365343570709 ),
    ( -0.764630913734436,0.0,-0.0797152668237686 ),
    ( -0.523047983646393,0.0,-0.434768915176392 ),
    ( -0.41252464056015,0.0,-0.265908032655716 ),
    ( -0.439230889081955,0.0,0.150825962424278 ),
    ( -0.459335803985596,0.0,0.535560190677643 ),
    ( -0.468168467283249,0.0,1.01066792011261 ),
    ( -0.261100679636002,0.0,1.04075109958649 ),
    ( -0.255842655897141,0.0,0.674316227436066 ),
    ( -0.200877845287323,0.0,0.193377047777176 ),
    ( -0.122820235788822,0.0,0.218923181295395 ),
    ( -0.11007771641016,0.0,0.739979863166809 ),
    ( -0.121693402528763,0.0,1.20271003246307 ),
    ( 0.12801256775856,0.0,1.2059713602066 ),
    ( 0.0936835706233978,0.0,0.727361381053925 ),
    ( 0.0843872427940369,0.0,0.238792389631271 ),
    ( 0.189410209655762,0.0,0.227438554167747 ),
    ( 0.200983062386513,0.0,0.718604862689972 ),
    ( 0.209904432296753,0.0,1.14940941333771 ),
    ( 0.435678869485855,0.0,1.13308680057526 ),
    ( 0.420008957386017,0.0,0.61379486322403 ),
    ( 0.387091159820557,0.0,0.177194803953171 ),
    ( 0.465325862169266,0.0,0.13681560754776 ),
    ( 0.586037158966064,0.0,0.385148823261261 ),
    ( 0.618980288505554,0.0,0.754843890666962 ),
    ( 0.822321057319641,0.0,0.72486424446106 ),
    ( 0.759187638759613,0.0,0.333903968334198 ),
    ( 0.64460277557373,0.0,-0.0211497098207474 ),
    ( 0.590713083744049,0.0,-0.467614144086838 ),
    ( 0.536983132362366,0.0,-1.01462519168854 ),
    ( 0.132896512746811,0.0,-0.979345679283142 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(width*0.5,1,length*0.5, relative=True )
    if flipSide == True: cmds.scale(-1,1,1, relative=True )
    if Plane == 'XY': cmds.rotate(-90,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,0,90, rfl=False)
    if Plane == 'ZX': cmds.rotate(0,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Mitten Control
#
# - Mitten control used as alternative hand-specific control icon.

def den_MakeMitten (nodeName='Mitten_Ctrl',pos=(0,0,0),length=10.0,width=10.0,doT=False,flipSide=0,Plane='ZX'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, p=[
    ( 0.042797443437439506,0.0,-0.07935716752615712 ),
    ( -0.10589629693045,0.0,-0.09102692250815114 ),
    ( -0.24950193245030827,0.0,-0.02786960565684496 ),
    ( -0.42561099188224466,0.0,0.2585725134173319 ),
    ( -0.5808073009719076,0.0,0.38545833173486443 ),
    ( -0.4465558297249194,0.0,0.4606270476331365 ),
    ( -0.36148795740501066,0.0,0.37045803870352956 ),
    ( -0.18543482081786763,0.0,0.2773616557875559 ),
    ( -0.19878794507877015,0.0,0.4857286533275529 ),
    ( -0.21325673417941715,0.0,0.9156496321717189 ),
    ( -0.040019201802174144,0.0,1.0116706883469493 ),
    ( 0.23866693420513485,0.0,0.9768590724030438 ),
    ( 0.34312888724907237,0.0,0.3997408172050402 ),
    ( 0.24484075324521698,0.0,-0.09699692372885615 ),
    ( 0.042797443437439506,0.0,-0.07935716752615712 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(width*0.5,1,length*0.5, relative=True )
    cmds.rotate(0,90,0, rfl=False)
    if flipSide == True: cmds.scale(-1,1,1, relative=True )
    if Plane == 'XY': cmds.rotate(-90,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,0,90, rfl=False)
    if Plane == 'ZX': cmds.rotate(0,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Foot Control
#
# - Foot control used as alternative foot-specific control icon.

def den_MakeFoot (nodeName='Foot_Ctrl',pos=(0,0,0),length=10.0,width=6.0,doT=False,flipSide=0,Plane='ZX'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, p=[
    ( -0.00735962390899658,0.0,-0.992805361747742 ),
    ( -0.155183672904968,0.0,-0.979252457618713 ),
    ( -0.236298784613609,0.0,-0.865706622600555 ),
    ( -0.236298784613609,0.0,-0.610096096992493 ),
    ( -0.192561194300652,0.0,-0.391179502010345 ),
    ( -0.182810857892036,0.0,-0.14228393137455 ),
    ( -0.309567093849182,0.0,0.168967470526695 ),
    ( -0.332181751728058,0.0,0.53178733587265 ),
    ( -0.254931509494781,0.0,0.69559907913208 ),
    ( -0.319464862346649,0.0,0.761254370212555 ),
    ( -0.221974015235901,0.0,0.97146874666214 ),
    ( -0.0758093595504761,0.0,1.00941228866577 ),
    ( -0.0267009884119034,0.0,0.962047696113586 ),
    ( 0.015304297208786,0.0,0.983547925949097 ),
    ( 0.123179629445076,0.0,0.970612287521362 ),
    ( 0.129174843430519,0.0,0.908947110176086 ),
    ( 0.177993103861809,0.0,0.921794056892395 ),
    ( 0.249935805797577,0.0,0.878970980644226 ),
    ( 0.241371184587479,0.0,0.787155151367188 ),
    ( 0.267921477556229,0.0,0.773451745510101 ),
    ( 0.323591411113739,0.0,0.729946851730347 ),
    ( 0.318452656269073,0.0,0.674276947975159 ),
    ( 0.362988591194153,0.0,0.678559243679047 ),
    ( 0.403836220502853,0.0,0.622708022594452 ),
    ( 0.410198241472244,0.0,0.532392382621765 ),
    ( 0.390486508607864,0.0,0.410090982913971 ),
    ( 0.426273375749588,0.0,0.309025913476944 ),
    ( 0.408830523490906,0.0,0.154532194137573 ),
    ( 0.353150546550751,0.0,-0.139504283666611 ),
    ( 0.291592478752136,0.0,-0.432280093431473 ),
    ( 0.258251994848251,0.0,-0.774020254611969 ),
    ( 0.177679106593132,0.0,-0.979619979858398 ),
    ( -0.00735962390899658,0.0,-0.992805361747742 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(width*0.5,1,length*0.5, relative=True )
    if flipSide == True: cmds.scale(-1,1,1, relative=True )
    if Plane == 'XY': cmds.rotate(-90,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,0,90, rfl=False)
    if Plane == 'ZX': cmds.rotate(0,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Foot Control
#
# - Foot control used by CAAR for shoulders.

def caar_FootCtrl (nodeName='Foot_Ctrl',pos=(0,0,0),length=10.0,width=6.0,doT=False,flipSide=0,Plane='ZX'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
    ( -1.1100856969603225e-16,-6.785732323110917e-17,5.522389342278821 ),
    ( 1.8334901309796905,-4.798237340988472e-17,3.312469066183078 ),
    ( 1.4699969999536724,-9.253679210110099e-33,-5.735966605990051e-16 ),
    ( 1.2204214980138874,4.798237340988473e-17,-4.290419556087412 ),
    ( 6.785732323110912e-17,6.785732323110912e-17,-5.310925891255016 ),
    ( -1.2204214980138874,4.798237340988472e-17,-4.290419556087412 ),
    ( -0.7463913751551039,3.517735619006027e-33,-1.6129645840569515e-15 ),
    ( -1.8334901309796905,-4.7982373409884725e-17,3.9049189522776677 ),
    ( -1.1100856969603225e-16,-6.785732323110917e-17,5.522389342278821 ),
    ( 1.8334901309796905,-4.798237340988472e-17,3.312469066183078 ),
    ( 1.4699969999536724,-9.253679210110099e-33,-5.735966605990051e-16 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(width*0.5,1,length*0.5, relative=True )
    if flipSide == True: cmds.scale(-1,1,1, relative=True )
    if Plane == 'XY': cmds.rotate(-90,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,0,90, rfl=False)
    if Plane == 'ZX': cmds.rotate(0,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# Paw Foot Control
#
# - Paw Foot control used as alternative foot-specific control icon for animals.

def den_MakePaw (nodeName='Paw_Ctrl',pos=(0,0,0),length=10.0,width=6.0,doT=False,flipSide=0,Plane='ZX'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, p=[
    ( 0.00239582825452089,0.0,0.675144672393799 ),
    ( 0.208657398819923,0.0,0.965265870094299 ),
    ( 0.513342380523682,0.0,0.819695949554443 ),
    ( 0.55867475271225,0.0,0.313184678554535 ),
    ( 0.55867475271225,0.0,0.313184678554535 ),
    ( 0.731642484664917,0.0,0.504274487495422 ),
    ( 1.00520014762878,0.0,0.330960363149643 ),
    ( 1.00520002841949,0.0,-0.205905020236969 ),
    ( 0.617333948612213,0.0,-0.864027738571167 ),
    ( 0.00239573488943279,0.0,-1.05501067638397 ),
    ( -0.597679436206818,0.0,-0.864027619361877 ),
    ( -1.02440166473389,0.0,-0.205905079841614 ),
    ( -1.02440166473389,0.0,0.655509233474731 ),
    ( -0.711987614631653,0.0,0.828823328018188 ),
    ( -0.560393333435059,0.0,0.571013927459717 ),
    ( -0.560393333435059,0.0,0.571013927459717 ),
    ( -0.449882805347443,0.0,0.971422135829926 ),
    ( -0.16737174987793,0.0,1.05615627765656 ),
    ( 0.00239582825452089,0.0,0.675144672393799 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(width*0.5,1,length*0.5, relative=True )
    if flipSide == True: cmds.scale(-1,1,1, relative=True )
    if Plane == 'XY': cmds.rotate(-90,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,0,90, rfl=False)
    if Plane == 'ZX': cmds.rotate(0,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Head Control
#
# - Head control used by CAAR for character head.

def caar_HeadCtrl (nodeName='Head_Ctrl',pos=(0,0,0),radius=1,doT=False):
    #nodeName='Cube_Ctrl'
    #pos=(0,5,1)
    #radius=2.3
    #doT=True
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], p=[
	( 4.4199352728922303,19.903381853022136,-3.2174337044908272 ),
	( 2.4749402361388334e-15,20.965212125702788,-3.7820188752988102 ),
	( -4.4199352728922374,19.903381853022136,-3.2174337044908272 ),
	( -9.0091132473647537,16.879545068480432,-1.6096311663450837 ),
	( -10.366606373043718,12.354053511375428,0.7966153774720377 ),
	( -9.5294488565432864,7.0158722475932489,3.6349767033436153 ),
	( -7.533423177845715,1.6776909838110696,6.473338029215193 ),
	( -6.6257161733385628,0.17915846391943013,11.374817045786386 ),
	( -3.9005575641993944,-0.82212895409953557,14.649880618868945 ),
	( 7.702550689831802e-16,-1.1737343375454943,15.79993000798628 ),
	( 3.9005575641993975,-0.82212895409953557,14.649880618868945 ),
	( 6.6257161733385619,0.17915846391943457,11.374817045786376 ),
	( 7.5334231778457177,1.6776909838110732,6.4733380292151912 ),
	( 9.5294488565432811,7.0158722475932516,3.634976703343614 ),
	( 10.366606373043718,12.354053511375435,0.79661537747203504 ),
	( 9.0091132473647502,16.879545068480432,-1.6096311663450846 ),
	( 4.4199352728922303,19.903381853022136,-3.2174337044908272 ),
	( 2.4749402361388334e-15,20.965212125702788,-3.7820188752988102 ),
	( -4.4199352728922374,19.903381853022136,-3.2174337044908272 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    cmds.move(pos[0],pos[1],pos[2], relative=True )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Neck Control
#
# - Neck control used by CAAR for character neck or spine controls.

def caar_NeckCtrl (nodeName='Neck_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
	( 3.1088464742549182, -0.16118066186453728, 0 ),
	( 2.6921244322874004e-16, 2.8545602041723361, 0 ),
	( -3.1088464742549182, -0.1611806618645375, 0 ),
	( -4.3965728472270804, -0.51161096757509239, 0 ),
	( -3.1088464742549182, -1.7284039116469867, 0 ),
	( -4.4040770906059008e-16, 0.63817182906356074, 0 ),
	( 3.1088464742549182, -1.7284039116469863, 0 ),
	( 4.3965728472270804, -0.51161096757509261, 0 ),
	( 3.1088464742549182, -0.16118066186453728, 0 ),
	( 2.6921244322874004e-16, 2.8545602041723361, 0 ),
	( -3.1088464742549182, -0.1611806618645375, 0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Chest Control
#
# - Chest control used by CAAR for character chest.

def caar_ChestCtrl (nodeName='Chest_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
	( 7.2007365387318849, 9.3872523191584101, 0 ),
	( 6.6766816779705306e-16, 5.5270920570113988, 0 ),
	( -7.2007365387318849, 9.3872523191584101, 0 ),
	( -11.389875756552613, 2.285856416880931e-15, 0 ),
	( -6.6895244041155122, -9.6779526062861621, 0 ),
	( -1.0922459774355285e-15, -2.5615605251203273, 0 ),
	( 6.6895244041155122, -9.6779526062861621, 0 ),
	( 11.389875756552613, 8.8709955749423899e-16, 0 ),
	( 7.2007365387318849, 9.3872523191584101, 0 ),
	( 6.6766816779705306e-16, 5.5270920570113988, 0 ),
	( -7.2007365387318849, 9.3872523191584101, 0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Stomach Control
#
# - Stomach control used by CAAR for character stomach.

def caar_StomachCtrl (nodeName='Stomach_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
	( 6.3529465569175656, 4.2338889289893986, 0 ),
	( 5.5542204511292355e-16, 6.2242094478875014, 0 ),
	( -6.3529465569175656, 4.2338889289893968, 0 ),
	( -8.8691585700726741, -0.76597559689683148, 0 ),
	( -5.6783963522335039, -5.5225751949665103, 0 ),
	( -9.086212639959287e-16, -1.6503694856030728, 0 ),
	( 5.6783963522335039, -5.5225751949665103, 0 ),
	( 8.8691585700726741, -0.76597559689683259, 0 ),
	( 6.3529465569175656, 4.2338889289893986, 0 ),
	( 5.5542204511292355e-16, 6.2242094478875014, 0 ),
	( -6.3529465569175656, 4.2338889289893968, 0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Hip Control
#
# - Hip control used by CAAR for character hips/pelvis.

def caar_HipCtrl (nodeName='Hip_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
    ( 3.9394248191045897,3.3397259028806587,7.450518798828132e-12 ),
    ( 5.987616282934396e-15,3.524422497840817,7.450518798828122e-12 ),
    ( -3.939424819104612,3.3397259028806587,7.450518798828134e-12 ),
    ( -7.639611553544983,0.01574644251411428,7.450518798828127e-12 ),
    ( -3.93942481910461,-3.443439143337585,7.450518798828114e-12 ),
    ( -1.13122626211706e-14,-3.401421489636519,7.45051879882815e-12 ),
    ( 3.9394248191046017,-3.4434391433376135,7.450518798828114e-12 ),
    ( 7.639611553545,0.01574644251412849,7.450518798828127e-12 ),
    ( 3.9394248191045897,3.3397259028806587,7.450518798828132e-12 ),
    ( 5.987616282934396e-15,3.524422497840817,7.450518798828122e-12 ),
    ( -3.939424819104612,3.3397259028806587,7.450518798828134e-12 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Rotate Control
#
# - Rotate control used by CAAR for rotation-only controls.

def caar_RotateCtrl (nodeName='Rotate_Ctrl',pos=(0,0,0),radius=1,doT=False,axis='+Y',flip=False):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
	( 0, 0, 0 ),
	( 2.5278613118576751e-16, 7.4505187988281261, -4.1283108135630133 ),
	( 1.7874678755136844e-16, 10.369675369944286, -2.9191565711161607 ),
	( 1.3104477679355846e-32, 11.578829612391139, -2.1401236158016656e-16 ),
	( -1.7874678755136844e-16, 10.369675369944286, 2.9191565711161607 ),
	( -2.5278613118576766e-16, 7.4505187988281261, 4.128310813563016 ),
	( 0, 0, 0 ),
	( 0, 0, 0 ),
	( 0, 0, 0 ),
	( 2.5278613118576751e-16, 7.4505187988281261, -4.1283108135630133 ),
	( 1.7874678755136844e-16, 10.369675369944286, -2.9191565711161607 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.move(0,0,0, relative=True )
    cmds.scale(radius,radius,radius, relative=True )
    if flip == True: cmds.rotate(0,90,0)
    if axis == '+X': cmds.rotate(0,0,-90)
    if axis == '-X': cmds.rotate(0,0,90)
    if axis == '+Y': cmds.rotate(0,0,0)
    if axis == '-Y': cmds.rotate(0,0,180)
    if axis == '+Z': cmds.rotate(90,0,0)
    if axis == '-Z': cmds.rotate(-90,0,0)
    cmds.move(pos[0],pos[1],pos[2], relative=True )
     
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Rotate Control
#
# - Rotate control used by CAAR for rotation-only controls.

def caar_CogCtrl (nodeName='Cog_Ctrl',pos=(0,0,0),radius=1,doT=False):
#def caar_CogCtrl (nodeName='Cog_Ctrl',pos=(0,0,0),radius=1,doT=False,Plane='XY'):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10], p=[
	( 10.576129835601327, 4.8570089137220236e-16, -7.93209751105978 ),
	( 9.1584636826718631e-16, 2.2163374228528028, -11.217679878206594 ),
	( -10.576129835601327, 4.8570089137220217e-16, -7.93209751105978 ),
	( -14.956906250926117, 2.6049486529631209e-31, -3.6199246241594149e-15 ),
	( -10.576129835601327, -4.8570089137220227e-16, 7.93209751105978 ),
	( -1.4982435286518474e-15, 2.4521179997520344, 11.217679878206612 ),
	( 10.576129835601327, -4.8570089137220217e-16, 7.93209751105978 ),
	( 14.956906250926117, 1.3121640060686057e-31, -1.5086470741023628e-15 ),
	( 10.576129835601327, 4.8570089137220236e-16, -7.93209751105978 ),
	( 9.1584636826718631e-16, 2.2163374228528028, -11.217679878206594 ),
	( -10.576129835601327, 4.8570089137220217e-16, -7.93209751105978 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.scale(radius,radius,radius, relative=True )
    #if Plane == 'XY': cmds.rotate(0,0,0, rfl=False)
    #if Plane == 'YZ': cmds.rotate(0,90,0, rfl=False)
    #if Plane == 'ZX': cmds.rotate(90,0,0, rfl=False)
    cmds.move(pos[0],pos[1],pos[2], relative=True, rfl=False )
    
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Finger Control
#
# - Finger control used by CAAR for finger-specific rotation-only controls.

def caar_FingCtrl (nodeName='Fing_Ctrl',pos=(0,0,0),radius=1,doT=False,axis='+Y',flip=False):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(True,False,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=3, periodic=True, k=[-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], p=[
	( 0.49438089604612495, 1.9868050130208332, -0.7898629067503764 ),
	( 0.53511402585389056, 2.1358153889973956, -4.8930672158986953e-16 ),
	( 0.49438089604612495, 1.9868050130208332, 0.78986290675037762 ),
	( 0.75676551277863902, 1.7384543863932291, 1.0810935896837703 ),
	( 0.40955854424093635, 1.7384543863932291, 1.4125168458460717 ),
	( -4.9367036037182201e-17, 1.7384543863932291, 1.528897216725402 ),
	( -0.40955854424093641, 1.7384543863932291, 1.4125168458460711 ),
	( -0.75676551277863935, 1.7384543863932291, 1.0810935896837703 ),
	( -0.49438089604612506, 1.9868050130208332, 0.7898629067503774 ),
	( -0.53511402585389056, 2.1358153889973956, -1.5597665146909395e-16 ),
	( -0.49438089604612495, 1.9868050130208332, -0.78986290675037796 ),
	( -0.7567655127786389, 1.7384543863932291, -1.0810935896837701 ),
	( -0.40955854424093618, 1.7384543863932291, -1.4125168458460722 ),
	( 1.8385983483863323e-16, 1.7384543863932291, -1.5288972167254016 ),
	( 0.40955854424093679, 1.7384543863932291, -1.4125168458460717 ),
	( 0.75676551277863935, 1.7384543863932291, -1.0810935896837699 ),
	( 0.49438089604612495, 1.9868050130208332, -0.7898629067503764 ),
	( 0.53511402585389056, 2.1358153889973956, -4.8930672158986953e-16 ),
	( 0.49438089604612495, 1.9868050130208332, 0.78986290675037762 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.move(0,0,0, relative=True )
    cmds.scale(radius,radius,radius, relative=True )
    if flip == True: cmds.rotate(0,90,0)
    if axis == '+X': cmds.rotate(0,0,-90)
    if axis == '-X': cmds.rotate(0,0,90)
    if axis == '+Y': cmds.rotate(0,0,0)
    if axis == '-Y': cmds.rotate(0,0,180)
    if axis == '+Z': cmds.rotate(90,0,0)
    if axis == '-Z': cmds.rotate(-90,0,0)
    cmds.move(pos[0],pos[1],pos[2], relative=True )
     
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl



#-------------------------------------------------------------------------
# CAAR Elbow Control
#
# - Elbow control used by CAAR for pole-vector controls for elbows, knees, etc.

def caar_ElbowCtrl (nodeName='Elbow_Ctrl',pos=(0,0,0),radius=1,doT=False,axis='+Y',flip=False):
    
    # - record state of symmetry setting, then turn off symmetry to avoid messing up the control shape when changing position of cvs
    sym = cmds.symmetricModelling(query=True, symmetry=True); print( 'sym =', sym )
    cmds.symmetricModelling(symmetry=0)
    
    den_Ctrl = cmds.createNode( 'transform', name=nodeName )
    den_LockAttr(False,True,True,False)
    tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[
	( 0, 1, 0 ),
	( 0.5, 0, 0 ),
	( -0.5, 0, 0 ),
	( 0, 1, 0 ),
    ] )
    
    den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
    cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
    cmds.delete(tmp)
    
    den_Shape1 = cmds.listRelatives( den_Ctrl, children=True, shapes=True, fullPath=True )
    cmds.select(den_Shape1[0]+'.cv[*]', replace=True )
    cmds.move(0,0,0, relative=True )
    cmds.scale(radius,radius,radius, relative=True )
    if flip == True: cmds.rotate(0,90,0)
    if axis == '+X': cmds.rotate(0,0,-90)
    if axis == '-X': cmds.rotate(0,0,90)
    if axis == '+Y': cmds.rotate(0,0,0)
    if axis == '-Y': cmds.rotate(0,0,180)
    if axis == '+Z': cmds.rotate(90,0,0)
    if axis == '-Z': cmds.rotate(-90,0,0)
    cmds.move(pos[0],pos[1],pos[2], relative=True )
     
    if doT:
        tmp = cmds.curve( name=nodeName+'_crap', degree=1, p=[(0,0,0),(pos[0],pos[1],pos[2])])
        den_ShapeNodes = cmds.listRelatives( tmp, children=True, shapes=True, fullPath=True )
        cmds.parent(den_ShapeNodes, den_Ctrl, shape=True, relative=True )
        cmds.delete(tmp)
    
    # - restore the recorded state of symmetry setting
    cmds.symmetricModelling(symmetry=sym)
    
    cmds.select(den_Ctrl, replace=True )
    return den_Ctrl








#-------------------------------------------------------------------------
# - splits a string up into sections at the specified character and returns the section specified by num
# --- OBSELETE

def den_SplitAt(nodeName, splitChar, num):
    words = nodeName.split(splitChar)
    return splitChar.join(words[:num]), splitChar.join(words[num:])



#-------------------------------------------------------------------------
# - custom joint command to make a joint leaving selected optional - maybe obselete

def den_makeJoint( nodeName='Joint_Jx', pos=(0,0,0), radius=2.0, leaveSelected=False ):
    #print( name )
    foo = cmds.joint( name=nodeName, position=pos, radius=radius )
    if leaveSelected==False:
        cmds.select( clear=True )
    return foo


#-------------------------------------------------------------------------
# - custom joint command to make a locator with extra options not available in cmds.spaceLocator

def den_makeLoc ( nodeName='Locator_Loc', pos=(0,0,0), rot=(0,0,0), radius=1 ):
    foo = cmds.spaceLocator (n=nodeName)
    foo = cmds.ls( uuid=True, selection=True )
    foo = cmds.ls( foo, long=True )
    cmds.xform (foo, t=pos, ro=rot)
    cmds.setAttr( foo[0]+'|'+foo[0]+'Shape.localScaleX', radius )
    cmds.setAttr( foo[0]+'|'+foo[0]+'Shape.localScaleY', radius )
    cmds.setAttr( foo[0]+'|'+foo[0]+'Shape.localScaleZ', radius )
    return foo


#-------------------------------------------------------------------------
# - custom group command to make a locator with extra options not available in cmds.group

def den_makeGrp ( nodeName='Group_Grp', pos=(0,0,0) ):
    cmds.select( clear=True )
    foo = cmds.group(empty=True, name=nodeName )
    #print( foo )
    foo = cmds.ls( foo, long=True )[0]
    #print( foo )
    cmds.xform( foo, t=pos )
    #print( 'grrr', foo )
    return foo



#-------------------------------------------------------------------------
# - adds a joint with a _Jnt siffix below listed _Jx joints - currently obselete

def den_makeBindJoints(JxJnts=[],radius=2.5):
    for JxJnt in JxJnts:
        JxJntName = cmds.ls( JxJnt )[0]
        JxJntRotOrd = cmds.getAttr( JxJntName+'.rotateOrder' )
        JxJntRadius = cmds.getAttr( JxJntName+'.radius' )
        #print JxJntName, JxJntRotOrd
        JxJntNameRoot = den_SplitAt(JxJntName,'_Jx',1)[0]
        JxJntParent = cmds.listRelatives( JxJnt, parent=True )
        
        cmds.select( clear=True )
        Bind = cmds.joint( n=JxJntNameRoot+'_Jnt', radius=JxJntRadius*1.1 )
        Bind = cmds.parent( Bind, JxJnt, relative=True )[0]

        cmds.select( Bind )
        den_ColorObject(20)





#-------------------------------------------------------------------------
# - connects proxy/sushi geo with _Mesh suffix to corresponging joint with _Jnt suffix

def den_connectProxyGeo(Jnts=[]):
    
    for Jnt in Jnts:
        JntName = cmds.ls( Jnt )[0]
        JntNameRoot = den_SplitAt(JntName,'_Jnt',1)[0]
        proxyMeshName = JntNameRoot+'_Mesh'
        #JntName = JxJntNameRoot+'_Jx'
        if cmds.objExists (proxyMeshName):
            #print( proxyMeshName,'exists' )
            proxyMesh = cmds.ls( proxyMeshName, long=True )[0]
            cmds.parentConstraint( Jnt, proxyMesh, mo=True )
            cmds.scaleConstraint( Jnt, proxyMesh, mo=True )
        else:
            print( 'WARNING:', proxyMeshName,'does NOT EXIST' )
            proxyMesh = None
        #print( JxJntNameRoot, proxyMeshName, proxyMesh )



#-------------------------------------------------------------------------
# - connects box model geo with _Box suffix to corresponging joint with _Jnt suffix

def den_connectBoxGeo(Jnts=[]):
    
    for Jnt in Jnts:
        JntName = cmds.ls( Jnt )[0]
        JntNameRoot = den_SplitAt(JntName,'_Jnt',1)[0]
        boxMeshName = JntNameRoot+'_Box'
        #JntName = JxJntNameRoot+'_Jx'
        if cmds.objExists (boxMeshName):
            #print( boxMeshName,'exists' )
            boxMesh = cmds.ls( boxMeshName, long=True )[0]
            cmds.parentConstraint( Jnt, boxMesh, mo=True )
            cmds.scaleConstraint( Jnt, boxMesh, mo=True )
        else:
            print( 'WARNING:', boxMeshName,'does NOT EXIST' )
            boxMesh = None
        #print( JxJntNameRoot, boxMeshName, boxMesh )



def den_bindProxyGeo(JxJnts=[]):
    print( 'ERROR - den_bindProxyGeo command is no longer supported' )
    print( 'info - use den_tempBindProxyGeo command instead' )
    print( 'info - den_tempBindProxyGeo command needs list of _Jnt not _Jx' )
    '''
    for JxJnt in JxJnts:
        JxJntName = cmds.ls( JxJnt )[0]
        print( 'JxJntName', JxJntName )
        JxJntNameRoot = den_SplitAt(JxJntName,'_Jx',1)[0]
        proxyMeshName = JxJntNameRoot+'_Mesh'
        JxJntName = JxJntNameRoot+'_Jnt'
        if cmds.objExists (proxyMeshName):
            #print( proxyMeshName,'exists' )
            proxyMesh = cmds.ls( proxyMeshName, long=True )[0]
            print( 'proxyMesh', proxyMesh )
            #cmds.parentConstraint( JxJnt, proxyMesh, mo=True )
            skinClust = cmds.skinCluster( proxyMesh, JxJnts, tsb=True, name=JxJntNameRoot+'_skinCluster' )[0]
            cmds.skinPercent( skinClust, proxyMesh, transformValue=(JxJnt,1.0) )
            #skinClustHist = cmds.listHistory( skinClust, pdo=True )
            #skinTweak = cmds.ls( skinClustHist, type='tweak' )
            #skinTweak = cmds.rename( skinTweak, JxJntNameRoot+'_tweak' )
        else:
            print( 'WARNING:', proxyMeshName, 'does NOT EXIST' )
            proxyMesh = None
        #print( JxJntNameRoot, proxyMeshName, proxyMesh )
    '''




#-------------------------------------------------------------------------
# - temporarily binds each proxy/sushi geo with _Mesh suffix to corresponging joint with _Jnt suffix
# - this results in temporary double-transforms on the proxy/sushi that can be ignored

def den_tempBindProxyGeo(Jnts=[]):
    
    for Jnt in Jnts:
        JntName = cmds.ls( Jnt )[0]
        print( 'JntName', JntName )
        JntNameRoot = den_SplitAt(JntName,'_Jnt',1)[0]
        proxyMeshName = JntNameRoot+'_Mesh'
        #JntName = JntNameRoot+'_Jnt'
        if cmds.objExists (proxyMeshName):
            #print( proxyMeshName,'exists' )
            proxyMesh = cmds.ls( proxyMeshName, long=True )[0]
            print( 'proxyMesh', proxyMesh )
            skinClust = cmds.skinCluster( proxyMesh, Jnts, tsb=True, name=JntNameRoot+'_skinCluster' )[0]
            cmds.skinPercent( skinClust, proxyMesh, transformValue=(Jnt,1.0) )
        else:
            print( 'WARNING:', proxyMeshName, 'does NOT EXIST' )
            proxyMesh = None
        #print( JntNameRoot, proxyMeshName, proxyMesh )




def den_ParentMultiCon():
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- find the last selected node, which will be our Ctrl object
      
    den_CtrlNode = cmds.ls( long=True, selection=True, tail=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the long name of the node again, as the for loop seems to mess with this somehow and it messes up the 'if' comparison  
        den_node = cmds.ls(den_node, long=True)
        
        #----- if the node is not the last-selected Ctrl object then duplicat and reparent shape nodes, otherwise do other stuff
        if (den_node != den_CtrlNode):
            cmds.parentConstraint( den_CtrlNode, den_node, mo=True )
        else:
            print( ' --- ',den_CtrlNode, 'now controls the others' )
    return True



def den_PrintTranslateCmd():
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the short name of the node 
        den_node = cmds.ls(den_node, long=False)
        den_nodeName = den_node[0]
        Trn = cmds.xform( den_node, q=True, r=True, t=True )
        #print( "cmds.setAttr( '"+den_nodeName+".t', "+str(Trn[0])+", "+str(Trn[1])+", "+str(Trn[2])+" )" )
        print( "cmds.xform( '"+den_nodeName+"', t=( "+str(Trn[0])+", "+str(Trn[1])+", "+str(Trn[2])+" ) )" )
        
    return True



def den_PrintRotateCmd():
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the short name of the node 
        den_node = cmds.ls(den_node, long=False)
        den_nodeName = den_node[0]
        Rot = cmds.xform( den_node, q=True, r=True, ro=True )
        #print Rot
        #print( "cmds.setAttr( '"+den_nodeName+".r', "+str(Rot[0])+", "+str(Rot[1])+", "+str(Rot[2])+" )" )
        print( "cmds.xform( '"+den_nodeName+"', ro=( "+str(Rot[0])+", "+str(Rot[1])+", "+str(Rot[2])+" ) )" )
        
    return True



def den_PrintScaleCmd():
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the short name of the node 
        den_node = cmds.ls(den_node, long=False)
        den_nodeName = den_node[0]
        Scl = cmds.xform( den_node, q=True, r=True, s=True )
        #print Rot
        #print( "cmds.setAttr( '"+den_nodeName+".r', "+str(Rot[0])+", "+str(Rot[1])+", "+str(Rot[2])+" )" )
        print( "cmds.xform( '"+den_nodeName+"', s=( "+str(Scl[0])+", "+str(Scl[1])+", "+str(Scl[2])+" ) )" )
        
    return True



def den_PrintLocalTransformCmd():
    
    #----- make a list of all selected nodes
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    #----- loop through all selected objects
    for den_node in den_SelectedNodes:
        #----- get the short name of the node 
        den_node = cmds.ls(den_node, long=False)
        den_nodeName = den_node[0]
        #print( den_nodeName )
        Trn = cmds.xform( den_node, q=True, r=True, t=True )
        Rot = cmds.xform( den_node, q=True, r=True, ro=True )
        Scl = cmds.xform( den_node, q=True, r=True, s=True )
        # - build the python command and print it out
        print( "cmds.xform( '"+den_nodeName+"', t=( "+str(Trn[0])+", "+str(Trn[1])+", "+str(Trn[2])+" ), ro=( "+str(Rot[0])+", "+str(Rot[1])+", "+str(Rot[2])+" ), s=( "+str(Scl[0])+", "+str(Scl[1])+", "+str(Scl[2])+" ) )" )
        
    return True

#den_PrintLocalTransformCmd()



def den_PrintConCmd():
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the short name of the node 
        den_node = cmds.ls(den_node, long=False)
        den_nodeName = den_node[0]
        if den_nodeName[0] == 'L':
            attrs = [ '.L_JawHinge_RestW0', '.L_JawHinge_AnimW1', '.L_JawHinge_UpFloatW2', '.L_JawHinge_DnFloatW3' ]
        else:
            attrs = [ '.R_JawHinge_RestW0', '.R_JawHinge_AnimW1', '.R_JawHinge_UpFloatW2', '.R_JawHinge_DnFloatW3' ]
        for attr in attrs:
            Rot = cmds.xform( den_node, ws=True, q=True, ro=True )
            Val = cmds.getAttr( den_node[0]+attr )
            #print Val
            print( "cmds.setAttr( '"+den_nodeName+attr+"', "+str(Val)+" )" )
        
    return True


def den_PrintCVposCmd():
    selObjs = cmds.ls( sl=True )
    #print( selObjs )
    for obj in selObjs:
        print( obj )
        curveCVs = cmds.ls(obj+'.cv[*]', fl=True)
        for i, cv in enumerate(curveCVs):
            pos = cmds.pointPosition( cv )
            print( '    ( '+str(pos[0])+','+str(pos[1])+','+str(pos[2])+' ),' )



def den_PythonPathAppend(newPath='N:/M/Projects_DC_Systems/RigTools_DEN/maya/scripts/global'):
    doCmd = 1
    #projString = newPath
    #print projString
    for pythonPath in sys.path:
        if pythonPath == newPath:
            print( 'FYI --',pythonPath,'already exists -- SKIPPING' )
            doCmd = 0
    if doCmd:
        print( 'adding',newPath,'to the python path' )
        sys.path.append(newPath)



def den_DiagPause( seconds=1.0 ):
    print( '=========== pausing for ', seconds, ' seconds' )
    cmds.refresh( f=True ) # diagnostic refresh
    time.sleep(seconds) # diagnostic pause


def den_AddSpaceOUTs(Jnts=[]):
    OUTs = []
    for Jnt in Jnts:
        JntName = cmds.ls( Jnt )[0]
        #JntNameRoot = den_SplitAt(JntName,'_',1)[0]
        #OutName = JntNameRoot+'_SpaceOUT'
        if '_Jnt' in JntName:
            OutName = JntName.replace('_Jnt','Space_OUT')
        elif '_Jx' in JntName:
            OutName = JntName.replace('_Jx','Space_OUT')
        elif '_Ctrl' in JntName:
            OutName = JntName.replace('_Ctrl','Space_OUT')
        else:
            JntName = JntName+'Space_OUT'
        print( OutName )
        
        if cmds.objExists(OutName):
            print( 'WARNING - ', OutName, 'exists already, not making another one' )
            OUTs += [OutName]
        else:
            OUT = cmds.group(empty=True, name=OutName )
            OUT = cmds.parent( OUT, Jnt )
            OUTs += OUT

    return OUTs


def den_AddSuffix(suffix='_Mesh'):
    
    #----- make a list of all selected nodes
      
    den_SelectedNodes = cmds.ls( long=True, selection=True )
    
    
    #----- loop through all selected objects
      
    for den_node in den_SelectedNodes:
        
        #----- get the short name of the node 
        den_node = cmds.ls(den_node, long=False)
        den_nodeName = den_node[0]
        Rot = cmds.rename( den_node, den_nodeName+suffix )
        #print Rot
        
    return True


def den_GeoBbox():
    objs = cmds.ls(type="mesh")
    bb = cmds.exactWorldBoundingBox(objs)
    size = bb[4]
    sizeX = bb[3]
    sizeY = bb[4]
    sizeZ = bb[5]
    
    return sizeX, sizeY, sizeZ





'''
# I got this from the internet, but it does not seem to work.  I suspect a maya bug in 2023
def createWrap(*args,**kwargs):
    
    influence=args[0]
    surface = args[1]
    
    shapes = cmds.listRelatives(influence,shapes=True)
    influenceShape = shapes[0]

    shapes = cmds.listRelatives(surface,shapes=True)
    surfaceShape = shapes[0]

    #create wrap deformer
    weightThreshold = kwargs.get('weightThreshold',0.0)
    maxDistance = kwargs.get('maxDistance',1.0)
    exclusiveBind = kwargs.get('exclusiveBind',False)
    autoWeightThreshold = kwargs.get('autoWeightThreshold',True)
    falloffMode = kwargs.get('falloffMode',0)

    wrapData = cmds.deformer(surface, type='wrap')
    wrapNode = wrapData[0]

    cmds.setAttr(wrapNode+'.weightThreshold',weightThreshold)
    cmds.setAttr(wrapNode+'.maxDistance',maxDistance)
    cmds.setAttr(wrapNode+'.exclusiveBind',exclusiveBind)
    cmds.setAttr(wrapNode+'.autoWeightThreshold',autoWeightThreshold)
    cmds.setAttr(wrapNode+'.falloffMode',falloffMode)

    cmds.connectAttr(surface+'.worldMatrix[0]',wrapNode+'.geomMatrix')
    
    #add influence
    duplicateData = cmds.duplicate(influence,name=influence+'Base')
    base = duplicateData[0]
    shapes = cmds.listRelatives(base,shapes=True)
    baseShape = shapes[0]
    cmds.hide(base)
    
    #create dropoff attr if it doesn't exist
    if not cmds.attributeQuery('dropoff',n=influence,exists=True):
        cmds.addAttr( influence, sn='dr', ln='dropoff', dv=4.0, min=0.0, max=20.0  )
        cmds.setAttr( influence+'.dr', k=True )
    
    #if type mesh
    if cmds.nodeType(influenceShape) == 'mesh':
        #create smoothness attr if it doesn't exist
        if not cmds.attributeQuery('smoothness',n=influence,exists=True):
            cmds.addAttr( influence, sn='smt', ln='smoothness', dv=0.0, min=0.0  )
            cmds.setAttr( influence+'.smt', k=True )

        #create the inflType attr if it doesn't exist
        if not cmds.attributeQuery('inflType',n=influence,exists=True):
            cmds.addAttr( influence, at='short', sn='ift', ln='inflType', dv=2, min=1, max=2  )

        cmds.connectAttr(influenceShape+'.worldMesh',wrapNode+'.driverPoints[0]')
        cmds.connectAttr(baseShape+'.worldMesh',wrapNode+'.basePoints[0]')
        cmds.connectAttr(influence+'.inflType',wrapNode+'.inflType[0]')
        cmds.connectAttr(influence+'.smoothness',wrapNode+'.smoothness[0]')

    #if type nurbsCurve or nurbsSurface
    if cmds.nodeType(influenceShape) == 'nurbsCurve' or cmds.nodeType(influenceShape) == 'nurbsSurface':
        #create the wrapSamples attr if it doesn't exist
        if not cmds.attributeQuery('wrapSamples',n=influence,exists=True):
            cmds.addAttr( influence, at='short', sn='wsm', ln='wrapSamples', dv=10, min=1  )
            cmds.setAttr( influence+'.wsm', k=True )

        cmds.connectAttr(influenceShape+'.ws',wrapNode+'.driverPoints[0]')
        cmds.connectAttr(baseShape+'.ws',wrapNode+'.basePoints[0]')
        cmds.connectAttr(influence+'.wsm',wrapNode+'.nurbsSamples[0]')

    cmds.connectAttr(influence+'.dropoff',wrapNode+'.dropoff[0]')
    # I want to return a pyNode object for the wrap deformer.
    # I do not see the reason to rewrite the code here into pymel.
    # return wrapNode
    return pm.nt.Wrap(wrapNode)
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# - this tool was created by Ramy Sobhy Saad Zaky (DC student) in Jan.2023
# - he is awesome!
def RZA_MatrixPC( driver='', driven='', scaleConstraint=True, maintainOffeset=True ):

    #maintainOffeset = True
    #scaleConstraint = True
    if driver == '' or driven == '':
        obj = cmds.ls( selection=True, fl=True )
        driver = obj[0]
        driven = obj[1]
    print(driver, driven)
    
    multMatrix1 = cmds.shadingNode( 'multMatrix', asUtility=True )
    decomposeMatrix1 = cmds.shadingNode( 'decomposeMatrix', asUtility=True )
    
    if scaleConstraint:
        cmds.connectAttr( decomposeMatrix1+'.outputScale', driven+'.scale' )
        cmds.refresh( f=True ) # diagnostic refresh
        time.sleep(0.01) # diagnostic pause
    
    if maintainOffeset:
        cmds.delete(decomposeMatrix1)
        cmds.connectAttr( driver+'.worldMatrix[0]', multMatrix1+'.matrixIn[0]' )
        cmds.connectAttr( multMatrix1+'.matrixSum', driven+'.offsetParentMatrix' )
        cmds.refresh( f=True ) # diagnostic refresh
        time.sleep(0.01) # diagnostic pause

    else:
        cmds.connectAttr( driver+'.worldMatrix[0]', multMatrix1+'.matrixIn[0]' )
        cmds.connectAttr( multMatrix1+'.matrixSum', decomposeMatrix1+'.inputMatrix' )
        cmds.connectAttr( decomposeMatrix1+'.outputTranslate', driven+'.translate' )
        cmds.connectAttr( decomposeMatrix1+'.outputRotate', driven+'.rotate' )
        cmds.refresh( f=True ) # diagnostic refresh
        time.sleep(0.01) # diagnostic pause
        #cmds.connectAttr( selection2+'.parentInverseMatrix[0]', multMatrix1+'.matrixIn[1]' )



#__________________________________________________________________________________________
# Move Transforms To Matrices
def Ra_MoveTransformsToMatrix(objs=[]):
    
    if not objs:
        objs=cmds.ls(selection=True, flatten=True)
    if isinstance(objs, str): objs= [objs]
    matrices=[]
    for i in objs:
        Matrix= cmds.getAttr(i+'.dagLocalMatrix')
        matrices+=Matrix          
        cmds.setAttr( i + '.offsetParentMatrix', Matrix, type='matrix' )
        cmds.setAttr( i+'.translate', 0,0,0 )
        cmds.setAttr( i+'.rotate', 0,0,0 )
        cmds.setAttr( i+'.scale', 1,1,1 )
        if cmds.nodeType(i) == 'joint':
            cmds.setAttr(i + '.jointOrientX', 0)
            cmds.setAttr(i + '.jointOrientY', 0)
            cmds.setAttr(i + '.jointOrientZ', 0) 
    return matrices


#__________________________________________________________________________________________
# Make offset group
def Ra_MakeOffsetGrp( objs=[], name='Offset' ):
    '''
    objs= []
    name= ''
    '''
    
    nulls=[]
    if not objs: objs = cmds.ls(selection=True, flatten=True)
    if isinstance(objs, str): objs= [objs]; print(objs)
    
    for obj in objs:
        # Get the transformation values of the children
        objParent= cmds.listRelatives( obj, parent=True, fullPath=True)
        objM= cmds.xform( obj, q=True, ws= True, matrix=True ); print(objM)
        if objParent: objParentM= cmds.xform( objParent, q=True, ws= True, matrix=True )        
        Ra_MoveTransformsToMatrix( objs= obj )
        cmds.setAttr( obj+'.offsetParentMatrix', type= 'matrix', *[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])
        # Create a null
        null = cmds.group( empty=True, name= obj+'Offset' if not name else name )
        # Set the transformation values of the null to match the child
        cmds.xform( null, ws= True, matrix= objM, relative= True )
        obj= cmds.parent( obj, null, relative=True )[0]
        if objParent: null= cmds.parent( null, objParent )[0]
        nulls+=[null]
    
    print(nulls)
    cmds.select(nulls)
    return nulls


#__________________________________________________________________________________________
# matrix parent constraint

def Ra_ParentConst_v01( objs= [], mo= True, name= ''):   
    '''
    objs= []
    mo= False
    name= ''
    '''
    
    if not objs: objs = cmds.ls( selection=True, flatten=True )
    if len(objs) < 2:
        print('ERROR: Select at least one driver and a driven.')
        exit()
    
    drivers= objs[:-1]
    driven= [objs[-1]]
    if isinstance(drivers, str): drivers= [drivers]
    if isinstance(driven, str): driven= [driven]
    print(drivers)
    print(driven)
    
    parentConst= Ra_MakeOffsetGrp( driven, name= driven[0]+'_parentConst' if not name else name )
    drivenParentM= cmds.createNode('parentMatrix', n= driven[0]+'_ParentM')
    
    for i in range(len(drivers)):
        driverMultM= cmds.shadingNode( 'multMatrix', asUtility=True, n= drivers[i]+'_MultM' )
        cmds.connectAttr( drivers[i]+'.worldMatrix[0]', driverMultM+'.matrixIn[0]')
        cmds.connectAttr( parentConst[0]+'.worldInverseMatrix[0]', driverMultM+'.matrixIn[1]')
        cmds.connectAttr( driverMultM+'.matrixSum', drivenParentM+'.target['+str(i)+'].targetMatrix' )
        if mo:
            mult= cmds.shadingNode( 'multMatrix', asUtility=True )
            cmds.connectAttr( parentConst[0]+'.worldMatrix[0]', mult+'.matrixIn[0]')
            cmds.connectAttr( drivers[i]+'.worldInverseMatrix[0]', mult+'.matrixIn[1]')
            offsetM= cmds.getAttr( mult+'.matrixSum')
            cmds.setAttr( drivenParentM+'.target['+str(i)+'].offsetMatrix', offsetM, type='matrix' )
            cmds.delete( mult )
    
    cmds.connectAttr( drivenParentM+'.outputMatrix', driven[0]+'.offsetParentMatrix', force=True)
    cmds.select( [] )
    return parentConst[0]
    
#Ra_ParentConst_v01( objs= [], mo= True, name= '')

#__________________________________________________________________________________________
# matrix parent constraint
def Ra_ParentConst_v02( objs= [], mo= True, tW= 1, roW= 1, sW= 1, name= ''):
    '''
    objs= []
    mo= True
    tW= 1
    roW= 1
    sW= 1
    name= ''
    '''
    if not objs: objs = cmds.ls( selection=True, flatten=True )
    if len(objs) < 2:
        print('ERROR: Select at least one driver and a driven.')
        exit()
    
    drivers= objs[:-1]
    driven= [objs[-1]]
    if isinstance(drivers, str): drivers= [drivers]
    if isinstance(driven, str): driven= [driven]
    print(drivers)
    print(driven)
    
    parentConst= Ra_MakeOffsetGrp( driven, name= driven[0]+'_parentConst' if not name else name )
    drivenParentM= cmds.createNode('parentMatrix', n= driven[0]+'_ParentM')
    
    cmds.addAttr( parentConst[0], ln= 'Const_W', nn='_________', at='enum', en= 'ConstWeights' )
    cmds.setAttr( parentConst[0]+'.Const_W', lock=True, keyable=False, channelBox=True )

    for i in range(len(drivers)):
        cmds.addAttr( parentConst[0], ln= drivers[i]+'_W', dv= 1, min= 0.0, max= 1.0 )
        cmds.setAttr( parentConst[0]+'.'+drivers[i]+'_W', lock=False, keyable=True )
        driverMultM= cmds.shadingNode( 'multMatrix', asUtility=True, n= drivers[i]+'_MultM' )
        cmds.connectAttr( drivers[i]+'.worldMatrix[0]', driverMultM+'.matrixIn[0]')
        cmds.connectAttr( parentConst[0]+'.worldInverseMatrix[0]', driverMultM+'.matrixIn[1]')
        cmds.connectAttr( driverMultM+'.matrixSum', drivenParentM+'.target['+str(i)+'].targetMatrix' )
        cmds.connectAttr( parentConst[0]+'.'+drivers[i]+'_W', drivenParentM+'.target['+str(i)+'].weight' )
        if mo:
            mult= cmds.shadingNode( 'multMatrix', asUtility=True )
            cmds.connectAttr( parentConst[0]+'.worldMatrix[0]', mult+'.matrixIn[0]')
            cmds.connectAttr( drivers[i]+'.worldInverseMatrix[0]', mult+'.matrixIn[1]')
            offsetM= cmds.getAttr( mult+'.matrixSum')
            cmds.setAttr( drivenParentM+'.target['+str(i)+'].offsetMatrix', offsetM, type='matrix' )
            cmds.delete( mult )
    
    cmds.connectAttr( drivenParentM+'.outputMatrix', driven[0]+'.offsetParentMatrix', force=True)
    cmds.select( [] )
    return parentConst[0]
    
#Ra_ParentConst_v02( objs= [], mo= True, tW= 1, roW= 1, sW= 1, name= '')

#__________________________________________________________________________________________
# matrix parent constraint
def Ra_ParentConst_v03( objs= [], mo= True, tW= 1, roW= 1, sW= 1, name= ''):
    '''
    objs= []
    mo= True
    tW= 1
    roW= 1
    sW= 1
    name= ''
    '''
    if not objs: objs = cmds.ls( selection=True, flatten=True )
    if len(objs) < 2:
        print('ERROR: Select at least one driver and a driven.')
        exit()
    
    drivers= objs[:-1]
    driven= [objs[-1]]
    if isinstance(drivers, str): drivers= [drivers]
    if isinstance(driven, str): driven= [driven]
    print(drivers)
    print(driven)
    
    parentConst= Ra_MakeOffsetGrp( driven, name= driven[0]+'_parentConst' if not name else name )
    drivenParentM= cmds.createNode('parentMatrix', n= driven[0]+'_ParentM')
    drivenBlendM= cmds.createNode('blendMatrix', n= driven[0]+'_BlendM')
    cmds.connectAttr( drivenParentM+'.outputMatrix', drivenBlendM+'.target[0].targetMatrix')
    
    cmds.addAttr( parentConst[0], ln= 'Const_W', nn='_________', at='enum', en= 'ConstWeights' )
    cmds.setAttr( parentConst[0]+'.Const_W', lock=True, keyable=False, channelBox=True )
    cmds.addAttr( parentConst[0], ln= 'TranslateW', dv= tW, min= 0.0, max= 1.0 )
    cmds.setAttr( parentConst[0]+'.TranslateW', lock=False, keyable=True )
    cmds.addAttr( parentConst[0], ln= 'RotateW', dv= roW, min= 0.0, max= 1.0 )
    cmds.setAttr( parentConst[0]+'.RotateW', lock=False, keyable=True )
    cmds.addAttr( parentConst[0], ln= 'ScaleW', dv= sW, min= 0.0, max= 1.0 )
    cmds.setAttr( parentConst[0]+'.ScaleW', lock=False, keyable=True )
    
    cmds.connectAttr( parentConst[0]+'.TranslateW', drivenBlendM+'.target[0].translateWeight')
    cmds.connectAttr( parentConst[0]+'.RotateW', drivenBlendM+'.target[0].rotateWeight')
    cmds.connectAttr( parentConst[0]+'.ScaleW', drivenBlendM+'.target[0].scaleWeight')
    
    for i in range(len(drivers)):
        cmds.addAttr( parentConst[0], ln= drivers[i]+'_W', dv= 1, min= 0.0, max= 1.0 )
        cmds.setAttr( parentConst[0]+'.'+drivers[i]+'_W', lock=False, keyable=True )
        driverMultM= cmds.shadingNode( 'multMatrix', asUtility=True, n= drivers[i]+'_MultM' )
        cmds.connectAttr( drivers[i]+'.worldMatrix[0]', driverMultM+'.matrixIn[0]')
        cmds.connectAttr( parentConst[0]+'.worldInverseMatrix[0]', driverMultM+'.matrixIn[1]')
        cmds.connectAttr( driverMultM+'.matrixSum', drivenParentM+'.target['+str(i)+'].targetMatrix' )
        cmds.connectAttr( parentConst[0]+'.'+drivers[i]+'_W', drivenParentM+'.target['+str(i)+'].weight' )
        if mo:
            mult= cmds.shadingNode( 'multMatrix', asUtility=True )
            cmds.connectAttr( parentConst[0]+'.worldMatrix[0]', mult+'.matrixIn[0]')
            cmds.connectAttr( drivers[i]+'.worldInverseMatrix[0]', mult+'.matrixIn[1]')
            offsetM= cmds.getAttr( mult+'.matrixSum')
            cmds.setAttr( drivenParentM+'.target['+str(i)+'].offsetMatrix', offsetM, type='matrix' )
            cmds.delete( mult )
    
    cmds.connectAttr( drivenBlendM+'.outputMatrix', driven[0]+'.offsetParentMatrix', force=True)
    cmds.select( [] )
    return parentConst[0]
    
#Ra_ParentConst_v03( objs= [], mo= True, tW= 1, roW= 1, sW= 1, name= '')


#__________________________________________________________________________________________
# Parent constraint UI
def Ra_ParentConstUI():
    def Ra_ParentConst(*args):
        Ra_ParentConst_v03(
        objs=[],
        mo= cmds.checkBox( 'moField', query=True, value=True ),
        tW= cmds.floatField( 'tWField', query=True, value=True ),
        roW= cmds.floatField( 'roWField', query=True, value=True ),
        sW= cmds.floatField( 'sWField', query=True, value=True ))
        
    def tWSliderV(value):
        cmds.floatSlider( 'tWSlider', edit=True, value=value )
    def tWFieldV(value):
        cmds.floatField( 'tWField', edit=True, value=value )
    
    def roWSliderV(value):
        cmds.floatSlider( 'roWSlider', edit=True, value=value )
    def roWFieldV(value):
        cmds.floatField( 'roWField', edit=True, value=value )
        
    def sWSliderV(value):
        cmds.floatSlider( 'sWSlider', edit=True, value=value )
    def sWFieldV(value):
        cmds.floatField( 'sWField', edit=True, value=value )
        
    # Create a window
    if cmds.window( 'ParentConst', exists=True ):
        cmds.deleteUI( 'ParentConst', window=True )
    cmds.window( 'ParentConst', title='Parent Constraint Options', sizeable=True)
    
    cmds.columnLayout( adjustableColumn=True, margins=6 )
    
    cmds.text( label='   Constraint weights', backgroundColor=(.4, .4, .4), align='left', h=20)
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(90, 70, 70), columnAttach=[(1, 'right', 5), (2, 'left', 0), (3, 'left', 0)], h=25)
    cmds.text( label='Translate Weight:' )
    tWField = cmds.floatField('tWField', min=0, max=1, value=1, changeCommand= tWSliderV, w=70 )
    cmds.floatSlider('tWSlider', min=0, max=1, value=1, dragCommand= tWFieldV, w=200 )
    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(90, 70, 70), columnAttach=[(1, 'right', 5), (2, 'left', 0), (3, 'left', 0)], h=25)
    cmds.text( label='Rotate Weight:' )
    roWField = cmds.floatField('roWField', min=0, max=1, value=1, changeCommand= roWSliderV, w=70 )
    cmds.floatSlider('roWSlider', min=0, max=1, value=1, dragCommand= roWFieldV, w=200 )
    cmds.setParent('..')
    
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(90, 70, 70), columnAttach=[(1, 'right', 5), (2, 'left', 0), (3, 'left', 0)], h=25)
    cmds.text( label='Scale Weight:' )
    sWField = cmds.floatField('sWField', min=0, max=1, value=1, changeCommand= sWSliderV, w=70 )
    cmds.floatSlider('sWSlider', min=0, max=1, value=1, dragCommand= sWFieldV, w=200 )
    cmds.setParent('..')
    
    cmds.rowLayout( numberOfColumns=3, columnWidth3=(90, 70, 70), columnAttach=[(1, 'right', 5), (2, 'left', 0), (3, 'right', 0)], h=25)
    cmds.text( label=' Maintain offset:' )
    cmds.checkBox('moField', label='', value=True, h=15)
    cmds.setParent('..')
    
    cmds.rowLayout( numberOfColumns=2, columnWidth2=(380, 1), columnAttach=[(1, 'right', 5), (2, 'right', 0)], h=30)
    cmds.button( label='Apply', command= Ra_ParentConst, w=100)
    cmds.setParent('..')
        
    cmds.showWindow( 'ParentConst' )

#Ra_ParentConstUI()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





def den_AddSafetyCovers( rigGroup='Torso_Grp', attrs=True, lock=True ):
    #--------------------- testing variables
    #rigGroup='locator1'
    #---------------------
    if attrs:
        if cmds.attributeQuery( 'Show_Controls', node=rigGroup, exists=True ) != True:# check if attr exists already
            cmds.addAttr( rigGroup, longName='Show_Controls', attributeType='enum', enumName=' off ---: --- on' )
            cmds.setAttr ( rigGroup+'.Show_Controls', 1, lock=False, channelBox=True )
        if cmds.attributeQuery( 'Ctrl_Color', node=rigGroup, exists=True ) != True:# check if attr exists already
            cmds.addAttr( rigGroup, ln="Ctrl_Color", uac=True, at="float3" )
            cmds.addAttr( rigGroup, ln="Ctrl_ColorR", at="float", parent="Ctrl_Color")
            cmds.addAttr( rigGroup, ln="Ctrl_ColorG", at="float", parent="Ctrl_Color")
            cmds.addAttr( rigGroup, ln="Ctrl_ColorB", at="float", parent="Ctrl_Color")
            cmds.setAttr( rigGroup+'.Ctrl_Color', 1, 0, 1 )
        if cmds.attributeQuery( 'Show_Ribbons', node=rigGroup, exists=True ) != True:
            cmds.addAttr( rigGroup, longName='Show_Ribbons', attributeType='enum', enumName=' off ---: --- on' )
            cmds.setAttr ( rigGroup+'.Show_Ribbons', lock=False, channelBox=True )
        if cmds.attributeQuery( 'Show_Guts', node=rigGroup, exists=True ) != True:
            cmds.addAttr( rigGroup, longName='Show_Guts', attributeType='enum', enumName=' off ---: --- on' )
            cmds.setAttr ( rigGroup+'.Show_Guts', lock=False, channelBox=True )
        if cmds.attributeQuery( 'Bone_Draw_Style', node=rigGroup, exists=True ) != True:
            cmds.addAttr( rigGroup, longName='Bone_Draw_Style', attributeType='enum', enumName='Bone:Multi-child as Box:None' )
            cmds.setAttr ( rigGroup+'.Bone_Draw_Style', lock=False, channelBox=True )
    
    if lock:
        nodes = cmds.ls( rigGroup, dag=True )
        for node in nodes:
            
            if '_Ctrl' in node:
                if node.split('_')[-1] == 'Ctrl':
                    if cmds.connectionInfo( node+'.Ctrl_Color', isDestination=True) != True:
                        cmds.connectAttr( rigGroup+'.Ctrl_Color', node+'.Ctrl_Color' )
                    shapes = cmds.listRelatives( node, shapes=True )
                    for shape in shapes:
                        print( 'shape -', shape, 'attr has input =', cmds.connectionInfo( shape+'.visibility', isDestination=True) )
                        if cmds.connectionInfo( shape+'.visibility', isDestination=True) != True:
                            cmds.connectAttr( rigGroup+'.Show_Controls', shape+'.visibility' )
                elif node.split('_')[-1] == 'CtrlZero':
                    cmds.select( node )
                    den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
            
            elif cmds.nodeType( node ) == 'locator':
                #nodeParent = cmds.listRelatives( node, parent=True )[0]
                print( 'locator -', node, 'attr has input =', cmds.connectionInfo( node+'.visibility', isDestination=True) )
                if cmds.connectionInfo( node+'.visibility', isDestination=True) != True:
                    cmds.connectAttr( rigGroup+'.Show_Guts', node+'.visibility' )
                #cmds.select( node )
                #den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
            
            elif cmds.nodeType( node ) == 'joint':
                print( 'joint -', node, 'attr has input =', cmds.connectionInfo( node+'.drawStyle', isDestination=True) )
                if cmds.connectionInfo( node+'.drawStyle', isDestination=True) != True:
                    cmds.connectAttr( rigGroup+'.Bone_Draw_Style', node+'.drawStyle' )
                cmds.select( node )
                den_Lock(  1,1,1 , 0,0,0 , 1,1,1 , 1 )
            
            elif cmds.nodeType( node ) == 'ikHandle':
                print( 'ikHandle -', node, 'attr has input =', cmds.connectionInfo( node+'.visibility', isDestination=True) )
                joints = cmds.ikHandle( node, q=True, jl=True )# find all the joints driven by ik
                for j in joints:
                    cmds.select( j )
                    den_Lock(  1,1,1 , 0,0,0 , 1,1,1 , 1 )# make sure the rotates on ik joints are not locked, or the ik will stop working
                if cmds.connectionInfo( node+'.visibility', isDestination=True) != True:
                    cmds.connectAttr( rigGroup+'.Show_Guts', node+'.visibility' )
                cmds.select( node )
                den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
    
            elif cmds.nodeType( node ) == 'transform':
                if 'Ribbon' in node:
                    cmds.connectAttr( rigGroup+'.Show_Ribbons', node+'.visibility' )
                #print( 'transform -', node, 'attr has input =', cmds.connectionInfo( node+'.visibility', isDestination=True) )
                #if cmds.connectionInfo( node+'.visibility', isDestination=True) != True:
                #    cmds.connectAttr( rigGroup+'.Show_Guts', node+'.visibility' )
                cmds.select( node )
                den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 0 )


#den_AddSafetyCovers( rigGroup='L_Arm_Grp' )


def den_RemoveSafetyCovers( rigGroup='Torso_Grp' ):
    #--------------------- testing variables
    #rigGroup='locator1'
    #---------------------
    '''
    if attrs:
        if cmds.attributeQuery( 'Show_Controls', node=rigGroup, exists=True ) != True:# check if attr exists already
            cmds.addAttr( rigGroup, longName='Show_Controls', attributeType='enum', enumName=' off ---: --- on' )
            cmds.setAttr ( rigGroup+'.Show_Controls', 1, lock=False, channelBox=True )
        if cmds.attributeQuery( 'Ctrl_Color', node=rigGroup, exists=True ) != True:# check if attr exists already
            cmds.addAttr( rigGroup, ln="Ctrl_Color", uac=True, at="float3" )
            cmds.addAttr( rigGroup, ln="Ctrl_ColorR", at="float", parent="Ctrl_Color")
            cmds.addAttr( rigGroup, ln="Ctrl_ColorG", at="float", parent="Ctrl_Color")
            cmds.addAttr( rigGroup, ln="Ctrl_ColorB", at="float", parent="Ctrl_Color")
            cmds.setAttr( rigGroup+'.Ctrl_Color', 1, 0, 1 )
        if cmds.attributeQuery( 'Show_Ribbons', node=rigGroup, exists=True ) != True:
            cmds.addAttr( rigGroup, longName='Show_Ribbons', attributeType='enum', enumName=' off ---: --- on' )
            cmds.setAttr ( rigGroup+'.Show_Ribbons', lock=False, channelBox=True )
        if cmds.attributeQuery( 'Show_Guts', node=rigGroup, exists=True ) != True:
            cmds.addAttr( rigGroup, longName='Show_Guts', attributeType='enum', enumName=' off ---: --- on' )
            cmds.setAttr ( rigGroup+'.Show_Guts', lock=False, channelBox=True )
        if cmds.attributeQuery( 'Bone_Draw_Style', node=rigGroup, exists=True ) != True:
            cmds.addAttr( rigGroup, longName='Bone_Draw_Style', attributeType='enum', enumName='Bone:Multi-child as Box:None' )
            cmds.setAttr ( rigGroup+'.Bone_Draw_Style', lock=False, channelBox=True )
    '''
    if True:
        nodes = cmds.ls( rigGroup, dag=True )
        for node in nodes:
            
            if '_Ctrl' in node:
                if node.split('_')[-1] == 'Ctrl':
                    cmds.connectAttr( rigGroup+'.Ctrl_Color', node+'.Ctrl_Color' )
                    shapes = cmds.listRelatives( node, shapes=True )
                    for shape in shapes:
                        print( 'shape -', shape, 'attr has input =', cmds.connectionInfo( shape+'.visibility', isDestination=True) )
                        if cmds.connectionInfo( shape+'.visibility', isDestination=True) != True:
                            cmds.connectAttr( rigGroup+'.Show_Controls', shape+'.visibility' )
                elif node.split('_')[-1] == 'CtrlZero':
                    cmds.select( node )
                    den_Lock(  0,0,0 , 0,0,0 , 0,0,0 , 0 )
            
            elif cmds.nodeType( node ) == 'locator':
                #nodeParent = cmds.listRelatives( node, parent=True )[0]
                print( 'locator -', node, 'attr has input =', cmds.connectionInfo( node+'.visibility', isDestination=True) )
                if cmds.connectionInfo( node+'.visibility', isDestination=True) != True:
                    cmds.connectAttr( rigGroup+'.Show_Guts', node+'.visibility' )
                #cmds.select( node )
                #den_Lock(  1,1,1 , 1,1,1 , 1,1,1 , 1 )
            
            elif cmds.nodeType( node ) == 'joint':
                print( 'joint -', node, 'attr has input =', cmds.connectionInfo( node+'.drawStyle', isDestination=True) )
                if cmds.connectionInfo( node+'.drawStyle', isDestination=True) != True:
                    cmds.connectAttr( rigGroup+'.Bone_Draw_Style', node+'.drawStyle' )
                cmds.select( node )
                den_Lock(  0,0,0 , 0,0,0 , 0,0,0 , 0 )
            
            elif cmds.nodeType( node ) == 'ikHandle':
                print( 'ikHandle -', node, 'attr has input =', cmds.connectionInfo( node+'.visibility', isDestination=True) )
                joints = cmds.ikHandle( node, q=True, jl=True )# find all the joints driven by ik
                for j in joints:
                    cmds.select( j )
                    den_Lock(  0,0,0 , 0,0,0 , 0,0,0 , 0 )# make sure the rotates on ik joints are not locked, or the ik will stop working
                if cmds.connectionInfo( node+'.visibility', isDestination=True) != True:
                    cmds.connectAttr( rigGroup+'.Show_Guts', node+'.visibility' )
                cmds.select( node )
                den_Lock(  0,0,0 , 0,0,0 , 0,0,0 , 0 )
    
            elif cmds.nodeType( node ) == 'transform':
                if 'Ribbon' in node:
                    cmds.connectAttr( rigGroup+'.Show_Ribbons', node+'.visibility' )
                #print( 'transform -', node, 'attr has input =', cmds.connectionInfo( node+'.visibility', isDestination=True) )
                #if cmds.connectionInfo( node+'.visibility', isDestination=True) != True:
                #    cmds.connectAttr( rigGroup+'.Show_Guts', node+'.visibility' )
                cmds.select( node )
                den_Lock(  0,0,0 , 0,0,0 , 0,0,0 , 0 )


#den_AddSafetyCovers( rigGroup='L_Arm_Grp' )


