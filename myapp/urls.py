from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('del_qrcode/', views.del_qrcode, name='del_qrcode'),
]
