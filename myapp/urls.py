from django.urls import path
from .views import MyModelListCreateView, MyModelDetailView

urlpatterns = [
    path('mymodel/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
    path('mymodel/<int:pk>/', MyModelDetailView.as_view(), name='mymodel-detail'),
]
