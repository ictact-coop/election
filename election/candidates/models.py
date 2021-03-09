from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_name = models.CharField(max_length=64)
    resident_number = models.CharField(max_length=16, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)
    type = models.CharField(max_length=12, null=False, blank=False)
    pledge = models.TextField(default='', null=False, blank=False)
    contact = models.CharField(max_length=64, null=False, blank=False)
    career1 = models.CharField(max_length=64, null=False, blank=False)
    career2 = models.CharField(default='', max_length=64, null=True, blank=True)
    signature = models.FileField(blank=True, null=True, upload_to="uploads/candidates/%Y/%m")
    available = models.CharField(max_length=12, null=True, blank=True, default='접수')
    recommendation_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.candidate_name

class Recommendation(models.Model):
    candidate = models.ForeignKey(Candidate, null=False, blank=False, on_delete=models.CASCADE)
    reason = models.TextField(default='', null=False, blank=False)
    recommender = models.CharField(max_length=64, null=False, blank=False)
    contact = models.CharField(max_length=64, null=False, blank=False)
    signature = models.FileField(blank=True, null=True, upload_to="uploads/%Y/%m")
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.candidate.candidate_name

    def is_over(self):
        if Recommendation.objects.filter(recommender = self.recommender).count() >= 3:
            return True
        return False
