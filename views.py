from rest_framework.decorators import api_view
from rest_framework.response import Response

# This view returns the current user details
@api_view(['GET'])
def current_user(request):
    user = request.user
    if request.user.is_authenticated:
        return Response({
            'auth': 1,
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })
    else:
        return Response({'auth': '0'}, status=401)
