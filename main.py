import subprocess

class pip_api:
    def __init__(self):
        return None
    
    @staticmethod
    def install(package_name=None, from_filepath=None, upgrade=None, py_version=None):
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
        else:
            raise SyntaxError("Python version argument has to be a number")

        subprocess.call(args)


