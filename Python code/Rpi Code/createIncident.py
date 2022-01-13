import requests

server_ip="54.220.116.252"

def Create():
    # Creating token
    url=f"http://{server_ip}:8008/api/jwt/login"
    response=requests.post(url,data={'username':'Demo','password':'123'})
    token=response.text
    # Creating incident
    url=f"http://{server_ip}:8008/api/arsys/v1/entry/HPD:IncidentInterface_Create/"
    js={
        "values":{
            "z1D_Action":"CREATE",
            "Last_Name":"Allbrook",
            "First_Name":"Allen",
            "Description":"Temperature Exceeds 37*C !!!",
            "Impact": "1-Extensive/Widespread",
            "Urgency": "1-Critical",
            "Reported Source": "Direct Input",
            "Service_Type": "User Service Restoration"
        }
    }
    response=requests.post(url,headers={'Authorization':f"AR-JWT {token}"},json=js)
    print(response.status_code)
