from django.urls import path,include
from .views import async_view
urlpatterns = [
    path("async_view/",async_view)
]