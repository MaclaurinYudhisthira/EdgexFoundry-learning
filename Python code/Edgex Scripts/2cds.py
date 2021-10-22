import requests

edgex_ip    = "localhost"
core-metadata = 59881


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


if __name__ == "__main__":
    createDeviceService()