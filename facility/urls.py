from django.urls import path
from .views import FacilityViewSet, RecommendFacilityView


urlpatterns = [
    path('facility/', FacilityViewSet.as_view({'get': 'list'}), name='facility-list'),
    path('facility/<int:pk>/', FacilityViewSet.as_view({'get': 'retrieve'}), name='pharmacy-detail'),
    path('recommend_facility/', RecommendFacilityView.as_view(), name='recommend_facility'),
]
