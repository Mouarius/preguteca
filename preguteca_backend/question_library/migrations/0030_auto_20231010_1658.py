# Generated by Django 4.1.7 on 2023-10-10 14:58

from django.db import migrations

def populate_fake_category_description(apps, schema_editor):
    Category = apps.get_model("question_library", "Category")
    for cat in Category.objects.all():
        cat.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eu nisi consequat, dignissim felis et, ultricies risus. Vivamus eget velit sed arcu vehicula convallis non eget elit. Praesent pretium bibendum erat sit amet lacinia. Suspendisse convallis congue turpis rutrum gravida. Nam maximus diam sit amet tortor auctor fringilla. Sed congue, mi at luctus mollis, orci tellus pretium ipsum, ut ullamcorper ante mi sit amet tellus. Fusce sit amet feugiat libero."
        cat.save()


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0029_category_description_and_more"),
    ]

    operations = [ migrations.RunPython(populate_fake_category_description)]
