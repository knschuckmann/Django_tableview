# -*- coding: utf-8 -*-
from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.TableView.as_view(), name='webapp'),
]