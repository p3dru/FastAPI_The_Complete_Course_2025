from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'user'
    assert response.json()['email'] == 'user@user.com'
    assert response.json()['first_name'] == 'user'
    assert response.json()['last_name'] == 'test'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '23478656789'

def test_change_password_sucess(test_user):
    response = client.put('/user/password', json = {'password': 'user1', 'new_password': 'user123'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json = {'password': 'senhaerrada', 'new_password': 'user123'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/2323232')
    assert response.status_code == status.HTTP_204_NO_CONTENT