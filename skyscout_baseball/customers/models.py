from django.db import models

# We only have one product so far --> SkyScout Baseball

class Waitlist(models.Model):

    WAYS_IN_BASEBALL_CHOICES = [
        ("Pl", "Player (current or former)"),
        ("Co", "Coach"),
        ("Pa", "Parent"),
        ("N/A", 'Not in industry')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    job_title = models.CharField(max_length=255)
    been_in_baseball_industry = models.BooleanField() # if true, there is a following question
    type_of_involvement = models.CharField(max_length=5, choices=WAYS_IN_BASEBALL_CHOICES)
    comments = models.TextField(null=True, blank=True, max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    testimonial = models.BooleanField() # we will have a section specifically to high-end testimonials
 
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.email}"


