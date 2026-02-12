
from django.contrib import admin
from django.urls import path,re_path,include
from hello import views
news_patterns=[ path("",views.news) , path("concreate",views.concreate),path("info",views.info)]


urlpatterns = [
    path('', views.home),
    path('user/', views.user),
    path('news/', views.news),  # Убрали / в начале
    path('news/<int:id>/info/', views.info),
    path('news/<int:id>/concreate/', views.concreate), # Убрали / в начале
]





#product_patterns=[ path("",views.products) , path("price",views.price),path("info",views.info)]

















#path (route , view ,kwargs=None,name = None)
#re_path(route , view ,kwargs=None,name = None)
# path('product/<int:id>/', views.product_view),
    #re_path(r'^data/(?P<data>\w+)/$', views.dynamic_view),
    #re_path(r'^user/(?P<name>\w+)/$', views.user_view),
    #path('about/', views.about_view, name='about'),
    #path('', views.index_view, name='index'),
    #re_path(r'^user/(?P<username>\w+)/order/(?P<order_id>\d+)/$', views.user_order_view),


