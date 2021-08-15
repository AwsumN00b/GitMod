main: spec config_copy
	pyinstaller GitMod.spec

spec:
	pyi-makespec main.py --icon=GitMod.ico --noconsole -n GitMod

debug: debug_spec config_copy
	pyinstaller GitMod_DEBUG.spec

debug_spec:
	pyi-makespec main.py --icon=GitMod.ico -n GitMod_DEBUG

config_copy:
	cp .\\config.txt .\\dist\\GitMod\\
	cp .\\config.txt .\\dist\\GitMod_DEBUG\\
