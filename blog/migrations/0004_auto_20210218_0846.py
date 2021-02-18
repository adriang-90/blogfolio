# Generated by Django 3.1.6 on 2021-02-18 08:46

from django.db import migrations
import streamfieldblocks.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='body',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='main_content',
            field=wagtail.core.fields.StreamField([('responsive_image', streamfieldblocks.models.ResponsiveImageBlock()), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock())]))], blank=True),
        ),
    ]