from cefpython3 import cefpython as cef
import platform
import sys


def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://maps.google.com/?q=-16.328546,-48.953403",
                          window_title="Chord Map Application")
    cef.MessageLoop()
    cef.Shutdown()
    # lat -16.328546 lng -48.953403

def check_versions():
    print("[hello_world.py] CEF Python {ver}".format(ver=cef.__version__))
    
if __name__ == '__main__':
    main()