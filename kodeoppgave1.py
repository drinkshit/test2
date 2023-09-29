def nummerert_liste(forst:str, andre:str, tredje:str,forte:str, femte:str): 
 """this function makes a numbered list of its arguements"""
 return( list((forst, andre,tredje, forte,femte)))


my_list1 =  nummerert_liste("one","two","three","four","five")
for index, item in enumerate(my_list1, start=1):
    print(f"{index}. {item}")

print("-")
my_list2 =  nummerert_liste("abc","def","ghi","lmo","nop")
for index, item in enumerate(my_list2, start=1):
    print(f"{index}. {item}")
print("-")
my_list3 =  nummerert_liste("test1","test2","test3","test4","test5")
for index, item in enumerate(my_list3, start=1):
    print(f"{index}. {item}")

#forste oppgave slutt her



def fravaer(udokumentert_fravaer : int, dokumenter_fravaer:int, arstimer:int): 
    """this function checks a value of the given atributes and prints out answer according to it"""
    return(arstimer%udokumentert_fravaer, arstimer%dokumenter_fravaer)
#test1
arstimer = 300
udokumentert_fravaer = 2
dokumentert_fravaer = 250


if dokumentert_fravaer/arstimer > 0.10 and udokumentert_fravaer/arstimer > 0.05: 
    print("Mister karakteren i faget") 

elif dokumentert_fravaer/arstimer > 0.20 and udokumentert_fravaer/arstimer > 0.10: 
    print("Mister karakteren i faget") 


elif  udokumentert_fravaer/arstimer > 0.10: 
    print("Mister karakteren i faget") 
elif dokumentert_fravaer/arstimer > 0.20: 
    print("Send varsel om fare for å miste karakteren grunnet manglende vurderingsgrunnlag")

elif udokumentert_fravaer/arstimer > 0.05 : 
    print("Send varsel om fare for å miste karakteren grunnet fravær")


else :
    print("")

#test2 
arstimer1 = 300
udokumentert_fravaer1 = 10
dokumentert_fravaer1 = 70


if dokumentert_fravaer1/arstimer1 > 0.10 and udokumentert_fravaer1/arstimer1 > 0.05: 
    print("Mister karakteren i faget") 

elif dokumentert_fravaer1/arstimer1 > 0.20 and udokumentert_fravaer1/arstimer1 > 0.10: 
    print("Mister karakteren i faget") 


elif  udokumentert_fravaer1/arstimer1 > 0.10: 
    print("Mister karakteren i faget") 
elif dokumentert_fravaer1/arstimer1 > 0.20: 
    print("Send varsel om fare for å miste karakteren grunnet manglende vurderingsgrunnlag")

elif udokumentert_fravaer1/arstimer1 > 0.05 : 
    print("Send varsel om fare for å miste karakteren grunnet fravær")


else :
    print("")

#test3
arstimer2 = 300
udokumentert_fravaer2 = 150
dokumentert_fravaer2 = 54


if dokumentert_fravaer/arstimer2 > 0.10 and udokumentert_fravaer2/arstimer2 > 0.05: 
    print("Mister karakteren i faget") 

elif dokumentert_fravaer2/arstimer2 > 0.20 and udokumentert_fravaer2/arstimer2 > 0.10: 
    print("Mister karakteren i faget") 


elif  udokumentert_fravaer2/arstimer2 > 0.10: 
    print("Mister karakteren i faget") 
elif dokumentert_fravaer2/arstimer2 > 0.20: 
    print("Send varsel om fare for å miste karakteren grunnet manglende vurderingsgrunnlag")

elif udokumentert_fravaer2/arstimer2 > 0.05 : 
    print("Send varsel om fare for å miste karakteren grunnet fravær")


else :
    print("")

#andre oppgave slutt her


def baufort(original_speed:int, baufort_speed:int): 
    """it checks information and gives answer"""
    return(original_speed%baufort_speed)
original_speed = int(input("Whats the speed"))


if original_speed < 0.02 :
    print("Wind speed in buafort = 0")
elif original_speed < 1.5 :
    print("Wind speed in buafort = 1")
elif original_speed < 3.3 :
    print("Wind speed in buafort = 2")
elif original_speed < 5.4 :
    print("Wind speed in buafort = 3")
elif original_speed < 7.9 :
    print("Wind speed in buafort = 4")
elif original_speed < 10.7 :
    print("Wind speed in buafort = 5")
elif original_speed < 13.8:
    print("Wind speed in buafort = 6")
elif original_speed < 17.1:
    print("Wind speed in buafort = 7")
elif original_speed < 20.7:
    print("Wind speed in buafort = 8")
elif original_speed < 24.4:
    print("Wind speed in buafort = 9")
elif original_speed < 28.4 :
    print("Wind speed in buafort = 10")
elif original_speed < 32.6:
    print("Wind speed in buafort = 11")
elif original_speed > 32.7:
    print("Wind speed in buafort = 12")

