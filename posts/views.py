from typing import Any, Dict

from django.shortcuts import render
from django.contrib.auth.views import LoginView

from django.contrib.auth import logout, login

# Create your views here.
from posts.forms import *
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, CreateView, DeleteView
from posts.models import *

# Create your views here.

class Main(ListView):
    paginate_by = 3
    model = Content
    template_name = 'posts/main_page.html'
    context_object_name = 'main'
    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Main'
        context['selected'] = 'Article'
        return context
    def get_queryset(self):
        return Content.objects.all().reverse()


class Categories(ListView):
    model = Category
    template_name = 'posts/categories.html'
    context_object_name = 'category'
    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'categories'
        context['selected'] = 'categories'
        return context
    


    


class Category_posts(ListView):
    model = Category
    template_name = 'posts/category_posts.html'
    context_object_name = 'category_posts'
    
    def get_queryset(self):
        return Category.objects.filter(slug=self.kwargs['category_slug'])[0].content_set.all()


class Show_post(ListView):
    model = Content
    template_name = 'posts/post.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Content.objects.filter(slug=self.kwargs['post_slug'])[0]


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'posts/register.html'
    success_url = reverse_lazy('log_in')
    context_object_name = 'form'
    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Sign up'
        context['selected'] = 'Sign_up'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'posts/login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Log in'
        context['selected'] = 'Log_in'
        return context
    def get_success_url(self):
        return reverse_lazy('main')
    
def add_new_post(request):

    if request.method == 'POST':
        print('hello')
        form = AddNewForm(request.POST, request.FILES)
       
        if form.is_valid():
           
            
            form.save()
            print('hello')
            return redirect('main')
                
            
    else:
        form = AddNewForm()
    return render(request, 'posts/add_new.html', {'title': 'add_new_post', 'selected':'add_new_post', 'form':form})



def logout_user(request):
    logout(request)
    return redirect('log_in')

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Sorry Page Not Found. Please Check and try again</h1>')




    



    

