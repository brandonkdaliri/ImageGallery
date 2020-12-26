from django.shortcuts import render, redirect
from .models import Image
from .forms import AddImageForm, EditImageForm

# Create your views here.
def display_images(response):
    if response.user.is_authenticated:
        params = {
            'Images': response.user.image_set.all(),
            'gallery_status': 'active'
        }
        return render(response, 'main/gallery.html', params)
    else:
        return render(response, 'main/home.html')

def add_image(response):
    params = {
        'form': AddImageForm(),
        'add_status': 'active',
    }
    if response.user.is_authenticated:
        if response.method == 'POST':
            form = AddImageForm(response.POST, response.FILES)
            if form.is_valid():
                image_title = form.cleaned_data.get('image_title')
                image_desc = form.cleaned_data.get('image_desc')
                image = form.cleaned_data.get('image')
                response.user.image_set.create(image_title=image_title, image_desc=image_desc, image=image)
                return redirect('/')
            else:
                print(form.errors)
        else:
            params['form'] = AddImageForm()
        return render(response, 'main/add.html', params)
    else:
        return redirect('/')
    
def edit_image(response, image_id):
    params = {
        'image': response.user.image_set.get(id=image_id)
    }
    if response.user.is_authenticated:
        instance = response.user.image_set.get(id=image_id)
        form = EditImageForm(response.POST)
        if response.method == 'POST':
            if form.is_valid():
                form = EditImageForm(response.POST, instance=instance)
                form.save()
                return redirect('/')
            else:
                print(form.errors)
        else:
            params['form'] = EditImageForm(instance=instance)
        return render(response, "main/edit.html", params)
    else:
        return redirect('/')
    
def delete_image(response, image_id):
    if response.user.is_authenticated and response.method == "POST":
        # Image.objects.filter(id=image_id).delete()
        instance = response.user.image_set.get(id=image_id)
        instance.image.delete(False)
        instance.delete()
        
    return redirect('/')