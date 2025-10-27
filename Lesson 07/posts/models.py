from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def description_word_count(self) -> int:
        text = (self.description or "").strip()
        if not text:
            return 0
        return len([w for w in text.split() if w])
