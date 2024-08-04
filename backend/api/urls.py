from django.urls import path
from .views import URLListCreate, URLRetrieveUpdateDestroy, redirect_view

urlpatterns = [
    path('urls/', URLListCreate.as_view(), name='url-list-create'),
    path('urls/<int:pk>/', URLRetrieveUpdateDestroy.as_view(), name='url-retrieve-update-destroy'),
    path('r/<str:short_url>/', redirect_view, name='redirect'),
]
