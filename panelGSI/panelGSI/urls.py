"""
URL configuration for panelGSI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tablero_GSI.views import lineabaseViewSet, CMDBViewSet, eventosViewSet, llaveViewSet, CMDBvsEventosViewSet, LineabasevsEventosViewSet

#lineabase router

lineabase_router = routers.SimpleRouter()
lineabase_router.register(
    r'lineabase',
    lineabaseViewSet,
    basename='lineabase'
)

#CMDB router

CMDB_router = routers.SimpleRouter()
CMDB_router.register(
    r'CMDB',
    CMDBViewSet,
    basename='CMDB'
)

#evento router

evento_router = routers.SimpleRouter()
evento_router.register(
    r'eventos',
    eventosViewSet,
    basename='eventos'
)

#llave router

llave_router = routers.SimpleRouter()
llave_router.register(
    r'llave',
    llaveViewSet,
    basename='llave'
)

#CMDBvsEventos router

CMDBvsEventos_router = routers.SimpleRouter()
CMDBvsEventos_router.register(
    r'CMDBvseventos',
    CMDBvsEventosViewSet,
    basename='CMDBvsEventos'
)

#LineabasevsEventos router

LineabasevsEventosRouter = routers.SimpleRouter()
LineabasevsEventosRouter.register(
    r'LineabasevsEventos',
    LineabasevsEventosViewSet,
    basename ='LineabasevsEventos'
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/', include(lineabase_router.urls)),
    path('api/', include(CMDB_router.urls)),
    path('api/', include(evento_router.urls)),
    path('api/', include(llave_router.urls)),
    path('api/', include(CMDBvsEventos_router.urls)),
    path('api/', include(LineabasevsEventosRouter.urls))
]
