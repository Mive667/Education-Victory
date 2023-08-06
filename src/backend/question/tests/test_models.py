from django.test import TestCase
from django.utils import timezone
from question.models import Category, Question


# class CategoryModelTest(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(name='Test Category', weight=2)

#     def test_category_creation(self):
#         """
#         Test if the Category model can be created correctly.
#         """
#         self.assertEqual(self.category.name, 'Test Category')
#         self.assertEqual(self.category.weight, 2)
#         self.assertLessEqual(self.category.created_at, timezone.now())
#         self.assertLessEqual(self.category.updated_at, timezone.now())
#         self.assertEqual(str(self.category), 'Test Category')

#     def test_default_weight_value(self):
#         """
#         Test if the default weight value is correctly set when not provided.
#         """
#         default_category = Category.objects.create(name='Default Category')
#         self.assertEqual(default_category.weight, 1)

#     def test_category_name_max_length(self):
#         """
#         Test if the name field has the correct max length constraint.
#         """
#         max_length = Category._meta.get_field('name').max_length
#         self.assertEqual(max_length, 30)


class QuestionModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category', weight=2)
        self.question = Question.objects.create(
            name='Test Question',
            description={'content': 'This is a test question.'},
            upvote=10,
            downvote=3,
            publish=True,
            URL='http://example.com/test',
        )
        self.question.category_id_list.add(self.category)

    def test_question_creation(self):
        """
        Test if the Question model can be created correctly.
        """
        self.assertEqual(self.question.name, 'Test Question')
        self.assertEqual(self.question.description, {'content': 'This is a test question.'})
        self.assertEqual(self.question.upvote, 10)
        self.assertEqual(self.question.downvote, 3)
        self.assertTrue(self.question.publish)
        self.assertEqual(self.question.URL, 'http://example.com/test')
        self.assertLessEqual(self.question.created_at, timezone.now())
        self.assertLessEqual(self.question.updated_at, timezone.now())
        self.assertEqual(str(self.question), 'Test Question')

    def test_question_category_relationship(self):
        """
        Test if the question is associated with the correct category.
        """
        self.assertEqual(self.question.category_id_list.count(), 1)
        self.assertEqual(self.question.category_id_list.first(), self.category)

    def test_default_upvote_and_downvote_value(self):
        """
        Test if the default upvote and downvote values are correctly set when not provided.
        """
        default_question = Question.objects.create(name='Default Question',
                                                   description={'content': 'This is a test question.'})
        self.assertEqual(default_question.upvote, 1)
        self.assertEqual(default_question.downvote, 1)

    def test_question_name_max_length(self):
        """
        Test if the name field has the correct max length constraint.
        """
        max_length = Question._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_question_url_max_length(self):
        """
        Test if the URL field has the correct max length constraint.
        """
        max_length = Question._meta.get_field('URL').max_length
        self.assertEqual(max_length, 20)