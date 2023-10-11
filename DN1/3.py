def naloga_3():
    prva=input("Vnesi stevilko: ")
    druga=input("Vnesi stevilko: ")
    tretja=input("Vnesi stevilko: ")

    print(prva + ", " + str(type(prva)))
    print(druga + ", " + str(type(druga)))
    print(tretja + ", " + str(type(tretja)))

    if(druga==prva and tretja<=prva):
        print("pogoj drzi")

naloga_3()