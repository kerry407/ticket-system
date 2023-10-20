from ..utils.setup import APITestSetup 
from django.urls import reverse 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.api.serializers import HostUserProfileSerializer
from authentication.models import HostUserProfile

class AuthTestCase(APITestSetup):
    
    def setUp(self) -> None:
        self.user1 = self.create_test_user()
        self.user2 = self.create_test_superuser()
        return super().setUp()
    
    def test_user_sign_up(self):
        url = reverse("create-account")
        user_data = {
            "email": "patrickonyeogo@gmail.com",
            "password": "Akpororo1",
            "password2": "Akpororo1"
        }
        res = self.client.post(url, user_data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        
        
    def test_login_user(self):
        login_data = {
            "email": "test@test.com",
            "password": "testpassword1"
        }
        res = self.client.post(reverse("token_obtain_pair"), login_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_login_user_with_invalid_credentials(self):
        login_data = {
            "email": "test@test.com",
            "password": "Akpororo1"
        }
        res = self.client.post(reverse("token_obtain_pair"), login_data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_refresh_token(self):
        url = reverse('token_refresh')
        data = {
            "refresh": str(RefreshToken.for_user(self.user2))
        }
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
      

class HostProfileTestCase(APITestSetup):
    
    def setUp(self) -> None:
        self.superuser = self.create_test_superuser()
        self.user = self.create_test_user()
        refresh = RefreshToken.for_user(self.user)
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
        self.host_profile = host_profile_serializer.save(user=self.superuser)
        
        access_token = refresh.access_token
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        return super().setUp()
    
    def test_create_host_profile(self):
        data = {
            'company_name': 'Amazon',
            'company_description': 'Mobile Electronic company',
            'website_url': 'https://amazon.com/',
            'phone_number': '+2348109283458',
            'address': '123 Pharell close',
            'city': 'Southampton',
            'state': 'London',
            'country': 'United Kingdom',
            'zip_code': '12032',
            'twitter': 'https://x.com/amazon/',
            'facebook': 'https://facebook.com/amazon/',
            'instagram': 'https://instagram.com/amazon/'
        }
        
        res = self.client.post(path=reverse('create-event-host-profile'), data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = res.json()['data']['user']
        profile = HostUserProfile.objects.get(user__email=user)
        self.assertTrue(profile.user.event_hoster)
        
        # test again with the same user 
        data['company_name'] = 'Airbus'
        res = self.client.post(path=reverse('create-event-host-profile'), data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        

        
    
        
          
    
        
    
        
    
