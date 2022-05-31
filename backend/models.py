from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    title = models.CharField(max_length=64, null=True)

    # If yes this is considered as core tag.
    core_tags = models.BooleanField(null=True)

    # This is for making it easy for recommending the posts
    # to the users.
    derived_from = models.OneToOneField(
        "Tag", on_delete=models.CASCADE, null=True, blank=True
    )

    short_discription = models.CharField(max_length=128, null=True)
    long_discription = models.TextField(max_length=1024, null=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tag")

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    title = models.CharField(max_length=64, null=True)

    # raw_content contains post content in the form of markdown.
    raw_content = models.TextField(max_length=100000, null=True)

    # compiled_content contains post content in form of html markup
    # which can be render.
    compiled_content = models.TextField(max_length=150000, null=True)

    author = models.OneToOneField

    # Relavent tags to this post.
    tags = models.ManyToManyField(Tag)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Post")

    def __str__(self):
        return str(self.title)


class Comment(models.Model):

    # Replies for a comment is also considered as Comments.

    content = models.TextField(max_length=4096, blank=True)

    author = models.OneToOneField(User, on_delete=models.CASCADE)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    # This is set to null by default but if anyone replies to this
    # comment then that comment will be added to this field.
    sub_comments = models.ManyToManyField("Comment", blank=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.author)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    posts_list = models.ManyToManyField(Post, blank=True)

    interested_topics = models.ManyToManyField(Tag, related_name="interested")
    extracted_topics = models.ManyToManyField(Tag, blank=True, related_name="extracted")

    # Here comments and replies are listed
    comments_author = models.ManyToManyField(Comment, blank=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profile")

    def __str__(self):
        return str(self.user)


class UserDataExtending(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, null=True, blank=True
    )

    history = models.ManyToManyField(Post, blank=True)

    class Meta:
        verbose_name = _("User Data Extension")
        verbose_name_plural = "User Data Extension"

    def __str__(self):
        return self.user
