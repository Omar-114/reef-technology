import requests
import os

email = os.getenv('USER_EMAIL')
password = os.getenv('USER_PASSWORD')
app_token = os.getenv('USER_APP_TOKEN')
REEF_API_URL = "https://mutator.reef.pl"

def retrieve_auth_token():
  url = f"{REEF_API_URL}/v475/members/authentication?app_token={app_token}"
  payload = {
    "email": email,
    "password": password
  }
  try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    global auth_token
    response_result = response.json()
    auth_token = response_result["auth_token"]
    return auth_token
  except requests.exceptions.RequestException as e:
    print("error:", str(e))
    
def retrieve_orgs():
  global auth_token
  url = f"{REEF_API_URL}/v475/groups?app_token={app_token}&auth_token={auth_token}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    global reef_orgs_ids
    response_result = response.json()
    reef_orgs = response_result["organizations"]
    reef_orgs_ids = [org["id"] for org in reef_orgs]
    if not reef_orgs_ids:
      return []
    return reef_orgs_ids
  
  except requests.exceptions.RequestException as e:
    print("error:", str(e))
    return []
    
def retrieve_projects(orgId):
  global auth_token
  url = f"{REEF_API_URL}/v475/groups/{orgId}/tasks?app_token={app_token}&auth_token={auth_token}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    response_result = response.json()
    reef_projects = response_result["projects"]
    return reef_projects
    
  except requests.exceptions.RequestException as e:
    print("error:", str(e))
    return []

def retrieve_staff_members(projId):
  global auth_token
  url = f"{REEF_API_URL}/v475/tasks/{projId}/staff_member?app_token={app_token}&auth_token={auth_token}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    response_result = response.json()
    return response_result["members"]
  except requests.exceptions.RequestException as e:
    print("error:", str(e))
    return []
  
def retrieve_time_sheets(orgId):
  global auth_token
  url = f"{REEF_API_URL}/v475/groups/{orgId}/time_sheets?app_token={app_token}&auth_token={auth_token}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    response_result = response.json()
    return response_result["timesheets"]
  except requests.exceptions.RequestException as e:
    print("error:", str(e))
    return []
  
def retrieve_user(userId):
  global auth_token
  url = f"{REEF_API_URL}/v475/members/{userId}?app_token={app_token}&auth_token={auth_token}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    response_result = response.json()
    return response_result["user"]
  except requests.exceptions.RequestException as e:
    print("error:", str(e))
    return []
  
def retrieve_data():
  reef_orgs_ids = retrieve_orgs()
  first_id = reef_orgs_ids[0]
  
  # Retrieve projects with organization id
  reef_projects = retrieve_projects(first_id)
  staff_for_projects = {}
  for project in reef_projects:
    proj_id = project['id']  # Assuming each project has an 'id' field
    staff_members = retrieve_staff_members(proj_id)
    staff_for_projects[proj_id] = staff_members  # Store staff members by project ID
    
  # Extract unique user_ids
  unique_user_ids = {member['user_id'] for members in staff_for_projects.values() for member in members}

  # Convert user_ids to list
  unique_user_ids_list = list(unique_user_ids)
  
  user_data = {}
  for user_id in unique_user_ids_list:
    user_info = retrieve_user(user_id)
    user_data[user_id] = user_info
        
  time_sheets = retrieve_time_sheets(first_id)

  returnData = {
    "staff_for_projects": staff_for_projects,
    "reef_projects": reef_projects,
    "time_sheets": time_sheets,
    "users": user_data
  }
  return returnData