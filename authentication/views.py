from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout

from . import forms


def logout_user(request):
    logout(request)
    return redirect("login")


def login_page(request):
    # """ instances vide du formulaire lors du premier chargement """
    form = forms.LoginForm()
    # """ variable de formatage de message  """
    message = ""
    # """ detection de l'envoie du formulaire  """
    if request.method == "POST":
        # """ on remplie le formulaire avec les donnees envoyers """
        form = forms.LoginForm(request.POST)
        # """ Si le formulaire est valide """
        if form.is_valid():
            # """ Verifie dans la BD si les infos correspondent
            # a ceux d'un user """
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            # """ Si l'utilisateur existe  """
            if user is not None:
                # """ creer une session pour l'utilisateur """
                login(request, user)
                return redirect("home")
                # """ sinon """
            else:
                #  Affiche ce massage """
                message = "Identifiants invalides."

    return render(
        request, "authentication/login.html", context={"form": form, "message": message}
    )
