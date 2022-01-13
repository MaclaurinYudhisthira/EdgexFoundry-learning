import requests

edgex_ip    = "localhost"
core-metadata = 59881

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




if __name__ == "__main__":
    uploadDeviceProfile()