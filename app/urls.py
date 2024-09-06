from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index_view,blog_view
urlpatterns = [
    path('',index_view,name='home-page'),
    path('blog/',blog_view,name='blog-page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)