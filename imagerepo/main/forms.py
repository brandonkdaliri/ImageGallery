from django import forms
from .models import Image

class AddImageForm(forms.Form):
    image_title = forms.CharField(label='Image Title', max_length=100)
    image_desc = forms.CharField(label='Image Description', required=False, max_length=500)
    image = forms.ImageField(label='Image')
    
class EditImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditImageForm, self).__init__(*args, **kwargs)
        self.fields['image_title'].label = 'Image Title'
        self.fields['image_desc'].label = 'Image Description'
        
    class Meta:
        model = Image
        fields = [
            'image_title',
            'image_desc'
        ]