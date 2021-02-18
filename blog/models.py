from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from streamfieldblocks.models import ResponsiveImageBlock, CardBlock, SimpleRichTextBlock, CarouselBlock, FlushListBlock
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel


# Create your models here.
class BlogListingPage(Page):
	background_image = models.ForeignKey(
		'wagtailimages.Image',
		blank=True,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)

	headline_text=models.CharField(
		max_length=70,
		blank=True,
		help_text="Blog listing page header text."
		)

	def get_context(self, request):
		# Update context to include only published, reversed posts
		context = super().get_context(request)
		blogpages = self.get_children().live().order_by('-first_published_at')
		context['blogpages'] = blogpages
		return context

	content_panels = Page.content_panels + [
		ImageChooserPanel("background_image"),
		FieldPanel("headline_text"),
		]

class BlogPage(Page):
	date = models.DateField("Article Date")
	intro = models.TextField("Introduction")
	main_content = StreamField([
		('richtext', SimpleRichTextBlock()),
		('carousel', CarouselBlock()),
		('responsive_image', ResponsiveImageBlock()),
		('card', CardBlock()),
		('flush_list', FlushListBlock()),
		], blank=True)
	featured = models.BooleanField(default=False)

	content_panels = Page.content_panels + [
	FieldPanel('date'),
	FieldPanel('featured'),
	FieldPanel('intro'),
	StreamFieldPanel('main_content'),
	]