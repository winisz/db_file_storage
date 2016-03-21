# django
from django.conf.urls import url

from db_file_storage import views


urlpatterns = [
    url(
        r'^db_file_storage/download/',
        views.get_file,
        {'add_attachment_headers': True},
        name='db_file_storage.download_file'
    ),
    url(
        r'^db_file_storage/get/',
        views.get_file,
        {'add_attachment_headers': False},
        name='db_file_storage.get_file'
    )
]
