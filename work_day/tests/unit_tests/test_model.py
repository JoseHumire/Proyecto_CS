from django.test import TestCase

from work_day.models import *


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='UserTest', password='PasswordTest')
        self.country = Country.objects.create(name='CountryTest')
        self.city = City.objects.create(country=self.country, name='CityTest')
        self.school = School.objects.create(name='SchoolTest', city=self.city)
        self.profession = Profession.objects.create(
            name='ProfessionTest', description='ProfessionDescription')
        self.professional = Professional.objects.create(
            user=self.user, city=self.city, phone='999999999',
            id_number='11111111', birthdate=datetime.date.today()
        )
        self.curriculum = Curriculum.objects.create(
            owner=self.professional, contract_price=100, score=5)
        self.job = Job.objects.create(
            cv=self.curriculum, profession=self.profession,
            description='JobDescription'
        )
        self.study = Study.objects.create(
            cv=self.curriculum, school=self.school,
            profession=self.profession, name='StudyTest'
        )
        self.job_offer = JobOffer.objects.create(
            user=self.professional, city=self.city, description='JobOfferTest',
        )
        self.employment = Employment.objects.create(
            offer=self.job_offer, profession=self.profession,
            description='EmploymentTest', reward=1000,
        )


class CountryModelTests(BaseTest):

    def setUp(self) -> None:
        super().setUp()

    def test_country_is_created_with_the_right_name(self):
        self.assertEqual(self.country.name, 'CountryTest')

    def test_str_function(self):
        self.assertEqual(self.country.__str__(), 'CountryTest')

    def test_cities_related_name_is_correct(self):
        self.assertEqual(len(self.country.cities.all()), 1)


class CityModelTests(BaseTest):

    def setUp(self) -> None:
        super().setUp()

    def test_city_is_created_with_the_right_name(self):
        self.assertEqual(self.city.name, 'CityTest')

    def test_str_function(self):
        self.assertEqual(self.city.__str__(), 'CityTest')


class SchoolModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_school_is_created_with_the_right_name(self):
        self.assertEqual(self.school.name, 'SchoolTest')

    def test_str_function(self):
        self.assertEqual(self.school.__str__(), 'SchoolTest')


class ProfessionModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_profession_is_created_with_the_right_attrs(self):
        self.assertEqual(self.profession.name, 'ProfessionTest')
        self.assertEqual(self.profession.description, 'ProfessionDescription')

    def test_str_function(self):
        self.assertEqual(self.profession.__str__(), 'ProfessionTest')


class ProfessionalModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_professional_is_created_with_the_right_attrs(self):
        self.assertEqual(self.professional.user, self.user)
        self.assertEqual(self.professional.city, self.city)
        self.assertEqual(self.professional.phone, '999999999')
        self.assertEqual(self.professional.id_number, '11111111')
        self.assertEqual(self.professional.birthdate, datetime.date.today())

    def test_str_function(self):
        self.assertEqual(self.professional.__str__(), 'UserTest')

    def test_professional_is_created_with_a_correct_birthdate(self):
        self.assertGreaterEqual(
            self.professional.birthdate, datetime.date.today())


class CurriculumModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_curriculum_is_created_with_the_right_attrs(self):
        self.assertEqual(self.curriculum.owner, self.professional)
        self.assertEqual(self.curriculum.contract_price, 100)
        self.assertEqual(self.curriculum.score, 5)

    def test_str_function(self):
        self.assertEqual(self.curriculum.__str__(), 'UserTest-cv')


class JobModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_job_is_created_with_the_right_attrs(self):
        self.assertEqual(self.job.cv, self.curriculum)
        self.assertEqual(self.job.profession, self.profession)
        self.assertEqual(self.job.description, 'JobDescription')


class StudyModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_study_is_created_with_the_right_attrs(self):
        self.assertEqual(self.study.cv, self.curriculum)
        self.assertEqual(self.study.profession, self.profession)
        self.assertEqual(self.study.name, 'StudyTest')
        self.assertEqual(self.study.school, self.school)


class JobOfferModelTest(BaseTest):
    def setUp(self) -> None:
        super().setUp()

    def test_job_offer_is_created_with_the_right_attrs(self):
        self.assertEqual(self.job_offer.user, self.professional)
        self.assertEqual(self.job_offer.city, self.city)
        self.assertEqual(self.job_offer.description, 'JobOfferTest')

    def test_job_offer_has_related_employments(self):
        self.assertEqual(
            self.job_offer.employments.all().first(), self.employment)
