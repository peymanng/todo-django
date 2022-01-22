from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='list'),
    path('/update-task/<str:pk>' , views.update_task , name="update-task"),
    path('/delete-task/<str:pk>' , views.delete_task , name="delete")
]
