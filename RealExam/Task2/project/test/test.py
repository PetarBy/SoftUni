import unittest
from project.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.social_media = SocialMedia("test_user", "Instagram", 1000, "photo")

    def test_correct_init(self):
        self.assertEqual(self.social_media.username, "test_user")
        self.assertEqual(self.social_media.platform, "Instagram")
        self.assertEqual(self.social_media.followers, 1000)
        self.assertEqual(self.social_media.content_type, "photo")
        self.assertEqual(len(self.social_media._posts), 0)

    def test_platform_setter_valid_platform(self):
        self.social_media.platform = "YouTube"
        self.assertEqual(self.social_media.platform, "YouTube")

    def test_platform_setter_invalid_platform(self):
        with self.assertRaises(ValueError):
            self.social_media.platform = "Snapchat"

    def test_followers_setter_negative_followers(self):
        with self.assertRaises(ValueError):
            self.social_media.followers = -100

    def test_create_post(self):
        self.assertEqual(self.social_media.create_post("Test post"), "New photo post created by test_user on Instagram.")

    def test_like_post_within_limit(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.like_post(0), "Post liked by test_user.")

    def test_like_post_exceed_limit(self):
        self.social_media.create_post("Test post")
        for _ in range(10):
            self.social_media.like_post(0)
        self.assertEqual(self.social_media.like_post(0), "Post has reached the maximum number of likes.")

    def test_like_post_invalid_index(self):
        self.assertEqual(self.social_media.like_post(0), "Invalid post index.")

    def test_comment_on_post_valid_comment(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "This is a test comment."), "Comment added by test_user on the post.")

    def test_comment_on_post_invalid_comment(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Short"), "Comment should be more than 10 characters.")


if __name__ == '__main__':
    unittest.main()
