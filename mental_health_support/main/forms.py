from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Consultation
from django import forms
from .models import Quiz, Question, Choice

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

from django import forms
from .models import Therapist, Consultation

class BookConsultationForm(forms.ModelForm):
    therapist = forms.ModelChoiceField(queryset=Therapist.objects.all(), label='Select Therapist')

    class Meta:
        model = Consultation
        fields = ['date', 'time', 'therapist']  # Include therapist in the fields list
        widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'time': forms.TimeInput(attrs={'type': 'time'}),
        }



class QuizForm(forms.Form):
    def __init__(self, quiz, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = quiz.questions.all()
        for question in questions:
            choices = question.choices.all()
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[(choice.id, choice.text) for choice in choices],
                widget=forms.RadioSelect,
                required=True
            )


