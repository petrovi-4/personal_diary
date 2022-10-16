from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group', 'image']
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост',
            'image': 'Добавить картинку',
        }
        labels = {
            'text': 'Текст записи',
            'group': 'Группа',
            'image': 'Изображение'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Текст комментария.'}
        help_texts = {'text': 'Напиши сюда текст комментария.'}
