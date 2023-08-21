def sum(f1,f2):
    result={}
    result["s"]=(k1["s"]*k2["m"])+(k2["s"]*k1["m"])
    result["m"]=k1["m"]*k2["m"]
    return result
def zarb(f1,f2):
    result={}
    result["s"]=k1["s"]*k2["s"]
    result["m"]=k1["m"]*k2["m"]
    return result 
def menha(f1,f2):
    result={}
    result["s"]=(k1["s"]*k2["m"])-(k2["s"]*k1["m"])
    result["m"]=k1["m"]*k2["m"]
    return result
def taghsim(f1,f2):
    result={}
    result["s"]=k1["s"]*k2["m"]
    result["m"]=k1["m"]*k2["s"]
    return result

def show(result):
    print(f"{result['s']}/{result['m']}")

sorat_k1=int(input("Enter a number for sorat kasr1 :"))
makhraj_k1=int(input("Enter a number for makhraj kasr1 :"))

sorat_k2=int(input("Enter a number for sorat kasr2 :"))
makhraj_k2=int(input("Enter a number for makhraj kasr2 :"))

k1={"s":sorat_k1,"m":makhraj_k1}
k2={"s":sorat_k2,"m":makhraj_k2}

result_sum=sum(k1,k2)
print("result sum:")
show(result_sum)

result_zarb=zarb(k1,k2)
print("result zarb:")
show(result_zarb)

result_menha=menha(k1,k2)
print("result menha:")
show(result_menha)

result_taghsim=taghsim(k1,k2)
print("result taghsim:")
show(result_taghsim)