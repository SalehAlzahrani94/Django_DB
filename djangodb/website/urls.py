from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('join', views.join, name="join"),
    path('publisher', views.Publisher, name="publisher"),
    path('movie_list', views.MoviesList, name="movie_list"),
    path('forms/<int:pk>/', views.Member_edit, name="Member_edit"),
    path('forms/new', views.Member_edit, name="Member_create"),
    path('add', views.add, name="add"),
    path('update', views.update, name="update"),
    path('update/<int:pk>/', views.update, name="update_pk"),
 
]
