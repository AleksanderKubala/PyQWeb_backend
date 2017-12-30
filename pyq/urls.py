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
from .pyqweb.views import CircuitView
from .pyqweb.views.CircuitSizeView import CircuitSizeView
from .pyqweb.views.GateView import GateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^circuit/add/', CircuitView.add_gate),
    url(r'^circuit/remove/', CircuitView.clean_slots),
    url(r'^circuit/compute', CircuitView.compute),
    url(r'^circuit/size/', CircuitSizeView.as_view()),
    url(r'^circuit/state/', CircuitView.set_state),
    url(r'^gates/', GateView.as_view())
]
