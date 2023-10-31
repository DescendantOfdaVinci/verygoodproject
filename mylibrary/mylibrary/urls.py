
from django.contrib import admin
from django.urls import path

from library.views import *

urlpatterns = [
    path('', show_start_page),
    path('showbooks/', show_showbooks_page, name='showbooks'),
    path('showreaders/', show_showreaders_page, name='showreaders'),
    path('addboоk/', show_addbook_page, name='addbook'),
    path('addreader/', show_addreader_page, name='addreader'),
    path('addrent/', show_addrent_page, name='addrent'),
    path('admin/', admin.site.urls),
]

