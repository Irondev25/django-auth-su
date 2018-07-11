from django.conf.urls import url
from .views import PostDetail, PostList, PostCreate, PostUpdate, PostDelete, PostArchiveYear, PostArchiveMonth

app_name = 'blog'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/$', PostArchiveYear.as_view(), name='post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostArchiveMonth.as_view(), name='post_archive_month'),
    url(r'^create/$', PostCreate.as_view(), name='post_create'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$', PostUpdate.as_view(), name='post_update'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$', PostDelete.as_view(), name='post_delete'),
]
