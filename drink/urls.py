from django.urls import path
from . import views

urlpatterns = [
    path('logins/', views.logins,name='login'),
    path('signup/', views.signup, name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.activate, name='activate'),

]
