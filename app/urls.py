from django.urls import path
from . import views

urlpatterns = [

    path("taom/", views.StudentListView.as_view(), name='user_list'),
    path('taom/create', views.StudentCreateView.as_view(), name='user_create'),
    path('taom/<slug:slug>/', views.StudentDetailView.as_view(), name='user_detail'),
    path('taom/<slug:slug>/edit/', views.StudentUpdateView.as_view(), name='user_edit'),
    path('taom/<slug:slug>/delete/', views.StudentDeleteView.as_view(), name='user_delete')

]