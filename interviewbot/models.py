from django.db import models

# Create your models here.
from django.db import models

class Chat(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question[:30]}... | A: {self.answer[:30]}..."
