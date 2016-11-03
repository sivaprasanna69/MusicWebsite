from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from .models import Album,Song
from django.views.generic import View
from .forms import UserForm, LoginForm


class HomeView(generic.TemplateView):
    template_name = 'music/home.html'


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class SongView(generic.ListView):
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()

class SongaddView(CreateView,):
    template_name = 'music/addsong.html'
    model=Song
    fields=['song_title','file_type','is_favorite','album']
    def get_success_url(self):
        return '/music/index'


class ContactView(generic.TemplateView):
    template_name='music/contact.html'


class LogoutView(generic.TemplateView):
    template_name = 'music/logout.html'


class DetailView(generic.DetailView):
    model=Album
    template_name='music/detail.html'

class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class UserFormView(View):
    form_class= UserForm
    template_name='music/registration_form.html'

    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)


        if form.is_valid():
            user=form.save(commit=False)


            #cleaned (normalised data)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('music:index')
        return render(request,self.template_name,{'form':form})

class LoginView(View):
    form_class= LoginForm
    template_name='music/registration_form.html'

    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('music:index')
        return render(request,self.template_name,{'form':form})

class Search(generic.ListView):
    model = Album
    template_name = 'music/search.html'
    context_object_name = 'search_list'

    def get_queryset(self):
        print self.request.GET
        query = self.request.GET["q"]
        return self.model.objects.filter(album_title__icontains=query)



