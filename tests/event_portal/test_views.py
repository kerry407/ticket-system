from ..utils.setup import APITestSetup 
from django.urls import reverse 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from event_portal.models import Category
from event_portal.api.serializers import EventSerializer, CategorySerializer


class CategoryTestCase(APITestSetup):
    
    def setUp(self) -> None:
        self.superuser = self.create_test_superuser()
        refresh = RefreshToken.for_user(self.superuser)
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        category_serializer = CategorySerializer(data={
            "name": "Technology"
        })
        category_serializer.is_valid(raise_exception=True)
        self.category = category_serializer.save()
        return super().setUp()
    
    def test_create_category(self):
        data = {
            "name": "Conferences"
        }
        res = self.client.post(path=reverse('create-category'), data=data)
        user = res.wsgi_request.user
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user.is_staff)
        
    def test_create_category_by_non_staff(self):
        refresh = RefreshToken.for_user(self.create_test_user())
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        data = {
            "name": "Conferences"
        }
        res = self.client.post(path=reverse('create-category'), data=data)
        user = res.wsgi_request.user
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(user.is_staff)
        
    def test_list_category(self):
        res = self.client.get(path=reverse('category-list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_retrieve_category(self):
        res = self.client.get(path=reverse('category-detail', args=[self.category.slug]))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_delete_category(self):
        res = self.client.delete(path=reverse('category-detail', args=[self.category.slug]))
        user = res.wsgi_request.user
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(user.is_staff)
        
    def test_delete_category_by_non_creator(self):
        refresh = RefreshToken.for_user(self.create_test_user())
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        res = self.client.delete(path=reverse('category-detail', args=[self.category.slug]))
        user = res.wsgi_request.user 
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(user.is_staff) 
               


class EventTestCase(APITestSetup):
    
    def setUp(self) -> None:
        self.user = self.create_test_user()
        self.superuser = self.create_test_superuser()
        refresh = RefreshToken.for_user(self.superuser)
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        self.category = Category.objects.create(name="Technology")
        # Event 1
        event_serializer = EventSerializer(data={
            "title": "Bridging the gap between Finance and Technology",
            "event_start_date": "2023-10-30",
            "event_start_time": "12:00:00",
            "event_end_date": "2023-11-01",
            "event_end_time": "06:00:00",
            "location": "Lagos",
            "address": "16, Fawobi Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A tech event"
        })
        event_serializer.is_valid(raise_exception=True)
        self.event = event_serializer.save(host=self.superuser)
        return super().setUp()
    
    def test_create_event(self):
        data = {
            "title": "The Coinessance",
            "event_start_date": "2023-10-30",
            "event_start_time": "12:00:00",
            "event_end_date": "2023-11-01",
            "event_end_time": "06:00:00",
            "location": "Lagos",
            "address": "16, Fawobi Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A blockchain tech event"
        }
        res = self.client.post(path=reverse('create-event'), data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        
    def test_create_event_non_unique_name(self):
        data = {
            "title": "Bridging the gap between Finance and Technology",
            "event_start_date": "2023-10-30",
            "event_start_time": "12:00:00",
            "event_end_date": "2023-11-01",
            "event_end_time": "06:00:00",
            "location": "Lagos",
            "address": "16, Fawobi Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A tech event"
        }
        res = self.client.post(path=reverse('create-event'), data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_list_event(self):
        res = self.client.get(path=reverse('events-list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_filter_event_list(self):
        res = self.client.get(path=reverse('events-list') + "?category__name=Conferences")
        results = res.json()['data']['results']
        self.assertEqual(len(results), 0)
        
    def test_retrieve_event(self):
        res = self.client.get(path=reverse('event-detail', args=[self.event.slug]))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_update_event(self):
        data = {
            "title": "Bridging the gap between Finance and Technology",
            "event_start_date": "2023-10-19",
            "event_start_time": "12:00:00",
            "event_end_date": "2023-10-21",
            "event_end_time": "06:00:00",
            "location": "Lagos",
            "address": "16, Adeleke Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A tech event"
        }
        res = self.client.put(path=reverse('event-detail', args=[self.event.slug]), data=data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_update_event_by_non_creator(self):
        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        data = {
            "title": "Bridging the gap between Finance and Technology",
            "event_start_date": "2023-10-19",
            "event_start_time": "12:00:00",
            "event_end_date": "2023-10-21",
            "event_end_time": "06:00:00",
            "location": "Lagos",
            "address": "16, Adeleke Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A tech event"
        }
        res = self.client.put(path=reverse('event-detail', args=[self.event.slug]), data=data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_partial_update_event(self):
        data = {
            "address": "16, Adeleke Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A technology event"
        }
        res = self.client.patch(path=reverse('event-detail', args=[self.event.slug]), data=data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_partial_update_event_by_non_creator(self):
        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        data = {
            "address": "16, Adeleke Street, Allen Avenue, Ikeja",
            "category": [
                self.category.id
            ],
            "about": "A technology event"
        }
        res = self.client.patch(path=reverse('event-detail', args=[self.event.slug]), data=data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_delete_event(self):
        res = self.client.delete(path=reverse('event-detail', args=[self.event.slug]))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_delete_event(self):
        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token 
        self.client.credentials(HTTP_AUTHORIZATION= f"Bearer {access_token}")
        res = self.client.delete(path=reverse('event-detail', args=[self.event.slug]))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        

        