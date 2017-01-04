from django.conf.urls import url

from .views import EntryListView, EntryDetailView, EntryCreateView

urlpatterns = [
    url(r'^entries/$', EntryListView.as_view(), name="bloglist"),
    url(r'^entries/all/$', EntryListView.as_view(), name="bloglist_all"),
    url(r'^entries/all/user/(?P<user_id>[0-9]+)?$', EntryListView.as_view(), name="bloglist_peruser"),
    url(r'^entries/new$', EntryCreateView.as_view(), name="blogcreate"),
    url(r'^entries/(?P<pk>[0-9]+)?', EntryDetailView.as_view(), name="blogdetail"),
]
