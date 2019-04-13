import re
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

@deconstructible
class CustomUsernameValidator(object):
    message = _('Invalid username')

    def __call__(self, value):
        # allows standart django username strings and /.
        if not re.match(r'[a-zA-Z0-9_@/-]+', value):
            raise ValidationError(self.message, code='invalid_username')


custom_usename_validator = [CustomUsernameValidator()]
