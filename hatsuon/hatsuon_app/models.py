import uuid
from django.db import models


class Collection(models.Model):
    """
    Collection
    """

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(
        "auth.User", related_name="collections", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_date"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
