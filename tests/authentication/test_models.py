from authentication.models import *
from tests.utils.setup import TestSetup
from authentication.api.serializers import HostUserProfileSerializer


class CustomUserModelTestCase(TestSetup):
    
    def test_custom_user_creation(self):
        user = self.create_test_user()
        self.assertTrue(isinstance(user, CustomUser))
        
    def test_custom_superuser_creation(self):
        user = self.create_test_superuser()
        self.assertTrue(user.is_superuser)
        
        
class HostProfileModelTestCase(TestSetup):

    def setUp(self) -> None:
        host_profile_serializer = HostUserProfileSerializer(data={
            'company_name': 'AT & T',
            'company_description': 'Mobile Electronic company',
            'website_url': 'https://atandt.com/',
            'phone_number': '+2348109283458',
            'address': '123 Pharell close',
            'city': 'Southampton',
            'state': 'London',
            'country': 'United Kingdom',
            'zip_code': '12032',
            'twitter': 'https://x.com/atandt/',
            'facebook': 'https://facebook.com/atandt/',
            'instagram': 'https://instagram.com/atandt/'
        })
        host_profile_serializer.is_valid(raise_exception=True)
        self.host_profile = host_profile_serializer.save(user=self.create_test_user())
        return super().setUp()
    
    def test_host_profile(self):
        self.assertTrue(isinstance(self.host_profile, HostUserProfile))
        self.assertEqual(self.host_profile.user.email, 'test@test.com')

        
        
    
        
     
        
