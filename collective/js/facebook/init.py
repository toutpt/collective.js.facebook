from zope import interface
from zope import component
from plone.app.layout.viewlets.common import ViewletBase


class IFacebookInitCodeProvider(interface.Interface):
    """a named adapter which should provide code in the facebook init"""

    def available():
        """ return True or False if this code should be added"""

    def get_code():
        """return a unicode string of javascript valid code"""



class InitViewlet(ViewletBase):
    """facebook init viewlet. For documentation please refer to 
    https://developers.facebook.com/docs/reference/javascript/#loading
    """

    def app_id(self):
        return ''

    def status(self):
        return 'true'

    def cookie(self):
        return 'true'

    def xfbml(self):
        return 'true'

    def addition_init_code(self):
        code = u""
        providers = component.getAdapters(self, IFacebookInitCodeProvider)
        for provider in providers:
            if provider.available():
                code += provider.get_code()
        return code

    def language_code(self):
        return 'fr_FR' #fr is not a valid local
