import requests

bd_server = ""
base_url = "https://"+bd_server
auth_url = base_url+"/api/tokens/authenticate"


api_token = ""
payload={}




headers = {
  'Content-Type': 'application/json',
  'Authorization': 'token '+api_token
}

response = requests.request("POST", auth_url, headers=headers, data=payload, verify=False)

bearerToken = response.json()['bearerToken']
xcsrfToken = response.headers['X-CSRF-TOKEN']

if bearerToken:
    print("Got Bearer Token.")
if xcsrfToken:
    print("Got X-CSRF Token.")
    
#print("BearerToken: ", bearerToken)
#print("X-CSRF Token: ", xcsrfToken)



headers = {
  'Accept':'application/vnd.blackducksoftware.component-detail-5+json',
  'Content-Type':'application/json',
  'Authorization':'bearer '+bearerToken,
  'X-CSRF-TOKEN':xcsrfToken
}

componentId="ce7ad18a-6e02-4565-a51c-4fc2c5bc7c47"
componentVersionId="a24dfb9f-877a-4fce-9ac8-cacf0a72e0b6"

comp_ver_url = base_url+"/api/components/"+componentId+"/versions/"+componentVersionId


#GET the component version in the BOM of the project version and determine usage
#either GET /api/projects/{projectId}/versions/{projectVersionId}/components or GET /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}
#If it's anything other than the desired usage, perform a PUT to update usage 
#PUT /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}


response = requests.request("GET", comp_ver_url, headers=headers, verify=False)



