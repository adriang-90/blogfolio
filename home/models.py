from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    hero_title = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section")

    # Configure admin interface
    content_panels = Page.content_panels + [
    	FieldPanel("hero_title"), 
    ]

