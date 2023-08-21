def sum(t1,t2):
    result={}
    result["h"]=t1["h"]+t2["h"]
    result["m"]=t1["m"]+t2["m"]
    result["s"]=t1["s"]+t2["s"]
    if result["s"]>=60:
        a=result["s"]//60
        result["s"]-=a*60
        result["m"]+=a
    if result["m"]>=60:
        b=result["m"]//60
        result["m"]-=b*60
        result["h"]+=b
    return result

def menha(t1,t2):
    result={}
    result["h"]=t1["h"]-t2["h"]
    result["m"]=t1["m"]-t2["m"]
    result["s"]=t1["s"]-t2["s"]

    if result["m"]<0:
        b=(result["m"]//-60)+1
        result["m"]+=b*60
        result["h"]-=b

    if result["h"]<0:
        print("Error!!!,((h)) baiad mosbat bashad!!!")

    if result["s"]<0:
        a=(result["s"]//-60)+1
        result["s"]+=a*60
        result["m"]-=a
    return result

def show(result):
    print(f"{result['h']}:{result['m']}:{result['s']}")

time1_h=int(input("Enter a number for (((h1))):"))
time1_m=int(input("Enter a number for (((m1))):"))
time1_s=int(input("Enter a number for (((s1))):"))

time2_h=int(input("Enter a number for (((h2))):"))
time2_m=int(input("Enter a number for (((m2))):"))
time2_s=int(input("Enter a number for (((s2))):"))

time1={"h":time1_h,"m":time1_m,"s":time1_s}
time2={"h":time2_h,"m":time2_m,"s":time2_s}

result_s=sum(time1,time2)
show(result_s)
result_m=menha(time1,time2)
show(result_m)