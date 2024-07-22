from django.urls import path
from .views import RiderViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'rides', RiderViewSet)

urlpatterns = [
    path('',RiderViewSet.as_view(),name="rides")
]

# urlpatterns += router.urls