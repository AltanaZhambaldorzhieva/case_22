from person import Person

class Employee(Person):
    """
        Class describes a employee info.
    """

    AVAILABLE_PROFESSIONS = ['врач', 'медсестра', 'медицинская сестра']

    def __init__(self, full_name, gender, birthday, place_birth, married,
                 passport, residence_address,
                 level_education, phone_number,
                 know_foreign_language, education_document,
                 year_graduation, qualification, specialty,
                 profession, work_experience):
        super().__init__(full_name, gender, birthday, place_birth, married, passport, residence_address,
                         level_education, phone_number)

        self.know_foreign_language = know_foreign_language if isinstance(know_foreign_language, bool) else None
        self.education_document = education_document if isinstance(education_document, str) else None
        self.year_graduation = year_graduation
        self.qualification = qualification if isinstance(qualification, str) else None
        self.specialty = specialty if isinstance(specialty, str) else None
        self.profession = profession
        self.work_experience = work_experience

    @property
    def year_graduation(self):
        """
            Returns year graduation.
        """
        return self.__year_graduation

    @property
    def profession(self):
        """
            Returns a profession of employee.
        """
        return self.__profession

    @property
    def work_experience(self):
        """
            Returns a work experience of employee.
        """
        return self.__work_experience

    @year_graduation.setter
    def year_graduation(self, value):
        """
            Sets a year graduation.
        """
        if isinstance(value, int) and 1950 <= value <= 2030:
            self.__year_graduation = value
        else:
            self.__year_graduation = None

    @profession.setter
    def profession(self, value):
        """
            Sets the profession of the employee, ensuring it is one of the available professions.
        """
        if isinstance(value, str) and value in Employee.AVAILABLE_PROFESSIONS:
            self.__profession = value
        else:
            self.__profession = None

    @work_experience.setter
    def work_experience(self, value):
        """
            Sets the years of work experience, ensuring it is between 0 and 60.
        """
        if isinstance(value, int) and 0 <= value <= 60:
            self.__work_experience = value
        else:
            self.__work_experience = None

    def __str__(self):
        person_info = super().__str__()
        foreign_language = f'Знание иностранного языка: {"да" if self.know_foreign_language == "True"
        else "нет" if self.know_foreign_language == "False" else ""}\n'
        education = f'Документ об образовании: {self.education_document}\n' if self.education_document else ''
        graduation = f'Год окончания: {self.year_graduation}\n' if self.year_graduation else ''
        qualification = f'Квалификация: {self.qualification}\n' if self.qualification else ''
        specialty = f'Специальность: {self.specialty}\n' if self.specialty else ''
        profession = f'Профессия: {self.profession}\n' if self.profession else ''
        experience = f'Опыт работы: {self.work_experience}\n' if self.work_experience else ''

        return ''.join(
            [person_info, foreign_language, education, graduation, qualification, specialty, profession, experience])

    def __repr__(self):
        return super().__repr__()
