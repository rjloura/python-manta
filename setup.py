#!/usr/bin/env python

"""python-manta Python package setup script"""

import os
import sys

assert sys.version_info > (2, 5), \
    "python-manta does not support this Python version: %s" % sys.version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


TOP = os.path.dirname(os.path.abspath(__file__))

def get_version():
    """Get the python-manta version without having to import the manta package,
    which requires deps to already be installed.
    """
    _globals = {}
    _locals = {}
    print(TOP + "/manta/version.py")
    execfile(TOP + "/manta/version.py", _globals, _locals)
    return _locals["__version__"]


setup(
    name="manta",
    version=get_version(),
    description="A Python SDK for Manta",
    long_description="""A Python SDK for Manta (Joyent's object store and cloud compute system).

This provides a Python 'manta' package and a 'mantash' (Manta Shell) CLI
and shell.
""",
    author="Joyent",
    author_email="support@joyent.com",
    maintainer="Joyent",
    maintainer_email="support@joyent.com",
    url="https://github.com/joyent/python-manta",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    # Python Packaging voodoo.
    packages=["manta"],
    package_dir={"manta": "manta"},
    package_data={
        '': ['*.txt'],
    },
    include_package_data=True,
    install_requires=open(TOP + '/requirements.txt').read().splitlines(),
    platform="any",
    scripts=[
        (sys.platform == "win32" and "bin\\mantash" or "bin/mantash")
    ],
    zip_safe=False,
)
