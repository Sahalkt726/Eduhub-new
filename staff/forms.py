from django import forms
from home . models import *
from . models import *
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_image', 'title', 'description']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message']


class StaffChangeForm(BaseUserChangeForm):
    profile_image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_image']



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']
        widgets = {
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

ChoiceFormSet = forms.inlineformset_factory(Question, Choice, form=ChoiceForm, extra=4)

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['course', 'title', 'file']