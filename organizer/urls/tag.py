from django.conf.urls import url
from organizer.views import TagList, TagCreate, TagDetail, TagUpdate, TagDelete

app_name = 'organizer_tag'

urlpatterns = [
    url(r'^$', TagList.as_view(), name='list'),
    url(r'^create/$', TagCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', TagDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', TagUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', TagDelete.as_view(), name='delete'),
]
    