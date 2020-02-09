class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        if not self.__is_valid_date(self.year, self.month, self.day):
            return f'{self.day}.{self.month}.{self.year}'

    def __repr__(self):
        return f'Date({self.year}, {self.month!r}, {self.day!r})'

    @property  # лишнее
    def kolvo_dnei(self):
        return self.year * 365 + (self.month - 1) * 30 + self.day

    @staticmethod
    def is_leap_year(year):
        return False  #

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        return self.__str__

    @classmethod
    def __is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        pass

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    @staticmethod
    def date2_date1(date2, date1):
        pass

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                elif self.day > other.day:
                    return False

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.__day += other

    def __radd__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.__day += other

if __name__ == "__main__":
    # data = Date(2019, 9, 19)
    # print(data)
    d1 = Date(2020, 2, 7)
    d2 = Date(2020, 2, 6)
    print(d1.kolvo_dnei - d2.kolvo_dnei)
    print(d1 > d2)
    # __add__
    d1 + 5
    print(d1)
    # __radd__
    5 + d1
    print(d1)
