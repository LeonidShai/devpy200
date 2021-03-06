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
        """
        Проверка вводимого значения, перевод в int
        :param value: int, str
        :return: int
        """
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
        """
        Проверки вводимых значений
        :param year: int
        :param month: int
        :param day: int
        :return: None
        """
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
        print("Хочу, чтобы была дата:")
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

    def add_day(self, day):
        """
        Добавляет количество дней к дате
        :param day: int, str
        :return: str
        """
        day = self.__valid_type_value(day)  # провурка верности ввода
        d = day

        month = self.__month
        year = self.__year
        den = self.__day

        # 112 - 117 вычисление года
        zn = day // (3 * 365 + 366)
        year += zn * 4
        zn = day % (3 * 365 + 366)
        zn = zn // 365
        year += zn

        day = (day % (3 * 365 + 366)) % 365  # остаток дней после вычисления года
        gde = 0
        if self.is_leap_year(year):
            gde = 1

        # 124 - 134 вычисление месяца
        zn = 0
        kolvo = self.DAY_OF_MONTH[gde][0]
        while kolvo < day:
            zn += 1
            kolvo += self.DAY_OF_MONTH[gde][zn]

        day = day - (kolvo - self.DAY_OF_MONTH[gde][zn])
        month += zn
        if month > 12:
            year += 1
            month -= 12

        gde = 0
        if self.is_leap_year(year):
            gde = 1

        # 141 - 144 calculate the day
        den += day
        if den > self.DAY_OF_MONTH[gde][month - 1]:
            den -= self.DAY_OF_MONTH[gde][month - 1]
            month += 1
        if month > 12:
            year += 1
            month -= 12

        return f"Через {d} дней будет {den}.{month}.{year}"

    def add_month(self, month):
        """
        Добавляет месяц к дате
        :param month: int, str
        :return: str
        """
        month = self.__valid_type_value(month)
        return f"Через {month} месяцев будет {self.day}.{self.month + (month%12)}.{self.year + (month//12)}"

    def add_year(self, year):
        """
        Добавляет год к дате
        :param year: int, str
        :return: str
        """
        year = self.__valid_type_value(year)
        return f"Через {year} лет будет {self.day}.{self.month}.{self.year + year}"

    @staticmethod
    def date2_date1(date1, date2):
        """
        Определяет промежуток времени от одной даты до другой в днях, месяцах и годах
        :param date1: str
        :param date2: str
        :return: str
        """
        date1 = date1.split(".")
        date2 = date2.split(".")
        d1, d2 = int(date1[0]), int(date2[0])
        m1, m2 = int(date1[1]), int(date2[1])
        y1, y2 = int(date1[2]), int(date2[2])
        if y2 < y1:
            y2, y1 = y1, y2
            m2, m1 = m1, m2
            d2, d1 = d1, d2

        y = y2 - y1
        m = m2 - m1
        if m < 0:
            y -= 1
            m = 12 + m

        d = d2 - d1
        if d < 0:
            gde = 0
            if Date.is_leap_year(y):
                gde = 1
            m -= 1
            d = Date.DAY_OF_MONTH[gde][m - 1] + d
        if m < 0:
            y -= 1
            m = 12 + m

        return f"От {d2}.{m2}.{y2} до {d1}.{m1}.{y1} {d} дней, {m} месяцев, {y} лет."


if __name__ == "__main__":
    data = Date(2019, 9, 19)
    print(data)
    data.date = '23.2.2020'
    print(data)
    print(data.is_leap_year('2019'))
    print(data.get_max_day(2019, 2))
    print(data.add_year(15))
    print(data.add_month(13))
    print(data.add_day(1365))
    print(data.date2_date1("12.3.2020", "9.4.2021"))
    ld = Date(2019, 4, 6)
    print(ld.get_max_day(2019, 4))
