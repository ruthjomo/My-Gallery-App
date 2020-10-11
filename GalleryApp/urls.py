from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]
urlpatterns=[
    #......
    url('^today/$',views.GalleryApp_of_day,name='GalleryAppToday')
]