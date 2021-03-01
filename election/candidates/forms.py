from django import forms
from .models import Candidate, Recommendation

class RecommendationForm(forms.ModelForm):
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all(), required=False)
    class Meta:
        model = Recommendation
        fields = '__all__'
        widgets = {
        }
