from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    try:
        request.session["count"] += 1
    except KeyError:
        request.session["count"] = 1
    return render(request, "index.html")

def register(request):
    print(request.POST)
    request.session["user"] = {
        "name": request.POST["name"],
        "email": request.POST["email"],
        "password": request.POST["password"]
    }
    return redirect("/home")

def success(request):
    if "user" not in request.session:
        return redirect("/")
    return render(request, "success.html")

def reset(request):
    request.session.clear()
    return redirect("/")
