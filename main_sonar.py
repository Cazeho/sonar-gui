import os,json
from sonarqube import *
import re



'''
f=open(os.path.join("C:/Users/romain/Desktop", "unitest.txt"))
data = json.load(f)
long=len(data)
print(long)
with open(os.path.join("C:/Users/romain/Desktop", "unitest2.txt"),'w') as file:
    file.write("["+'\n')
    for i in data:
        long-=1
        print(long)
        x={"value":i["key"]}
        if long !=0:
            file.write(json.dumps(x,indent=4, sort_keys=True) +',' + '\n')
        else:
            file.write(json.dumps(x,indent=4, sort_keys=True) + '\n')
    file.write("]")
    

f=open(os.path.join("C:/Users/romain/Desktop", "unitest2.txt"),'r')
d=json.load(f)


with open(os.path.join("C:/Users/romain/Desktop", "unitest2.txt"),'w') as file:
    file.write(json.dumps(d,indent=4, sort_keys=True))

'''
f=open(os.path.join("C:/Users/romain/Desktop", "data.txt"))
data = json.load(f)
'''
long=len(data)
with open(os.path.join("C:/Users/romain/Desktop", "data.txt"),'w') as file:
    file.write(json.dumps(data,indent=4, sort_keys=True))
'''

#print(data[0]["key"])


###############
rule=[]


for y in range(len(data)):
    #print(y)
    k=(data[y]["rule"])
    rule.append(k)
    rule=list(dict.fromkeys(rule))

#pls=[]
taille=[]
count=0
number=[]


with open(os.path.join("C:/Users/romain/Desktop", "sortdata.txt"),'w') as f:
    #f.write("["+'\n')
    test=[]
    test2=[]
    json_dict = {}
    
    for i in rule:
    #print(i)
        u=i
        #print(len(data))
        
        ####print("========================="+i+"=========================")
        #number.append(len(pls))
        #test.append(pls)
        
        pls=[]
        pls2=[]
        for j in range(len(data)):
            #print(i)
            a=str(json.dumps(data[j]["rule"], indent=4, sort_keys=True))
            x = re.findall(i, a)
           
            
            #print(j)
            if x:
                #data2=len((data[j]["code"][1]["src"]))
                #print(data2)
                #pls2=taille.append(data2)
                data1=str((data[j]["code"][1]["src"]))
                data2=str((data[j]["key"]))
                pls2.append(data2)
                #pls.append("{"+data1+"}")
                pls.append(data1)
                #data1.replace(" ",'')
                pls2=list(dict.fromkeys(pls2))
                pls=list(dict.fromkeys(pls))
                #print(data1)
                #f.write(data1 + "\n" )
            
        test.append(pls)
        test2.append(pls2)
        #print(pls)
                
                      
    #f.write("]")
    #print(test[0])
    
        


###############################formatting
    ###print(test)
    ###print(rule)
    for i in range(len(test)):
        ###print(i)
        tmp_dict = {}
        #f.write("==========================" + rule[i] + '\n')
        for j in range(len(test[i])):
            ###print(test[i][j])
            ###f.write(test[i][j]+ '\n')
            tmp_dict["data"] = [{"src": test[i][j]} for j in range(len(test[i]))]
        json_dict[str(rule[i])] = tmp_dict
    f.write(json.dumps(json_dict, indent=4, sort_keys=True))
        
        

########################
            






################
'''
    for i in rule:
        print(i)
      '''  
##############    
'''
sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')

issues1 = list(sonar.issues.search_issues(componentKeys="ecomanif", branch="master"))
js=json.dumps(issues1, indent=4, sort_keys=True)
y = json.loads(js)

long=len(y)
print(long)

for i in y:
    print(i)
    print(10*"===")
'''
