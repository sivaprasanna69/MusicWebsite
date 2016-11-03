from django.conf.urls import url
from .import views
app_name='music'
urlpatterns=[


    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^index$', views.IndexView.as_view(), name="index"),
    url(r'^search/$', views.Search.as_view(), name="search"),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album_add'),
    url(r'^songs/$', views.SongView.as_view(), name='songs'),
    url(r'^songs/add/$', views.SongaddView.as_view(), name='songadd'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),

]