from django import forms
from website.models import Emotion
from website.models import AudioSample
import os

#class UploadSampleForm(forms.Form):
#    title = forms.CharField(max_length=50)
#    file = forms.FileField()
#    emotion = forms.ModelMultipleChoiceField(queryset=Emotion.objects.all())

class UploadSampleForm(forms.ModelForm):

    class Meta:
        model = AudioSample
        fields = ('title',
                  'emotion',
                  'audio_file'
                  )

    def clean_audio_file(self):
        file = self.cleaned_data.get('audio_file')
        if file:
            if not os.path.splitext(file.name)[1] in [".mp3", ".wav"]:
                raise forms.ValidationError("Doesn't have proper extension")
            return file
        else:
            raise forms.ValidationError("Couldn't read uploaded file")