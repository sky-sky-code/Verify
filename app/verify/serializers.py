from rest_framework import serializers
from app.verify.models import File, Verify

class VerifySerializers(serializers.ModelSerializer):
    class Meta:
        model = Verify
        fields = ("__all__", )


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("uid", "name", "upload_file", "created", 'modified')


class FileVerifySerializers(serializers.ModelSerializer):
    file = FileSerializers()

    class Meta:
        model = Verify
        fields = ("file", "email", "result_code")

class AddFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('name', "upload_file", )