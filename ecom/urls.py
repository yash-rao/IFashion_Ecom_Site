from django.urls import path
from . import views

urlpatterns=[
      path('',views.store,name='store'),
      path('cart/',views.cart,name='cart'),
      path('checkout',views.checkout,name='checkout'),
      path('kys/',views.kys,name='kys'),
      path('update_item/',views.updateItem,name='updateItem'),
      
      path('hiw',views.hiw,name='hiw'),
    
#     bodytype templates
      path('triangle',views.triangle,name='triangle'),
      path('invertedtriangle',views.invertedtriangle,name='inverted-triangle'),
      path('rectangle',views.rectangle,name='rectangle'),
      path('apple',views.apple,name='apple'),
      path('hourglass',views.hourglass,name='hourglass'),

      # login 
      path('register', views.registerPage, name='register'),
      path('login',views.loginPage,name='login'),
      path('logout',views.logout,name='logout'),
      path('shop',views.shop,name='shop')

]