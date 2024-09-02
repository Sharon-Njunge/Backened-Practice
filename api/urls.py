from django.urls import path
from .views import (
    UserViewSet,
    PoliceOfficerViewSet,
    MortuaryViewSet,
    MortuaryStaffViewSet,
    PoliceStationViewSet,
    MissingPersonViewSet,
    UnidentifiedBodyViewSet
)
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'police-officers', PoliceOfficerViewSet, basename='police-officer')
router.register(r'mortuaries', MortuaryViewSet, basename='mortuary')
router.register(r'mortuary-staff', MortuaryStaffViewSet, basename='mortuary-staff')
router.register(r'police-stations', PoliceStationViewSet, basename='police-station')
router.register(r'missing-persons', MissingPersonViewSet, basename='missing-person')
router.register(r'unidentified-bodies', UnidentifiedBodyViewSet, basename='unidentified-body')

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    path('police-officers/', PoliceOfficerViewSet.as_view({'get': 'list', 'post': 'create'}), name='police-officer-list'),
    path('police-officers/<int:pk>/', PoliceOfficerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='police-officer-detail'),
    path('mortuaries/', MortuaryViewSet.as_view({'get': 'list', 'post': 'create'}), name='mortuary-list'),
    path('mortuaries/<int:pk>/', MortuaryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='mortuary-detail'),
    path('mortuary-staff/', MortuaryStaffViewSet.as_view({'get': 'list', 'post': 'create'}), name='mortuary-staff-list'),
    path('mortuary-staff/<int:pk>/', MortuaryStaffViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='mortuary-staff-detail'),
    path('police-stations/', PoliceStationViewSet.as_view({'get': 'list', 'post': 'create'}), name='police-station-list'),
    path('police-stations/<int:pk>/', PoliceStationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='police-station-detail'),
    path('missing-persons/', MissingPersonViewSet.as_view({'get': 'list', 'post': 'create'}), name='missing-person-list'),
    path('missing-persons/<int:pk>/', MissingPersonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='missing-person-detail'),
    path('unidentified-bodies/', UnidentifiedBodyViewSet.as_view({'get': 'list', 'post': 'create'}), name='unidentified-body-list'),
    path('unidentified-bodies/<int:pk>/', UnidentifiedBodyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='unidentified-body-detail'),
]
