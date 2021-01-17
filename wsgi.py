#!/usr/bin/env python3
import sys
sys.path.insert(0, '/srv/http/nel.johnbond.org')
from . webapp import app as application
application.secret_key = 'a secret'
