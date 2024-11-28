from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Basic tools for FMNlib'
LONG_DESCRIPTION = 'README.md'

setup(name="amylib", 
      version = VERSION,
      author = "amyzeth",
      author_email = "",
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      packages = find_packages(exclude=('tests')),
      package_data={"":["*.json"]},
      install_requires = [], 
      keywords = ['python'],
      classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)