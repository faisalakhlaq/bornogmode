from .base import *


CONTACTUS_FORM_EMAIL = 'my_email@domain.extension'
DEBUG = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

## Send email via postfix on localhost
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'mu_email@gmail.com'
# EMAIL_HOST_PASSWORD = PW
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

## if using email, we need unlock
## captha to enable sending emails via django
