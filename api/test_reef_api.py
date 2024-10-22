import os
import unittest
from unittest.mock import patch
from api.reef_api import retrieve_auth_token, retrieve_orgs, retrieve_projects, retrieve_staff_members, retrieve_time_sheets, retrieve_user

app_token = os.getenv('USER_APP_TOKEN')

class TestReefAPI(unittest.TestCase):

  @patch('api.reef_api.requests.post')
  def test_retrieve_auth_token(self, mock_post):
    # Mock response
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"auth_token": "test_token"}
    
    auth_token = retrieve_auth_token()  # Call the function that sets the global variable
    self.assertEqual(auth_token, "test_token")  # Assert the global variable's value

  @patch('api.reef_api.requests.get')
  def test_retrieve_orgs(self, mock_get):
    # Mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"organizations": [{"id": 1}]}
    
    orgs = retrieve_orgs()
    self.assertEqual(orgs, [1])

  @patch('api.reef_api.requests.get')
  def test_retrieve_projects(self, mock_get):
    # Mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"projects": [{'id': 3144968, 'name': 'Project B', 'created_at': '2024-09-11T11:41:34.577974Z', 'updated_at': '2024-09-11T11:41:34.577974Z', 'status': 'active', 'billable': True, 'metadata': {}}, 
                                                            {'id': 3144969, 'name': 'hubstaff bot818', 'created_at': '2024-09-11T11:41:34.744013Z', 'updated_at': '2024-09-11T11:41:34.744013Z', 'status': 'active', 'billable': True, 'metadata': {}}, 
                                                            {'id': 3144970, 'name': 'Project A', 'created_at': '2024-09-11T11:41:34.901344Z', 'updated_at': '2024-09-11T11:41:34.901344Z', 'status': 'active', 'billable': True, 'metadata': {}}]}
    
    projects = retrieve_projects(601669)
    self.assertEqual(projects, [{'id': 3144968, 'name': 'Project B', 'created_at': '2024-09-11T11:41:34.577974Z', 'updated_at': '2024-09-11T11:41:34.577974Z', 'status': 'active', 'billable': True, 'metadata': {}},
                                {'id': 3144969, 'name': 'hubstaff bot818', 'created_at': '2024-09-11T11:41:34.744013Z', 'updated_at': '2024-09-11T11:41:34.744013Z', 'status': 'active', 'billable': True, 'metadata': {}}, {'id': 3144970, 'name': 'Project A', 'created_at': '2024-09-11T11:41:34.901344Z', 'updated_at': '2024-09-11T11:41:34.901344Z', 'status': 'active', 'billable': True, 'metadata': {}}])

  @patch('api.reef_api.requests.get')
  def test_retrieve_staff_members(self, mock_get):
    # Mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"members": [{'user_id': 2865091, 'currency': 'USD', 'membership_role': 'manager', 'membership_status': 'active', 'created_at': '2024-09-11T17:21:15.834262Z', 'updated_at': '2024-09-11T17:21:15.834262Z', 'last_client_activity': None}]}
    
    staff_members = retrieve_staff_members(3144968)
    self.assertEqual(staff_members, [{'user_id': 2865091, 'currency': 'USD', 'membership_role': 'manager', 'membership_status': 'active', 'created_at': '2024-09-11T17:21:15.834262Z', 'updated_at': '2024-09-11T17:21:15.834262Z', 'last_client_activity': None}])

  @patch('api.reef_api.requests.get')
  def test_retrieve_time_sheets(self, mock_get):
    # Mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"timesheets": []}
    
    time_sheets = retrieve_time_sheets(601669)
    self.assertEqual(time_sheets, [])

  @patch('api.reef_api.requests.get')
  def test_retrieve_user(self, mock_get):
    # Mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"user": {'id': 2865091, 'name': 'Alex Drigpaul', 'first_name': 'Alex', 'last_name': 'Drigpaul', 'email': 'alexdrigpaul8@gmail.com', 'time_zone': 'America/New_York', 'ip_address': '2603:7000:ca01:8d57:a4ec:784b:8177:b140', 'status': 'active', 'created_at': '2024-09-11T17:21:15.199010Z', 'updated_at': '2024-09-12T19:45:46.788500Z'}}
    
    user = retrieve_user(2865091)
    self.assertEqual(user, {'id': 2865091, 'name': 'Alex Drigpaul', 'first_name': 'Alex', 'last_name': 'Drigpaul', 'email': 'alexdrigpaul8@gmail.com', 'time_zone': 'America/New_York', 'ip_address': '2603:7000:ca01:8d57:a4ec:784b:8177:b140', 'status': 'active', 'created_at': '2024-09-11T17:21:15.199010Z', 'updated_at': '2024-09-12T19:45:46.788500Z'})

if __name__ == '__main__':
  unittest.main()
