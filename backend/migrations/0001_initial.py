# Generated by Django 4.0.4 on 2022-05-30 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(blank=True, max_length=4096)),
                ("likes", models.PositiveIntegerField(default=0)),
                ("dislikes", models.PositiveIntegerField(default=0)),
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sub_comments",
                    models.ManyToManyField(blank=True, to="backend.comment"),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, null=True)),
                ("raw_content", models.TextField(max_length=100000, null=True)),
                ("compiled_content", models.TextField(max_length=150000, null=True)),
                ("likes", models.PositiveIntegerField(default=0)),
                ("dislikes", models.PositiveIntegerField(default=0)),
                ("time", models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Post",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "comments_author",
                    models.ManyToManyField(blank=True, to="backend.comment"),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profile",
            },
        ),
        migrations.CreateModel(
            name="UserDataExtending",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("history", models.ManyToManyField(blank=True, to="backend.post")),
                (
                    "profile",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.profile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, null=True)),
                ("core_tags", models.BooleanField(null=True)),
                ("short_discription", models.CharField(max_length=128, null=True)),
                ("long_discription", models.TextField(max_length=1024, null=True)),
                (
                    "derived_from",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.tag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tag",
            },
        ),
        migrations.AddField(
            model_name="profile",
            name="extracted_topics",
            field=models.ManyToManyField(
                blank=True, related_name="extracted", to="backend.tag"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="interested_topics",
            field=models.ManyToManyField(related_name="interested", to="backend.tag"),
        ),
        migrations.AddField(
            model_name="profile",
            name="posts_list",
            field=models.ManyToManyField(blank=True, to="backend.post"),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="backend.tag"),
        ),
    ]
