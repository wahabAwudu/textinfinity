from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


# override this to change the link you get for an account verification
class AccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_PREFIX + 'accounts/verify-email/' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.content_subtype = 'html'
        msg.send()
