from django.forms import ModelForm
from testapp.models import student

class studentform(ModelForm):
    class Meta:
        model = student
        fields = "__all__"

