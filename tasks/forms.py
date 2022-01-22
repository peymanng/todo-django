from django.forms import ModelForm, fields
from .models import Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'add-box',
        'placeholder' : 'Enter Your Task...',
        })
        self.fields['complete'].widget.attrs.update({'class' : 'complete-box'})
    