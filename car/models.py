from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='car-main-image/%Y/%m/%d')
    manufactured_at = models.DateField()
    car_model_type = models.ForeignKey('Car_Model_Type', on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f'{self.brand} {self.title}'


class Appearance_Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='appearance_images')
    image = models.ImageField(upload_to='car-appearance-image/%Y/%m/%d')

    def __str__(self):
        return f'Appearance images for {self.car.brand} {self.car.title}'


class Appearance_Detail(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='appearance_details')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'Apperance details for {self.car.brand} {self.car.title}'


class Interior_Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='interior_images')
    image = models.ImageField(upload_to='car-interior-image/%Y/%m/%d')

    def __str__(self):
        return f'Interior images for {self.car.brand} {self.car.title}'


class Interior_Detail(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='interior_details')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'Interior details for {self.car.brand} {self.car.title}'


class Colored_Image(models.Model):
    car_position_category = models.ForeignKey('Image_for_Car_PositionCategory', on_delete=models.CASCADE,
                                              related_name='colored_images')
    color_ibi = models.PositiveIntegerField()
    color_title = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255)
    image = models.ImageField(upload_to='color-image/%Y/%m/%d')

    def __str__(self):
        return f'{self.color_title} {self.car_position_category.car.brand} {self.car_position_category.car.title} {self.car_position_category.position_category.title} image'


class Image_for_Car_PositionCategory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='image_for_car_positioncategory')
    position_category = models.ForeignKey('PositionCategory', on_delete=models.CASCADE,
                                          related_name='images_for_positioncategory')

    def __str__(self):
        return f'Colored images for {self.car.brand} {self.car.title} {self.position_category.title}'

    class Meta:
        verbose_name_plural = 'Image_for_Car_PositionCategories'


class Attribute(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=2550)
    attribute_category = models.ForeignKey('Attribute_Category', on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.title


class Attribute_Category(models.Model):
    car_position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='attribute_category')
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'Attribute Category for {self.car_position.car.brand} {self.car_position.car.title} position'

    class Meta:
        verbose_name_plural = 'Attribute_Categories'


class Position(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='positions')
    title = models.CharField(max_length=255)
    position_category = models.ForeignKey('PositionCategory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car-price-image/%Y/%m/%d')
    min_price = models.IntegerField()
    transmission_name = models.CharField(max_length=255)
    wheel_drive_name = models.CharField(max_length=255)
    fuel_type_name = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255)
    engine_displacement = models.CharField(max_length=255)
    engine_power = models.PositiveIntegerField()
    working_volume = models.PositiveIntegerField()
    time_to_100_speed = models.CharField(max_length=255)
    max_speed = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} characteristics'


class PositionCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'PositionCategories'


class Car_Model_Type(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='galleries')
    image = models.ImageField(upload_to='image/%Y/%m/%d')

    def __str__(self):
        return f'{self.car.brand} {self.car.title} gallery'

    class Meta:
        verbose_name_plural = 'Galleries'


class Video(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='video/%Y/%m/%d')

    def __str__(self):
        return f'{self.car.brand} {self.car.title} videos'
