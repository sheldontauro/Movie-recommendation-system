"""hostelmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from finder import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^genre/(?P<home_action>.*)/$', views.homeaction, name = "homeaction"),
    url(r'^directors/(?P<direc_action>.*)/$', views.direcaction, name = "direcaction"),
    url(r'^directors/$', views.directors, name = "directors"),
    url(r'^home/', views.home, name = "home"),
    url(r'^success/', views.success, name = "success"),
    url(r'^$',auth_views.login,{'template_name': 'finder/login.html'},name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/',views.index,name="index"),
    url(r'^about/',views.about,name="about"),
    url(r'^error/',views.error,name="error"),
    url(r'^search/', views.search, name = "search"),
    url(r'^movie/(?P<movie_prof>.*)/$' , views.movieprof , name = 'movieprof'),
    url(r'^movie/(?P<movie_prof>.*)/((?P<movie_rate>[0-9]+))$' , views.movierate , name = 'movierate'),
    url(r'^profile/(?P<cust_prof>.*)/$' , views.custprof , name = 'custprof'),

    #url(r'^details/$',views.details,name="details"),
]
