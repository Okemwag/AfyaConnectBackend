from django.urls import path
from .views import PharmacyViewSet


urlpatterns = [
    path('pharmacy/', PharmacyViewSet.as_view({'get': 'list'}), name='pharmacy-list'),
    path('pharmacy/<int:pk>/', PharmacyViewSet.as_view({'get': 'retrieve'}), name='pharmacy-detail'),
]