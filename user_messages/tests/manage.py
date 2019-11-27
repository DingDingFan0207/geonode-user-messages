# #!/usr/bin/env python
# from django.core.management import execute_manager
# try:
#     import settings # Assumed to be in the same directory.
# except ImportError:
#     import sys
#     sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
#     sys.exit(1)

# if __name__ == "__main__":
#     execute_manager(settings)

#*****************************************************************************************************************
# The following changes were made to resolve the ImportError caused by execute_manager
# excute manager was deprecated and then deleted in Django 1.6
# The changes made are compatible with Django 1.11
# Original codes are commented out above.
#*****************************************************************************************************************

import os
import sys
import tempfile

import django
from django.conf import settings
from django.test.utils import get_runner

ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.join(ROOT, '..')
sys.path.append(APP_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


# We do this here because settings.py has a tendency to be imported more than
# once, in certain situations, and we only want one temporary test folder.
MEDIA_ROOT = os.path.join(tempfile.gettempdir(), 'user_messages')
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(os.path.join(MEDIA_ROOT, 'test'))
settings.MEDIA_ROOT = MEDIA_ROOT


if __name__ == "__main__":
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['user_messages'], verbosity=1)
    if failures:
        sys.exit(failures)