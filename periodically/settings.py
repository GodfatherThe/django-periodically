from django.conf import settings as project_settings
from .backends import DefaultBackend
import datetime


_settings = getattr(project_settings, 'PERIODICALLY_SETTINGS', {})
DEFAULT_BACKEND = _settings.get('DEFAULT_BACKEND', DefaultBackend)
DEFAULT_TIMEOUT = _settings.get('DEFAULT_TIMEOUT', datetime.timedelta(minutes=10))
BACKEND_GROUPS = _settings.get('BACKEND_GROUPS', {})
