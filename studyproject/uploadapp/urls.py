from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.fileupload, name="upload"),
    path("uploadmulti/", views.fileuploadmulti, name="uploadmulti")
]