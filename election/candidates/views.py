from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import RecommendationForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.created_at = timezone.now()
            recommendation.save()
    else:
        form = RecommendationForm()

    context = { 'form': form }

    return render(request, 'candidates/index.html', context)
