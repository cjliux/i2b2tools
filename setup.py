from distutils.core import setup

import glob
py_files = [file[:-3] for file in glob.glob("i2b2tools/**/*.py", recursive=True)]
print(py_files)

setup(name="i2b2tools",
      version="1.0",
      description="A set of tools for working with i2b2 documents.",
      author="Dan LaManna",
      author_email="me@danlamanna.com",
      url="https://github.com/danlamanna/i2b2tools",
      license="Apache",
      # packages=["i2b2tools"]
      py_modules=py_files
)
