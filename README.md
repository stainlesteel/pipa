# pipA
*short for pip Api.*

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/stainlesteel/pipa/python-publish.yml?logo=github&label=CI)
![PyPI - Status](https://img.shields.io/pypi/v/pipa.py?logo=python&label=PyPI&logoColor=white&color=yellow)

![GitHub License](https://img.shields.io/github/license/stainlesteel/pipa?color=green&label=License)
![GitHub repo size](https://img.shields.io/github/repo-size/stainlesteel/pipa?color=green&label=Repo%20Size)
![GitHub last commit](https://img.shields.io/github/last-commit/stainlesteel/pipa?color=green&label=Last%20Commit)

A dead simple wrapper for the `pip` module.

Virtual environments are not handled (yet), either you'd have to manually handle it or not use one.

## WARNING 
This module is not cross-platform and doesn't work for Windows.

It only works for unix-based platforms. (Linux, MacOS, BSD, .etc)

## Installation
### pip
You can use pip to install pipA.
```bash
pip install pipa.py
```
## Usage
References can be found ![here.](DOCS.md)

Here is an example of usage.
```python
import pipa

pip = pipa.pip()

pip.install('requests')
pip.uninstall('requests')

requests = pip.show('requests')
print(requests)
# here, pip.show doesn't print, you have to do it manually
```
