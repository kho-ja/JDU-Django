"""
Test file for Post views.
Topshiriq 5: Post viewlarini testlash - list va create operatsiyalar.
"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from posts.models import Post


@pytest.fixture
def api_client():
    """Fixture to provide API client"""
    return APIClient()


@pytest.fixture
def sample_post():
    """Fixture to create a sample post"""
    return Post.objects.create(
        title="Sample Post", content="Sample content for testing"
    )


@pytest.fixture
def multiple_posts():
    """Fixture to create multiple posts"""
    import time

    posts = []
    for i in range(5):
        posts.append(Post.objects.create(title=f"Post {i}", content=f"Content {i}"))
        time.sleep(0.001)  # Small delay to ensure different timestamps
    return posts


@pytest.mark.django_db
@pytest.mark.view
class TestPostListView:
    """Test cases for Post list endpoint"""

    def test_get_empty_post_list(self, api_client):
        """Test GET request with no posts"""
        url = reverse("post-list-create")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

    def test_get_post_list_with_posts(self, api_client, multiple_posts):
        """Test GET request returns all posts"""
        url = reverse("post-list-create")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5

    def test_post_list_returns_correct_fields(self, api_client, sample_post):
        """Test response contains correct fields"""
        url = reverse("post-list-create")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

        post_data = response.data[0]
        assert "id" in post_data
        assert "title" in post_data
        assert "content" in post_data
        assert "created_at" in post_data
        assert "updated_at" in post_data

    def test_post_list_ordering(self, api_client, multiple_posts):
        """Test posts are ordered by created_at descending"""
        url = reverse("post-list-create")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        # Most recent post should be first
        assert response.data[0]["title"] == "Post 4"

    def test_post_list_content_type(self, api_client, sample_post):
        """Test response content type is JSON"""
        url = reverse("post-list-create")
        response = api_client.get(url)

        assert response["Content-Type"] == "application/json"


@pytest.mark.django_db
@pytest.mark.view
class TestPostCreateView:
    """Test cases for Post create endpoint"""

    def test_create_post_with_valid_data(self, api_client):
        """Test creating a post with valid data"""
        url = reverse("post-list-create")
        data = {"title": "New Post", "content": "New post content"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert "message" in response.data
        assert response.data["message"] == "Post muvaffaqiyatli yaratildi!"
        assert "data" in response.data
        assert response.data["data"]["title"] == "New Post"
        assert response.data["data"]["content"] == "New post content"

    def test_create_post_saves_to_database(self, api_client):
        """Test that created post is saved to database"""
        url = reverse("post-list-create")
        data = {"title": "Database Test", "content": "Testing database save"}

        initial_count = Post.objects.count()
        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.count() == initial_count + 1

        # Verify the post exists in database
        post = Post.objects.get(title="Database Test")
        assert post.content == "Testing database save"

    def test_create_post_without_title(self, api_client):
        """Test creating post without title returns error"""
        url = reverse("post-list-create")
        data = {"content": "Content without title"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "title" in response.data

    def test_create_post_without_content(self, api_client):
        """Test creating post without content returns error"""
        url = reverse("post-list-create")
        data = {"title": "Title without content"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "content" in response.data

    def test_create_post_with_empty_title(self, api_client):
        """Test creating post with empty title"""
        url = reverse("post-list-create")
        data = {"title": "", "content": "Content"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_post_with_empty_content(self, api_client):
        """Test creating post with empty content"""
        url = reverse("post-list-create")
        data = {"title": "Title", "content": ""}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_post_with_long_title(self, api_client):
        """Test creating post with maximum length title"""
        url = reverse("post-list-create")
        data = {
            "title": "T" * 200,  # Max length
            "content": "Content",
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_post_with_too_long_title(self, api_client):
        """Test creating post with title exceeding max length"""
        url = reverse("post-list-create")
        data = {
            "title": "T" * 201,  # Over max length
            "content": "Content",
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_post_with_long_content(self, api_client):
        """Test creating post with very long content"""
        url = reverse("post-list-create")
        data = {
            "title": "Title",
            "content": "X" * 10000,  # Very long content
        }

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_post_response_includes_id(self, api_client):
        """Test created post response includes ID"""
        url = reverse("post-list-create")
        data = {"title": "Test Post", "content": "Test Content"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert "id" in response.data["data"]
        assert response.data["data"]["id"] is not None

    def test_create_post_response_includes_timestamps(self, api_client):
        """Test created post response includes timestamps"""
        url = reverse("post-list-create")
        data = {"title": "Test Post", "content": "Test Content"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert "created_at" in response.data["data"]
        assert "updated_at" in response.data["data"]


@pytest.mark.django_db
@pytest.mark.view
class TestPostViewIntegration:
    """Integration tests for Post views"""

    def test_create_and_retrieve_post(self, api_client):
        """Test creating a post and then retrieving it"""
        url = reverse("post-list-create")

        # Create post
        create_data = {
            "title": "Integration Test",
            "content": "Integration test content",
        }
        create_response = api_client.post(url, create_data, format="json")
        assert create_response.status_code == status.HTTP_201_CREATED

        # Retrieve posts
        list_response = api_client.get(url)
        assert list_response.status_code == status.HTTP_200_OK
        assert len(list_response.data) == 1
        assert list_response.data[0]["title"] == "Integration Test"

    def test_create_multiple_posts_and_list(self, api_client):
        """Test creating multiple posts and listing them"""
        url = reverse("post-list-create")

        # Create 3 posts
        for i in range(3):
            data = {"title": f"Post {i}", "content": f"Content {i}"}
            response = api_client.post(url, data, format="json")
            assert response.status_code == status.HTTP_201_CREATED

        # List all posts
        list_response = api_client.get(url)
        assert list_response.status_code == status.HTTP_200_OK
        assert len(list_response.data) == 3

    def test_database_consistency(self, api_client):
        """Test database and API response consistency"""
        url = reverse("post-list-create")
        data = {"title": "Consistency Test", "content": "Testing consistency"}

        response = api_client.post(url, data, format="json")
        post_id = response.data["data"]["id"]

        # Check database
        db_post = Post.objects.get(id=post_id)
        assert db_post.title == "Consistency Test"
        assert db_post.content == "Testing consistency"

        # Check API response
        assert response.data["data"]["title"] == db_post.title
        assert response.data["data"]["content"] == db_post.content


@pytest.mark.django_db
@pytest.mark.view
class TestPostViewSpecialCases:
    """Test special cases and edge cases"""

    def test_create_post_with_unicode(self, api_client):
        """Test creating post with Unicode characters"""
        url = reverse("post-list-create")
        data = {"title": "O'zbekcha sarlavha", "content": "Bu o'zbekcha mazmun"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["data"]["title"] == "O'zbekcha sarlavha"

    def test_create_post_with_special_characters(self, api_client):
        """Test creating post with special characters"""
        url = reverse("post-list-create")
        data = {"title": "Test! @#$%", "content": "Content with <html> tags"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_post_with_newlines(self, api_client):
        """Test creating post with newlines in content"""
        url = reverse("post-list-create")
        data = {"title": "Multiline", "content": "Line 1\nLine 2\nLine 3"}

        response = api_client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert "\n" in response.data["data"]["content"]

    def test_url_accessibility(self, api_client):
        """Test that URL is accessible"""
        url = reverse("post-list-create")
        response = api_client.get(url)

        assert response.status_code in [200, 201, 204]

    def test_method_not_allowed(self, api_client):
        """Test that unsupported methods return 405"""
        url = reverse("post-list-create")

        # PUT should not be allowed on list endpoint
        response = api_client.put(url, {}, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        # DELETE should not be allowed on list endpoint
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
@pytest.mark.view
@pytest.mark.parametrize(
    "title,content",
    [
        ("Test 1", "Content 1"),
        ("Test 2", "Content 2"),
        ("Python", "Django REST Framework"),
        ("Short", "X"),
        ("Numbers", "123456789"),
    ],
)
def test_create_post_parametrized(api_client, title, content):
    """Parametrized test for creating posts with different data"""
    url = reverse("post-list-create")
    data = {"title": title, "content": content}

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["data"]["title"] == title
    assert response.data["data"]["content"] == content
