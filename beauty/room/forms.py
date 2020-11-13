
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Feedback
from .models import Master


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class RecordForm(ModelForm):
    class Meta:
        model = Master
        fields = '__all__'


