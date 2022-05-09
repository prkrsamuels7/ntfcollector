from django.urls import path
from . import views

urlpatterns = [
  #      PATH | Mapped View | Route Name
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('nfts/', views.nfts_index, name='index'),
]