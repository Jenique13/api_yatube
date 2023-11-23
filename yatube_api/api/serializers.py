from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Cериализатор models.Post."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'group', 'author', 'pub_date', 'image')
        read_only_fields = ('id', 'pub_date', 'image')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор models.Group."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор models.Comment."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('id', 'post', 'created')
