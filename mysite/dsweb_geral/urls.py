from django.urls import path
from . import views

app_name = 'dsweb_geral'
urlpatterns = [
    path('', views.index, name='index'),
    path('enquete/<int:question_id>/', views.detail, name='detail'),
    path('enquete/<int:question_id>/results/', views.results, name='results'),
    path('enquete/<int:question_id>/vote/', views.vote, name='vote'),


]