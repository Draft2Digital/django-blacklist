from django.conf import settings


def get_setting(variable, default=None):
    """ get the 'variable' from settings if not there use the
    provided default """
    return getattr(settings, variable, default)


# see if the django app is sitting behind a reverse proxy
BEHIND_REVERSE_PROXY = get_setting('BLACKLIST_BEHIND_REVERSE_PROXY', False)


# if the django app is behind a reverse proxy, look for the
# ip address using this HTTP header value
REVERSE_PROXY_HEADER = get_setting('BLACKLIST_REVERSE_PROXY_HEADER',
                                   'HTTP_X_FORWARDED_FOR')
