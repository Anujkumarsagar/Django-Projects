from django.shortcuts import render

# Create your views here.
def sub_app(request):
    return render(request, template_name="subApp/sub-app.html")
