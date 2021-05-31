from os import error
# from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserAccountForm, UserProfileForm
from .models import Profile


@login_required
def index(request):
    return render(request, "accounts/index.html")

@login_required
def get_account_profile(request):
    try:
        profile = Profile.objects.get(user=request.user.id)
    except Profile.DoesNotExist:
        profile = None
    
    return render(request, "accounts/profile.html", {"profile": profile})

@login_required
def update_account_profile(request):
    # Setup for two forms to be filled out
    user_form = UserAccountForm(instance=request.user)
    profile_form = UserProfileForm()
    # When a form is submitted
    if request.method == "POST":
        user_form = UserAccountForm(data=request.POST, instance=request.user)

        try:
            profile = Profile.objects.get(user=request.user.id)
        except Profile.DoesNotExist:
            profile = None
        
        if not profile:
            # create one from user input
            profile_form = UserProfileForm(
                request.POST or None, 
                request.FILES or None
            )
        else:
            # profile exists, update it
            # pass the profile instance to be updated
            profile_form = UserProfileForm(
                request.POST or None, 
                request.FILES or None, 
                instance=profile
            )

        

        if user_form.is_valid() and profile_form.is_valid():
            # Update User record
            updated_user = user_form.save(commit=False)
            updated_user.save()

            # Update Profile
            updated_profile = profile_form.save(commit=False)
            updated_profile.user = updated_user
            updated_profile.save()
            # Use the save data
            username = user_form.cleaned_data["username"]
            messages.success(request, f"Profile for {username} updated successfully!")
            return redirect("accounts:account_profile")
        context = {
            "profile_form": profile_form,
            "user_form": user_form,
        }
        return render(request, "accounts/update-profile.html", context)

    
    # User just wants to EDIT/Create his profile
    try:
        profile = Profile.objects.get(user=request.user.id)
    except Profile.DoesNotExist:
        profile = None
    
    if profile:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserAccountForm(instance=profile.user)

    context = {
        "profile_form": profile_form,
        "user_form": user_form,
    }
    return render(request, "accounts/update-profile.html", context)

  


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        # User submitted a signup form
        # Get submited records and validate
        email = request.POST["email"].strip()
        username = request.POST["username"].strip()
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        #@TODO Validate user input
        if not email or email == "" or len(email) < 2:
            messages.error(request, "Invalid email")
        if len(username) < 8 or not username or not username.isalpha():
            messages.error(request, "Username is invalid")
        if len(password) < 6 or password == "" or password != confirm_password:
            messages.error(request, "Password is invalid")
       
        if messages.get_messages(request):
            return render(request, "accounts/signup.html") 

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.info(request, "Account already exists, log in")
     
        else:
            user = User.objects.create_user(email=email, password=password, username=username)
            user.save()
            if user:
                print("user ", user.username)
                messages.success(request, f"Account created for {username}")
                return redirect("accounts:login") 
            else:
                messages.info(request, f"Account creation FAILED for {username}")

    
    return render(request, "accounts/signup.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:accounts_home')
    # is_username = False # lets pretend user logs in with email
    if request.method == "POST":
        # Login form has been submitted
        username = request.POST["username"].strip()
        password = request.POST["password"]
        # Valusernameate input
        if len(username) < 6 or not username:
            messages.error(request, "Invalid credentials")
            return render(request, "accounts/login.html")
            
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, f"Welcome {username}")
            auth.login(request, user)
            return redirect("accounts:login")
        else:
            messages.error(request, "Account does not exist")

    return render(request, "accounts/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
