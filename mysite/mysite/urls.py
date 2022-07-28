from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dsweb_geral.urls')),
    path('', include('plataforma.urls')),
]






'''

from django.contrib import admin
from django.urls import path
from dsweb_atividade1.views import home
from dsweb_geral.views import index, detail, results, vote


urlpatterns = [
    path('admin/', admin.site.urls),
    path('atividade1/', home, name='atividade1'),
    path('', index, name='index'),
    path('enquete/<int:question_id>/', detail, name='detail'),
    path('enquete/<int:question_id>/results/', results, name='results'),
    path('enquete/<int:question_id>/vote/', vote, name='vote'),


]
'''