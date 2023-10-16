from django.contrib import admin
from django.urls import path, include, url
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static

#sitemaps = {'posts': PostSiteMap}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('kontakt/', include('contact.urls', namespace='contact')),
   # path('sitemap.xml', sitemap, { 'sitemaps' : sitemaps },
   #     name="django.contrib.sitemaps.views.sitemap",),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
