from sonarqube import *
import json
import os
import re


sq="python:S1192"
sq1="python:S125"

info="INFO"
val="AXcqnskc-n2LilEsa3ap"
sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')
sonar.issues.issue_change_severity(issue=val, severity="CRITICAL")


issues1 = list(sonar.issues.search_issues(componentKeys="ecomanif", branch="master"))
js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)



with open(os.path.join("C:/Users/romain/Desktop", "duplicateKey.txt"),"w") as f:
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall(sq, a)
        k= re.findall(sq1,a)
        #print(x)
        if x or k:
            string=(json.dumps(y[i]["key"], indent=4, sort_keys=True))
            reg=string.replace('"','')
            f.write(str(json.dumps(y[i]["key"], indent=4, sort_keys=True))+ "\n")
            sonar.issues.issue_change_severity(issue=reg, severity=info)
            
