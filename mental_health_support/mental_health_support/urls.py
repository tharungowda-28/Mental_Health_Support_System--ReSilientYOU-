# urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('therapists/', views.therapist_list, name='therapist_list'),
    path('therapists/<int:pk>/', views.therapist_detail, name='therapist_detail'),
    path('mind_care/', views.yoga_list, name='yoga_list'),
    path('mind_care/<int:pk>/', views.yoga_detail, name='yoga_detail'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('book_consultation/<int:therapist_id>/', views.book_consultation, name='book_consultation'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)