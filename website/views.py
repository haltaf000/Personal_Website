from audioop import reverse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm, ProjectForm, SkillForm, PostForm
from website.models import Project, Skills, Post
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def home(request): 
    return render(request, "website/home.html", {})
    
def about(request):
    return render(request, "website/about.html", {})

def success(request):
    return render(request, "website/success.html", {})

def resume_page(request):
    return render(request, "website/resume.html", {})

def about(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        send_mail(subject, message, email, ['haideraltaf00@outlook.com'],)
        return redirect('success')
    else:
        return render(request, 'website/about.html', {})


# Blog
class HomeView(ListView):
    model = Post
    template_name = 'website/writings.html'
    ordering = ['-date']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'website/article_details.html' 
   
class AddPostView(CreateView):
    model = Post
    form_class: PostForm
    template_name = 'website/post.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'website/post.html'
    fields = ['title', 'description', 'body', 'date']

    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'website/delete_post.html'
    success_url = reverse_lazy('writings')

 
# Project    
    
class ProjectView(ListView):
    model = Project
    template_name = 'website/portfolio.html'
    ordering = ['-id']
        
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'website/Project_details.html'
    
class AddProjectView(CreateView):
    model = Project
    form_class: ProjectForm
    template_name = 'website/project.html'
    fields = '__all__'

class UpdateProjectView(UpdateView):
    model = Project
    form_class: ProjectForm
    template_name = 'website/project.html'
    fields = ['title', 'description', 'url']
    
class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'website/delete_project.html'
    success_url = reverse_lazy('portfolio')
    
# Tech SKills

class TechView(ListView):
    model = Skills
    template_name = 'website/tech.html'
        
class TechDetailView(DetailView):
    model = Skills
    template_name = 'website/skills_details.html'
    
class AddTechView(CreateView):
    model = Skills
    form_class: SkillForm
    template_name = 'website/skill.html'
    fields = '__all__'

class UpdateTechView(UpdateView):
    model = Skills
    form_class: SkillForm
    template_name = 'website/skill.html'
    fields = ['title', 'body']
    
class DeleteTechView(DeleteView):
    model = Skills
    template_name = 'website/delete_skill.html'
    success_url = reverse_lazy('tech')