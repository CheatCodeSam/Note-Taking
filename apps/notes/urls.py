from django.urls import path
from .views import index

urlpatterns = [
    path("<str:shortuuid>/", index, name="home"),
]
