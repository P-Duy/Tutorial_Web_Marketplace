# Generated by Django 4.1.7 on 2023-04-11 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ('-modified_ad',)},
        ),
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='Conversation',
            new_name='conversation',
        ),
    ]
