from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Recommendation, Candidate
from .forms import RecommendationForm, RegistrationForm
from django.conf import settings
import base64
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required

def index(request):
    # return render(request, 'candidates/index.html')
    return redirect('candidates:register')

def register(request):
    message = ''
    registration_result = None

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration = form.save(commit=False)
            # 이미 등록되어 있는지 확인 (현재 동명이인 없으므로 이름만 확인)
            if Candidate.objects.filter(candidate_name=registration.candidate_name).exists():
                message = registration.candidate_name + '님은 이미 후보로 등록되어 있습니다. 등록 내용을 변경하려면 선관위에 문의해주세요'
            else:
                registration.created_at = timezone.now()
                # 즉석 서명 이미지가 있으면 저장하고 이번 추천의 서명으로 등록
                image_data = request.POST.get('new_signature_img', '')
                if not registration.signature:
                    if image_data != '':
                        format, imgstr = image_data.split(';base64,')
                        ext = format.split('/')[-1]
                        data = ContentFile(base64.b64decode(imgstr), name=registration.candidate_name + '.' + ext)
                        registration.signature = data
                        # filepath = getattr(settings, 'MEDIA_ROOT', None)
                        # filename = 'new_sign_' + registration.candidate_name + '.png'
                        # real_filename = filepath + '/' + filename
                        # # 헤더 부분 제거
                        # image_data = image_data[22:]
                        # new_signature = open(real_filename, 'wb')
                        # new_signature.write(base64.b64decode(image_data))
                        # new_signature.close()
                        # registration.signature = real_filename
                registration.save()
                message = registration.candidate_name + '님의 임원 후보 등록 신청이 접수되었습니다. 조합원 3명 이상의 추천을 모아주시면 선관위에서 확인 후 공식 후보로 확정됩니다.'
                registration_result = registration
            form = RegistrationForm()

        else:
            message = '후보 등록 신청에 실패했습니다. 다시 확인해주세요'

    else:
        form = RegistrationForm()

    context = { 'form': form, 'message': message, 'registration_result': registration_result }

    return render(request, 'candidates/register.html', context)

def recommend(request):
    message = ''

    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            recommendation = form.save(commit=False)
            # 추천 제한 수를 넘었는지 확인
            if recommendation.is_over():
                message = recommendation.recommender + '님의 추천가능수를 초과했습니다. 앞의 추천을 변경하시려면 선관위에 문의해주세요'
            elif recommendation.is_exists():
                message = recommendation.recommender + '님은 ' + recommendation.candidate.candidate_name + ' 후보를 이미 추천하셨습니다. 앞의 추천을 변경하시려면 선관위에 문의해주세요'
            else:
                recommendation.created_at = timezone.now()
                # 즉석 서명 이미지가 있으면 저장하고 이번 추천의 서명으로 등록
                image_data = request.POST.get('new_signature_img', '')
                if not recommendation.signature:
                    if image_data != '':
                        format, imgstr = image_data.split(';base64,')
                        ext = format.split('/')[-1]
                        data = ContentFile(base64.b64decode(imgstr), name=recommendation.candidate.candidate_name + '.' + ext)
                        recommendation.signature = data
                        # filepath = getattr(settings, 'MEDIA_ROOT', None)
                        # filename = filepath + '/' + 'new_sign_' + recommendation.recommender + '.png'
                        # # 헤더 부분 제거
                        # image_data = image_data[22:]
                        # new_signature = open(filename, 'wb')
                        # new_signature.write(base64.b64decode(image_data))
                        # new_signature.close()
                        # recommendation.signature = filename
                recommendation.save()
                message = recommendation.candidate.candidate_name + '님이 추천되었습니다.'

            form = RecommendationForm(initial={'recommender': recommendation.recommender, 'contact': recommendation.contact})
        else:
            message = '후보 추천에 실패했습니다. 다시 확인해주세요'

    else:
        form = RecommendationForm()

    candidates = Candidate.objects.all

    context = { 'form': form, 'message': message, 'candidates': candidates }

    return render(request, 'candidates/recommend.html', context)

@login_required
def commission(request):
    candidates = Candidate.objects.all
    context = { 'candidates': candidates }
    return render(request, 'candidates/commission.html', context)

def create_signature(request):
    if request.method == 'POST':
        signature = request.FILES('new_signature')
