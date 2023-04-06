from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=50, read_only=True)
    author_last_name = serializers.CharField(max_length=50, read_only=True)
    author_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image"
        ]

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'title', 'image', 'price', 'description', 'author', 'created_at']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.CharField(source='author.id', read_only=True)


    class Meta:
        model = Ad
        fields = ['pk', 'title', 'image', 'price', 'description', 'author', 'created_at', 'author_first_name',
                  'author_last_name', 'author_id']

