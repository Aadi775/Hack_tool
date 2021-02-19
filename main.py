import socket

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
print(get_ip())

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













#while True:

#     read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])
#
#     for sock in read_sockets:
#
#         if sock == server_socket:
#
#             sockfd, client_address = server_socket.accept()
#             connected_clients_sockets.append(sockfd)
#
#         else:
#             try:
#
#                 data = sock.recv(4096)
#                 txt = str(data)
#
#                 if txt.startswith('SIZE'):
#                     tmp = txt.split()
#                     size = int(tmp[1])
#
#                     print 'got size'
#
#                     sock.send("GOT SIZE")
#
#                 elif txt.startswith('BYE'):
#                     sock.shutdown()
#
#                 elif data:
#
#                     myfile = open(basename % imgcounter, 'wb')
#
#                     data = sock.recv(40960000)
#                     if not data:
#                         myfile.close()
#                         break
#                     myfile.write(data)
#                     myfile.close()
#
#                     sock.send("GOT IMAGE")
#                     sock.shutdown()
#             except:
#                 sock.close()
#                 connected_clients_sockets.remove(sock)
#                 continue
#         imgcounter += 1
# server_socket.close()
