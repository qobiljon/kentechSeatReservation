from django.urls import path, include
from django.contrib import admin
from app import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),

	path('', views.redirect_to_student, name='index'),
	path('student', views.index, name='student'),
	path('professor', views.index, name='professor'),

	path('get_professor_seat', views.get_professor_seat, name='getProfessorSeatApi'),
	path('get_student_seat', views.get_student_seat, name='getStudentSeatApi'),
]
