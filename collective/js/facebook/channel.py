from Products.Five.browser import BrowserView
from datetime import datetime, timedelta
from email import utils


class ChannelFile(BrowserView):
    """This view is the channel file. documentation:
    https://developers.facebook.com/docs/reference/javascript/#channel
    """

    def __call__(self):
        cache_age = 31536000 #60*60*24*365
        cache_expires = datetime.now() + timedelta(days=365)
        max_age = 'max-age=' + str(cache_age)
        self.request.response.setHeader('Pragma', 'public')
        self.request.response.setHeader('Cache-Control', max_age)
        self.request.response.setHeader('Expires', utils.formatdate())
        script = u"""<script src="//connect.facebook.net/%s/all.js"></script>"""

        return script%self.language()

    def language(self):
        return 'fr_Fr'
