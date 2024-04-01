from django.core.validators import URLValidator
from django.core.files.base import ContentFile
from .models import document

from rest_framework import serializers

from urllib.request import urlretrieve

class FileUrlField(serializers.FileField):
    def to_internal_value(self, data):
        try:
            URLValidator()(data)
        except ValidationError as e:
            raise ValidationError('Invalid Url')

        # download the contents from the URL
        file, http_message = urlretrieve(data)
        file = File(open(file, 'rb'))
        return super(FileUrlField, self).to_internal_value(ContentFile(file.read(), name=file.name))


class FileSerializer(serializers.ModelSerializer):
    doc = FileUrlField()
    class Meta:
        model = document
        fields = '__all__'