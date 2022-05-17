# -*- coding: utf-8 -*-
"""
flaskext.uploads
================
This module provides upload support for Flask. The basic pattern is to set up
an `UploadSet` object and upload your files to it.

:copyright: 2010 Matthew "LeafStorm" Frazier
:license:   MIT/X11, see LICENSE for details
"""

import sys

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
else:
    string_types = basestring,

import os.path
import posixpath

from flask import current_app, send_from_directory, abort, url_for
# -*- coding: utf-8 -*-
"""
flaskext.uploads
================
This module provides upload support for Flask. The basic pattern is to set up
an `UploadSet` object and upload your files to it.

:copyright: 2010 Matthew "LeafStorm" Frazier
:license:   MIT/X11, see LICENSE for details
"""

import sys

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
else:
    string_types = basestring,

import os.path
import posixpath

from flask import current_app, send_from_directory, abort, url_for