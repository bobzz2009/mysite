from django.urls import path,include
from . import views

urlpatterns = [

        path('',views.IndexView.as_view(),name='index'),
        path('gallery/',views.Gall.as_view(),name = 'gall'),
        path('blog/',views.Blog.as_view(),name = 'blog'),
        path('contact/',views.Contact.as_view(),name = 'contact'),
        path('single/',views.Single.as_view(),name = 'single'),
        path('myworks/',views.Works.as_view(),name = 'works'),
        path('account/profile/',views.Profile.as_view(),name = 'profile'),
        #path('signview/',views.SignupView.as_view(),name = 'signview'),
        path('login/',views.LoginView.as_view(),name='login'),
        path('logout-r/',views.LogoutView.as_view(),name='logout-r'),

        ]
