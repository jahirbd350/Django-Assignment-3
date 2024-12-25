from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_task, name="add_task"),
    path('edit/<int:id>', views.edit_task, name="edit_task"),
    path('del/<int:id>', views.del_task, name="del_task"),
]
