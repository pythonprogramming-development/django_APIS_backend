from django.urls import path
from .views import HistoryAddedView, history_list, BookmarkAddedView, bookmark_list

urlpatterns = [
    path('', HistoryAddedView.as_view(), name='history-add'),
    path('history/list/', history_list, name='history-list'),
    path('bookmark/list/', bookmark_list, name='bookmark-list'),
    path('bookmark/add/', BookmarkAddedView.as_view(), name='bookmark-add'),
]