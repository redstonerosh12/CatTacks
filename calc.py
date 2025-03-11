import data
import datetime

def main():
    print(f"supported places: {data.SupportedPlaces}")
    place = input("Place to go: ")
    now = datetime.datetime.now().time().replace(second=0, microsecond=0)
    availableTime = False
    for bus in data.Buses:
        if place in bus.destinations:
            nextBus = next((t for t in bus.timings if t >= now))
            print(f"For bus {bus.name}, The next bus is at: {nextBus}")
            availableTime = True

    if not availableTime:
        print("sorry there are no buses in the current scope of the project")

if __name__ == '__main__':
    main()


