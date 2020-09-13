from django.urls import path
from .views import HomeTemplateView, AboutTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
]
