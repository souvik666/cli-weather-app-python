import requests
import weatherstack

params = {
  'query': input("please select your location:\n")
}
api_result = requests.get('http://api.weatherstack.com/current?access_key=put your key here', params)

api_response = api_result.json()
print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))