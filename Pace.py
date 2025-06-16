from Const import Const
import sys

class Pace(object):
    _marathon = Const(42195)
    _mile = Const(1609.34)

    class TimeFormatError(Exception):
        pass

    def __init__(self, distance, time):
        self._seconds = self.time_to_seconds(time)
        self._meters = self.distance_to_meter(str(distance))

    def __repr__(self):
        return 'Pace("' + str(self._meters) + '", "' + self.seconds_to_time(self._seconds) + '")'

    def __str__(self):
        return '(meters: ' + str(self._meters) + ', seconds: ' + str(self._seconds) +')'

    @staticmethod
    def seconds_to_time(time):
        if time < 10:
            return '0:0' + str(time)
        if time < 60:
            return '0:' + str(time)
        if time < 3600:
            s = time % 60
            if s < 10:
                return str(time//60) + ':0' + str(s)
            return str(time//60) + ':' + str(s)
        s = time % 60
        m = time % 3600
        m //= 60
        time = str(time // 3600)
        if m < 10:
            time = time + ':0' + str(m)
        else:
            time = time + ':' + str(m)
        if s < 10:
            return time + ':0' + str(s)
        return time + ':' + str(s)       

    @staticmethod
    def time_to_seconds(time):
        f = time.split(':')
        if len(f) > 3 or len(f) < 2:
            raise TimeFormatError("invalid time format" + time)
        s = int(f[0]) * 60
        s += int(f[1])
        if len(f) == 3:
            s *= 60
            s += int(f[2])
        return s

    def distance_to_meter(self, distance):
        if distance == 'full':
            return float(self._marathon.value)
        if distance == 'half':
            return float(self._marathon.value) / 2
        if distance == 'pace' or distance == 'mile':
            return self._mile.value
        if distance == 'k5' or distance == 'K5':
            return float(1500)
        if distance == 'km' or distance == 'Km':
            return float(1000)
        if distance.endswith('M'):
            return float(distance[:-1]) * self._mile.value
        if distance.endswith('k') or distance.endswith('K'):
            return float(distance[:-1]) * 1000
        if distance.endswith('m') or distance.endswith('K'):
            return float(distance[:-1])
        return float(distance)

    # adjusted by 1.02 to account for inaccuray of GPS tracked distance
    @property
    def gps_mile(self):
        return self.seconds_to_time(int((self._seconds * self._mile.value)
                                        // (self._meters * 1.02)))

    @property
    def mile(self):
        return self.seconds_to_time(int(self._seconds * self._mile.value // self._meters))

    @property
    def full(self):
        return self.seconds_to_time(int(self._seconds * self._marathon.value // self._meters))

    @property
    def half(self):
        return self.seconds_to_time(int(self._seconds * self._marathon.value // self._meters // 2))

    @property
    def tenK(self):
        return self.seconds_to_time(int(self._seconds * 10000 // self._meters))
    tenk = tenK

    @property
    def fiveK(self):
        return self.seconds_to_time(int(self._seconds * 5000 // self._meters))
    fivek = fiveK

    @property
    def K5(self):
        return self.seconds_to_time(int(self._seconds * 1500 // self._meters))
    k5 = K5

    @property
    def Km(self):
        return self.seconds_to_time(int(self._seconds * 1000 // self._meters))
    km = Km

    def pace(self, distance):
        distance = str(distance)
        return self.seconds_to_time(int(self._seconds * self.distance_to_meter(distance) // self._meters))

if __name__ == '__main__':
    argv = sys.argv[1:]
    argc = len(argv)
    if argc == 0:
        print('Usage: python pace.py <full marathon time>')
        print('       python pace.py <distance> <time>')
        print('                      <distance>: full half pace k5 km *[kKMm]')
        print('                      <time>    : *:* or *:*:*')
        quit()
    if argc == 1:
        p = Pace('full', argv[0])
    else:
        p = Pace(argv[0], argv[1])
    print('GPS ' + p.gps_mile + ', Pace ' + p.mile + ', Full ' + p.full + ', 10k ' + p.tenK + ', 5k ' + p.fiveK + ', 1500m ' + p.K5 + ', 1000m ' + p.Km)
        


                                
