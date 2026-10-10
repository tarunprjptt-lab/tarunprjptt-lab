from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    recipesdata = requests.get("https://dummyjson.com/recipes").json()
    context = {
        "recipes" : recipesdata["recipes"]
    }
    return render(request, "index.html", context)

def recipes(request):
    recipesdata = requests.get("https://dummyjson.com/recipes").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    context = {
        "recipes" : recipesdata["recipes"],
        "tags" : tags
    }
    return render(request, "recipes.html", context)

def recipebytag(request, tag):
    recipesdata = requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    context = {
        "recipes": recipesdata["recipes"],
        "tags": tags
    }
    return render(request, "recipesbytag.html", context)

def recipe(request,id):
    recipesdata = requests.get(f"https://dummyjson.com/recipes/{id}").json()
    context = {
        "recipedetails": recipesdata,
        "ingredients" : recipesdata["ingredients"],
        "instructions" : recipesdata["instructions"]
    }
    return render(request, "recipe.html", context)

def contact(request):
    return render(request, "contact.html")

def search(request):
    recipesdata = requests.get("https://dummyjson.com/recipes").json()
    context = {
        "recipes" : recipesdata["recipes"]
    }
    return render(request, "search.html", context)


def searchresults(request):
    if request.method == "GET":
        query = request.GET.get("query")
        recipesdata = requests.get(f"https://dummyjson.com/recipes/search?q={query}").json()
        context = {
            "recipes": recipesdata["recipes"]
        }
    return render(request, "searchresults.html", context)
