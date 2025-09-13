import main as pi

pip = pi.pip_api()

pip.verbose = True
call = pip.uninstall('sg_api.py', always_confirm=True)
