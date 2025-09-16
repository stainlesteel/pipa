# pipA - Reference 
---
# Dependencies 
`subprocess`: Part of Python3 Standard Library. 
# Classes
## `pip`
### Variables
### Example Usage
```python
pipa.quiet_output = True
pipa.verbose = True
pipa.log_path = 'log.txt'
```
---
`quiet_output`

**Default: False**

**Options: True | False**

This allows you to silence the output of the module, however this isn't required for functions that don't print by themselves.

---
`verbose`

**Default: False**

**Options: True | False**

This increases the verbosity of the terminal output for any command you run.

---
`pip_version_check`

**Default: False**

**Options: True | False**

This disables the notice that your pip install is outdated.

---
`log_path`

**Default: None**

**Options : file_path (str) | None**

This allows pip to make a log file for each command you run (you may need to change the filepath or disable it, depending on your use case.)

---
### Functions
### Example Usage
```python
pip.install('requests', upgrade=True)
pip.uninstall('requests', always_confirm=True)
```
---

`install()`

Install a package from pip.

### Kwargs
`package_name`

**Default: None**

**Options: name (str) | None**

The package's name you want to install, this is not required for downloading from a file, .etc.

---
`from_filepath`

**Default: None**

**Options: filepath (str) | None**

Select the package name(s) from a .txt file, if you need to install packages from a requirements.txt, this is what you need.

---
`upgrade`

**Default: None**

**Options: True | False | None**

Forces pip to upgrade the selected package if a new version is available.

---

