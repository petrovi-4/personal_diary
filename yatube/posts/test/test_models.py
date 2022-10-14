from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post, Comment, Follow

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.post = Post.objects.create(
            text="а" * 15, author=User.objects.create_user(username="tester")
        )
        cls.TEXT_FIELD = "text"
        cls.GROUP_FIELD = "group"

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        field_verboses = {
            self.TEXT_FIELD: "Текст поста",
            "pub_date": "Дата публикации",
            "author": "Автор",
            self.GROUP_FIELD: "Группа",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    Post._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        field_help_texts = {
            self.TEXT_FIELD: "Введите текст поста",
            self.GROUP_FIELD: "Выберите группу",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    Post._meta.get_field(value).help_text, expected
                )

    def test_post_str(self):
        post = self.post
        expected_object_name = post.text[:15]
        self.assertEquals(expected_object_name, str(post))


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title="Тестовое название", description="Тестовое описание"
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        field_verboses = {
            "title": "Название",
            "slug": "Ссылка",
            "description": "Описание",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    Group._meta.get_field(value).verbose_name, expected
                )

    def test_object_str(self):
        group = GroupModelTest.group
        expected_object_name = group.title
        self.assertEquals(expected_object_name, str(group))


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="auth")
        cls.post = Post.objects.create(
            text="Тестовый пост",
            author=cls.user,
        )
        cls.comment = Comment.objects.create(
            text="Комментарии поста",
            author=cls.user,
            post=cls.post,
        )

    def test_comment_str(self):
        """Проверка __str__ у comment."""
        self.assertEqual(self.comment.text[:15], str(self.comment))

    def test_comment_verbose_name(self):
        """Проверка verbose_name у comments"""
        field_verboses = {
            "post": "Пост",
            "author": "Автор",
            "text": "Комментарий",
            "created": "Создан",
            "updated": "Обновлен",
            "active": "Активен",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.comment._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)


class FollowModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user1 = User.objects.create_user(username="auth1")
        cls.user2 = User.objects.create_user(username="auth2")
        cls.follow = Follow.objects.create(
            user=cls.user1,
            author=cls.user2,
        )

    def test_follow_str(self):
        """Проверка __str__ у follow."""
        self.assertEqual(
            f"{self.follow.user} подписался на {self.follow.author}",
            str(self.follow),
        )

    def test_follow_verbose_name(self):
        """Проверка verbose_name у follow."""
        field_verboses = {
            "user": "Пользователь",
            "author": "Автор",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.follow._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)
