from django.urls import path

from . import views

# add this urlpatterns in django.urls root path
app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'), # name= index here index is view name
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote')

]