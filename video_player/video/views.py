from .models import History, Bookmark
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class HistoryListView(ListView):
    model = History
    template_name = 'video/history.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    ordering = ['-date_watched']


@method_decorator(csrf_exempt, name='dispatch')
class HistoryAddedView(CreateView):
    model = History
    success_url = '/'
    fields = ['history_url']

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'video/bookmarks.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_added']


@method_decorator(csrf_exempt, name='dispatch')
class BookmarkAddedView(CreateView):
    model = Bookmark
    success_url = '/'
    fields = ['bookmark_url']

    def form_valid(self, form):
        return super().form_valid(form)
