from django.urls import path, include
from .views import *
from rest_framework import routers

#CONFIGURAMOS LAS URLS PARA LA API
router = routers.DefaultRouter()
router.register('mecanicos', MecanicoViewSet)
router.register('tipomecanicos', TipoMecanicoViewSet)
router.register('generos', GeneroViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('aboutus/', aboutus, name="aboutus"),
    path('contact/', contact, name="contact"),
    path('services/', services, name="services"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('register/', register, name="register"),
    path('administrador/', administrador, name="administrador"),
    path('mecanicos/', mecanicos, name="mecanicos"),
    path('mecanicos/add/', mecanicosadd, name="mecanicosadd"),
    path('mecanicos/update/<id>/', mecanicosupdate, name="mecanicosupdate"),
    path('mecanicos/delete/<id>/', mecanicosdelete, name="mecanicosdelete"),
    path('account_locked/', account_locked, name="account_locked"),
    #CONFIGURACIÓN DE LA API
    path('api/', include(router.urls)),
    path('mecanicosapi/', mecanicosapi, name="mecanicosapi"),
    path('mecanicodetalle/<id>/', mecanicodetalle, name="mecanicodetalle"),
]