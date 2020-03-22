from django.forms import ModelForm
from .models import Track


class AddTrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['track_num', 'name', 'release']
