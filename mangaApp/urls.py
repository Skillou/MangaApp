from django.conf.urls.static import static
from django.urls import path
from mangaApp import views
from mangaProjet import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('series/', views.series_list, name='series_list'),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    # path('tome/', views.tome_list, name='tome_list'),
    path('series/<int:series_id>/tomes/', views.tome_list, name='tome_list'),
    path('tome/<int:tome_id>/', views.tome_detail, name='tome_detail'),
    path('chapter/', views.chapter_list, name='chapter_list'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
