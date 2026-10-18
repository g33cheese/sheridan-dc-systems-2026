import time
import maya.cmds as cmds

def den_DiagPause( seconds=1.0 ):
    print( '=========== pausing for ', seconds, ' seconds' )
    cmds.refresh( f=True ) # diagnostic refresh
    time.sleep(seconds) # diagnostic pause

