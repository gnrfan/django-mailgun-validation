from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _, ungettext_lazy
from django.utils.encoding import force_text
from django.conf import settings

from mailgun.api import MailgunAPI
from mailgun.api import MailgunException

class EmailValidator(object):
    message = _('Enter a valid email address.')
    code = 'invalid'

    def __init__(self, message=None, code=None, whitelist=None, api_key=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if whitelist is not None:
            self.domain_whitelist = whitelist

    def __call__(self, value):
        value = force_text(value)

        if api_key is None:
            raise MailgunException('No API key was provided.')

        mailgun = MailgunAPI(api_key=api_key)
        result = mailgun.validate_address(value)

        if result['is_valid'] == False:
            raise ValidationError(self.message, code=self.code)


api_key = None
if hasattr(settings, 'MAILGUN_API_KEY'):
    api_key = settings.MAILGUN_API_KEY

validate_email = EmailValidator(api_key=api_key)
