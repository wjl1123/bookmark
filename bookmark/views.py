from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List Page:

# 클래스형 뷰,                 함수형 뷰
# = 제네릭 뷰                  = 커스터마이징뷰

# 웹페이즈에 접속 -> 페이지를 본다..
# URL을 입력 -> 웹서버가 뷰를 찾아서 동작시킨다.. -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark  # need Model attr


class BookmarkCreateView(CreateView): # create / update 뷰들은 어떤 내용을 수정할 건지 알려주는 field가 필요하다
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    #template_name_suffix = '_update'