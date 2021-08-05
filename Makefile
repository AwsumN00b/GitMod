main: spec
	pyinstaller GitMod.spec

spec:
	pyi-makespec main.py -F --icon=GitMod.ico --noconsole -n GitMod

debug: debug_spec
	pyinstaller GitMod_DEBUG.spec

debug_spec:
	pyi-makespec main.py -F --icon=GitMod.ico -n GitMod_DEBUG
