from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage
from .models import User, Car, Insurance, Post

import time

# Create views


def profile(request, user_id):
    user_profile = User.objects.get(pk=user_id)
    if request.method == 'GET':
        id_num = getattr(user_profile, "ID_number", "")
        dl_num = getattr(user_profile, "driving_licence_number", "")
        date_of_birth = getattr(user_profile, "date_of_birth", "")
        return render(request, "insurance/profile.html", {
            "user_id": user_profile.id,
            "username": user_profile.username,
            "first_name": user_profile.first_name,
            "last_name": user_profile.last_name,
            "id_number": id_num,
            "dl_number": dl_num,
            "date_of_birth": date_of_birth,
            "email": user_profile.email
        })
    else:
        try:
            user_profile.first_name = request.POST['f_name']
            user_profile.last_name = request.POST['l_name']
            user_profile.username = request.POST['username']
            user_profile.email = request.POST['email']
            user_profile.ID_number = request.POST['id_num']
            user_profile.driving_licence_number = request.POST['dl_num']
            user_profile.date_of_birth = request.POST['date_of_birth']
            
            user_profile.save()
            return render(request, "insurance/profile.html", {
                "user_id": user_id,
                "message": "saved successfully"
            })

        except IntegrityError:
            return render(request, "insurance/profile.html", {
                "user_id": user_id,
                "message": "ERROR!"
            })

    
def form(request):
    return render(request, "insurance/form.html")


def save_application(request):
    if request.method == 'POST':
        license_plate = request.POST['license']
        vin = request.POST['VIN']
        year = request.POST['year']
        brand = request.POST['carName']
        serie = request.POST['carSeries']
        
        new_car = Car(
            license_plate=license_plate,
            vin=vin,
            year=year,                                              
            brand=brand,
            serie=serie
        )
        new_car.save()
        insured = new_car

        cost = request.POST['cost']
        coverage_fire = bool(request.POST.get('fire'))
        coverage_theft = bool(request.POST.get('theft'))
        coverage_natural_disaster = bool(request.POST.get('natural_disaster'))
        no_clame_discount = request.POST.get('noclaim', '')
        policyholder = request.user
        
        new_contract = Insurance(
            cost=cost,
            coverage_fire=coverage_fire,
            coverage_theft=coverage_theft,
            coverage_natural_disaster=coverage_natural_disaster,
            no_clame_discount=no_clame_discount,
            insured=insured,
            policyholder=policyholder
        )
        new_contract.save()

        return render(request, "insurance/index.html", {
                    "message": "Thank you for choosing us! Please contact us if you have any questions or need help."
                })


def index(request):
    return render(request, "insurance/index.html")


def posts(request):
    all_posts = Post.objects.all().order_by("-date_of_upload")
    post_data = [
        {
            "title": post.title,
            "content": post.content,
            "date_of_upload": post.date_of_upload,
            "image": post.image.url if post.image else None,
        }
        for post in all_posts
    ]
    return JsonResponse({
        "posts": post_data
        })


def check_auth_status(request):
    if request.user.is_authenticated:
        return JsonResponse({"is_authenticated": True})
    else:
        return JsonResponse({"is_authenticated": False}, status=401)


@user_passes_test(lambda u: u.is_superuser)
def upload_post(request):
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.FILES["image"]  
        new_post = Post(
            title=title,
            content=content,
            image=image
        )
        new_post.save()
        all_posts = Post.objects.all().order_by("date_of_upload").reverse()
        return render(request, "insurance/index.html", {
            "all_posts": all_posts
        })
    return render(request, "insurance/post.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "insurance/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "insurance/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "insurance/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.date_of_birth = None
            user.ID_number = None
            user.driving_licence_number = None
            user.save()
        except IntegrityError:
            return render(request, "insurance/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "insurance/register.html")