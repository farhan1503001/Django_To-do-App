from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('delete/<id>',views.delete,name='delete'),
    path('change/<id>',views.change_status,name='changed'),
    path('edit/<id>',views.edit,name='edit')
]