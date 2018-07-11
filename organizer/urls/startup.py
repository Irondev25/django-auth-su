from django.conf.urls import url
from organizer.views import StartupList, StartupCreate, StartupDetail, StartupUpdate, StartupDelete
from organizer.views import NewslinkCreate, NewslinkDelete, NewslinkUpdate

app_name = 'organizer_startup'


urlpatterns = [
    url(r'^$', StartupList.as_view(), name='list'),
    url(r'^create/$', StartupCreate.as_view(), name='create'),
    url(r'^(?P<slug>[\w\-]+)/$', StartupDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(), name='delete'),
    url(r'^(?P<startup_slug>[\w\-]+)/add_article_link/$', NewslinkCreate.as_view(), name='newslink_create'),
    url(r'^(?P<startup_slug>[\w\-]+)/(?P<newslink_slug>[\w\-]+)/delete/$', NewslinkDelete.as_view(), name='newslink_delete'),
    url(r'^(?P<startup_slug>[\w\-]+)/(?P<newslink_slug>[\w\-]+)/update/$', NewslinkUpdate.as_view(), name='newslink_update'),
]
