#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests
import time

#ISSPASS = "http://api.open-notify.org/iss-pass.json?lat=38.9&lon=-77.03"

def main():
    """your code goes below here"""
    userLat = input("Input your desired latitude: ")
    userLong = input("Input your desired longitude: ")
    
    ISSPASS2 = f"http://api.open-notify.org/iss-pass.json?lat={userLat}&lon={userLong}"
    
    #print(ISSPASS2)
    
    #resp = requests.get(ISSPASS)
    resp = requests.get(ISSPASS2)

    result = resp.json()

    #print(result)

    epochTime = result["response"][0].get("risetime")
    print(epochTime)

    localTime = time.ctime(epochTime)
    #print(result["request"].get("latitude"))
    localUserLat = result["request"].get("latitude")
    localUserLong = result["request"].get("longitude")
    #print(localUserLat)
    #print(localUserLong)
    
    resultStr = f"The ISS will be overhead at {localUserLat} and {localUserLong} in {localTime}"
    print(resultStr)


    # stuck? you can always write comments
    # Try describe the steps you would take manually



if __name__ == "__main__":
    main()

