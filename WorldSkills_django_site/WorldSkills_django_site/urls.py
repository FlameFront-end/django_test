from django.contrib import admin
from django.urls import path

from women.views import WomenApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenApiView.as_view()),
    path('api/v1/women/', WomenApiView.as_view()),
    path('api/v1/women/<int:pk>/', WomenApiView.as_view()),
]
