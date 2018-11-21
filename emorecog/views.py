from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadSampleForm
from django.contrib.auth.decorators import login_required
from website.models import AudioSample


@login_required(login_url='/login/')
def upload_sample(request):
    if request.method == 'POST':
        form = UploadSampleForm(request.POST, request.FILES)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.user = request.user
            sample.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadSampleForm()
    return render(request, 'emorecog/upload_sample.html', {'form': form})

@login_required(login_url='/login/')
def my_samples(request):
    user_samples = AudioSample.objects.filter(user=request.user)
    context = {'user_samples': user_samples}
    return render(request, 'emorecog/my_samples.html', context)