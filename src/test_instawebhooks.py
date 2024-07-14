"""
Tests for instawebhooks
"""

from datetime import datetime

import pytest

from instawebhooks import create_embed_json


class MockPost:
    """Mock Post object for testing"""

    def __init__(self):
        self.owner_username = "testuser"
        self.caption = "This is a test caption"
        self.shortcode = "ABC123"
        self.date = datetime.now()
        self.owner_profile = type('', (), {
                                  "full_name": "Test User", "profile_pic_url": "https://example.com/profile.jpg"})()
        self.url = "https://example.com/post.jpg"


@pytest.fixture
def mock_post():
    """Return a mock Post object"""
    return MockPost()


def test_create_embed_json_returns_dict(mock_post):
    """Test that create_embed_json returns a dictionary"""
    embed = create_embed_json(mock_post)
    assert isinstance(embed, dict)


def test_create_embed_json_keys(mock_post):
    """Test that create_embed_json returns a dictionary with the expected keys"""
    embed = create_embed_json(mock_post)
    expected_keys = ["title", "description", "url",
                     "color", "timestamp", "author", "footer", "image"]
    assert all(key in embed for key in expected_keys)


def test_create_embed_json_content(mock_post):
    """Test that create_embed_json returns a dictionary with the expected content"""
    embed = create_embed_json(mock_post)
    assert embed["title"] == mock_post.owner_username
    assert embed["description"] == mock_post.caption
    assert embed["url"] == f"https://instagram.com/p/{mock_post.shortcode}/"
    assert embed["author"]["name"] == mock_post.owner_profile.full_name
    assert embed["image"]["url"] == mock_post.url
