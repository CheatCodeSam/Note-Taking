from django.urls import path
from .views import detail

urlpatterns = [
    path("<str:shortuuid>/", detail, name="detail"),
]
