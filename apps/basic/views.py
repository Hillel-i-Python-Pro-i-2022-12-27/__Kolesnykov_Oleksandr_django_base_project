from django.shortcuts import render


def index(request):
    context = {
        "title": "Home Page",
    }

    return render(
        request=request,
        template_name="index.html",
        context=context,
    )


def about_us(request):
    context = {
        "title": "About us",
    }

    return render(
        request=request,
        template_name="about_us.html",
        context=context,
    )
