from datetime import date, timedelta
from sys import argv

class TrainWeeks(object):
    def __init__(self, month, day, year, nr_weeks=16, nr_days=0):
        self._race = date(year, month, day)
        self._duration = timedelta(weeks=nr_weeks, days=nr_days)
        self._start = self._race - self._duration + timedelta(1)

    @property
    def race_day(self):
        return '{m}/{d}/{y}'.format(
                m=self._race.month, d=self._race.day, y=self._race.year)
    
    @property
    def training_start_day(self):
        return '{m}/{d}/{y}'.format(
                m=self._start.month, d=self._start.day, y=self._start.year)

    @property
    def duration(self):
        return self._duration.days

    def __str__(self):
        return 'Training of {d} days starts at {s} for race day {r} '.format(
                r=self.race_day, s=self.training_start_day, d=self.duration)

    def __repr__(self):
        return 'TrainWeeks({m}, {d}, {y}, nr_days={u})'.format(
                m=self._race.month,
                d=self._race.day,
                y=self._race.year,
                u=self._duration.days)
if __name__ == '__main__':
    def usage_and_exit():
        print('Today is {t}.\nUsage: {c} <mm/dd/yy> <number of weeks>'.format(
            t=date.today(), c=argv[0].split('/')[-1]))
        exit()
    argc = len(argv)
    if argc == 1:
        usage_and_exit()
    date_minutes = argv[1].split('/')
    if len(date_minutes) < 2:
        usage_and_exit()
    if len(date_minutes) < 3:
        date_minutes.append(str(date.today().year))
    if argc < 3:
        tw = TrainWeeks(int(date_minutes[0]),
                        int(date_minutes[1]),
                        int(date_minutes[2]))
    else:
        tw = TrainWeeks(int(date_minutes[0]),
                        int(date_minutes[1]),
                        int(date_minutes[2]),
                        nr_weeks=int(argv[2]))
    print(tw)
