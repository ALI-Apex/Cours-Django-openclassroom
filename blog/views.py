from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.

""" ce decorateur permet de restreindre des partie de notre site
web aux utilisateurs non connecter"""


@login_required
def home(request):
    return render(request, "blog/home.html")
