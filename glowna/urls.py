from django.urls import path
from . import views

urlpatterns = [    
    path('import/', views.importExcel, name='push_excel'),
    path("", views.home, name="home"),
    path('graf/', views.graf, name='graf')
    
]