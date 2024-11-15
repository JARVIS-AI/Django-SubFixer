from django.urls import path
from .views import upload_subtitle, counter

urlpatterns = [
    path('', upload_subtitle, name='upload_subtitle'),
    path('addcount/', counter, name='counter'),
]
