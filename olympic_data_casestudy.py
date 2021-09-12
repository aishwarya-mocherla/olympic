import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
all_ds = pd.DataFrame()
for f in ('C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/Olympic-data/OLYMPIC_2004_RESULT.xlsx','C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/Olympic-data/OLYMPIC_2008_RESULT.xlsx',
          'C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/Olympic-data/OLYMPIC_2012_RESULT.xlsx','C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/Olympic-data/OLYMPIC_2016_RESULT.xlsx'):
    data = pd.read_excel(f,'Sheet1')
    all_ds = all_ds.append(data)
print(all_ds)




#NUMBER OF GOLDS SILVERS AND BRONZES ACHIVED BY COUNTRIES IN 2009
# plt.scatter(data['COUNTRY'],data['GOLD'], label="Gold Medals Won",color="blue")
# plt.scatter(data['COUNTRY'],data['SILVER'], label="Silver Medals Won",color="red")
# plt.scatter(data['COUNTRY'],data['BRONGE'], label="Bronze Medals Won",color="green")
# plt.xlabel("COUNTRY")
# plt.ylabel("INDIVIDUAL MEDALS")
# plt.show()




#TOTAL NUMBER OF ALL 3 MEDALS ACHIVED BY COUNTRIES IN 2009 
# plt.bar(data['COUNTRY'],data['TOTAL'],color="yellow",width=0.5)
# plt.legend()
# plt.xlabel("days")
# plt.ylabel("number of medals")
# plt.title("TOTAL MEDALS")
# plt.show()






#COUNTRY WITH THE HIGHEST NUMBER OF MEDALS OVER ALL 4 (ALL THE GOLDS SILVERS AND BRONZES COMBINED)
#Q1) Of all the Medals won by these 5 countries across all olympics, 
#what is the percentage medals won by each one of them?
final_data1 = {} 
final_data5 = {}
for i in all_ds['COUNTRY']:
    x = i 
    t1 = (all_ds[(all_ds.COUNTRY==x)&(all_ds.YEAR==2004)].TOTAL).tolist() 
    t2 = (all_ds[(all_ds.COUNTRY==x)&(all_ds.YEAR==2008)].TOTAL).tolist() 
    t3 = (all_ds[(all_ds.COUNTRY==x)&(all_ds.YEAR==2012)].TOTAL).tolist()
    t4 = (all_ds[(all_ds.COUNTRY==x)&(all_ds.YEAR==2016)].TOTAL).tolist()
    t5 = t1 + t2 +t3 + t4
    # print("===================================================================================")
    # print("name of country: ",i)
    # print("no of medals in 2004: ",int(sum(t1[0:])))
    # print("no of medals in 2008: ",int(sum(t2[0:])))
    # print("no of medals in 2012: ",int(sum(t3[0:])))
    # print("no of medals in 2016: ",int(sum(t4[0:])))
    # print("total no of medals: ",int(sum(t5)))
    # final_data1.update({i:int(sum(t5))}) 
    # plt.bar(final_data1.keys(),final_data1.values(),color="blue")
    # plt.xlabel("country")
    # plt.ylabel("total number of medals won")
    # plt.xticks(rotation=90)
    top = int(sum(t5))
    # print(i,top)
    bottom = all_ds['TOTAL'].sum()
    percent = (top/bottom)*100
    final_data5.update({i:percent}) 
    plt.bar(final_data5.keys(),final_data5.values(),color="green")
    plt.xlabel("country")
    plt.ylabel("% of medals won")
    plt.title("QUESTION 1")
    plt.xticks(rotation=90)
plt.show()




    







# Q2] COUNTRY WITH THE BEST GOLD TO BRONZE RATIO OVER ALL OLYMPICS    
final_data2 = {}
for j in all_ds['COUNTRY']:
    y = j
    u1 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2004)].GOLD).tolist()  
    u2 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2008)].GOLD).tolist() 
    u3 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2012)].GOLD).tolist()
    u4 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2016)].GOLD).tolist()
    u5 = u1 + u2 + u3 + u4
    # print("===================================================================================")
    # print("name of country: ",j)
    # print("no of gold medals in 2004: ",int(sum(u1[0:])))
    # print("no of gold medals in 2008: ",int(sum(u2[0:])))
    # print("no of gold medals in 2012: ",int(sum(u3[0:])))
    # print("no of gold medals in 2016: ",int(sum(u4[0:])))
    # print("total gold no of medals: ",int(sum(u5)))
    v1 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2004)].BRONGE).tolist() 
    v2 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2008)].BRONGE).tolist() 
    v3 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2012)].BRONGE).tolist()
    v4 = (all_ds[(all_ds.COUNTRY==y)&(all_ds.YEAR==2016)].BRONGE).tolist()
    v5 = v1 + v2 + v3 + v4
    # print("===================================================================================")
    # print("name of country: ",j)
    # print("no of bronze medals in 2004: ",int(sum(v1[0:])))
    # print("no of bronze medals in 2008: ",int(sum(v2[0:])))
    # print("no of bronze medals in 2012: ",int(sum(v3[0:])))
    # print("no of bronze medals in 2016: ",int(sum(v4[0:])))
    # print("total bronze no of medals: ",int(sum(v5)))
    final_data2.update({j:(int(sum(u5))/int(sum(v5)))})
    plt.bar(final_data2.keys(),final_data2.values(),color="blue")
    plt.xlabel("COUNTRY")
    plt.ylabel("GOLD:BRONZE")
    plt.title("QUESTION 2")
    plt.xticks(rotation=90)
plt.show()
    
    








# Q3] if we comparethe years 2006 and 2018, which country has made the maximum progress in perentage , in terms of the number of medal wons.
final_data3 = {}
for k in all_ds['COUNTRY']:
    z = k
    w1 = (all_ds[(all_ds.COUNTRY==z)&(all_ds.YEAR==2004)].TOTAL).tolist() 
    w2 = (all_ds[(all_ds.COUNTRY==z)&(all_ds.YEAR==2016)].TOTAL).tolist()
    # print("===================================================================================")
    og=int(sum(w1[0:]))
    new=int(sum(w2[0:]))
    increase = new-og
    percent = (increase/og)*100
    # print("name of country: ",k)
    # print("2004 total: ",og)
    # print("2016 total: ",new)
    # print("increase: ",increase)
    # print("% increase: ",percent)
    final_data3.update({k:percent}) 
    plt.bar(final_data3.keys(),final_data3.values(),color="black")
    plt.xlabel("COUNTRY")
    plt.ylabel("% increase")
    plt.title("QUESTION 3")
    plt.xticks(rotation=90)
plt.show()








# Q4]Which country has won atleast 4 bronze medals per every Gold medal won in 2014 edition    
all_ds1=pd.DataFrame()
for f in ['C:/Users/Aishwarya Mocherla/Desktop/python/live/data_set/Olympic-data/OLYMPIC_2012_RESULT.xlsx']:
    data=pd.read_excel(f,'Sheet1')
    all_ds1= all_ds1.append(data)
print("\n")
print("QUESTION 4]")
print(all_ds1)
final_data4 = {}
for l in all_ds1['COUNTRY']:
    a = l
    p1 = (all_ds1[(all_ds1.COUNTRY==a)&(all_ds1.YEAR==2012)].BRONGE).tolist() 
    p2 = (all_ds1[(all_ds1.COUNTRY==a)&(all_ds1.YEAR==2012)].GOLD).tolist()
 
    bronzeno=int(sum(p1[0:]))
    goldno=int(sum(p2[0:]))
    print("\n")
    print("bronze medals won by ",a,"=",bronzeno)
    print("gold medals won by ",a,"=",goldno)
    
    if (goldno !=0):
          if bronzeno%goldno >= 0:
            print(a,"has won atleast 4 bronze medals per every Gold medal won in 2014 edition \n")
          else:
            print(a,"has not won atleast 4 bronze medals per every Gold medal won in 2014 edition \n")
    else:
        print(a, "has not won any gold medals in 2012 \n")











# Q5) Across all editions, if we compare US and INDIA, which 
# country has a better gold-to –silver ratio i.e. which country has won 
# most silver medals per every gold won.
final_data6 = {} #FOR USA
e1 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2004)].GOLD).tolist() 
e2 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2008)].GOLD).tolist() 
e3 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2012)].GOLD).tolist()
e4 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2016)].GOLD).tolist()
e5 = e1 + e2 + e3 + e4
tot_us_gold = int(sum(e5))
print("QUESTION 5 \n")
print("total gold no of medals: ",tot_us_gold)


f1 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2004)].SILVER).tolist()
f2 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2008)].SILVER).tolist() 
f3 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2012)].SILVER).tolist()
f4 = (all_ds[(all_ds.COUNTRY=='USA')&(all_ds.YEAR==2016)].SILVER).tolist()
f5 = f1 + f2 + f3 + f4
tot_us_silver = int(sum(f5))
print("total bronze no of medals: ",tot_us_silver)


us_ratio = tot_us_gold/tot_us_silver
final_data6.update({"USA":us_ratio}) 
plt.bar(final_data6.keys(),final_data6.values(),color="blue")
plt.xlabel("COUNTRY")
plt.ylabel("GOLD:SILVER RATIO")
plt.xticks(rotation=90)

#////////////////////////////////////////////////////////////////////////////////////#

final_data7 = {} #FOR INDIA
g1 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2004)].GOLD).tolist() 
g2 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2008)].GOLD).tolist() 
g3 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2012)].GOLD).tolist()
g4 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2016)].GOLD).tolist()
g5 = g1 + g2 + g3 + g4
tot_india_gold = int(sum(g5))
print("total gold no of medals: ",tot_india_gold)


h1 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2004)].SILVER).tolist() 
h2 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2008)].SILVER).tolist() 
h3 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2012)].SILVER).tolist()
h4 = (all_ds[(all_ds.COUNTRY=='INDIA')&(all_ds.YEAR==2016)].SILVER).tolist()
h5 = h1 + h2 + h3 + h4
tot_india_silver = int(sum(h5))
print("total bronze no of medals: ",tot_india_silver)


india_ratio = tot_india_gold/tot_india_silver
final_data7.update({"INDIA":india_ratio}) 
plt.bar(final_data7.keys(),final_data7.values(),color="green")
plt.xlabel("COUNTRY")
plt.ylabel("GOLD:SILVER RATIO")
plt.title("QUESTION 5")
plt.xticks(rotation=90)












    
    
    
    
  































