from django.urls import path
from .views import LocationList, LocationDetail

urlpatterns = [
    path('', LocationList.as_view()),
    path('<int:pk>/', LocationDetail.as_view()),
]