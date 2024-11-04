from django.urls import path

from .views import *

urlpatterns = [
    path("", render_index_page, name="render_index_page"),
]