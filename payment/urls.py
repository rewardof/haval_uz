from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payment import views

router = DefaultRouter()
router.register('credits', views.CreditViewSet, 'credits')
router.register('payments', views.PaymentViewSet, 'payments')


urlpatterns = [
    path('', include(router.urls)),
]