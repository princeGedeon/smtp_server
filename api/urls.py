from django.urls import path

from api.views import SendEmailAPI

urlpatterns = [
    path('send-email/', SendEmailAPI.as_view(), name='send-email')

]