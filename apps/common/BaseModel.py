from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True 

    def delete(self, *args, **kwargs):
        """
        Soft delete method. Instead of removing the record from the database,
        it sets the 'is_active' field to False.
        """
        self.is_active = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        """
        Hard delete method. Actually removes the record from the database.
        """
        super(BaseModel, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Custom save method. Can be extended with additional logic.
        """
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)