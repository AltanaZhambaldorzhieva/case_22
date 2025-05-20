import re

class Person:
    """
        Class of a personal info of a medical personal and patients.
    """

    VALID_GENDERS = ['муж.', 'жен.']
    VALID_EDUCATION = ['высшее', 'ср.спец', 'среднее']


    __id = 1

    def __init__(self, full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number):
        self.__id = Person.__id
        Person.__id += 1

        self.full_name = full_name
        self.gender = gender
        self.birthday = birthday
        self.place_birth = place_birth if isinstance(place_birth, str) else None
        self.married = married if isinstance(married, bool) else None
        self.passport = passport
        self.residence_address = residence_address if isinstance(residence_address, str) else None
        self.level_education = level_education
        self.phone_number = phone_number

    @property
    def full_name(self):
        """
            Returns a full name of a person.
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        """
            Sets a full name of a person.
        """
        if isinstance(value, str):
            self.__full_name = value[:25]
        else:
            self.__full_name = None

    @property
    def gender(self):
        """
            Returns a gender.
        """
        return self.__gender

    @gender.setter
    def gender(self, value):
        """
            Sets a gender.
        """
        if isinstance(value, str) and value in Person.VALID_GENDERS:
            self.__gender = value
        else:
            self.__gender = None

    @property
    def birthday(self):
        """
            Returns a birthday date.
        """
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        """
            Sets the birthday of the person if the format is correct.
        """
        if re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', value):
            self.__birthday = value
        else:
            self.__birthday = None

    @property
    def passport(self):
        """
            Returns the passport details of the person.
        """
        return self.__passport

    @passport.setter
    def passport(self, value):
        """
            Sets the passport details of the person if the format is correct.
        """
        if re.fullmatch(r'^\d{4}\s\d{6}\s\d{2}\.\d{2}\.\d{4}$', value):
            self.__passport = value
        else:
            self.__passport = None

    @property
    def level_education(self):
        """
            Returns the level of education of the person.
        """
        return self.__level_education

    @level_education.setter
    def level_education(self, value):
        """
            Returns the level of education options.
        """
        if isinstance(value, str) and value in Person.VALID_EDUCATION:
            self.__level_education = value
        else:
            self.__level_education = None

    @property
    def phone_number(self):
        """
            Return a phone number.
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        """
            Sets a phone number.
        """
        if (isinstance(value, str)
                and re.fullmatch(r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$', value)):
            self.__phone_number = value
        else:
            self.__phone_number = None

    def __str__(self):
        _id = f'Номер: {self.__id}\n'
        name = f'ФИО: {self.full_name}\n' if self.full_name else ''
        gender = f'Пол: {self.gender}\n' if self.gender else ''
        birth = f'Дата рождения: {self.birthday}\n' if self.birthday else ''
        place_birth = f'Место рождения: {self.place_birth}\n' if self.place_birth else ''
        married = f'В браке: {"да" if self.married else "нет"}\n'
        passport = f'Паспорт: {self.passport}\n' if self.passport else ''
        residence_address = f'Адрес регистрации: {self.residence_address}\n' if self.residence_address else ''
        education = f'Уровень образования: {self.level_education}\n' if self.level_education else ''
        phone = f'Телефон: {self.phone_number}\n' if self.phone_number else ''

        return ''.join([
            _id, name, gender, birth, place_birth, married,
            passport, residence_address, education, phone
        ])

    def __repr__(self):
        """
            Returns a string.
        """
        return f'{self.__id}, {self.full_name}'
