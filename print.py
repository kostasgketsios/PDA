import http.client
import json
import time
import subprocess


conn = http.client.HTTPConnection("localhost:1337")

payload = ""

headers = { 'content-type': "application/json" }

payload2 = "{\"data\":{\"isPrinted\":true}}"


# list = []
print_data = ""

while(True):
    for trapezi in range (1, 12):
        

        conn.request("GET", "/api/paraggelies?filters[readyToPrint][$eq]=true&filters[arithmos_trapeziou][$eq]="+str(trapezi)+"&filters[isPrinted][$eq]=false", payload, headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")
        data = json.loads(data)

        if(len(data["data"])>0):
            print("Trapezi: "+str(trapezi))
            print_data = "Trapezi: "+str(trapezi)

            for info in range (len(data["data"])):

                print(str(data["data"][info]["id"])+" : "+data["data"][info]["attributes"]["proion"]+" "+str(data["data"][info]["attributes"]["sxolia"]).replace("null", ""))
                print_data = print_data + data["data"][info]["attributes"]["proion"]+" "+str(data["data"][info]["attributes"]["sxolia"]).replace("null", "") +"\n"
                conn = http.client.HTTPConnection("localhost:1337")
                headers = { 'content-type': "application/json" }
                payload2 = "{\"data\":{\"isPrinted\":true}}"
                conn.request("PUT", "/api/paraggelies/"+str(data["data"][info]["id"]), payload2, headers)
                conn.close()
            if(print_data != ""):
                lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
                print_data = bytes(print_data, 'utf-8')
                lpr.stdin.write(print_data)
                print_data = ""
                lpr.stdin.close()
            res = ""
            data = ""