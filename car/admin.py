from django.contrib import admin
from .models import Car, PositionCategory, Attribute_Category, Attribute, Car_Model_Type, Colored_Image, \
    Image_for_Car_PositionCategory, \
    Position, Appearance_Image, Gallery, Video, Interior_Image, Interior_Detail, Appearance_Detail

admin.site.register(Car)
admin.site.register(PositionCategory)
admin.site.register(Attribute_Category)
admin.site.register(Attribute)
admin.site.register(Car_Model_Type)
admin.site.register(Colored_Image)
admin.site.register(Image_for_Car_PositionCategory)
admin.site.register(Position)
admin.site.register(Appearance_Image)
admin.site.register(Appearance_Detail)
admin.site.register(Interior_Image)
admin.site.register(Interior_Detail)
admin.site.register(Gallery)
admin.site.register(Video)
