from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, authenticate
from django.contrib.auth.decorators import login_required

from .models import Tab, Article, Emotion, AudioSample, ArticleImage


class IndexView(generic.ListView):
    template_name = 'website/index.html'
    context_object_name = 'tab_list'

    def get_queryset(self):
        return Tab.objects.all()


class ProjectsOverview(generic.DetailView):
    model = Tab
    template_name = 'website/projects_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.tab_id = get_object_or_404(Tab, id=self.kwargs['pk'])
        context['article_list'] = Article.objects.filter(tab=self.tab_id)
        return context


class TabDetail(generic.DetailView):
    model = Tab
    template_name = 'website/skills.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.tab_id = get_object_or_404(Tab, id=self.kwargs['pk'])
        context['article_list'] = Article.objects.filter(tab=self.tab_id)
        return context


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'website/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.article_id = get_object_or_404(Article, id=self.kwargs['pk'])
        context['images'] = ArticleImage.objects.filter(article=self.article_id)
        return context

@login_required(login_url='/login/')
def chose_sample(request):
    emotions = Emotion.objects.all()

    if request.method == 'POST' and request.FILES['chosen_sample']:
        audio_sample = request.FILES['chosen_sample']
        fs = FileSystemStorage()
        filename = fs.save(audio_sample.name, audio_sample)
        uploaded_file_url = fs.url(filename)
        return render(request, 'website/upload_sample.html', {
            'emotions': emotions,
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'website/upload_sample.html', {
        'emotions': emotions
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)