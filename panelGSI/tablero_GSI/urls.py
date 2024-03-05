from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^aplicacion$', views.AplicacionList.as_view()),
    re_path(r'^aplicacion/(?P<pk>[0-9]+)$', views.AplicacionDetail.as_view())
]


