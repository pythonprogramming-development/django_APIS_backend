from django.urls import path
from .views import HistoryListView, HistoryAddedView, BookmarkAddedView, BookmarkListView

urlpatterns = [
    path('', HistoryAddedView.as_view(), name='history-add'),
    path('history/list/', HistoryListView.as_view(), name='history-list'),
    path('bookmark/list/', BookmarkListView.as_view(), name='bookmark-list'),
    path('bookmark/add/', BookmarkAddedView.as_view(), name='bookmark-add'),
]