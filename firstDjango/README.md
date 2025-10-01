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



----------------------------------------------

python manage.py startapp web-app-name

----------------------------------------------

django sirf apps ko bnata hai install nahi karta

step one mei hota ke main project ko aware karwana hamare paas mei ek nayi app aayi hai

```python 
main-app -> settings.py -> installed_apps -> [add 'web-app-name']
```

----------------------------------------------
kuch industry standards hote hia jab bhi ham koi new app bnate hia unki templates rakhne ke liye 

web-app-name -> templates -> web-app-name -> html_files

isko karte time ek problem hoti hai ki yaha suggestion nahi milte hia usko ok karne ke liye ham kuch steps follow karte hia woh hai 

settings -> search["emmet"] -> include languages -> add item [ django-html --- html]


----------------------------------------------------

to create a subApp routes like if you have multiple apps in your project like take an example 
Instagram clone 
    in this project you can have multiple subApps Like: 
        1:Reels
        2:Profile
        3:Feed
        4:Notification

now there is possbility you have multiplel endpoints in your each apps Like
        Profile 
            -> /profile 
            -> /profile/edit
            -> /profile/followers
            -> /profile/following
            -> /profile/posts
            -> /profile/settings
        Reels
            -> /reels
            -> /reels/create
            -> /reels/like
            -> /reels/comment
            -> /reels/share
            -> /reels/save

and so on 

now  you need to mapped your subapp routes with the main project routes 

you can do this by 

```python 

path("subApp/", include("subApp.urls"), name="subApp")

```

----------------------------------------------------

--------------------Jinja----------------------------
to craete layout.html file 

what can layout.html does
    -> a static navbar in all subapps and pages
    -> Define a static navbar / header / footer
    -> Use {% block %} tags for custom content
    -> Load static files (CSS, JS, images)
    -> Include reusable snippets ({% include %})
    -> Add global JavaScript or analytics code
    -> Control different page sections with multiple blocks
    -> Inherit across subapps for consistency

process:
    create a file where where all these sub components and things will be prsent for all application 
        -> we can create a `layout.html` main-app -> templates -> layout.html file
        -> then make some blocks like when we use {children} in react

        ```html
        {% load static %}

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>
                    {% block title %}
                    Default value
                    {% endblock title %}

                </title>

                {% block css %}{% endblock css %}
            </head>
            <body>

                <nav>
                    <div class="logo">CloudFlow</div>
                    <ul class="nav-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="#features">Features</a></li>
                        <li><a href="/contact">Contact</a></li>
                        <li><a href="/about">About</a></li>
                    </ul>
                    <button class="cta-btn">Get Started</button>
                </nav>

                {% block content %}{% endblock content %}
            </body>

            </html>
        ```

        -> these block can overwrite and we can put the things acccrodingly in diffrent diffrent html files 

                ```html

                    {% extends "layout.html" %} --> fetches the layout file with all block
                    {% load static %}

                    {% block title %} --> overwrite the title block
                    CloudFlow - Next-Gen SaaS Platform
                    {% endblock title %}

                    {% block css %} --> overwrite the css block
                        <link rel="stylesheet" href="{% static 'home.css' %}">
                    {% endblock css %}

                    {% block content %} --> overwrite the content block
                            <div> .... </div>
                    {% endblock content %}

                ```



    Tailwind Integration : [Article Link](https://docs.chaicode.com/youtube/chai-aur-django/tailwind/)
