#!/usr/bin/python3
"""Defines Unittest cases for Review class"""

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_review_instance(self):
        """Tests Review instance creation and attributes"""

        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_review_attributes(self):
        """Tests Review attributes"""

        review = Review()
        review.place_id = "568"
        review.user_id = "6598"
        review.text = "Acc 6598: Awaiting your arival"
        self.assertEqual(review.place_id, "568")
        self.assertEqual(review.user_id, "6598")
        self.assertEqual(review.text, "Acc 6598: Awaiting your arival")

if __name__ == "__main__":
    unittest.main()
