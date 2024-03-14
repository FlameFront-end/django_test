from django.contrib import admin
from django.urls import path

from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/list', WomenAPIList.as_view()),
    path('api/v1/women/create', WomenAPICrete.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIRetrieve.as_view()),
    path('api/v1/women/update/<int:pk>', WomenAPIUpdate.as_view()),
    path('api/v1/women/delete/<int:pk>', WomenAPIDelete.as_view()),
]
