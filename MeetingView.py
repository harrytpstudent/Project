# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
from MeetingController import MeetingController

###########################################################################
## Class MinervaFrame
###########################################################################

class MinervaFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        self.meeting_controller = MeetingController()
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SEC EDGAR Web Scraper", pos = wx.DefaultPosition, size = wx.Size( 1352,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer33 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel26.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
        
        self.m_panel28 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer35 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer36 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel27 = wx.Panel( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer36.Add( self.m_panel27, 1, wx.ALL, 5 )
        
        self.m_bitmap4 = wx.StaticBitmap( self.m_panel28, wx.ID_ANY, wx.Bitmap( u"cropped-cropped-logo-1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer36.Add( self.m_bitmap4, 0, wx.ALL, 5 )
        
        
        bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )
        
        self.m_panel19 = wx.Panel( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        search_sizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel19, wx.ID_ANY, u"Search" ), wx.VERTICAL )
        
        self.companyName = wx.StaticText( search_sizer.GetStaticBox(), wx.ID_ANY, u"Company Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.companyName.Wrap( -1 )
        search_sizer.Add( self.companyName, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.company_search = wx.TextCtrl( search_sizer.GetStaticBox(), wx.ID_ANY, u"Company Name...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.company_search.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        
        search_sizer.Add( self.company_search, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.documentCreation = wx.StaticText( search_sizer.GetStaticBox(), wx.ID_ANY, u"Document year created between:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.documentCreation.Wrap( -1 )
        search_sizer.Add( self.documentCreation, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.m_spinCtrl1 = wx.SpinCtrl( search_sizer.GetStaticBox(), wx.ID_ANY, u"2000", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 2000, 10 )
        search_sizer.Add( self.m_spinCtrl1, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.m_spinCtrl2 = wx.SpinCtrl( search_sizer.GetStaticBox(), wx.ID_ANY, u"2019", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2000, 2999, 0 )
        search_sizer.Add( self.m_spinCtrl2, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        
        self.m_panel19.SetSizer( search_sizer )
        self.m_panel19.Layout()
        search_sizer.Fit( self.m_panel19 )
        bSizer35.Add( self.m_panel19, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel32 = wx.Panel( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.search_button = wx.Button( self.m_panel32, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_button.Bind(wx.EVT_BUTTON, self.displayLogData)
        bSizer39.Add( self.search_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 25 )
        
        self.cancel_button = wx.Button( self.m_panel32, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer39.Add( self.cancel_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 25 )
        
        self.savelog_button = wx.Button( self.m_panel32, wx.ID_ANY, u"Save Log", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer39.Add( self.savelog_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 25 )
        
        self.exit_button = wx.Button( self.m_panel32, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer39.Add( self.exit_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 25 )
        
        
        self.m_panel32.SetSizer( bSizer39 )
        self.m_panel32.Layout()
        bSizer39.Fit( self.m_panel32 )
        bSizer35.Add( self.m_panel32, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel28.SetSizer( bSizer35 )
        self.m_panel28.Layout()
        bSizer35.Fit( self.m_panel28 )
        gSizer2.Add( self.m_panel28, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel20 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_panel20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        sizer_log = wx.StaticBoxSizer( wx.StaticBox( self.m_panel20, wx.ID_ANY, u"log" ), wx.VERTICAL )
        
        self.info_log = wx.richtext.RichTextCtrl( sizer_log.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        sizer_log.Add( self.info_log, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel20.SetSizer( sizer_log )
        self.m_panel20.Layout()
        sizer_log.Fit( self.m_panel20 )
        gSizer2.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel26.SetSizer( gSizer2 )
        self.m_panel26.Layout()
        gSizer2.Fit( self.m_panel26 )
        bSizer33.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer33 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    
    def displayLogData(self, event):
        """text_to_log = self.meeting_controller.updateView()
        self.info_log.AppendText(text_to_log)"""
        self.meeting_controller.getMeetingData(self.company_search.GetValue(), 2015, 2019)
        

if __name__ == "__main__":
    app = wx.App()
    frame = MinervaFrame(None)
    frame.Show()
    app.MainLoop()
