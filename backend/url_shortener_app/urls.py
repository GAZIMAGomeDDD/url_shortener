from django.urls import path
from .views import CreateShortLinkView, CreateCustomShortLinkView, GetURL

urlpatterns = [
    path('api/create-short-link/', CreateShortLinkView.as_view()),
    path('api/create-custom-short-link/', CreateCustomShortLinkView.as_view()),
    path('api/<str:short_link>', GetURL.as_view()),
]
