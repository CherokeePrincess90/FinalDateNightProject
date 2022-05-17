# Program name: Bush_Cynthia_ProjectM08
# Author: Cynthia Bush
# Date: 5/14/2022
# Summary: Program asks a series of questions and suggests a restaurant based on user answers
# Variables:
#   Q1-Q4=questions
#   score=file imported with restaurant names

from score import *

#print welcome
print("Welcome to your date night assistant. Let's find a place to eat!!")

#ask user questions about food they like/want
Q1=input("What type of food are you wanting to eat? Type CC to quit. \na) American \nb) Mexican \nc) Italian \nd) Asian \ne) Buffet\nf) Seafood\n")
if Q1 == "a":
    Q2=input("Which type of American food do you want? \na) steak \nb) BBQ \nc) burgers \nd) chicken \n")
    if Q2 == "a":
        Outback+=1
        RedPepper+=1
        USASteakhouse+=1
    elif Q2 == "b":
        MissionBBQ+=1
        SmokinCrowes+=1
    elif Q2 == "c":
        Bubba+=1
        HobokenEddies+=1
        MusselBurgerBar+=1
    elif Q2 == "d":
        Joella+=1
        Outback+=1
        Rooster+=1
        HarrysStoneGrill+=1
    else:
        print("I didn't understand that answer.")
elif Q1 == "b":
    ElNopal+=1
    SenorIguanas+=1
elif Q1 == "c":
    OliveGarden+=1
    RedPepperoni+=1
    RapidFire+=1
    BlackOlive+=1
elif Q1 == "d":
    ChinaWind+=1
    KansaiJapeneseSteakhouse+=1
elif Q1 == "e":
    Ponderosa+=1
    GoldenCorral+=1
elif Q1=="f":
    CaptainD+=1
    StorminCrab+=1
    RedLobster+=1
    KingFish+=1
elif Q1 == "CC":
    quit
else:
    print("I didn't understand that answer.")

Q3=input("How far are you wanting to travel? \na) ten miles \nb) twenty miles\n")
if Q3 == "a":
    Ponderosa+=1
    ChinaWind+=1
    ElNopal+=1
    RedPepper+=1
    SmokinCrowes+=1
    HobokenEddies+=1
    HarrysStoneGrill+=1
    USASteakhouse+=1
    RedPepperoni+=1
    BlackOlive+=1
    CaptainD+=1
    StorminCrab+=1
elif Q3 == "b":
    OliveGarden+=1
    RapidFire+=1
    Joella+=1
    Bubba+=1
    MissionBBQ+=1
    Outback+=1
    GoldenCorral+=1
    Rooster+=1
    KansaiJapeneseSteakhouse+=1
    SenorIguanas+=1
    RedLobster+=1
    KingFish+=1
    MusselBurgerBar+=1
else:
    print("I didn't understand that answer.")

Q4=input("How much are you willing to pay? \na) more affordable \nb) more expensive\n")
if Q4 == "a":
    Ponderosa+=1
    ChinaWind+=1
    ElNopal+=1
    RapidFire+=1
    Joella+=1
    Bubba+=1
    RedPepper+=1
    SmokinCrowes+=1
    HobokenEddies+=1
    RedPepperoni+=1
    CaptainD+=1
    RedLobster+=1
elif Q4 == "b":
    OliveGarden+=1
    MissionBBQ+=1
    USASteakhouse+=1
    GoldenCorral+=1
    Rooster+=1
    HarrysStoneGrill+=1
    KansaiJapeneseSteakhouse+=1
    SenorIguanas+=1
    BlackOlive+=1
    StorminCrab+=1
    KingFish+=1
    MusselBurgerBar+=1
else:
    print("I didn't understand that answer.")
    
#calculate output based on scores
if Ponderosa > MusselBurgerBar and Ponderosa > ChinaWind and Ponderosa > CaptainD and Ponderosa > BlackOlive and Ponderosa > SenorIguanas and Ponderosa > RedPepperoni and Ponderosa > OliveGarden and Ponderosa > KansaiJapeneseSteakhouse and Ponderosa > HarrysStoneGrill and Ponderosa > Rooster and Ponderosa > HobokenEddies and Ponderosa > Outback and Ponderosa > SmokinCrowes and Ponderosa > RedPepper and Ponder > GoldenCorral and Ponderosa > USASteakhouse and Ponderosa > RapidFire and Ponderosa > MissionBBQ and Ponderosa > ElNopal and Ponderosa > Bubba and Ponderosa > StorminCrab and Ponderosa > RedLobster and Ponderosa > KingFish and Ponderosa > Joella:
    print(" Ponderosa!!\n The address is:\n 1211 W McClain Ave\n Scottsburg")
elif ChinaWind > MusselBurgerBar and ChinaWind > Ponderosa and ChinaWind > CaptainD and ChinaWind > BlackOlive and ChinaWind > SenorIguanas and ChinaWind > RedPepperoni and ChinaWind > OliveGarden and ChinaWind > KansaiJapeneseSteakhouse and ChinaWind > HarrysStoneGrill and ChinaWind > Rooster and ChinaWind > HobokenEddies and ChinaWind > SmokinCrowes and ChinaWind > RedPepper and ChinaWind > USASteakhouse and ChinaWind > GoldenCorral and ChinaWind > Outback and ChinaWind > RapidFire and ChinaWind > MissionBBQ and ChinaWind > StorminCrab and ChinaWind > RedLobster and ChinaWind > KingFish and ChinaWind > ElNopal and ChinaWind > Bubba and ChinaWind > Joella:
    print("China Wind!!!\n The address is:\n 1096 W McClain Ave\n Scottsburg")
elif OliveGarden > MusselBurgerBar and OliveGarden > ChinaWind and OliveGarden > CaptainD and OliveGarden > BlackOlive and OliveGarden > SenorIguanas and OliveGarden > RedPepperoni and OliveGarden > Ponderosa and OliveGarden > KansaiJapeneseSteakhouse and OliveGarden > HarrysStoneGrill and OliveGarden > Rooster and OliveGarden > HobokenEddies and OliveGarden > SmokinCrowes and OliveGarden > RedPepper and OliveGarden > GoldenCorral and OliveGarden > USASteakhouse and OliveGarden > Outback and OliveGarden > RapidFire and OliveGarden > RedLobster and OliveGarden > StorminCrab and OliveGarden > KingFish and OliveGarden > MissionBBQ and OliveGarden > ElNopal and OliveGarden > Bubba and OliveGarden > Joella:
    print("Olive Garden!!\n The address is:\n 1230 Veterans Pkwy\n Clarksville")
elif Outback > MusselBurgerBar and Outback > ChinaWind and Outback > CaptainD and Outback > BlackOlive and Outback > SenorIguanas and Outback > RedPepperoni and Outback > OliveGarden and Outback > KansaiJapeneseSteakhouse and Outback > HarrysStoneGrill and Outback > Rooster and Outback > HobokenEddies and Outback > SmokinCrowes and Outback > RedPepper and Outback > GoldenCorral and Outback > USASteakhouse and Outback > Ponderosa and Outback > RapidFire and Outback > MissionBBQ and Outback > StorminCrab and Outback > RedLobster and Outback > KingFish and Outback > ElNopal and Outback > Bubba and Outback > Joella:
    print("Outback!!\n The address is:\n 1209 Veterans Pkwy\n Clarksville")
elif RapidFire > MusselBurgerBar and RapidFire > ChinaWind and RapidFire > CaptainD and RapidFire > BlackOlive and RapidFire > SenorIguanas and RapidFire > RedPepperoni and RapidFire > OliveGarden and RapidFire > KansaiJapeneseSteakhouse and RapidFire > HarrysStoneGrill and RapidFire > Rooster and RapidFire > HobokenEddies and RapidFire > SmokinCrowes and RapidFire > RedPepper and RapidFire > GoldenCorral and RapidFire > USASteakhouse and RapidFire > Outback and RapidFire > Ponderosa and RapidFire > StorminCrab and RapidFire > RedLobster and RapidFire > KingFish and RapidFire > MissionBBQ and RapidFire > ElNopal and RapidFire > Bubba and RapidFire > Joella:
    print("Rapid Fire!!\n The address is :\n 1645 Veterans Pkwy\n Jeffersonville")
elif MissionBBQ > MusselBurgerBar and MissionBBQ > ChinaWind and MissionBBQ > CaptainD and MissionBBQ > BlackOlive and MissionBBQ > SenorIguanas and MissionBBQ > RedPepperoni and MissionBBQ > OliveGarden and MissionBBQ > KansaiJapeneseSteakhouse and MissionBBQ > HarrysStoneGrill and MissionBBQ > Rooster and MissionBBQ > HobokenEddies and MissionBBQ > SmokinCrowes and MissionBBQ > GoldenCorral and MissionBBQ > RedPepper and MissionBBQ > USASteakhouse and MissionBBQ > Outback and MissionBBQ > RapidFire and MissionBBQ > StorminCrab and MissionBBQ > RedLobster and MissionBBQ > KingFish and MissionBBQ > Ponderosa and MissionBBQ > ElNopal and MissionBBQ > Bubba and MissionBBQ > Joella:
    print("Mission BBQ!!\n The address is:\n 1213 Veterans Pkwy\n Clarksville")
elif ElNopal > MusselBurgerBar and ElNopal > ChinaWind and ElNopal > CaptainD and ElNopal > BlackOlive and ElNopal > SenorIguanas and ElNopal > RedPepperoni and  ElNopal > RedPepper and ElNopal > KansaiJapeneseSteakhouse and ElNopal > HarrysStoneGrill and ElNopal > Rooster and ElNopal > HobokenEddies and ElNopal > SmokinCrowes and ElNopal > GoldenCorral and ElNopal > USASteakhouse and ElNopal > OliveGarden and ElNopal > Outback and ElNopal > RapidFire and ElNopal > MissionBBQ and ElNopal > Ponderosa and ElNopal > StorminCrab and ElNopal > RedLobster and ElNopal > KingFish and ElNopal > Bubba and ElNopal > Joella:
    print("El Nopal!!\n The address is:\n 1863 E Tipton St\n Seymour")
elif Bubba > MusselBurgerBar and Bubba > ChinaWind and Bubba > CaptainD and Bubba > BlackOlive and Bubba > SenorIguanas and  Bubba > RedPepperoni and Bubba > RedPepper and Bubba > KansaiJapeneseSteakhouse and Bubba > HarrysStoneGrill and Bubba > Rooster and Bubba > HobokenEddies and Bubba > SmokinCrowes and Bubba > GoldenCorral and Bubba > USASteakhouse and Bubba > OliveGarden and Bubba > Outback and Bubba > RapidFire and Bubba > MissionBBQ and Bubba > StorminCrab and Bubba > RedLobster and Bubba > KingFish and Bubba > ElNopal and Bubba > Ponderosa and Bubba > Joella:
    print("Bubba's!!\n The address is:\n 4631 Medical Plaza Way\n Clarksville")
elif RedPepper > MusselBurgerBar and RedPepper > ChinaWind and RedPepper > CaptainD and RedPepper > BlackOlive and RedPepper > SenorIguanas and RedPepper > RedPepperoni and RedPepper > Rooster and RedPepper > KansaiJapeneseSteakhouse and RedPepper > HarrysStoneGrill and RedPepper > GoldenCorral and RedPepper > SmokinCrowes and RedPepper > HobokenEddies and  RedPepper > OliveGarden and RedPepper > Outback and RedPepper > RapidFire and RedPepper > StorminCrab and RedPepper > RedLobster and RedPepper > KingFish and RedPepper > MissionBBQ and RedPepper > ElNopal and RedPepper > Bubba and RedPepper > USASteakhouse and RedPepper > Ponderosa:
    print("Red Pepper!!\n The address is:\n 902 W Main St\n Scottsburg")
elif USASteakhouse > MusselBurgerBar and USASteakhouse > ChinaWind and USASteakhouse > CaptainD and USASteakhouse > BlackOlive and  USASteakhouse > SenorIguanas and USASteakhouse > RedPepperoni and USASteakhouse > Rooster and Joella > KansaiJapeneseSteakhouse and USASteakhouse > HarrysStoneGrill and USASteakhouse > SmokinCrowes and USASteakhouse > HobokenEddies and USASteakhouse > GoldenCorral and USASteakhouse > OliveGarden and USASteakhouse > StorminCrab and USASteakhouse > RedLobster and USASteakhouse > KingFish and USASteakhouse > Outback and USASteakhouse > RapidFire and USASteakhouse> MissionBBQ and USASteakhouse > ElNopal and USASteakhouse > Bubba and USASteakhouse > RedPepper and USASteakhouse > Ponderosa:
    print("USA Steakhouse!!\n The address is:\n 519 Beatrice Ave\n Scottsburg")
elif Joella > MusselBurgerBar and Joella > ChinaWind and Joella > CaptainD and Joella > StorminCrab and Joella > RedLobster and Joella > KingFish and Joella > BlackOlive and Joella > SenorIguanas and Joella > RedPepperoni and Joella > SmokinCrowes and Joella > Rooster and Joella > KansaiJapeneseSteakhouse and Joella > HarrysStoneGrill and Joella > HobokenEddies and Joella > RedPepper and Joella > GoldenCorral and Joella > USASteakhouse and Joella > OliveGarden and Joella > Outback and Joella > RapidFire and Joella > MissionBBQ and Joella > ElNopal and Joella > Bubba and Joella > Ponderosa:
    print("Joella's!!\n The address is:\n 1225 Veterans Pkway\n Suite 700\n Clarksville")
elif GoldenCorral > MusselBurgerBar and GoldenCorral > ChinaWind and GoldenCorral > StorminCrab and GoldenCorral > RedLobster and GoldenCorral > KingFish and GoldenCorral > CaptainD and GoldenCorral > BlackOlive and GoldenCorral > SenorIguanas and GoldenCorral > RedPepperoni and GoldenCorral > Rooster and GoldenCorral > KansaiJapeneseSteakhouse and GoldenCorral > HarrysStoneGrill and GoldenCorral > HobokenEddies and GoldenCorral > RedPepper and GoldenCorral > SmokinCrowes and GoldenCorral > USASteakhouse and GoldenCorral > OliveGarden and GoldenCorral > Outback and GoldenCorral > Joella and GoldenCorral > RapidFire and GoldenCorral > MissionBBQ and GoldenCorral > ElNopal and GoldenCorral > Bubba and GoldenCorral > Ponderosa:
    print("Golden Corral!!\n The address is:\n 1402 Cedar St\n Clarksville")
elif SmokinCrowes > MusselBurgerBar and SmokinCrowes > ChinaWind and SmokinCrowes > StorminCrab and SmokinCrowes > RedLobster and SmokinCrowes > KingFish and SmokinCrowes > CaptainD and SmokinCrowes > BlackOlive and SmokinCrowes > SenorIguanas and SmokinCrowes > RedPepperoni and SmokinCrowes > Rooster and  SmokinCrowes > KansaiJapeneseSteakhouse and SmokinCrowes > HarrysStoneGrill and SmokinCrowes > HobokenEddies and SmokinCrowes > RedPepper and SmokinCrowes > GoldenCorral and SmokinCrowes > USASteakhouse and SmokinCrowes > GoldenCorral and SmokinCrowes > OliveGarden and SmokinCrowes > Outback and SmokinCrowes > RapidFire and SmokinCrowes > MissionBBQ and SmokinCrowes > ElNopal and SmokinCrowes > Bubba and SmokinCrowes > Joella and SmokinCrowes> Ponderosa:
    print("Smokin Crowe's!!\n The address is:\n 5517 IN 56\n Hanover")
elif HobokenEddies > MusselBurgerBar and HobokenEddies > ChinaWind and HobokenEddies > StorminCrab and HobokenEddies > RedLobster and HobokenEddies > KingFish and HobokenEddies > CaptainD and HobokenEddies > BlackOlive and HobokenEddies > SenorIguanas and HobokenEddies > RedPepperoni and HobokenEddies > KansaiJapeneseSteakhouse and HobokenEddies > HarrysStoneGrill and HobokenEddies > Rooster and HobokenEddies > RedPepper and HobokenEddies > SmokinCrowes and HobokenEddies > Bubba and HobokenEddies > GoldenCorral and HobokenEddies > USASteakhouse and HobokenEddies > OliveGarden and HobokenEddies > Outback and HobokenEddies > RapidFire and HobokenEddies > MissionBBQ and HobokenEddies > ElNopal and HobokenEddies > Ponderosa and HobokenEddies > Joella:
    print("Hoboken Eddie's!!\n The address is:\n 2840 Wilson Ave\n Madison")
elif Rooster > MusselBurgerBar and Rooster > ChinaWind and Rooster > CaptainD and Rooster > StorminCrab and Rooster > RedLobster and Rooster > KingFish and Rooster > BlackOlive and Rooster > SenorIguanas and  Rooster > HarrysStoneGrill and Rooster > RedPepperoni and Rooster > KansaiJapeneseSteakhouse and  Rooster > Joella and Rooster > SmokinCrowes and Rooster> HobokenEddies and Rooster > RedPepper and Rooster > GoldenCorral and Rooster > USASteakhouse and Rooster > OliveGarden and Rooster > Outback and Rooster > RapidFire and Rooster > MissionBBQ and Rooster > ElNopal and Rooster > Bubba and Rooster > Ponderosa:
    print("Rooster's!!\n The address is:\n 1601 Greentree Blvd\n Clarksville")
elif HarrysStoneGrill > MusselBurgerBar and HarrysStoneGrill > ChinaWind and  HarrysStoneGrill > StorminCrab and HarrysStoneGrill > RedLobster and HarrysStoneGrill > KingFish and HarrysStoneGrill > CaptainD and HarrysStoneGrill > BlackOlive and HarrysStoneGrill > SenorIguanas and HarrysStoneGrill > RedPepperoni and HarrysStoneGrill > KansaiJapeneseSteakhouse and HarrysStoneGrill > Joella and HarrysStoneGrill > SmokinCrowes and HarrysStoneGrill > Rooster and HarrysStoneGrill > HobokenEddies and HarrysStoneGrill > RedPepper and HarrysStoneGrill > GoldenCorral and HarrysStoneGrill > USASteakhouse and HarrysStoneGrill > OliveGarden and HarrysStoneGrill > Outback and HarrysStoneGrill > RapidFire and HarrysStoneGrill > MissionBBQ and HarrysStoneGrill > ElNopal and HarrysStoneGrill > Bubba and HarrysStoneGrill > Ponderosa:
    print("Harry's Stone Grill!!\n The address is:\n 621 Clifty Dr\n Madison")
elif KansaiJapeneseSteakhouse > MusselBurgerBar and KansaiJapeneseSteakhouse > CaptainD and KansaiJapeneseSteakhouse > StorminCrab and KansaiJapeneseSteakhouse > RedLobster and KansaiJapeneseSteakhouse > KingFish and KansaiJapeneseSteakhouse > BlackOlive and KansaiJapeneseSteakhouse > ChinaWind and KansaiJapeneseSteakhouse > SenorIguanas and KansaiJapeneseSteakhouse > RedPepperoni and KansaiJapeneseSteakhouse > Joella and KansaiJapeneseSteakhouse > SmokinCrowes and KansaiJapeneseSteakhouse > Rooster and KansaiJapeneseSteakhouse > HarrysStoneGrill and KansaiJapeneseSteakhouse > HobokenEddies and KansaiJapeneseSteakhouse > RedPepper and KansaiJapeneseSteakhouse > GoldenCorral and KansaiJapeneseSteakhouse > USASteakhouse and KansaiJapeneseSteakhouse > OliveGarden and KansaiJapeneseSteakhouse > Outback and KansaiJapeneseSteakhouse > RapidFire and KansaiJapeneseSteakhouse > MissionBBQ and KansaiJapeneseSteakhouse > ElNopal and KansaiJapeneseSteakhouse > Bubba and KansaiJapeneseSteakhouse > Ponderosa:
    print("Kansai Japenese Steakhouse!!\n The address is:\n 1370 Veterans Pkwy\n Clarksville")
elif RedPepperoni > MusselBurgerBar and RedPepperoni > ChinaWind and RedPepperoni > StorminCrab and RedPepperoni > RedLobster and RedPepperoni > KingFish and RedPepperoni > CaptainD and RedPepperoni > BlackOlive and RedPepperoni >Joella and RedPepperoni > SenorIguanas and RedPepperoni > SmokinCrowes and RedPepperoni > Rooster and RedPepperoni > KansaiJapeneseSteakhouse and RedPepperoni > HarrysStoneGrill and RedPepperoni > HobokenEddies and RedPepperoni > RedPepper and RedPepperoni > GoldenCorral and RedPepperoni > USASteakhouse and RedPepperoni > OliveGarden and RedPepperoni > Outback and RedPepperoni > RapidFire and RedPepperoni > MissionBBQ and RedPepperoni > ElNopal and RedPepperoni > Bubba and RedPepperoni > Ponderosa:
    print("Red Pepperoni\n The address is:\n 842 W Main St\n Madison!!")
elif SenorIguanas > MusselBurgerBar and SenorIguanas > BlackOlive and SenorIguanas > StorminCrab and SenorIguanas > RedLobster and SenorIguanas > KingFish and SenorIguanas > CaptainD and SenorIguanas > ChinaWind and SenorIguanas > Joella and SenorIguanas > RedPepperoni and SenorIguanas > SmokinCrowes and SenorIguanas > Rooster and SenorIguanas > KansaiJapeneseSteakhouse and SenorIguanas > HarrysStoneGrill and SenorIguanas > HobokenEddies and SenorIguanas > RedPepper and SenorIguanas > GoldenCorral and SenorIguanas > USASteakhouse and SenorIguanas > OliveGarden and SenorIguanas > Outback and SenorIguanas > RapidFire and SenorIguanas > MissionBBQ and SenorIguanas > ElNopal and SenorIguanas > Bubba and SenorIguanas > Ponderosa:
    print("Senor Iguana's!!\n The address is:\n 1415 Broadway St\n Clarksville")
elif BlackOlive > MusselBurgerBar and BlackOlive > ChinaWind and BlackOlive > CaptainD and BlackOlive > SenorIguanas and BlackOlive > RedPepperoni and BlackOlive > SmokinCrowes and BlackOlive > Rooster and BlackOlive > KansaiJapeneseSteakhouse and BlackOlive > HarrysStoneGrill and BlackOlive > HobokenEddies and BlackOlive > RedPepper and BlackOlive > GoldenCorral and BlackOlive > USASteakhouse and BlackOlive > OliveGarden and BlackOlive > Outback and BlackOlive > RapidFire and BlackOlive > MissionBBQ and BlackOlive > ElNopal and BlackOlive> Joella and BlackOlive > Bubba and BlackOlive > Ponderosa:
    print("Black Olive!!\n The address is:\n 700 Clifty Dr\n Madison")
elif CaptainD > MusselBurgerBar and CaptainD > ChinaWind and CaptainD > BlackOlive and CaptainD > Joella and CaptainD > SenorIguanas and CaptainD > RedPepperoni and CaptainD > SmokinCrowes and CaptainD > Rooster and CaptainD > KansaiJapeneseSteakhouse and CaptainD > HarrysStoneGrill and CaptainD > HobokenEddies and CaptainD > RedPepper and CaptainD > GoldenCorral and CaptainD > USASteakhouse and CaptainD > OliveGarden and CaptainD > Outback and CaptainD > RapidFire and CaptainD > MissionBBQ and CaptainD > ElNopal and CaptainD > Bubba and CaptainD > Ponderosa:
    print("Captain D's!!\n The address is:\n 2614 Harry Nichols Ave\n Madison")
elif StorminCrab > MusselBurgerBar and StorminCrab > ChinaWind and StorminCrab > BlackOlive and StorminCrab > Joella and StorminCrab > SenorIguanas and StorminCrab > RedPepperoni and StorminCrab > SmokinCrowes and StorminCrab > Rooster and StorminCrab > KansaiJapeneseSteakhouse and StorminCrab > HarrysStoneGrill and StorminCrab > HobokenEddies and StorminCrab > RedPepper and StorminCrab > GoldenCorral and StorminCrab > USASteakhouse and StorminCrab > OliveGarden and StorminCrab > Outback and StorminCrab > RapidFire and StorminCrab > MissionBBQ and StorminCrab > ElNopal and StorminCrab > CaptainD and StorminCrab > Bubba and StorminCrab > RedLobster and StorminCrab > KingFish and StorminCrab > Ponderosa:
    print("Stormin' Crab!!\n The address is:\n 1360 Veterans Pkwy\n Clarksville")
elif RedLobster > MusselBurgerBar and RedLobster > ChinaWind and RedLobster > BlackOlive and RedLobster > Joella and RedLobster > SenorIguanas and RedLobster > RedPepperoni and RedLobster > SmokinCrowes and RedLobster > Rooster and RedLobster > KansaiJapeneseSteakhouse and RedLobster > HarrysStoneGrill and RedLobster > HobokenEddies and RedLobster > RedPepper and RedLobster > GoldenCorral and RedLobster > USASteakhouse and RedLobster > OliveGarden and RedLobster > Outback and RedLobster > RapidFire and RedLobster > MissionBBQ and RedLobster > ElNopal and RedLobster > CaptainD and RedLobster > StorminCrab and RedLobster > Bubba and RedLobster > KingFish and RedLobster > Ponderosa:
    print("Red Lobster!!\n The address is:\n 951 E Lewis and Clark Pkwy\n Suite 3004\n Clarksville")
elif KingFish > ChinaWind and KingFish > BlackOlive and KingFish > Joella and KingFish > SenorIguanas and KingFish > RedPepperoni and KingFish > SmokinCrowes and KingFish > Rooster and KingFish > KansaiJapeneseSteakhouse and KingFish > HarrysStoneGrill and KingFish > HobokenEddies and KingFish > RedPepper and KingFish > GoldenCorral and KingFish > USASteakhouse and KingFish > OliveGarden and KingFish > Outback and KingFish > RapidFire and KingFish > MissionBBQ and KingFish > ElNopal and KingFish > CaptainD and KingFish > StorminCrab and KingFish > Bubba and KingFish > RedLobster and KingFish > Ponderosa:
    print("King Fish!!\n The address is:\n 601 W Riverside Dr\n Jeffersonville")
elif MusselBurgerBar > ChinaWind and MusselBurgerBar > BlackOlive and MusselBurgerBar > Joella and MusselBurgerBar > SenorIguanas and MusselBurgerBar > RedPepperoni and MusselBurgerBar > SmokinCrowes and MusselBurgerBar > Rooster and MusselBurgerBar > KansaiJapeneseSteakhouse and MusselBurgerBar > HarrysStoneGrill and MusselBurgerBar > HobokenEddies and MusselBurgerBar > RedPepper and MusselBurgerBar > GoldenCorral and MusselBurgerBar > USASteakhouse and MusselBurgerBar > OliveGarden and MusselBurgerBar > Outback and MusselBurgerBar > RapidFire and MusselBurgerBar > MissionBBQ and MusselBurgerBar > ElNopal and MusselBurgerBar > CaptainD and MusselBurgerBar > StorminCrab and MusselBurgerBar > Bubba and MusselBurgerBar > RedLobster and MusselBurgerBar > KingFish and MusselBurgerBar > Ponderosa:
    print("Mussel and Burger Bar\n The address:\n 9200 Taylorsville Rd\n Louisville")
else:
    print("Too difficult to decide. Please try again later.")
print("Enjoy your night!!")
