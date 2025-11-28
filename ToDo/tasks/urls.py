from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('add_task', views.add_task, name='add_task'),
    path('update_task/<int:pk>/', views.update_task, name='update_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),  
    path('trash', views.trash, name='trash'),
    path('restore_task/<int:pk>/', views.restore_task, name='restore_task'),
    path('permanent_delete/<int:pk>/', views.permanent_delete, name='permanent_delete'),
    path('restore_all', views.restore_all, name='restore_all'),
    path('permanent_delete_all', views.permanent_delete_all, name='permanent_delete_all')
]