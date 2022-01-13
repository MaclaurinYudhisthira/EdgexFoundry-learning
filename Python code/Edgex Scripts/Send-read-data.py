# env-1\Scripts\activate
# Set-ExecutionPolicy Unrestricted -Scope Process
# python app.py
import requests
import json

edgex_ip    = "localhost"
core_metadata = 59881
core_data = 59880
core_command = 59882 
device_rest = 59986

device_name="Camera-Device-1"
sensor_name="Camera"
def sendData():

    url = f"http://{edgex_ip}:{device_rest}/api/v2/resource/{device_name}/{sensor_name}"
    payload=121
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

    print("Result of sending data: %s with message %s" % (response, response.text))

def readData():

    url = f"http://{edgex_ip}:{core_data}/api/v2/reading/device/name/{device_name}"
    response = requests.get(url)
    print(f"Result for Data read: {response}")
    for a in json.loads(response.text)['readings']:
        print(a['value'])

if __name__ == "__main__":
    sendData()
    readData()
    