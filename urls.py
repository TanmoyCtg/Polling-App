from django.urls import path

from . import views

# add this urlpatterns in django.urls root path
urlpatterns = [
	path('', views.index, name='index'), # name= index here index is view name
]