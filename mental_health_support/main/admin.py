from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Article, Choice, Quiz, Therapist, Question, Consultation, CustomUser, Journal, News, Video, YogaAsana, YogaDetail
from .forms import CustomUserCreationForm, UserProfileForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserProfileForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']


admin.site.register(Article)
admin.site.register(Journal)
admin.site.register(News)
admin.site.register(Video)
admin.site.register(Therapist)
admin.site.register(YogaAsana)
admin.site.register(YogaDetail)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Consultation)
admin.site.register(CustomUser, CustomUserAdmin)
