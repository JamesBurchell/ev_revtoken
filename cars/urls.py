from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /car/5/
    path('<int:car_id>/', views.detail, name='detail'),
    # ex: /car/5/results/
    path('<int:car_id>/results/', views.results, name='results'),
    # ex: /car/5/vote/
    path('<int:car_id>/vote/', views.vote, name='vote'),
]