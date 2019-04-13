from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# third party imports
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from allauth.account.views import ConfirmEmailView

# app imports
from users.views import (
    UserModelViewset,
    null_view,
    VerifyEmailView,
)
from lists.views import (
    ListModelViewset,
    NumberAdminModelViewset
)

from sms.views import (
    MessageModelViewset
)
from wallet.views import (
    DepositModelViewset,
    WalletModelViewset,
)

router = routers.DefaultRouter()
router.register('users', UserModelViewset, base_name='users')
router.register('lists', ListModelViewset, base_name='lists')
router.register('numbers', NumberAdminModelViewset, base_name='numbers')
router.register('messages', MessageModelViewset, base_name='messages')
router.register('wallet', WalletModelViewset, base_name='wallet')
router.register('deposits', DepositModelViewset, base_name='deposits')

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('docs/', include('rest_framework_docs.urls')),

    # App Specific url & namespaces
    path('api/v1/', include(router.urls)),

    # Authentication Setup urls
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('token-auth/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),

    # custom auth urls
    path('api/v1/rest-auth/registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    path('verify-email/<key>/', VerifyEmailView.as_view(), name='account_confirm_email'),
    path('api/v1/rest-auth/password/reset/confirm/<uidb64>/<token>/', null_view, name='password_reset_confirm'),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
