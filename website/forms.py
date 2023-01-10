from django import forms
from .models import Project, Skills, Post
# Create your forms here.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "description")
        
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.TextInput(attrs={'class': 'form-control'}),
    }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'url', 'github')
        
    widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control'}),
		'description': forms.TextInput(attrs={'class': 'form-control'}),
		'url': forms.URLInput(attrs={'class': 'form-control'}),
		'github': forms.URLInput(attrs={'class': 'form-control'})
	}
    
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('title', 'body')
        
    widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control'}),
		'body': forms.TextInput(attrs={'class': 'form-control'}),
	}
        

class ContactForm(forms.Form):
	full_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)