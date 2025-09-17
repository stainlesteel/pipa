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
### For functions that just return strings
```python
coll = pip.freeze()
print(coll) # freeze() and other commands don't print by themselves
# you have to do this manually.
```
#### `install()`

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
`py_version`

**Default: None**

**Options: Python Version (int | float) | None**

**Requires: `no_deps`**

Allows you to install a package for a specific python version, the flag `no_deps` is required.

---
`no_cache`

**Default: None**

**Options: True | False | None**

Disables cached files for a package.

---
`user_only`

**Default: None**

**Options: True | False | None**

Installs to only the local site-packages directory.

---
`no_deps`

**Default: None**

**Options: True | False | None**

**Required by: `py_version`**

Ignore dependencies (other modules) required by the package being installed.

---
#### `uninstall()`
Uninstall a package from pip.
### Kwargs
`package_name`

**Default: None**

**Options: name (str) | None**

The package's name you want to uninstall, this is not required for removing from a file, .etc.

---
`from_filepath`

**Default: None**

**Options: filepath (str) | None**

Select the package name(s) from a .txt file, if you need to remove packages from a requirements.txt, this is what you need.

---
`always_confirm`

**Default: None**

**Options: True | False | None** 

If confronted by pip to confirm removing a package, this kwarg silences it and goes ahead. Recommended for a quiet output.

---
`break_packages`

**Default: None**

**Options: True | False | None**

Ignore all caution from pip that your code may break other packages installed on system.

---
### `freeze()`
List all installed packages in a system.

**You have to run this function as a variable, then print its output. (for info, go to [`For functions that just return..`](#for-functions-that-just-return-strings))**
#### Kwargs
`user_only`

**Default: None**

**Options: True | False | None**

Only list installed packages from a user's local site-packages folder.

---
`to_file`

**Default: None**

**Options: True | False | None**

Will save list to a file named `requirements.txt`

---
### `list()`
Nicer freeze().
#### Kwargs
`user_only`

**Default: None**

**Options: True | False | None**

Only list installed packages from a user's local site-packages folder.

---
`outdated`

**Default: None**

**Options: True | False | None**

Only show outdated packages.

---
`uptodate`

**Default: None**

**Options: True | False | None**

Only show up-to-date packages.

---
`uptodate`

**Default: None**

**Options: True | False | None**

Only show up-to-date packages.

---
`editable`

**Default: None**

**Options: True | False | None**

Only show editable packages.

---
`unstable`

**Default: None**

**Options: True | False | None**

Only show unstable packages.

---------
### `show()`
Show information about an installed package.

**You have to run this function as a variable, then print its output. (for info, go to [`For functions that just return..`](#for-functions-that-just-return-strings))**
#### Kwargs
`package_name`

**Required**

**Options: package_name (str)**

The package name.

---
`show_files`

**Default: None**

**Options: True | False | None**

Show filepaths containing the package.

-----
### `debug()`
Debugs system install of pip.

----
### `inspect()`
Inspects entire pip installation and installed python packages.
#### Kwargs
`user_only`

**Default: None**

**Options: True | False | None**

Only inspects python packages from local site-packages folder.

----
`path`

**Default: None**

**Options: True | False | None**

Restrict to the specified installation path for listing packages (can be used multiple times).
