import logging
from venv import logger
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import BookConsultationForm, CustomUserCreationForm, QuizForm, UserProfileForm
from .models import Article, Choice, Quiz, Therapist, Therapist, Consultation, YogaAsana, YogaDetail
from django.contrib.auth.decorators import login_required
from .forms import ConsultationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'main/profile.html', {'form': form})

from .models import Article, Journal, News, Video

def article_list(request):
    articles = Article.objects.all()
    journals = Journal.objects.all()
    news_list = News.objects.all()
    videos = Video.objects.all()
    context = {
        'articles': articles,
        'journals': journals,
        'news_list': news_list,
        'videos': videos,
    }
    return render(request, 'main/article_list.html', context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'main/article_detail.html', context)


def therapist_list(request):
    therapists = Therapist.objects.all()
    return render(request, 'main/therapist_list.html', {'therapists': therapists})

def therapist_detail(request, pk):
    therapist = Therapist.objects.get(pk=pk)
    return render(request, 'main/therapist_detail.html', {'therapist': therapist})

def yoga_list(request):
    yoga_asanas = YogaAsana.objects.all()
    return render(request, 'main/yoga_list.html', {'yoga_asanas': yoga_asanas})

def yoga_detail(request, pk):
    yoga_asana = get_object_or_404(YogaAsana, pk=pk)
    yoga_detail = get_object_or_404(YogaDetail, asana=yoga_asana)
    return render(request, 'main/yoga_detail.html', {'yoga_asana': yoga_asana, 'yoga_detail': yoga_detail})


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'main/quiz_list.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        form = QuizForm(quiz, request.POST)
        if form.is_valid():
            total_score = 0
            for question in questions:
                selected_choice_id = form.cleaned_data.get(f'question_{question.id}')
                selected_choice = Choice.objects.get(id=selected_choice_id)
                total_score += selected_choice.score
            result = evaluate_result(total_score)
            return render(request, 'main/quiz_result.html', {'quiz': quiz, 'score': total_score, 'result': result})
    else:
        form = QuizForm(quiz)

    return render(request, 'main/take_quiz.html', {'quiz': quiz, 'form': form})

def evaluate_result(total_score):
    if total_score < 5:
        return "No indication of the problem"
    elif total_score < 10:
        return "Mild indication of the problem"
    else:
        return "Strong indication of the problem"


@login_required
def consultation_list(request):
    consultations = Consultation.objects.filter(user=request.user)
    return render(request, 'main/consultation_list.html', {'consultations': consultations})

@login_required
def book_consultation(request, therapist_id):
    if request.method == 'POST':
        form = BookConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()
            return redirect('consultation_list')
    else:
        form = BookConsultationForm()

    return render(request, 'main/book_consultation.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')  # Replace with the desired redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# @require_POST
# def logout_view(request):
#     logout(request)
#     return redirect('index')

def custom_logout(request):
    logout(request)
    return redirect('index')