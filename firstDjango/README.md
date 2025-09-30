In this project we saw some settings related to web pages rendering liek 


1(1): how we create routes by using views and urls file 

```python   

    #urls.py
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact")
```
```python   

    #views.py
    
    from django.http import HttpResponse
    from django.shortcuts import render

    def home(req): 
        # return HttpResponse("hell world , this is a home route")
        return render(req, template_name="website/home.html")

    def about(req):
        # return HttpResponse("this is the about route")
        return render(req, template_name="website/about.html")


    def contact(req):
        # return HttpResponse("this is the contact route")
        return render(req, template_name="website/contact.html")
    
    # creae functions -> urls.py [1: import , 2 : setup routes based on functions]
```



1: how actually pages created in templates / website  , and how the location is mapped in setting.py 

```python 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

2: how file css is linkedin via {% load static in html and link to the file via setting.py %}

```python 

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```
