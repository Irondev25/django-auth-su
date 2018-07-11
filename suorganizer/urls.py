"""suorganizer URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.conf.urls.static import static

from contact import urls as contact_urls
from organizer.urls import startup as startup_urls
from organizer.urls import tag as tag_urls
from user import urls as user_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(
        pattern_name='blog:post_list'
    ), name='homepage'),
    url(r'^blog/', include('blog.urls')),
    url(r'^startup/', include(startup_urls)),
    url(r'^tag/', include(tag_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^about/$', TemplateView.as_view(
        template_name='site/about.html'), name='about'),
    url(r'^user/', include(user_urls)),
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

