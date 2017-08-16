from django.conf.urls import url
from . import views
app_name = 'postApp'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^home$',views.home, name='home'),
    url(r'^fItems/(?P<tagWord>.+)/$',views.searchItem, name='searchItem'),
    url(r'^searchItems/$',views.searchBoxItem, name='searchBoxItem'),
	url(r'^listItem/$',views.listItem, name='listItem'),
	url(r'^(?P<page_num>[0-9]+)/(?P<start_num>[0-9]+)/$',views.viewPage, name='viewPage'),
    url(r'^(?P<itemNo>[0-9]+)$',views.details, name='details'),
    url(r'^addPost/$',views.addPost, name='addPost'),
    url(r'^addingPost/$',views.addingPost, name='addingPost'),
    url(r'^fItems/$',views.searchItem, name='searchItem'),
    url(r'^addingOffer$',views.addingOffer, name='addingOffer'),
    url(r'^updatingOffer$',views.updatingOffer, name='updatingOffer'),
    url(r'^cancellingOffer$',views.cancellingOffer, name='cancellingOffer'),
    url(r'^acceptOffer$',views.acceptOffer, name='acceptOffer'),
    url(r'^rejectOffer$',views.rejectOffer, name='rejectOffer'),
    url(r'^rejectOffer1$',views.rejectOffer1, name='rejectOffer1'),
    url(r'^acceptOffer1$',views.acceptOffer1, name='acceptOffer1'),
    url(r'^itemOccupation/(?P<tagOccupation>[0-9]+)/$',views.searchByOccupation, name='searchByOccupation'),
    url(r'^itemCondition/(?P<tagCondition>[0-9]+)/$',views.searchByCondition, name='searchByCondition'),
]
