from django.test import TestCase  
from django.contrib.auth import get_user_model 
from authentication.models import CustomUser
from rest_framework.test import APITestCase
from typing import Dict, Any 
from authentication.api.serializers import * 

User = get_user_model()


class TestSetup(TestCase):
    
    def setUp(self) -> None:
        print(f"Starting test for {str(self)}...")
        print("---------------")
        return super().setUp()
        
    def create_test_user(self, **kwargs: Dict[str, Any]) -> CustomUser:
        user_serializer = AccountSerializer(data={
            'email': 'test@test.com',
            'first_name': 'test',
            'last_name': 'test&test',
            'password': 'testpassword1',
            'password2': 'testpassword1'
        })
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return user
    
    def create_test_superuser(self, **kwargs: Dict[str, Any]) -> CustomUser:
        user = User.objects.create_superuser(
            email='test2@test.com', first_name='test',
            last_name='test&test', password="Akpororo1", 
            event_hoster=True
        )
        return user
        
    
    def tearDown(self) -> None:
        print(f"Finished test for {str(self)}...")
        print("---------------")
        return super().tearDown()
        

class APITestSetup(APITestCase):
    
    def setUp(self) -> None:
        print(f"Starting test for {str(self)}...")
        print("---------------")
        return super().setUp()
    
    def create_test_user(self, **kwargs: Dict[str, Any]) -> CustomUser:
        user_serializer = AccountSerializer(data={
            'email': 'test@test.com',
            'password': 'testpassword1',
            'password2': 'testpassword1'
        })
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return user
    
    def create_test_superuser(self, **kwargs: Dict[str, Any]) -> CustomUser:
        user = User.objects.create_superuser(
            email='test2@test.com',  password="Akpororo1", 
        )
        return user
    
    def tearDown(self) -> None:
        print(f"Finished test for {str(self)}...")
        print("---------------")
        return super().tearDown()
    
     
        
