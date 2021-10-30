from django.urls import path
from .views import *

urlpatterns = [
    # http::/127.0.0.1/bookmark/
    #                    .as_view() | 클래스형 뷰를 함수형 뷰처럼 동작하게해줌
    path('', BookmarkListView.as_view(), name='list'),
    #  2nd url       View               template name
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    # int:pk  =  (primary key) 북마크의 글번호!, 슬러그 형태 (함수이름같이 만든거 how to press)
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),

]