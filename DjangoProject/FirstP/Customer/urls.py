from django.urls import path
from Customer.views import index_c
urlpatterns = [
    path('index_c', index_c),
]