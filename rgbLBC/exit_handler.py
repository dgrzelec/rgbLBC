# source: https://stackoverflow.com/questions/36126165/how-to-handle-console-exit-and-object-destruction/36126780#36126780
import os, sys

def set_exit_handler(func):
    if os.name == "nt":
        try:
            import win32api
            win32api.SetConsoleCtrlHandler(func, True)
        except ImportError:
            version = '.'.join(map(str, sys.version_info[:2]))
            raise Exception("pywin32 not installed for Python " + version)
    else:
        import signal
        signal.signal(signal.SIGTERM, func)

if __name__ == "__main__":
    def on_exit(sig, func=None):
        print ("exit handler triggered")
        import time
        time.sleep(5)

    set_exit_handler(on_exit)
    print ("Press  to quit")
    input()
    print ("quit!")