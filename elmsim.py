#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#elmapp="tk"

import sys
try:
    from elmDevice import elmDevice
    device=elmDevice()
    device.start()
except ImportError:
    print "The module elmDevice can not be found"

#from elmsim_tk import simpleapp_tk

# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
#gui = 'tk'

try:
    if total > 1:
        print "use tk not wx"
        raise ImportError,"don't want to use wx right now"
    import wx
    #import wx1
    #import elmsim_wx
except ImportError:
    print "trying tkinter"
    try:
        import Tkinter
    except ImportError:
        print "The python-tk or the wxPython module is required to run this program."
    else:
        #gui = 'tk'
        print "running tk app"
        from elmsim_tk import simpleapp_tk
        app=simpleapp_tk(None,device)
        app.title('ELM327 Test Simulator TK')
        app.mainloop()
else:
    print "running wx app"
    #import elmsim_wx
    from elmsim_wx import simpleapp_wx
    #gui = 'wx'
    app = wx.App()
    frame = simpleapp_wx(None,-1,'ELM327 Simulator',device)
    app.MainLoop()

#app=simpleapp_tk(None,device)
#app.title('ELM327 Test Simulator TK')
#app.mainloop()
#if gui == 'wx':
    #app = wx.App()
    #frame = simpleapp_wx(None,-1,'ELM327 Simulator')
    #app.MainLoop()
#else:
    #app=simpleapp_tk(None,device)
    #app.title('ELM327 Test Simulator TK')
    #app.mainloop()
print "done"
