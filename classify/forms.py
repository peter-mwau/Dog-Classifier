# import forms
from django import forms
from .models import Dog



class ImageUploadForm(forms.ModelForm):
    """Image upload form."""
    class Meta:
        # image = forms.ImageField()
        model = Dog
        fields = '__all__'
      



