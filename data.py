import datetime
import Bus

def t(h, m):
    return datetime.time(h, m)


SupportedPlaces = ["target", "mercedmall", "walmart", "amtrak", "downtown"]

BobcatExpressTime = [t(11,11), t(12,51), t(14,16),
                 t(15,59), t(17,24), t(19,4)]

BobcatExpressPlace = ["target", "mercedmall", "walmart", "amtrak", "downtown"]


C2Time = [t(7,2), t(8,15), t(9,13), t(10,26), t(11,24),
          t(12,37), t(13,35), t(14,36), t(15,34), t(16,47),
          t(17,45), t(18,58), t(19,56), t(21,9), t(22,7)]

C2Place = ["target", "mercedmall"]


GLineTime = [t(6,57), t(8,20), t(9,28), t(10,36), t(11,44),
             t(13,7), t(14,15), t(15,28), t(16,51), t(17,59),
             t(19,7), t(20,30), t(21,38)]

GLinePlace = ["amtrak", "downtown"]



BobcatExpress = Bus.Bus("Bobcat Express", BobcatExpressTime, BobcatExpressPlace)
C2 = Bus.Bus("C2", C2Time, C2Place)
GLine = Bus.Bus("GLine", GLineTime, GLinePlace)

Buses = [BobcatExpress, C2, GLine]

if __name__ == '__main__':
    print("Welcome to data, data is not an executable")