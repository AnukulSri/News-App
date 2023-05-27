from django.urls import path
from . import views
urlpatterns = [
   path('',views.index),
   path('apple',views.apple),
   path('sport',views.sport),
   path('electronics',views.electronics),
   path('bolly',views.bolly)
]