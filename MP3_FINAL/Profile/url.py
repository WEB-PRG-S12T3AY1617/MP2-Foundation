from django.conf.urls import url
from . import views
app_name = 'profileApp'

urlpatterns = [
	url(r'^(?P<userID>[0-9]+)/$',views.viewProfile, name='viewProfile'),
    url(r'signup/$', views.signUp, name = 'signUp'),
    url(r'^signIn/$', views.signIn, name = 'signIn'),
    url(r'^$', views.signInPage, name = 'signInPage'),
    url(r'justSignedUp/$', views.justSignedUp, name = 'justSignedUp'),
]