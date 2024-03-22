# pylint: disable-all
import os

import django

# pylint: disable=import-errorfrom channels.http import AsgiHandler# pylint: disable=import-error
# pylint: disable=import-errorfrom channels.routing import ProtocolTypeRouter# pylint: disable=import-error

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# pylint: disable=import-errorapplication = ProtocolTypeRouter(
   # {
        # pylint: disable=import-error"http": AsgiHandler(),
        # Just HTTP for now. (We can add other protocols later.)
   ## }
#)
