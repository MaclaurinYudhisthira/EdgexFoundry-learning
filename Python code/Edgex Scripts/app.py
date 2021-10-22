import requests

edgex_ip    = "localhost"
core-metadata = 59881
core-data = 59880
core-command = 59882 

# def createAddressables():

#     # Create the addressable for the device. 
#     # This tells EdgeX Foundry how to find the device 
#     url = f"http://{edgex_ip}:{core-metadata}/api/v1/addressable" 
#     # Core metadata

#     payload = {
#         "name":"PiCamera",
#         "protocol":"HTTP",
#         "address":"localhost",
#         "port":5000,
#         "path":"/api/v2/device/register" # REST endpoint on the test app
#     }
#     headers = {'content-type': 'application/json'}
#     response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
#     print("Result for createAddressables: %s - Message: %s" % (response, response.text))

# Value descriptors are what they sound like: Describing data values
# Note that these correspond to the same values in the device profile YAML file
# def createValueDescriptors():
#     url = f"http://{edgex_ip}:48080/api/v1/valuedescriptor'

#     payload =   {
#                     "name":"color",
#                     "description":"Color to be shown in test app web UI",
#                     "type":"Str",
#                     "uomLabel":"color",
#                     "defaultValue":"green",
#                     "formatting":"%s",
#                     "labels":["color","testapp"]
#                 }
#     headers = {'content-type': 'application/json'}
#     response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
#     print("Result for createValueDescriptors #1: %s - Message: %s" % (response, response.text))


# To create a device we need a device profile in YAML format. This function uploads and registers
# the device profile with EdgeX Foundry. Based on the content of the device profile, EdgeX Foundry
# may create entries for the device in the command module as well as meta data.
def uploadDeviceProfile():

    url = f"http://{edgex_ip}:{core-metadata}/api/v2/deviceprofile"
    payload=[
        {
            "apiVersion": "v2",
            "profile": {
                "name": "Raspberry-pi-fusion",
                "manufacturer": "Rpi",
                "model": "4B",
                "labels": [
                    "rpi-1"
                ],
                "description": "Raspberry pi device",
                "deviceResources": [
                    {
                        "name": "Camera",
                        "description": "Counts people within visible area",
                        "properties": {
                            "valueType": "Int64",
                            "readWrite": "RW",
                            "defaultValue": "On",
                            "units": ""
                        }
                    }
                ]
            }
        }
    ]
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

    print("Result of uploading device profile: %s with message %s" % (response, response.text))




# This is a dummy device service since the existing REST device service doesn't yet support sending commands
def createDeviceService():
    url = f"http://{edgex_ip}:{core-metadata}/api/v2/deviceservice"

    payload = {
        "name":"Rpi-camera-service",
        "description":"Cam Serv",
        "labels":["cam-serv"],
        "adminState":"unlocked",
        "operatingState":"enabled",
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createDeviceService: %s - Message: %s" % (response, response.text))



# Finally we can create the actual device. It will be named and will also reference both the 
# device service it supports as well as the device profile it corresponds to
# The device creation requires a protocols section. Perhaps it can be expanded to include
# information about the device, like IP, port, etc. but isn't actively used for these tutorials
def addNewDevice():
    url = f"http://{edgex_ip}:{core-metadata}/api/v2/device"

    payload = [
        {
            "apiVersion": "v2",
            "device": {
                "name": "Camera-Device-1",
                "description": "Device created with Raspberry-pi-fusion device profile",
                "adminState": "UNLOCKED",
                "operatingState": "UP",
                "labels": [
                    "Camera-Device"
                ],
                "serviceName": "Rpi-camera-service",
                "profileName": "Raspberry-pi-fusion",
                "autoEvents": [
                    {
                        "interval": "30s",
                        "onChange": false,
                        "sourceName": "Float32"
                    },
                    {
                        "interval": "30s",
                        "onChange": false,
                        "sourceName": "Float64"
                    }
                ],
                "protocols": {
                    "other": {
                        "Address": "device-virtual-float-01",
                        "Protocol": "300"
                    }
                },
                "location": "Tokyo"
            }
        }
    ]
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for addNewDevice: {response} - Message: {response.text}")


if __name__ == "__main__":
    # createAddressables()
    # createValueDescriptors()
    uploadDeviceProfile()
    createDeviceService()
    addNewDevice()