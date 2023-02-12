from django.urls import path

from apps.userauths.views import register_view

apps_name = 'userauths'

urlpatterns = [
    path('sign-up/', register_view, name='sign-up'),
]
