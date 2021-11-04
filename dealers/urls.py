from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dealers import views

router = DefaultRouter()
router.register('dealers', views.DealerViewSet, 'dealers')

urlpatterns = [
    path('', include(router.urls)),
]