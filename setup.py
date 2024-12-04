from setuptools import setup, find_packages

VERSION = '0.1.0'
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
      install_requires = ["numpy >= 1.24.1", "matplotlib >= 3.6.3"], 
      keywords = ['python'],
      classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)