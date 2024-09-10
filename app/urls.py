from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index_view,BlogDetailView
urlpatterns = [
    path('',index_view,name='home-page'),
    path('blogs/<slug:slug>/',BlogDetailView.as_view(),name='blogs-page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)