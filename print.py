import http.client
import json
import time


conn = http.client.HTTPConnection("localhost:1337")

payload = ""

headers = { 'content-type': "application/json" }

payload2 = "{\"data\":{\"isPrinted\":true}}"


# list = []

while(True):
    for trapezi in range (1, 12):
        conn.request("GET", "/api/paraggelies?filters[readyToPrint][$eq]=true&filters[arithmos_trapeziou][$eq]="+str(trapezi)+"&filters[isPrinted][$eq]=false", payload, headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")
        data = json.loads(data)

        if(len(data["data"])>0):
            print("Trapezi: "+str(trapezi))
            for info in range (len(data["data"])):

# αντι για print θα δημιουργεί έναν αρχείο στον φάκελο toBePrinted 
# και μετά θα στέλνει εκτύπωση αυτο το αρχείο
# ίσως γίνει async για να μην χρειάζεται να περιμένει την εκτύπωση για να συνεχίσει 
                print(str(data["data"][info]["id"])+" : "+data["data"][info]["attributes"]["proion"]+" "+str(data["data"][info]["attributes"]["sxolia"]).replace("null", ""))
                conn = http.client.HTTPConnection("localhost:1337")
                headers = { 'content-type': "application/json" }
                payload2 = "{\"data\":{\"isPrinted\":true}}"
                conn.request("PUT", "/api/paraggelies/"+str(data["data"][info]["id"]), payload2, headers)
                conn.close()
            res = ""
            data = ""