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
        """
        Метод для проверки високосности года
        :param year: int, str
        :return: bool

        Example:
            year1 = 2019  # False
            year2 = 2020  # True
        """
        year = Date.__valid_type_value(year)

        if year % 4 != 0:
            return False
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    @classmethod
    def get_max_day(cls, year, month):
        """
        Возвращаетколичество дней в месяце, учитывает високосность года
        :param year: int, str
        :param month: int, str
        :return: int
        """
        year = cls.__valid_type_value(year)
        month = cls.__valid_type_value(month)

        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @classmethod
    def __valid_type_value(cls, value):
        if not isinstance(value, (int, str)):
            raise TypeError
        if isinstance(value, str):
            if not value.isdigit():
                raise ValueError
            else:
                value = int(value)
        return value

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

    @property
    def date(self):
        return self.__str__

    @date.setter
    def date(self, value):
        value = value.split(".")
        self.__day = int(value[0])
        self.__month = int(value[1])
        self.__year = int(value[2])

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def add_day(self, day):  #TODO
        day = self.__valid_type_value(day)
        if self.is_leap_year(self.year):
            year = self.year + (day // 366)
            month = self.month + ((366 % day) // 12)
            dnei = self.get_max_day(year, month)
            if ((366 % day) % 12) // dnei >= 1:
                month += 1
            day = ((day % 366) % 12) % dnei
            return f"{day}.{month}.{year}"
        else:
            year = self.year + (day // 365)
            month = self.month + ((day % 365) // 12)
            dnei = self.get_max_day(year, month)
            if ((day % 366) % 12) // dnei > 0:
                month += 1
            day = ((day % 366) % 12) % dnei
            return f"{day}.{month}.{year}"

    def add_month(self, month):
        month = self.__valid_type_value(month)
        return f"{self.day}.{self.month + (month%12)}.{self.year + (month//12)}"

    def add_year(self, year):
        year = self.__valid_type_value(year)
        return f"{self.day}.{self.month}.{self.year + year}"

    @staticmethod
    def date2_date1(date2, date1):  #TODO
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
    data = Date(2019, 9, 19)
    print(data)
    data.date = '23.2.2020'
    print(data)
    print(data.is_leap_year('2019'))
    print(data.get_max_day(2019, 2))
    print(data.add_year(15))
    print(data.add_month(13))
    print(data.add_day(15))
    # ld = Date(2019, 4, 6)
    # print(ld.get_max_day(2019, 4))
    # d1 = Date(2020, 2, 7)
    # d2 = Date(2020, 2, 6)
    # print(d1.kolvo_dnei - d2.kolvo_dnei)
    # print(d1 > d2)
    # # __add__
    # d1 + 5
    # print(d1)
    # # __radd__
    # 5 + d1
    # print(d1)
