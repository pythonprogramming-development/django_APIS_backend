from django.shortcuts import render
from .models import History, Bookmark
from django.views.generic import ListView, CreateView

def welcome(request):
    text = 'Hello World'
    return render(request, 'video/welcome.html',{'text' : text})

class HistoryListView(ListView):
    model = History
    template_name = 'video/history.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    ordering = ['-date_watched']

class HistoryAddedView(CreateView):
    model = History
    success_url = '/'
    fields = ['history_url']

    def form_valid(self, form):
        return super().form_valid(form)

class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'video/bookmarks.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_added']


class BookmarkAddedView(CreateView):
    model = Bookmark
    success_url = '/'
    fields = ['bookmark_url']

    def form_valid(self, form):
        return super().form_valid(form)

