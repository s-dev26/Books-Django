from django.test import TestCase
from django.utils import timezone
from .models import *

class ModelTestCase(TestCase):
    def setUp(self):
        self.slide1 = Slide.objects.create(image='test_slide1.jpg')
        self.slide2 = Slide.objects.create(image='test_slide2.png')
        self.home_section = HomeSection.objects.create(
            title='Test Home Section',
            content='Lorem ipsum dolor sit amet',
        )
        self.home_section.slides.add(self.slide1, self.slide2)
        self.book = Book.objects.create(
            title='Test Book',
            price=20.00,
            image='test_book.jpg',
        )
        self.noveltie = Noveltie.objects.create(
            title='Test Noveltie',
            image='test_noveltie.jpg',
            content='Lorem ipsum dolor sit amet',
            price=15.00,
            pub_date=timezone.now(),
        )
        self.announcement = Announcement.objects.create(
            title='Test Announcement',
            description='Lorem ipsum dolor sit amet',
            image='test_announcement.jpg',
        )
        self.review = Review.objects.create(
            author='Test Author',
            rating=4,
            content='Lorem ipsum dolor sit amet',
        )

    def test_slide_creation(self):
        self.assertEqual(self.slide1.image, 'test_slide1.jpg')
        self.assertEqual(self.slide2.image, 'test_slide2.png')
        self.assertEqual(Slide.objects.count(), 2)

    def test_home_section_creation(self):
        self.assertEqual(self.home_section.title, 'Test Home Section')
        self.assertEqual(self.home_section.content, 'Lorem ipsum dolor sit amet')
        self.assertEqual(self.home_section.slides.count(), 2)

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(float(self.book.price), 20.00)
        self.assertEqual(self.book.image, 'test_book.jpg')

    def test_noveltie_creation(self):
        self.assertEqual(self.noveltie.title, 'Test Noveltie')
        self.assertEqual(self.noveltie.content, 'Lorem ipsum dolor sit amet')
        self.assertEqual(float(self.noveltie.price), 15.00)
        self.assertIsNotNone(self.noveltie.pub_date)

    def test_announcement_creation(self):
        self.assertEqual(self.announcement.title, 'Test Announcement')
        self.assertEqual(self.announcement.description, 'Lorem ipsum dolor sit amet')
        self.assertEqual(self.announcement.image, 'test_announcement.jpg')

    def test_review_creation(self):
        self.assertEqual(self.review.author, 'Test Author')
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.content, 'Lorem ipsum dolor sit amet')
        self.assertEqual(list(self.review.get_stars()), [1, 2, 3, 4])
