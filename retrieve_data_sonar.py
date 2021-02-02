import os
import json
from sonarqube import *
import re

sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')

issues1 = list(sonar.issues.search_issues(componentKeys="ecomanif", branch="master"))
js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)

#gui_input(coponentKeys)


with open(os.path.join("C:/Users/romain/Desktop", "data.txt"),"w") as f:
    f.write("["+'\n')
    once=0
    for i in range(9724):
        a=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
        x = re.findall("python", a)
        k = re.findall("python:S1192",a)
        v= re.findall("python:S125",a)
        #print(x)


        
        if x and not k and not v:
            data1=str(json.dumps(y[i]["key"], indent=4, sort_keys=True))
            data2=str(json.dumps(y[i]["message"], indent=4, sort_keys=True))
            data3=str(json.dumps(y[i]["type"], indent=4, sort_keys=True))
            
            #data4=(json.dumps(y[i]["textRange"], indent=4, sort_keys=True))component
            key=json.dumps(y[i]["component"], indent=4, sort_keys=True)
            key=key.replace('"','')
            key=key.replace("\\u00e9","é")
            #print(key)
            
            
            data4_1=(json.dumps(y[i]["textRange"]["endLine"], indent=4, sort_keys=True))
            data4_2=(json.dumps(y[i]["textRange"]["endOffset"], indent=4, sort_keys=True))
            data4_3=(json.dumps(y[i]["textRange"]["startLine"], indent=4, sort_keys=True))
            data4_4=(json.dumps(y[i]["textRange"]["startOffset"], indent=4, sort_keys=True))
            
            data1=data1.replace('"','')
            data2=data2.replace('"','')
            data3=data3.replace('"','')
            

            data4_1=data4_1.replace('"','')
            data4_2=data4_2.replace('"','')
            data4_3=data4_3.replace('"','')
            data4_4=data4_4.replace('"','')

            #########
            data_r=str(json.dumps(y[i]["rule"], indent=4, sort_keys=True))
            data_r=data_r.replace('"','')


            ########""

            

            data5= sonar.sources.get_source_code(key=key, from_line=data4_3, to_line=data4_1)
            data5=json.dumps(data5["sources"][0][1])
            data5=data5.replace('"','')
            ######print(data1)
            data5= re.sub('</?span[^>]*>', '', data5)
            
            json_format={"key":data1,"msg":data2,"rule":data_r,"type":data3,"code":[{"endLine":data4_1,"endOffset":data4_2,"startLine":data4_3,"startOffset":data4_4},{"src":data5}]}
            
            if once==0:
                f.write(json.dumps(json_format,indent=4, sort_keys=True) )
                once=1
            else:
                f.write(","+"\n"+json.dumps(json_format,indent=4, sort_keys=True)+ "\n")
    f.write("]")




#tempfile ->fichier temporaire to mongodb
f=open(os.path.join("C:/Users/romain/Desktop", "data.txt"))
data = json.load(f)
long=len(data)
with open(os.path.join("C:/Users/romain/Desktop", "data.txt"),'w') as file:
    file.write(json.dumps(data,indent=4, sort_keys=True))
