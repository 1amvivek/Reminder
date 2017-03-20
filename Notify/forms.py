from django import forms

from .models import Task, TaskList


class AddTaskList(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'placeholder': 'Task Card Name'
            })


ACCEPTABLE_FORMATS = ['%m/%d/%y %H:%M', ]


class AddTask(forms.ModelForm):
    reminder = forms.DateField(input_formats=ACCEPTABLE_FORMATS)
    reminder = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dd/mm/yy', 'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = ('summary', 'description','created','reminder', 'TL',)


class FeedbackForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Id'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'enter your feedback comments here'})
    )



