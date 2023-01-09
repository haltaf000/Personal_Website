from django.urls import path 
from . import views
from .views import HomeView, PostDetailView, UpdatePostView, AddPostView, DeletePostView, AddTechView, DeleteTechView,  ProjectView, TechDetailView, TechView, AddProjectView, UpdateProjectView, DeleteProjectView, ProjectDetailView, UpdateTechView

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'), 
    path('porfolio', ProjectView.as_view(), name='portfolio'),
    path('tech', TechView.as_view(), name='tech'),
    path('success',views.success, name='success'),
    path('writings', HomeView.as_view(), name='writings'),
    
    path("projects/<int:pk>", ProjectDetailView.as_view(), name='Project_details'),
    path('project/', AddProjectView.as_view(), name='project'),
    path('projects/edit/<int:pk>', UpdateProjectView.as_view(), name="update_project"),
    path('projects/<int:pk>/remove', DeleteProjectView.as_view(), name="delete_project"),
    
    path("skills/<int:pk>", TechDetailView.as_view(), name='skill_details'),
    path('skill/', AddTechView.as_view(), name='skill'),
    path('skills/edit/<int:pk>', UpdateTechView.as_view(), name="update_skill"),
    path('skills/<int:pk>/remove', DeleteTechView.as_view(), name="delete_skill"),
    
    path("posts/<int:pk>", PostDetailView.as_view(), name='article_details'),
    path('post/', AddPostView.as_view(), name='post'),
    path('posts/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('posts/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    
    
]