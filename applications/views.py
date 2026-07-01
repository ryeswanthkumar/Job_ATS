from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from .models import ShortlistedCandidate, HoldCandidate, RejectedCandidate


# ── Shared context (sidebar badge counts) ──────────────────────────────── #

def _base_context():
    return {
        "shortlisted_count": ShortlistedCandidate.objects.count(),
        "hold_count": HoldCandidate.objects.count(),
        "rejected_count": RejectedCandidate.objects.count(),
    }


# ── SIGNUP ─────────────────────────────────────────────────────────────── #

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with that email already exists.")
            return redirect("signup")

        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        messages.success(request, "Account created — please sign in.")
        return redirect("login")

    return render(request, "signup.html")


# ── LOGIN ──────────────────────────────────────────────────────────────── #

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "login.html")


# ── LOGOUT ─────────────────────────────────────────────────────────────── #

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# ── DASHBOARD ──────────────────────────────────────────────────────────── #

@login_required
def dashboard(request):
    context = _base_context()
    context["shortlisted_recent"] = ShortlistedCandidate.objects.order_by("-id")[:5]
    context["hold_recent"] = HoldCandidate.objects.order_by("-id")[:5]
    return render(request, "dashboard.html", context)


# ── DASHBOARD API ──────────────────────────────────────────────────────── #

@login_required
def dashboard_counts(request):
    return JsonResponse({
        "shortlisted": ShortlistedCandidate.objects.count(),
        "hold": HoldCandidate.objects.count(),
        "rejected": RejectedCandidate.objects.count(),
    })


# ── CANDIDATES ─────────────────────────────────────────────────────────── #

@login_required
def shortlisted_view(request):
    context = _base_context()
    context["data"] = ShortlistedCandidate.objects.all()
    return render(request, "shortlisted.html", context)


@login_required
def hold_view(request):
    context = _base_context()
    context["data"] = HoldCandidate.objects.all()
    return render(request, "hold.html", context)


@login_required
def rejected_view(request):
    context = _base_context()
    context["data"] = RejectedCandidate.objects.all()
    return render(request, "rejected.html", context) 