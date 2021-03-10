from django import forms
from .models import Candidate, Recommendation

class RegistrationForm(forms.ModelForm):
    candidate_name = forms.CharField(
        label = '이름',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '본인의 이름을 적어주세요'
        })
    )
    resident_number = forms.CharField(
        label = '주민등록번호',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '주민등록번호를 입력해주세요'
        })
    )
    address = forms.CharField(
        label = '주소',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '주소를 적어주세요'
        })
    )
    type = forms.CharField(
        label = '임원 유형',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '이사 혹은 감사를 적어주세요. 감사는 사업감사와 회계감사가 있습니다'
        })
    )
    pledge = forms.CharField(
        label = '출마의 변(공약)',
        widget = forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': '임원 후보로 출마하는 다짐을 적어주세요'
        })
    )
    contact = forms.CharField(
        label = '연락처(전화번호)',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '본인 확인을 위해 전화번호를 적어주세요'
        })
    )
    signature = forms.FileField(
        label = '서명 이미지',
        required = False,
        widget = forms.FileInput(attrs={
            'class': 'form-control',
        })
    )
    career1 = forms.CharField(
        label = '경력',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '대표적인 경력을 적어주세요'
        })
    )
    career2 = forms.CharField(
        label = '경력',
        required = False,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '추가로 공유할 경력을 적어주세요'
        })
    )
    class Meta:
        model = Candidate
        fields = '__all__'
        widgets = {
            'recommendation_count': forms.HiddenInput(),
            'available': forms.HiddenInput(),
        }

class RecommendationForm(forms.ModelForm):
    candidate = forms.ModelChoiceField(
        queryset=Candidate.objects.all(),
        label = '추천 받으실 조합원',
        widget = forms.Select(attrs={
            'class': 'form-control',
            'placeholder': '추천하고 싶은 분(추천 받으실 분) 이름을 적어주세요'
        })
    )
    reason = forms.CharField(
        label = '추천 이유',
        widget = forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': '추천하는 이유를 적어주세요'
        })
    )
    recommender = forms.CharField(
        label = '추천인 이름',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '추천할 분 이름을 적어주세요'
        })
    )
    contact = forms.CharField(
        label = '연락처(전화번호)',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '본인 구분을 위해 전화번호를 적어주세요'
        })
    )
    signature = forms.FileField(
        label = '서명 이미지',
        required = False,
        widget = forms.FileInput(attrs={
            'class': 'form-control',
        })
    )
    class Meta:
        model = Recommendation
        fields = '__all__'
        widgets = {

        }
