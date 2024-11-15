from django.db import models

# Create your models here.
class BtnCounter(models.Model):
    counter_title = models.CharField("title", null=True, blank=True, default="", max_length=255)
    visit_counter = models.IntegerField("visit count", null=False, blank=False, default=0)
    
    def __str__(self):
        return f"{self.counter_title}"
    
    class Meta:
        verbose_name = "visit counter"
        verbose_name_plural = "visits counter"
        # ordering = [""]
        # db_table = ""
