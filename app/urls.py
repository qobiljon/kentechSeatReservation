from django.urls import path, include
from django.contrib import admin
from app import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),

	path('', views.index, name='index'),
	path('get_seat', views.get_seat, name='getSeatApi'),
]
