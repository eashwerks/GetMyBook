"""getmybook URL Configuration

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
from myapp import views
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/',views.home_view, name='home'),
    url(r'^signup/',views.signup_view, name='signup'),
    url(r'^login/',views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^user/', views.user_view, name='user'),
    url(r'^userbooks/', views.userbooks_view, name='userbooks'),
    url(r'^books/', views.BookListView.as_view(), name='books'),
    url(r'^book/(\d+)/', views.book_detail_view, name='book-detail'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
