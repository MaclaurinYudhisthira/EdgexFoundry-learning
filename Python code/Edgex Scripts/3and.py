import requests

edgex_ip    = "localhost"
core-metadata = 59881


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
    addNewDevice()