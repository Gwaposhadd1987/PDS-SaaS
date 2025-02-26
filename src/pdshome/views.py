from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent.parent


def home_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Precision Data Solutions"
    try: 
        percentage =  int(page_qs.count() / qs.count() * 100)
    except:
        percentage = 0

    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "page_visit_percentage": percentage,
        "total_visits": qs.count(),
    }
    path = request.path

    html_template = "home.html"
    PageVisit.objects.create(path=path)
    return render(request, html_template, my_context)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Precision Data Solutions"
    try: 
        percentage =  int(page_qs.count() / qs.count() * 100)
    except:
        percentage = 0

    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "page_visit_percentage": percentage,
        "total_visits": qs.count(),
    }
    path = request.path

    html_template = "about.html"
    PageVisit.objects.create(path=path)
    return render(request, html_template, my_context)       

def test_home_view(request, *args, **kwargs):
    path = request.path
    print("path", path)
    my_title = "Test Home Page"
    my_context = {"page_title": my_title}
    html_template = "test_home.html"
    return render(request, html_template, my_context)


def old_home_view(request, *args, **kwargs):
    path = request.path
    print("path", path)
    my_title = "My Page"
    my_context = {"page_title": my_title}
    html_ = ""
    html_file_path = this_dir / 'home.html'
    html_ = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>{page_title} is loaded in-line</h1>
        <h3> from the my_old_home_page view function </h3>
    </body>
    </html>
    """.format(**my_context)  # page_title=my_title
    return HttpResponse(html_)
