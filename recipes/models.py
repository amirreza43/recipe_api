from django.db import models

# Create your models here.
class Recipe(models.Model):
    # Fields for recipe details
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.JSONField()  # Using JSONField for a list of ingredients
    prompt = models.ForeignKey('prompts.Prompt', related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
