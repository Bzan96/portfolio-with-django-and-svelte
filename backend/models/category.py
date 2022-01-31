from django.db import models

class Category(models.Model):
    """Model representing a post category."""
    name = models.CharField(max_length=50, help_text='Enter a post category (e.g. "CSS")')
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """String for representing the Model object."""
        return self.name