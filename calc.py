import data
import datetime
import sys
import re

def main(now=datetime.datetime.now().time().replace(second=0, microsecond=0), isPreTime=False):
    print(f"supported places: {data.SupportedPlaces}")
    place = input("Place to go: ")
    availableTime = False
    for bus in data.Buses:
        if place in bus.destinations:
            nextBus = next((t for t in bus.timings if t >= now))
            if isPreTime:
                print(f"Leaving at time {now},", end=" ")
            print(f"For bus {bus.name}, The next bus is at: {nextBus}")
            availableTime = True

    if not availableTime:
        print("sorry there are no buses in the current scope of the project")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        time = sys.argv[1]
        pattern = r'^\d{1,2}:\d{1,2}$'  # Matches 1-2 digits, colon, then 2 digits
        if re.match(pattern, time):
            pretime = time.split(":")
            pretimetime = data.t(int(pretime[0]), int(pretime[1]))
            main(pretimetime, isPreTime=True)
        else:
            print("Error with pre defined time defintion defaulting to now")
            main()
    else:
        main()


