from django.urls import path, include
from rest_framework.routers import DefaultRouter

from car import views

router = DefaultRouter()
router.register('car-positioncategory-images', views.ImageForCarPositionCategoryViewSet,
                'image-for-car-postioncategory')
router.register('colored_images', views.ColoredImageViewSet, 'colored_images')
router.register('car_interior', views.InteriorViewSet, 'car_interior')
router.register('car_interior_details', views.CarInteriorDetailsViewSet, 'car_interior_details')
router.register('car_appearance', views.AppearanceViewSet, 'car_appearance')
router.register('car_appearance_details', views.CarAppearanceDetailsViewSet, 'car_appearance_details')
router.register('car_positions', views.CarPositionViewSet, 'car_positions')
router.register('attribute_categories', views.AttributeCategoryViewSet, 'attribute_categories')
router.register('attributes', views.AttributeViewSet, 'attributes')
router.register('cars_gallery', views.GalleryViewSet, 'cars_gallery')
router.register('cars_videos', views.VideoViewSet, 'cars_videos')


urlpatterns = [
    path('', include(router.urls)),
    path('cars/', views.CarListCreateApiView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', views.CarDetailApiView.as_view(), name='car-detail')
]
