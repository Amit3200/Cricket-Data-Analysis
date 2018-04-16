import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('cricket.csv')
ground=[]
grecords={}
count=0
count2=0
margin=[]
in1=0
in2=0
#print(df.dtypes)
df["Margin"]=df["Margin"].astype("str")
for i in df["Winner"]:
    if i=="India":
        ground.append(df["Ground"][count])
        margin.append(df["Margin"][count])
        count+=1
    else:
        count2+=1
for i in ground:
    grecords[i]=ground.count(i)    
#print(ground)
#print(margin)
for i in margin:
    if "runs" in i.lower() or "run" in i.lower():
        in1+=1
    elif "wickets" in i.lower() or "wicket" in i.lower():
        in2+=1
print(count)
in3=count-in1-in2
print(count2)
print(in1)
print(in2)
print(grecords)
inningm=[in1,in2,in3]
label=["Batting First","Bowling First","Cannot Say"]
index = [0.1,0.3,0.6]
#first
explodes=(0.3,0)
chartdata1=[count,count2]
fig1,ax1=plt.subplots()
ax1.pie(chartdata1,explode=explodes,labels=['India','Others'],autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Analysis of Cricket : India v/s Other Team")
plt.xlabel("Shows the Indias percentage winning with respect to other")
plt.plot([],[],'',label="India Win's Total: "+str(count))
plt.plot([],[],'',label="Others Team's Win and Draws : "+str(count2))
plt.legend()
plt.savefig('pic1.png')
plt.show()
plt.close()
# second
bar_width=0.1
fig, ax = plt.subplots()
plt.bar([0.1,0.3,0.6], inningm,bar_width,color="#1abc9c")
plt.xlabel('Innings', fontsize=8)
plt.ylabel('Matches Won', fontsize=8)
plt.xticks(index, label, fontsize=8, rotation=30)
plt.title('Batting First v/s Bowling First')
plt.savefig('pic2.png') 
plt.show()
plt.close()
#third
fig, ax = plt.subplots()
plt.bar(range(len(grecords)), list(grecords.values()), align='center')
plt.xticks(range(len(grecords)), list(grecords.keys()),rotation=90,fontsize=5)
plt.legend()
plt.xlabel("Grounds : Place where the match was held")
plt.ylabel("Wins in Particular Ground")
plt.title("Total Win Distribution all over various grounds")
plt.savefig('pic3.png') 
plt.show()
plt.close()
#fourth
fig, ax = plt.subplots()
winnersdic={}
winteams=[]
df["Winner"]=df["Winner"].astype("str")
for i in df["Winner"]:
    winteams.append(i)
for i in winteams:
    winnersdic[i]=winteams.count(i)
print(winnersdic)
plt.bar(range(len(winnersdic)), list(winnersdic.values()), align='center',color="#1abc9c")
plt.xticks(range(len(winnersdic)), list(winnersdic.keys()),rotation=90,fontsize=5)       
plt.legend()
plt.xlabel("Team Names")
plt.ylabel("Total Wins")
plt.title("Total Team Wins as per the dataset")
plt.savefig('pic4.png') 
plt.show()
plt.close()
#fifth - matches played in india and lost
lostto={}
one=[]
team=0
for i in range(len(df["Winner"])):
    if (df["Team 1"][i]=="India" or df["Team 2"][i]=="India") and (df["Winner"][i]!="India"):
        team+=1
        #print(df["Team 1"][i],df["Team 2"][i],df["Winner"][i])
        if df["Team 1"][i]=="India":
            one.append(df["Team 2"][i])
        else:
            one.append(df["Team 1"][i])
for i in one:
    lostto[i]=one.count(i)
print(lostto)
print(team)
plt.bar(range(len(lostto)), list(lostto.values()), align='center',color="#1abc9c")
plt.xticks(range(len(lostto)), list(lostto.keys()),rotation=90,fontsize=5)       
plt.legend()
plt.xlabel("Team Names")
plt.ylabel("Total Losses")
plt.title("Total Lost Against Other Teams By Team India")
plt.savefig('pic5.png') 
plt.show()
plt.close()        
#Total India's grand ratio
win=0
counter=0
counter1=0
for i in range(len(df["Winner"])):
    if((df["Team 1"][i]=="India" or df["Team 2"][i]=="India") and df["Winner"][i]!=""):
        counter+=1
    if((df["Team 1"][i]=="India" or df["Team 2"][i]=="India") and df["Winner"][i]=="tied" or (df["Winner"][i]=="no result")):
        counter1+=1
print(counter)
print(counter1)
win=counter-team
print("Total Lost Matches by India : "+str(team-counter1))
explodes=(0.1,0,0)
chartdata1=[win,team-counter1,counter1]
fig1,ax1=plt.subplots()
ax1.pie(chartdata1,explode=explodes,labels=['Win','Loss','Tied'],autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Analysis of Cricket : India's Overall Performance")
plt.xlabel("Shows the India's Stats")
#plt.plot([],[],'',label="India Played Total : "+str(count))
#plt.plot([],[],'',label="Others Played Total : "+str(count2))
plt.legend()
plt.savefig('pic6.png')
plt.show()
plt.close()
print("Final Report")
print("*************************************************************************************"+"\n\n")
print("Total Matches played by  India   : "+str(counter))
print("Total Team Wins of India         : "+str(win))
print("Total Team Loss of India         : "+str(team-counter1))
print("Total Team Draw of India         : "+str(counter1))
print("India Winning Batting First      : "+str(in1))
print("India Winning Bowling First      : "+str(in2))
print("Can't be determined about innings: "+str(in3))
mo={}
for i in margin:
    mo[i]=margin.count(i)
kop=[]
for i in mo.values():
    kop.append(i)
#print(max(kop))
possibles=[]
z=kop.index(max(kop))
for i in mo.keys():
    if mo[i]==max(kop):
        possibles.append(i)
print("Average Margin Winning Possibilites ",end=":")
print(possibles)
print("--------------------------------------------------")
print("India's Win Distribution over the various ground")
for i in grecords.keys():
    print(str(i)+" -> "+str(grecords[i]))
print("--------------------------------------------------")
print("Other Team's Win Records")
for i in winnersdic.keys():
    print(str(i)+"-> "+str(winnersdic[i]))
print("--------------------------------------------------")
print("India's Lost Record against other teams")
for i in lostto.keys():
    print(str(i)+"-> "+str(lostto[i]))









