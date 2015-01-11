import wx

class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title,device,queue):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.device=device
        self.returnQueue=queue
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        self.entry = wx.TextCtrl(self,wx.TE_PROCESS_ENTER,value=u"Enter text here.")
        self.entry.Bind(wx.EVT_KEY_UP, self.OnPressEnter, self.entry)
        sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)

        button = wx.Button(self,-1,label="Click me !")
        sizer.Add(button, (0,1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)
        #button.Bind(wx.EVT_KEY_UP, self.OnButtonClick, button)

        self.label = wx.StaticText(self,-1,label=u'Hello !')
        #self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.BLACK)
        sizer.Add( self.label, (1,0),(1,2), wx.EXPAND )

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)
        self.Show(True)

    def OnButtonClick(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You clicked the button)" )
        print "You clicked the button !"
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)
        self.device.stop()

    def OnPressEnter(self,event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.label.SetLabel( self.entry.GetValue() + " (You pressed ENTER)" )
            print "You pressed enter !"
            self.entry.SetFocus()
            self.entry.SetSelection(-1,-1)
            source = ['entry',self.entry.GetValue()]
            self.device.putData(source)

        event.Skip()


#app = wx.App()
#frame = simpleapp_wx(None,-1,'ELM327 Simulator')
#app.MainLoop()
