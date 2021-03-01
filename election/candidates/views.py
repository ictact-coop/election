from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import RecommendationForm

# Create your views here.
def index(request):
    message = ''
    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.created_at = timezone.now()
            recommendation.save()
            message = recommendation.candidate.candidate_name + '님이 추천되었습니다.'
        else:
            message = recommendation.candidate.candidate_name + '님 추천에 실패했습니다. 다시 확인해주세요'

    new_form = RecommendationForm()

    context = { 'form': new_form, 'message': message }

    return render(request, 'candidates/index.html', context)
