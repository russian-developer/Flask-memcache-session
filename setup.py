#!/usr/bin/python
from os.path import isfile, join
import glob
import os
import re

from setuptools import setup


if isfile("MANIFEST"):
    os.unlink("MANIFEST")


TOPDIR = os.path.dirname(__file__) or "."


setup(name="flask-memcache-session",
      version = 1,
      description = "Use memcache for store session data",
      author = "Constantine Slednev",
      author_email = "c.slednev@gmail.com",
      url = "https://github.com/unk2k/Flask-memcache-session",
      license = "BSD License",
      package_data={"": ["*.tar.gz"]},
      include_package_data=True,
      zip_safe=False,
      )
