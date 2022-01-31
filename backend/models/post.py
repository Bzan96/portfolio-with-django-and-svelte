from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from .category import Category

class Post(models.Model):
    """Model representing a post (but not a specific post)."""
    title = models.CharField(max_length=200)

    ## Note: This seems quite unnecessary for a portfolio site, but keeping it for structure purposes
    # Foreign Key used because post can only have one author, but authors can have multiple posts
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    body = RichTextField()

    # ManyToManyField used because category can contain many posts. Posts can cover many categories.
    # category class has already been defined so we can specify the object above.
    category = models.ManyToManyField(Category, help_text='Select a category for this post')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this post."""
        return reverse('post-detail', args=[str(self.id)])