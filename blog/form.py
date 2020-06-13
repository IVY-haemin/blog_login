from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model=Blog
        #fields='__all__'
        fields=['title','body','photo']
    def __int__(self,*args,**kwargs):
        super(PostForm, self),__init__(*args,**kwargs)
        self.fields['photo'].required=False

