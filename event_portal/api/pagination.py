from rest_framework.pagination import PageNumberPagination 

class CustomPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "max-size"
    max_page_size = 15