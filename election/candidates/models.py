from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_name = models.CharField(max_length=64)
    Recommendation_count = models.IntegerField(default=0)

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
