#!/usr/bin/env python3
import sys
import logging
sys.path.insert(0, '/srv/http/nel.johnbond.org/')
from webapp import app as application
logging.basicConfig(filename='/var/log/apache2/nel.johnbond.org_flask.log', level=logging.INFO)
application.secret_key = 'a secret'
