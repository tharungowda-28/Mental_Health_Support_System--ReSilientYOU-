from django.urls import path
from .views import article_detail, article_list, book_consultation, consultation_list, forum_detail, forum_list, quiz_list, register, profile, support_group_detail, support_group_list, take_quiz, therapist_detail, therapist_list

# urlpatterns = [
#     path('register/', register, name='register'),
#     path('profile/', profile, name='profile'),
#     path('articles/', article_list, name='article_list'),
#     path('articles/<int:pk>/', article_detail, name='article_detail'),
#     path('therapists/', therapist_list, name='therapist_list'),
#     path('therapists/<int:pk>/', therapist_detail, name='therapist_detail'),
#     path('support_groups/', support_group_list, name='support_group_list'),
#     path('support_groups/<int:pk>/', support_group_detail, name='support_group_detail'),
#     path('forums/', forum_list, name='forum_list'),
#     path('forums/<int:pk>/', forum_detail, name='forum_detail'),
#     path('quizzes/', quiz_list, name='quiz_list'),
#     path('quizzes/<int:quiz_id>/', take_quiz, name='take_quiz'),
#     path('consultations/', consultation_list, name='consultation_list'),
#     path('book_consultation/<int:therapist_id>/', book_consultation, name='book_consultation'),
# ]
