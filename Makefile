main: spec
	pyinstaller GUI.spec

spec:
	pyi-makespec GUI.py -F --icon=GitMod.ico
