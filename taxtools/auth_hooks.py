from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from django.utils.translation import gettext_lazy as _

from . import urls


@hooks.register('url_hook')
def register_url():
    return UrlHook(urls, 'taxtools', r'^tax/')
