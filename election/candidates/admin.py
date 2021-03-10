from django.contrib import admin

# Register your models here.
from .models import Candidate, Recommendation

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'contact', 'type')
    list_filter = ['created_at', 'candidate_name', 'type']

class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'recommender', 'contact')
    list_filter = ['created_at', 'candidate', 'recommender', 'contact']

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
