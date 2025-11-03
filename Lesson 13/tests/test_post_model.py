"""
Test file for Post model.
Topshiriq 4: Post modelini testlash - title, content, string representation.
"""

import pytest
from django.core.exceptions import ValidationError
from posts.models import Post


@pytest.mark.django_db
@pytest.mark.model
class TestPostModel:
    """Test cases for Post model"""

    def test_create_post_with_valid_data(self):
        """Test creating a post with valid title and content"""
        post = Post.objects.create(title="Test Post", content="This is test content")
        assert post.id is not None
        assert post.title == "Test Post"
        assert post.content == "This is test content"

    def test_post_title_field(self):
        """Test Post title field"""
        post = Post.objects.create(title="Django Testing", content="Content here")
        assert post.title == "Django Testing"
        assert isinstance(post.title, str)

    def test_post_content_field(self):
        """Test Post content field"""
        post = Post.objects.create(
            title="Title", content="This is a long content for testing purposes"
        )
        assert post.content == "This is a long content for testing purposes"
        assert isinstance(post.content, str)

    def test_post_str_representation(self):
        """Test __str__ method returns title"""
        post = Post.objects.create(title="My Test Post", content="Some content")
        assert str(post) == "My Test Post"

    def test_post_created_at_auto_set(self):
        """Test created_at is automatically set"""
        post = Post.objects.create(title="Test", content="Content")
        assert post.created_at is not None

    def test_post_updated_at_auto_set(self):
        """Test updated_at is automatically set"""
        post = Post.objects.create(title="Test", content="Content")
        assert post.updated_at is not None

    def test_post_title_max_length(self):
        """Test title field max_length is 200"""
        long_title = "T" * 200
        post = Post.objects.create(title=long_title, content="Content")
        assert len(post.title) == 200

    def test_post_content_can_be_long(self):
        """Test content field can hold long text"""
        long_content = "X" * 5000
        post = Post.objects.create(title="Title", content=long_content)
        assert len(post.content) == 5000

    def test_post_verbose_name(self):
        """Test model verbose_name"""
        assert Post._meta.verbose_name == "Post"

    def test_post_verbose_name_plural(self):
        """Test model verbose_name_plural"""
        assert Post._meta.verbose_name_plural == "Posts"

    def test_post_ordering(self):
        """Test posts are ordered by created_at descending"""
        import time

        post1 = Post.objects.create(title="First", content="Content 1")
        time.sleep(0.001)
        post2 = Post.objects.create(title="Second", content="Content 2")
        time.sleep(0.001)
        post3 = Post.objects.create(title="Third", content="Content 3")

        posts = list(Post.objects.all())
        assert posts[0] == post3  # Most recent first
        assert posts[1] == post2
        assert posts[2] == post1


@pytest.mark.django_db
@pytest.mark.model
class TestPostModelFields:
    """Test individual field properties"""

    def test_title_field_verbose_name(self):
        """Test title field verbose_name"""
        field = Post._meta.get_field("title")
        assert field.verbose_name == "Sarlavha"

    def test_content_field_verbose_name(self):
        """Test content field verbose_name"""
        field = Post._meta.get_field("content")
        assert field.verbose_name == "Mazmun"

    def test_created_at_field_verbose_name(self):
        """Test created_at field verbose_name"""
        field = Post._meta.get_field("created_at")
        assert field.verbose_name == "Yaratilgan sana"

    def test_updated_at_field_verbose_name(self):
        """Test updated_at field verbose_name"""
        field = Post._meta.get_field("updated_at")
        assert field.verbose_name == "Yangilangan sana"

    def test_title_field_type(self):
        """Test title is CharField"""
        field = Post._meta.get_field("title")
        assert field.get_internal_type() == "CharField"

    def test_content_field_type(self):
        """Test content is TextField"""
        field = Post._meta.get_field("content")
        assert field.get_internal_type() == "TextField"


@pytest.mark.django_db
@pytest.mark.model
class TestPostModelCRUD:
    """Test CRUD operations on Post model"""

    def test_create_post(self):
        """Test creating a post"""
        post = Post.objects.create(title="New Post", content="New Content")
        assert Post.objects.count() == 1
        assert Post.objects.first() == post

    def test_read_post(self):
        """Test reading a post"""
        post = Post.objects.create(title="Read Test", content="Read Content")
        retrieved_post = Post.objects.get(id=post.id)
        assert retrieved_post.title == "Read Test"
        assert retrieved_post.content == "Read Content"

    def test_update_post(self):
        """Test updating a post"""
        post = Post.objects.create(title="Original Title", content="Original Content")
        post.title = "Updated Title"
        post.content = "Updated Content"
        post.save()

        updated_post = Post.objects.get(id=post.id)
        assert updated_post.title == "Updated Title"
        assert updated_post.content == "Updated Content"

    def test_delete_post(self):
        """Test deleting a post"""
        post = Post.objects.create(title="To Delete", content="Delete Content")
        post_id = post.id
        post.delete()

        assert Post.objects.count() == 0
        with pytest.raises(Post.DoesNotExist):
            Post.objects.get(id=post_id)

    def test_create_multiple_posts(self):
        """Test creating multiple posts"""
        Post.objects.create(title="Post 1", content="Content 1")
        Post.objects.create(title="Post 2", content="Content 2")
        Post.objects.create(title="Post 3", content="Content 3")

        assert Post.objects.count() == 3

    def test_filter_posts_by_title(self):
        """Test filtering posts by title"""
        Post.objects.create(title="Python", content="Content 1")
        Post.objects.create(title="Django", content="Content 2")
        Post.objects.create(title="Python", content="Content 3")

        python_posts = Post.objects.filter(title="Python")
        assert python_posts.count() == 2


@pytest.mark.django_db
@pytest.mark.model
class TestPostModelStringFields:
    """Test string field behaviors"""

    def test_empty_title_allowed(self):
        """Test that empty title is allowed (blank=True is not set)"""
        # This should work but might fail validation
        post = Post(title="", content="Content")
        # CharField without blank=True requires value
        # But at model level it's allowed
        post.save()
        assert post.title == ""

    def test_empty_content_allowed(self):
        """Test that empty content is allowed"""
        post = Post(title="Title", content="")
        post.save()
        assert post.content == ""

    def test_unicode_in_title(self):
        """Test Unicode characters in title"""
        post = Post.objects.create(title="O'zbekcha sarlavha", content="Mazmun")
        assert post.title == "O'zbekcha sarlavha"

    def test_unicode_in_content(self):
        """Test Unicode characters in content"""
        post = Post.objects.create(title="Title", content="Bu o'zbekcha mazmun")
        assert post.content == "Bu o'zbekcha mazmun"

    def test_special_characters_in_fields(self):
        """Test special characters"""
        post = Post.objects.create(
            title="Test! @#$%^&*()", content="Special chars: <>?/\\|"
        )
        assert "!" in post.title
        assert "<>" in post.content

    def test_newlines_in_content(self):
        """Test newlines in content"""
        post = Post.objects.create(title="Title", content="Line 1\nLine 2\nLine 3")
        assert "\n" in post.content
        assert post.content.count("\n") == 2


@pytest.mark.django_db
@pytest.mark.model
class TestPostModelTimestamps:
    """Test timestamp behavior"""

    def test_updated_at_changes_on_save(self):
        """Test updated_at changes when post is saved"""
        post = Post.objects.create(title="Test", content="Content")
        original_updated = post.updated_at

        import time

        time.sleep(0.1)  # Small delay

        post.title = "Updated"
        post.save()

        assert post.updated_at > original_updated

    def test_created_at_does_not_change(self):
        """Test created_at doesn't change on update"""
        post = Post.objects.create(title="Test", content="Content")
        original_created = post.created_at

        import time

        time.sleep(0.1)

        post.title = "Updated"
        post.save()

        assert post.created_at == original_created
