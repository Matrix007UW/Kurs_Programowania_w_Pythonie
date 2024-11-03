import os, json, csv, argparse, random
from pathlib import Path

daysTable = ['pn', 'wt', 'śr', 'cz', 'pt', 'so', 'nd']
monthsTable = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
dayTimesTable = ['r', 'w']

def create_file(month, day, dayTime):
    folderPath = os.path.join(month, day, dayTime)
    os.makedirs(folderPath, exist_ok=True)

    filePath = os.path.join(folderPath, 'Dane.csv')
    if os.path.exists(filePath):
        print('Plik już istnieje')
    else:
        create_data_file(filePath)

def create_data_file(filePath):
    plik = open(filePath, 'w')
    model = random.choice(['A', 'B', 'C'])
    wynik = random.randint(0, 1000)
    czas = f"{random.randint(0, 1000)}s"

    plik.write("Model; Wynik; Czas; \n")
    plik.write(f"{model}; {wynik}; {czas}; \n")
    plik.close()

def readFile(month, day, dayTime):
    folderPath = os.path.join(month, day, dayTime)
    filePath = os.path.join(folderPath, 'Dane.csv')

    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            readFile = csv.reader(file)
            print("Miesiąc: " + month + ", Dzień: " + day + ", Pora: " + dayTime)
            i = 0
            for wiersz in readFile:
                if(i == 1):
                    print(wiersz)
                i += 1
    else:
        print('Plik nie istnieje')

def days_split(daysData):
    if(daysData in daysTable):
        returnValue = []
        returnValue.append(daysData)
    else:
        startingDay, endingDay = daysData.split('-')
        returnValue = daysTable[daysTable.index(startingDay):daysTable.index(endingDay) + 1]
    return returnValue

def split_and_do(monthsData, daysData, dayTimesData, tworzenie):
    dayTimesIterator = 0
    for i in range(len(monthsData)):
        month = monthsData[i]
        days = days_split(daysData[i])
        for day in days:
            if(dayTimesIterator > len(dayTimesData) - 1):
                dayTime = 'r'
            else:
                dayTime = dayTimesData[dayTimesIterator]
            if(tworzenie):
                create_file(month, day, dayTime)
            else:
                readFile(month, day, dayTime)
            dayTimesIterator += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Program do tworzenia i odczytywania plików csv w folderach.\n Przykład użycia: python3 Mateusz_Kamiński_03.py -t -m styczeń luty -d pn-wt śr-pt -p r w')
    parser.add_argument('-t', '--tworzenie', action='store_true', help='Tworzenie plików zamiast odczytu.')
    parser.add_argument('-m', '--miesiace', nargs='+', choices=monthsTable, required=True, help='Wybierz miesiące.')
    parser.add_argument('-d', '--dni', nargs='+', required=True, help='Wybierz zakres dni tygodnia (np. pn-wt, śr-pt).')
    parser.add_argument('-p', '--pora', nargs='*', default=['r'], choices=['r', 'w'], help='Wybierz porę dnia: rano (r), wieczór (w). Domyslnie rano.')
    args = parser.parse_args()
    
    split_and_do(args.miesiace, args.dni, args.pora, args.tworzenie)


