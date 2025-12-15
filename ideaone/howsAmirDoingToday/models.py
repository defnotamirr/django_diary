from django.db import models

class DiaryEntry(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
