from django.forms import ModelForm
from .models import Post, Email

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('date',)

class EmailForm(ModelForm):
	class Meta:
		model = Email
		exclude = ('id',)

#widget=forms.TextInput(attrs={'placeholder': 'Search'}))