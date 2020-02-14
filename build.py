import skidder
from subprocess import check_output
version = skidder.__version__
check_output(['python', 'setup.py', 'bdist_wheel'])
check_output(['python', 'setup.py', 'sdist'])
print(f"Bult distros for PyPi (version {version}). Now run:\n"
      f"twine upload dist/skidder-{version}-py3-none-any.whl\n"
      f"twine upload dist/skidder-{version}.tar.gz\n")
