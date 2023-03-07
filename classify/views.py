from django.shortcuts import render, redirect
# import requests, json, urllib
from django import forms
from .forms import  ImageUploadForm
from .models import Dog
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image
from io import BytesIO


import json, urllib, requests

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        # img_url = ''
        if form.is_valid():
            #get image url
            img_object = form.instance
            # 'ImageUploadForm' object has no attribute 'cleaned_data'

            # print(img_object)
            img_url =img_object.image.url
            encoded_image = base64.b64encode(img_object.image.read())

        
            response = requests.post("https://nothinglabs-minima.hf.space/run/predict", json={
	        "data": [
                "data:image/jpg;base64," + encoded_image.decode('utf-8'),
                
	        ]
            }).json()
            # print(response)

            dog = response["data"]
            #convert dictionary to string
            dog = json.dumps(dog)
            #convert string to dictionary
            dog = json.loads(dog)
            # print(dog)
            name = dog[0]['label']
            print(name)
            
            response = requests.post("https://elitecode-captioner.hf.space/run/predict", json={
	        "data": [
		        "data:image/jpg;base64," + encoded_image.decode('utf-8'),
	        ]
            })
            # .json()

            # data = response["data"]
            # caption = data['data']
            # caption = caption[0]
            # print(caption)
            data = response.json()
            caption = data['data']
            caption = caption[0]
            print(caption)
            # print(response)

            form.save()
            #save the name and caption to the database
            # dog = Dog.objects.create(name=name, caption=caption)
            # dog.save()

            form = ImageUploadForm(initial={'name': name, 'caption': caption})
            return render(request, 'index.html', {'form': form, 'name': name, 'img': img_url, 'caption': caption})
        else:
            return render(request, 'index.html', {'form': form, 'name': 'No dog found'})
    return render(request, 'index.html')


# @csrf_exempt
# def caption(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         # img_url = ''
#         if form.is_valid():
#             #get image url
#             img_object = form.instance
#             # 'ImageUploadForm' object has no attribute 'cleaned_data'

#             # print(img_object)
#             img_url =img_object.image.url
#             encoded_image = base64.b64encode(img_object.image.read())

        
#             response = requests.post("https://elitecode-captioner.hf.space/run/predict", json={
#             "data": [
#                 "data:image/png;base64," + encoded_image.decode('utf-8'),
#             ]
#             }).json()

#             data = response["data"]
#             caption = data['data']
#             caption = caption[0]
#             print(caption)

#             form.save()

#             form = ImageUploadForm(initial={'caption': caption})
#             return render(request, 'caption.html', {'form': form, 'breed': caption, 'img': img_url})
#         else:
#             return render(request, 'caption.html', {'form': form, 'caption': 'No caption found'})
#     return render(request, 'caption.html')



            
