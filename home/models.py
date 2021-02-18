from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from blog.models import BlogPage

class HomePage(Page):
    hero_title = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section")

    hero_subtitle = models.TextField(
    	max_length=200,
    	blank=True,
    	help_text="Subtitle following the maintitle in the hero section")

    cta_btn_text = models.CharField(
    	max_length=20,
    	blank=True,
    	default="Read more",
    	help_text="Call-To-Action Buttton Text",)

    cta_btn_link = models.ForeignKey(
    	'wagtailcore.page',
    	null=True,
    	blank=True,
    	related_name="+",
    	on_delete=models.SET_NULL,
    	help_text="Internal page link to send the user to article")

    def get_context(self, request):
    	context = super().get_context(request)
    	featured_articles = BlogPage.objects.live().filter(featured=True)
    	context['featured_articles'] = featured_articles
    	return context
    # Configure admin interface
    content_panels = Page.content_panels + [
    	FieldPanel("hero_title"),
    	FieldPanel("hero_subtitle"), 
    	FieldPanel("cta_btn_text"),
    	PageChooserPanel("cta_btn_link"),
    ]

