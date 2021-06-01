from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import Pathway
from accounts.models import Profile

@login_required
def pathways_list(request):
    pathways = Pathway.objects.all()
    context = {
        "pathways": pathways
    }
    return render(request, "pathways/index.html", context)

@login_required
def pathway_detail(request, pathway_id):
    try:
        pathway_profiles = Profile.objects.filter(pathway=pathway_id)
        pathway_info = Pathway.objects.get(pk=pathway_id)
    except Pathway.DoesNotExist:
        # No need to proceed
        pathway_profiles = None
        pathway_info = None
    
    context = {
        "pathway_info": pathway_info,
        "pathway_profiles": pathway_profiles
    }
    return render(request, "pathways/pathway-detail.html", context)