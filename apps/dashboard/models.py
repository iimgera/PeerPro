from django.db import models
from django.contrib.auth.models import User

# class Report(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     last_week = models.TextField( 
#         verbose_name='What did you do last week?'
#     )

#     this_week = models.TextField(
#         verbose_name='What are you working on until the next week?'
#     )

#     next_week = models.TextField(
#         verbose_name='What are your plans for the next week?'
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Report {self.id} by {self.user.username}"

#     class Meta:
#         verbose_name = 'Report'
#         verbose_name_plural = 'Reports'
#         ordering = ['-id']



class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    last_week = models.TextField(
        blank=True, 
        verbose_name='What did you do last week?'
        )
    this_week = models.TextField(
        blank=True, 
        verbose_name='What are you working on until the next week?'
        )
    next_week = models.TextField(
        blank=True, 
        verbose_name='What are your plans for the next week?'
        )
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Report {self.id} by {self.user.username}"

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        ordering = ['-id']

class ReportStatus(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
