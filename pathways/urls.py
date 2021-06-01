
from django.urls import path
from . import views as pathways_view

app_name = "pathways"
urlpatterns = [
    path("", pathways_view.pathways_list, name="pathways_list"),
    path("<pathway_id>/", pathways_view.pathway_detail, name="pathway_detail"),
]