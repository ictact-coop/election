from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import Recommendation
from .forms import RecommendationForm
from django.conf import settings
import base64

def index(request):
    message = ''

    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            recommendation = form.save(commit=False)
            # 추천 제한 수를 넘었는지 확인
            if recommendation.is_over():
                message = recommendation.recommender + '님의 추천가능수를 초과했습니다. 앞의 추천을 변경하시려면 선관위에 문의해주세요'
            else:
                recommendation.created_at = timezone.now()
                # 즉석 서명 이미지가 있으면 저장하고 이번 추천의 서명으로 등록
                image_data = request.POST.get('new_signature_img', '')
                if not recommendation.signature:
                    if image_data != '':
                        filepath = getattr(settings, 'MEDIA_ROOT', None)
                        filename = filepath + '/' + 'new_sign_' + recommendation.recommender + '.png'
                        # 헤더 부분 제거
                        image_data = image_data[22:]
                        new_signature = open(filename, 'wb')
                        new_signature.write(base64.b64decode(image_data))
                        new_signature.close()
                        recommendation.signature = filename
                recommendation.save()
                message = recommendation.candidate.candidate_name + '님이 추천되었습니다.'

            form = RecommendationForm(initial={'recommender': recommendation.recommender, 'contact': recommendation.contact})
        else:
            message = '후보 추천에 실패했습니다. 다시 확인해주세요'

    else:
        form = RecommendationForm()

    context = { 'form': form, 'message': message }

    return render(request, 'candidates/index.html', context)

def create_signature(request):
    if request.method == 'POST':
        signature = request.FILES('new_signature')
