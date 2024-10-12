from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/',views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_view, name='logout'),
]
