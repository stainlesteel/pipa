import subprocess

class pip_api:
    def __init__(self):
        self.quiet_output = False
        return None
    
    def process_run(self, args, capture=None):
        kwargs = {'check': True}
        if capture:
            kwargs.update({'capture_output': True})
            call = subprocess.run(args, **kwargs)
            return call.stdout
        else:
            subprocess.run(args, **kwargs)
    def install(self, package_name=None, from_filepath=None, upgrade=None, py_version=None, no_cache=None, user_only=None):
        # these are basic arguments
        args = ["python3", "-m", "pip", "install"]
        # here, it checks for any optional arguments before running the basic command 
        if from_filepath != None:
            args.append("-r")
            args.append(from_filepath)
        else:
            if from_filepath == None and isinstance(package_name, str):
                args.append(package_name)
            else:
                raise SyntaxError("The package name for pip cannot be anything but a string.")
        # check if user wants forced upgrade
        if upgrade == True:
            args.append("--upgrade")

        if py_version:
            args.append("--python-version")
            args.append(f"{py_version}")

        if no_cache == True:
            args.append("--no-cache-dir")

        if user_only == True:
            args.append("--user")

        self.process_run(args)
    def freeze(self):
        args = ['python3', '-m', 'pip', 'freeze']

        result = self.process_run(args, capture=True)
        godot = result.decode('utf-8')
        result_str = godot.replace('\n', ' \n')
        return result_str



