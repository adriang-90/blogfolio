from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks

# Create your models here.
class ResponsiveImageBlock(ImageChooserBlock):
	class Meta:
		icon = "image"
		template = "streamfieldblocks/responsive_image_block.html"

class CardBlock(blocks.StructBlock):
	image = ImageChooserBlock(required=False)
	title = blocks.CharBlock()
	body = blocks.TextBlock()
	page_link = blocks.PageChooserBlock()

	class Meta:
		icon = "placeholder"
		template = "streamfieldblocks/card_block.html"

class SimpleRichTextBlock(blocks.StructBlock):
	richtext = blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul'])

	class Meta:
		icon = "pilcrow"
		template = "streamfieldblocks/simple_richtext_block.html"

class CarouselBlock(blocks.StreamBlock):
	image = ImageChooserBlock()

	class Meta:
		icon = "cog"
		template = "streamfieldblocks/carousel_block.html"

class FlushListBlock(blocks.StructBlock):
	items = blocks.ListBlock(
		blocks.TextBlock(help_text="List item's body text.")
		)

	class Meta:
		icon = "list-ul"
		template = "streamfieldblocks/flish_list_block.html"