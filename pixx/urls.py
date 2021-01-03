from django.urls import path,include
from . import views

urlpatterns = [

        path('',views.IndexView.as_view(),name='index'),
        path('gallery/',views.Gall.as_view(),name = 'gall'),
        path('blog/',views.Blog.as_view(),name = 'blog'),
        path('contact/',views.Contact.as_view(),name = 'contact'),
        path('single/',views.Single.as_view(),name = 'single'),
        path('myworks/',views.Works.as_view(),name = 'works'),

        ]
