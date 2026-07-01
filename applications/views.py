from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from .models import ShortlistedCandidate, HoldCandidate, RejectedCandidate


<<<<<<< HEAD
# ── Shared context (sidebar badge counts) ──────────────────────────────── #

def _base_context():
    return {
        "shortlisted_count": ShortlistedCandidate.objects.count(),
        "hold_count":        HoldCandidate.objects.count(),
        "rejected_count":    RejectedCandidate.objects.count(),
    }


# ── SIGNUP ─────────────────────────────────────────────────────────────── #
=======
# ---------------- SIGNUP ---------------- #
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
<<<<<<< HEAD
        last_name  = request.POST.get("last_name")
        email      = request.POST.get("email")
        password   = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with that email already exists.")
            return redirect("signup")

        User.objects.create_user(
            username=email,
=======
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return redirect("signup")

        User.objects.create_user(
            username=email,   # email as username
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
<<<<<<< HEAD
        messages.success(request, "Account created — please sign in.")
=======

        messages.success(request, "Account created successfully")
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0
        return redirect("login")

    return render(request, "signup.html")


<<<<<<< HEAD
# ── LOGIN ──────────────────────────────────────────────────────────────── #

def login_view(request):
    if request.method == "POST":
        email    = request.POST.get("email")
        password = request.POST.get("password")
        user     = authenticate(request, username=email, password=password)
=======
# ---------------- LOGIN ---------------- #

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
<<<<<<< HEAD
            messages.error(request, "Invalid email or password.")
=======
            messages.error(request, "Invalid email or password")
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0
            return redirect("login")

    return render(request, "login.html")


<<<<<<< HEAD
# ── LOGOUT ─────────────────────────────────────────────────────────────── #
=======
# ---------------- LOGOUT ---------------- #
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


<<<<<<< HEAD
# ── DASHBOARD ──────────────────────────────────────────────────────────── #

@login_required
def dashboard(request):
    context = _base_context()
    context["shortlisted_recent"] = ShortlistedCandidate.objects.order_by("-id")[:5]
    context["hold_recent"]        = HoldCandidate.objects.order_by("-id")[:5]
    return render(request, "dashboard.html", context)


# ── DASHBOARD API ──────────────────────────────────────────────────────── #
=======
# ---------------- DASHBOARD ---------------- #

@login_required
def dashboard(request):
    context = {
        "shortlisted_count": ShortlistedCandidate.objects.count(),
        "hold_count": HoldCandidate.objects.count(),
        "rejected_count": RejectedCandidate.objects.count(),
    }
    return render(request, "dashboard.html", context)


# ---------------- DASHBOARD API (OPTIONAL) ---------------- #
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0

@login_required
def dashboard_counts(request):
    return JsonResponse({
        "shortlisted": ShortlistedCandidate.objects.count(),
<<<<<<< HEAD
        "hold":        HoldCandidate.objects.count(),
        "rejected":    RejectedCandidate.objects.count(),
    })


# ── CANDIDATES ─────────────────────────────────────────────────────────── #

@login_required
def shortlisted_view(request):
    context = _base_context()
    context["data"] = ShortlistedCandidate.objects.all()
    return render(request, "shortlisted.html", context)
=======
        "hold": HoldCandidate.objects.count(),
        "rejected": RejectedCandidate.objects.count(),
    })


# ---------------- CANDIDATES ---------------- #

@login_required
def shortlisted_view(request):
    data = ShortlistedCandidate.objects.all()
    return render(request, "shortlisted.html", {"data": data})
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0


@login_required
def hold_view(request):
<<<<<<< HEAD
    context = _base_context()
    context["data"] = HoldCandidate.objects.all()
    return render(request, "hold.html", context)
=======
    data = HoldCandidate.objects.all()
    return render(request, "hold.html", {"data": data})
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0


@login_required
def rejected_view(request):
<<<<<<< HEAD
    context = _base_context()
    context["data"] = RejectedCandidate.objects.all()
    return render(request, "rejected.html", context)
=======
    data = RejectedCandidate.objects.all()
    return render(request, "rejected.html", {"data": data})
>>>>>>> 8b09a7aacfab883d7840148ffc29c6645096c4e0
