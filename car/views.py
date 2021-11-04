from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Car, PositionCategory, Attribute_Category, Attribute, Car_Model_Type, Colored_Image, \
    Image_for_Car_PositionCategory, Position, Appearance_Image, Gallery, Video, Interior_Image, Appearance_Detail, \
    Interior_Detail
from .serializers import CarsListSerializer, CarCreateSerializer, ColoredImagesSerializer, \
    ImageForCarPositionCategorySerializer, CarRetrieveSerializer, AppearanceSerializer, \
    InteriorSerializer, CarPositionSerializer, AttributeSerializer, AttributeCategorySerializer, GallerySerializer, \
    VideoSerializer, AppearanceDetailSerializer, InteriorDetailSerializer, CarPositionsInDealerSerializer, \
    CarsAccordingToPositionCategory
from .filters import CarsPositionFilter


class CarListCreateApiView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

    def list(self, request, *args, **kwargs):
        cars = self.get_queryset()
        serializer = CarsListSerializer(cars, many=True)
        data = {
            'description': "",
            'results': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class CarDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        car = get_object_or_404(Car, pk=pk)
        serializer = CarRetrieveSerializer(car, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageForCarPositionCategoryViewSet(ModelViewSet):
    queryset = Image_for_Car_PositionCategory.objects.all()
    serializer_class = ImageForCarPositionCategorySerializer


class ColoredImageViewSet(ModelViewSet):
    queryset = Colored_Image.objects.all()
    serializer_class = ColoredImagesSerializer


class AppearanceViewSet(ModelViewSet):
    queryset = Appearance_Image.objects.all()
    serializer_class = AppearanceSerializer


class CarAppearanceDetailsViewSet(ModelViewSet):
    queryset = Appearance_Detail.objects.all()
    serializer_class = AppearanceDetailSerializer


class InteriorViewSet(ModelViewSet):
    queryset = Interior_Image.objects.all()
    serializer_class = InteriorSerializer


class CarInteriorDetailsViewSet(ModelViewSet):
    queryset = Interior_Detail.objects.all()
    serializer_class = InteriorDetailSerializer


class CarPositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = CarPositionSerializer


class AttributeCategoryViewSet(ModelViewSet):
    queryset = Attribute_Category.objects.all()
    serializer_class = AttributeCategorySerializer


class AttributeViewSet(ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CarPositionsInDealerViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = CarPositionsInDealerSerializer


class CarsAccordingToPositionCategoryListApiView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = CarsAccordingToPositionCategory
    filter_class = CarsPositionFilter
