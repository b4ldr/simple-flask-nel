#!/usr/bin/env python3
import sys
import logging
sys.path.insert(0, '/srv/http/nel.johnbond.org/')
from webapp import app as application
logging.basicConfig(filename='/srv/http/nel.johnbond.org/app.log', level=logging.INFO)
application.secret_key = 'a secret'
