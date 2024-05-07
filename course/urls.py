from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('category/',views.SubjectDetailView.as_view()),
    path('course/<int:id>/',views.CourseDetailView.as_view()),
    path('course_c/',views.CourseListView.as_view()),
    path('course_c/<int:id>/',views.CourseDetailView.as_view()),
    # path('<int:id>/', views.id),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
