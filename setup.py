"""
Helpers de TC -> Helper Functions by Taylor Curran
""" 

import setuptools 

# Required Packages
REQUIRED = [
  "numpy",
  "pandas"
]

# Use Readme for Long Description
with open("README.md", "r") as fl:
  LONG_DESCRIPTION = fl.read()

setuptools.setup(
	# use a - not an underscore
  name="helpersdetc",
	# Remember to Increment Version Numbers
	# These do NOT work as decimals.
	# For example: 0.342 > 0.38 since 342 > 38
  version="0.2.8",
  author="taylor-curran",
  description="Helper Functions by Taylor Curran",
  long_description=LONG_DESCRIPTION,
	# Content Type
  long_description_content="text/markdown",
  url='https://github.com/taylor-curran/eda_curran',
  packages=setuptools.find_packages(),
	# Test This!
  python_requires=">=3.8",
  install_requires=REQUIRED,
	# Meta Information that PiPy knows how to read
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ]
)