from django.urls import path

from app.verify.views import FileListView, AddFileView, FileVerifyView

urlpatterns = [
    path('api/email/', FileListView.as_view()),
    path('api/email/verify', FileVerifyView.as_view()),
    path('api/email/add/', AddFileView.as_view())
]