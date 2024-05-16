import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_save(self):
        initial_updated_at = self.base_model.updated_at
        with patch('models.base_model.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 5, 17)  # Mock datetime.now() to return a fixed value
            self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)
        self.assertEqual(self.base_model.updated_at, datetime(2024, 5, 17))

    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
