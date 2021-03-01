from django.contrib import admin

# Register your models here.
from .models import Candidate, Recommendation

admin.site.register(Candidate)
admin.site.register(Recommendation)
