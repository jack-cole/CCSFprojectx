"""projectx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views



urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),

	url(r'^$', views.index, name='index'),
	url(r'^index', RedirectView.as_view(pattern_name='index', permanent=False)),

	url(r'^clubs/', views.listclubs, name='clubs'),
	# Disabled. Will enable in the future when we can create a single use Auth Token.
	# url(r'^addclub/', views.addclub, name='addclub'),
	url(r'^editclub/', views.editclub, name='editclub'),

	url(r'^thanks/', views.thanks, name='addclub'),

	# registration
	url(r'^accounts/', include('registration.backends.default.urls')),
]
