# Generated by Django 3.0.4 on 2020-05-01 18:16

from django.db import migrations
import markdownme.fields


class Migration(migrations.Migration):

    def set_my_defaults(apps, schema_editor):
        series = apps.get_model('blog', 'post')
        for element in series.objects.all().iterator():
            element.summary = element.text
            element.save()

    def reverse_func(apps, schema_editor):
        pass  # code for reverting migration, if any


    dependencies = [
        ('blog', '0003_auto_20200329_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=markdownme.fields.MarkdownField(),
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=markdownme.fields.MarkdownField(null=True, max_length=500),
        ),
        migrations.RunPython(set_my_defaults, reverse_func),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=markdownme.fields.MarkdownField(max_length=500),
        ),
    ]
