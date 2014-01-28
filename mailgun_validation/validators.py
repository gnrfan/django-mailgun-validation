from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _, ungettext_lazy
from django.utils.encoding import force_text
from mailgun_validation.exceptions import MailgunException
import requests

class EmailValidator(object):
    message = _('Enter a valid email address.')
    code = 'invalid'

    def __init__(self, message=None, code=None, api_key=None):
        self.api_key = api_key
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        value = force_text(value)

        if self.api_key is None:
            raise MailgunException('No API key was provided.')

        validated = self.validate_address(value)

        if not validated:
            raise ValidationError(self.message, code=self.code)

    def validate_address(self, email):
        response = requests.get(
            "https://api.mailgun.net/v2/address/validate",
            auth=("api", self.api_key),
            params={"address": email}
        )
        if response.ok:
            response_data = response.json()
            return response_data['is_valid']
        else:
            raise MailgunException('Problems with the Mailgun web service')
            
        

api_key = None
if hasattr(settings, 'MAILGUN_API_KEY'):
    api_key = settings.MAILGUN_API_KEY

validate_email = EmailValidator(api_key=api_key)
