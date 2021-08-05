main: spec
	pyinstaller GitMod.spec

spec:
	pyi-makespec main.py -F --icon=GitMod.ico --noconsole -n GitMod
