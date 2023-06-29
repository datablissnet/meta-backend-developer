from django.urls import path, re_path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('menu_item/10', views.display_menu_item),
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item),
]
