import main as pip

pipk = pip.pip_api()
pipk.quiet_output = True
call = pipk.freeze()
print(f'{call}')
