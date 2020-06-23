from django.urls import path
from .views import list_duvida, create_duvida, update_duvida, delete_duvida

urlpatterns = [
    path('', list_duvida, name='list_duvida'),
    path('new', create_duvida, name='create_duvida'),
    path('update/<int:id>/', update_duvida, name='update_duvida'),
    path('delete/<int:id>/', delete_duvida, name='delete_duvida'),
]