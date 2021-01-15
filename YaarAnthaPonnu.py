def flames(name1,name2):
    total=len(name1)+len(name2)
    count=0 
    flame=['Just "Friends"','Uh-huh, "LOVE!"','Hmm, "Affection."',
            'Congrats, "Marriage.."','Whooops.."Enemy!"','Huh.."Sister."']

    for let1 in name1:
        if let1 in name2:
            name2.remove(let1)
            count+=1
    finc=total-(2*count)
    
    #Simple method
    while len(flame)>1:
            del flame[finc%len(flame)-1] 

    print (*flame)


if __name__ == "__main__":
    print("<----- FLAMES ----->")
    name1=list(input("Unga name sollunga.. -->").lower().strip())
    name2=list(input("Avanga name enna.. -->").lower().strip())
    flames(name1,name2)


'''
#Not Completed
import HerDefaults
def YaarAnthaPonnu(She):
    if She is Cute and Charming:
        if She is Topper and Intelligent:
            if She is Short and VeryGoodCharacter:
                return She is Programmer 

print(YaarAnthaPonnu())
'''