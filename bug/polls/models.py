from django.db import models




class Bug(models.Model):
    BUG_TYPES = (
        ('error', 'Error'),
        ('new_feature', 'New Feature'),
        ('enhancement', 'Enhancement'),
        ('security', 'Security'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('review', 'Review'),
        ('testing', 'Testing'),
    )

    description = models.TextField()
    bug_type = models.CharField(max_length=20, choices=BUG_TYPES, default='error')
    report_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do')

    def __str__(self):
        return self.description
