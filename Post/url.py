from django.conf.urls import url
from . import views
app_name = 'postApp'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^home$',views.home, name='home'),
    url(r'^fItems/(?P<tagWord>.+)/$',views.searchItem, name='searchItem'),
    url(r'^searchItems/$',views.searchBoxItem, name='searchBoxItem'),
	url(r'^listItem/$',views.listItem, name='listItem'),
	url(r'^(?P<page_num>[0-9]+)/$',views.viewPage, name='viewPage'),
    url(r'^(?P<itemNo>[0-9]+)$',views.details, name='details'),
    url(r'^addPost/$',views.addPost, name='addPost'),
    url(r'^addingPost/$',views.addingPost, name='addingPost'),
    url(r'^fItems/$',views.searchItem, name='searchItem'),
]
