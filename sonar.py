from sonarqube import *
from os import path
import json
import os
import re
sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')




issues1 = list(sonar.issues.search_issues(componentKeys="ecomanif", branch="master"))
js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)





with open(os.path.join("C:/Users/romain/Desktop", "issue.txt"),"w") as f:
    f.write(str(js))

with open(os.path.join("C:/Users/romain/Desktop", "test.txt"),"w") as f:
    f.write(str(json.dumps(y[0], indent=4, sort_keys=True)))

with open(os.path.join("C:/Users/romain/Desktop", "search.txt"),"a") as f:
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall("python", a)
        #print(x)
        if (x):
            f.write(str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))+ "\n")
        #else:
        #    print("nothing")
        
       
        

#changelog = sonar.issues.get_issue_changelog(issue="AXcaEl3h-n2LilEsZquY")
#print(changelog)
print(10*"==")
'''

tags = sonar.issues.get_issues_tags(project="ecomanif")
#print(tags)
js=json.dumps(tags, indent=4, sort_keys=True)
print(js)
with open(os.path.join("C:/Users/romain/Desktop", "tags.txt"),"w") as f:
    f.write(str(js))
print(10*"==")





metrics = list(sonar.metrics.search_metrics())
js=json.dumps(metrics, indent=4, sort_keys=True)
with open(os.path.join("C:/Users/romain/Desktop", "metrics.txt"),"w") as f:
    f.write(str(js))
#print(metrics)

scm = sonar.sources.get_source_file_scm(key="ecomanif:administration/admin/agent.py", from_line=98, to_line=98)
print(scm)

source_code = sonar.sources.get_source_code(key="ecomanif:administration/admin/agent.py", from_line=98, to_line=98)
print(source_code)

'''
