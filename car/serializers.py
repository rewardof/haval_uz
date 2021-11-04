from rest_framework import serializers
from .models import Car, PositionCategory, Attribute_Category, Attribute, Car_Model_Type, Colored_Image, \
    Image_for_Car_PositionCategory, Position, Appearance_Image, Gallery, Video, Interior_Image, \
    Appearance_Detail, Interior_Detail


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'title', 'image', 'price')


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ColoredImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colored_Image
        fields = ('car_position_category', 'color_ibi', 'color_title', 'color_code', 'image')


class ImageForCarPositionCategorySerializer(serializers.ModelSerializer):
    colored_images = ColoredImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Image_for_Car_PositionCategory
        fields = ('id', 'car', 'position_category', 'colored_images')


class AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance_Image
        fields = ('id', 'car', 'image')


class AppearanceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance_Detail
        fields = ('id', 'car', 'title')


class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior_Image
        fields = ('id', 'car', 'image')


class InteriorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior_Detail
        fields = ('id', 'car', 'title')


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('title', 'value', 'attribute_category')


class AttributeCategorySerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = Attribute_Category
        fields = ('car_position', 'title', 'attributes')


class CarPositionSerializer(serializers.ModelSerializer):
    attribute_category = AttributeCategorySerializer(many=True)

    class Meta:
        model = Position
        fields = ('id', 'car', 'title', 'position_category', 'image', 'min_price', 'transmission_name',
                  'wheel_drive_name', 'fuel_type_name', 'engine_type', 'engine_displacement', 'engine_power',
                  'working_volume', 'time_to_100_speed', 'max_speed', 'attribute_category'
                  )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'car', 'image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'car', 'video')


class CarRetrieveSerializer(serializers.ModelSerializer):
    car_model_type = serializers.SlugRelatedField(queryset=Car_Model_Type, slug_field='title')
    image_for_car_positioncategory = ImageForCarPositionCategorySerializer(many=True, read_only=True)
    appearance_images = AppearanceSerializer(many=True, read_only=True)
    appearance_details = AppearanceDetailSerializer(many=True, read_only=True)
    interior_images = InteriorSerializer(many=True, read_only=True)
    interior_details = InteriorDetailSerializer(many=True, read_only=True)
    positions = CarPositionSerializer(read_only=True)
    galleries = GallerySerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = (
            'id', 'brand', 'title', 'price', 'image_for_car_positioncategory', 'appearance_details',
            'appearance_images', 'interior_details', 'interior_images', 'car_model_type', 'positions',
            'galleries', 'videos'
        )

    def to_representation(self, instance):
        car_detail = super(CarRetrieveSerializer, self).to_representation(instance)
        car_detail['appearance_desc'] = ''
        car_detail['interior_desc'] = ''
        return car_detail


class PositionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionCategory
        fields = ('id', 'title')


class CarPositionsInDealerSerializer(serializers.ModelSerializer):
    dealers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Position
        fields = ('id', 'title', 'min_price', 'image', 'dealers')


class CarsAccordingToPositionCategory(serializers.ModelSerializer):
    positions = serializers.SerializerMethodField()
    position_category = serializers.SlugRelatedField(queryset=PositionCategory.objects.all(), slug_field='title')

    class Meta:
        model = Image_for_Car_PositionCategory
        fields = ('id', 'car', 'position_category', 'positions')

    def get_positions(self, obj):
        position_category = obj.position_category
        positions = Position.objects.filter(position_category=position_category)
        positions_serializer = CarPositionsInDealerSerializer(positions, many=True, context=self.context)
        return positions_serializer.data
