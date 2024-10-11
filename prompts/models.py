from django.db import models

# Create your models here.
class Prompt(models.Model):
    # Fields for prompt details
    user = models.ForeignKey('users.User', related_name='prompts', on_delete=models.CASCADE)
    ingredients = models.JSONField()  # List of ingredients provided by the user
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ingredients  # Return a shortened version of the prompt text

    