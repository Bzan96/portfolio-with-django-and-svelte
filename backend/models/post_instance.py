from django.db import models
import uuid

class PostInstance(models.Model):
    """Model representing a specific post."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular post')
    post = models.ForeignKey('Post', on_delete=models.RESTRICT, null=True)
    publish_date = models.DateField(null=True, blank=True)

    POST_STATUS = (
        ('p', 'Published'),
        ('d', 'Draft'),
        ('r', 'Removed'),
    )

    status = models.CharField(
        max_length=1,
        choices=POST_STATUS,
        blank=True,
        default='d',
        help_text='Post status',
    )

    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.post.title})'