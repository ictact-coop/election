from django import forms
from .models import Candidate, Recommendation

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
