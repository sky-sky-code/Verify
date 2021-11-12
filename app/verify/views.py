import os

from config.settings.base import ROOT_DIR
from rest_framework import generics

from app.verify.models import File, Verify
from app.verify.serializers import FileSerializers, AddFileSerializers, FileVerifySerializers
from app.verify.logics.tasks import check_email_task


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializers

class FileVerifyView(generics.ListAPIView):
    queryset = Verify.objects.all()
    serializer_class = FileVerifySerializers

class AddFileView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = AddFileSerializers

    def perform_create(self, serializer):
        serializer.save()
        file_last = File.objects.all()[::-1][0]
        file_path = file_last.upload_file.path
        file_uid = file_last.uid
        check_email_task.delay({'file_path': file_path, 'file_uid': file_uid})