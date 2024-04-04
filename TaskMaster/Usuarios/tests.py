from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .views import borrar_usuario

# Create your tests here.
def test_borrar_usuario():
    # Create a test user
    user = User.objects.create(username='testuser')

    # Create a RequestFactory object
    factory = RequestFactory()

    # Create a request object with the authenticated user
    request = factory.delete(reverse('borrar_usuario', kwargs={'id': user.id}))
    request.user = user

    # Test the view with the request object
    response = borrar_usuario(request, user.id)

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the user has been deleted
    assert User.objects.filter(id=user.id).count() == 0