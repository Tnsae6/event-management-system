from django.db import models

# Create your models here.


class summaryModel(models.Model):
    id = models.IntegerField(primary_key=True)
    summary_title = models.CharField(max_length=20)
    summary_detail = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    def __str__(self):
        return f"summary: {self.summary_title}"


class CommentModel(models.Model):
    your_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    summary = models.ForeignKey('summaryModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by Name: {self.your_name}"
