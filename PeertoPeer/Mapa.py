from cefpython3 import cefpython as cef
import platform
import sys
import random

def loadMap(dataUrl):
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url=dataUrl,window_title="Chord Map Application")
    cef.MessageLoop()
    cef.Shutdown()
    # lat -16.328546 lng -48.953403