import sys

from django.conf import settings
from django.conf.urls import url
from django.http import JsonResponse
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    SECRET_KEY='I_AM_A_DUMMY_KEY_CHANGE_ME',
    ROOT_URLCONF=sys.modules[__name__],
    ALLOWED_HOSTS=['*'],
)


def index(request):
    response = {'data': 'A minimal Django server'}
    return JsonResponse(response)

urlpatterns = [
    url(r'^$', index),
]


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
