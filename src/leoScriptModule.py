# A module holding the script to be debugged.
import rpdb2
if rpdb2.g_debugger is not None: # don't hang if the debugger isn't running.
  rpdb2.start_embedded_debugger(pwd="",fAllowUnencrypted=True) # Hard breakpoint.
# Predefine c, g and p.
import leoGlobals as g
c = g.app.scriptDict.get("c")
p = c.currentPosition()
# Actual script starts here.
print 'hello'
