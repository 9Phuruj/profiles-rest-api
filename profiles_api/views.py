from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview =[
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manuallly to URLs',
        ]    
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        