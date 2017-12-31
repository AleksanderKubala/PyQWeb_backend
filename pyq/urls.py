"""pyq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from .pyqweb.views.CircuitView import CircuitView
from .pyqweb.views.RegisterView import RegisterView
from .pyqweb.views.GateView import GateView
from .pyqweb.views.ComputeView import ComputeView
from pyq.pyqweb.views import GeneralView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^circuit/', CircuitView.as_view()),
    url(r'^circuit/add/', GeneralView.add_gate),
    url(r'^circuit/remove/', GeneralView.clean_slots),
    url(r'^compute/', ComputeView.as_view()),
    url(r'^register/', RegisterView.as_view()),
    url(r'^gates/', GateView.as_view())
]
