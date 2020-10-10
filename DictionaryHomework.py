import datetime

def GuessGame(DictKey, DictVal):
    for dictKey in SongLibrary:
        if (dictKey == DictKey and DictVal == SongLibrary[DictKey]) :
            print("You are correct!")
            return True
        else:
            print("You are wrong!")
            return False

SongLibrary = {
"Title" : "Old Time Religion",
"Artist" : "Parker Millshap",
"Genre" : "Country",
"DurationSecs" : 234,
"DurationMins": 3.9,
"FirstListenDate" : datetime.datetime(2019,10,23),
"FavouriteVerse" : "And he had a vision\nOf a fire it burned up all of the land\nYou could call it superstition\nYou could run just as fast as you can\nHe took a beating\nHis father screamed at the top of his lungs\nAn Old Testament reading\nIf you spare the rod you spoil the son"
}

for DictKey in SongLibrary:
    dictKey = input("Do you want to make an educated guess about which key is coming?\n")
    dictVal = input("Do you want to make an educated guess about which value is coming?\n")
    GuessGame(dictKey, dictVal)
    print(DictKey, ": ", SongLibrary[DictKey])