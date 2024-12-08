from django.shortcuts import render

from django.http import HttpResponse


class Nurseries:
    def __init__(self, name, image):
        self.name = name
        self.image = image

nurseries =[
    Nurseries('tree','https://img.freepik.com/free-photo/tree-with-white-background_1232-574.jpg?t=st=1733642842~exp=1733646442~hmac=7fa5cefa1763ede182a880bd1c5d9f7ff62cdf9b7e39b54cf12dc2b62fa50ac9&w=740'),
    Nurseries('vegetable','https://img.freepik.com/free-photo/green-broccoli-levitating-white-background_485709-79.jpg?t=st=1733642873~exp=1733646473~hmac=186afc585dc73cd937dbb208dd078bb2dd9517cc500790d13f80f28a0e158397&w=360'),
    Nurseries('ornamental','https://img.freepik.com/free-photo/large-set-isolated-vegetables-white-background_485709-44.jpg?t=st=1733642907~exp=1733646507~hmac=9a05489191b93f27ba3b174eee541edd6a7459493d577c5f199da7d64ab94182&w=900'),
]        

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nurseries_index(request):
    return render(request, 'nurseries/index.html', {'nurseries': nurseries})
