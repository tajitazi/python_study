# シリアライザー
# シリアライザーはデータ の入出力を扱い、モデルへの橋渡しをするクラス
# APIのリクエスト/レスポンスに特化した機能を提供

from django.utils.html import linebreaks, urlize
from rest_framework import serializers
from .models import Category, Post

# カテゴリ取得用シリアライザー
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'color',)

# 記事一覧用シリアライザー
class SimplePostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ('main_text', 'created_at')

# 記事詳細用シリアライザー
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    main_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_main_text(self, instance):
        return urlize(linebreaks(instance.main_text))
