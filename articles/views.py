from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article


class ArticleListView (LoginRequiredMixin,ListView):
    model =  Article
    template_name ='article_list.html'
    login_url ='login'


class ArticleDetailView (LoginRequiredMixin,DetailView):
    model = Article
    template_name ='article_detail.html'
    login_url ='login'


class ArticleUpdateView (LoginRequiredMixin,UpdateView):
    model =  Article
    fields = [ 'title' , 'body' , ]
    template_name ='article_edit.html'
    login_url ='login'

class ArticleDeleteView (LoginRequiredMixin,DeleteView):
    model =  Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy( 'article_list' )
    login_url = 'login'


class ArticleCreateView( CreateView,LoginRequiredMixin): # new
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body') # new
    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
