from django.urls import path
from django.utils.translation import templatize
from . import views as account_view

# Namespace
app_name = "accounts"

urlpatterns = [
    path("", account_view.index, name="accounts_home"),
    path("profile/", 
        account_view.get_account_profile, 
        name="account_profile"
    ),
    path("profile/<profile_id>/", 
        account_view.get_account_profile, 
        name="view_alumni_profile"
    ),
    path("update-profile/", 
        account_view.update_account_profile, 
        name="update_account_profile"
    ),
    path("signup/", account_view.signup, name="signup"),
    path("login/", account_view.login, name="login"),
    path("logout/", account_view.logout, name="logout"),

]