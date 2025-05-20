from patient import Patient

class AmbulatoryPatient(Patient):
    """
        Class describes an ambulatory patient, inheriting from the Patient class, with additional details.
    """

    AVAILABLE_DISABILITY = ['0', '1', '2', '3']
    AVAILABLE_HEALTH_GROUP = ['I', 'II', 'III']

    def __init__(self, full_name, gender, birthday,
                 place_birth, married, passport,
                 residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study,
                 blood_type, rhesus_affiliation, allergic_reactions,
                 territorial_number, disability, health_group, chronic_diagnosis):
        super().__init__(full_name, gender, birthday,
                         place_birth, married, passport,
                         residence_address, level_education, phone_number,
                         medical_policy, status, place_work_study,
                         blood_type, rhesus_affiliation, allergic_reactions)

        self.territorial_number = territorial_number
        self.disability = disability
        self.health_group = health_group
        self.chronic_diagnosis = chronic_diagnosis if isinstance(chronic_diagnosis, str) else None

    @property
    def territorial_number(self):
        """
            Returns a territorial number.
        """
        return self.__territorial_number

    @property
    def disability(self):
        """
            Return a disability of patient.
        """
        return self.__disability

    @property
    def health_group(self):
        """
            Returns a health group.
        """
        return self.__health_group

    @territorial_number.setter
    def territorial_number(self, value):
        """
            Sets the territorial number, ensuring it is an integer between 1 and 20.
        """
        if isinstance(value, int) and 1 <= int(value) <= 20:
            self.__territorial_number = value
        else:
            self.__territorial_number = None

    @disability.setter
    def disability(self, value):
        """
            Sets the disability category, ensuring it is one of the valid categories.
        """
        if isinstance(value, int) and value in AmbulatoryPatient.AVAILABLE_DISABILITY:
            self.__disability = value
        else:
            self.__disability = None

    @health_group.setter
    def health_group(self, value):
        """
            Sets the health group, ensuring it is one of the valid groups.
        """
        if isinstance(value, int) and value in AmbulatoryPatient.AVAILABLE_HEALTH_GROUP:
            self.__health_group = value
        else:
            self.__health_group = None

    def __str__(self):
        patient_info = super().__str__()

        territorial = f'Территориальный номер: {self.territorial_number}\n' if self.territorial_number else ''
        disability = f'Группа инвалидности: {self.disability}\n' if self.__disability and self.disability != '0' else ''
        health = f'Группа здоровья: {self.health_group}\n' if self.health_group else ''
        diagnosis = f'Хронический диагноз: {self.chronic_diagnosis}\n' if self.chronic_diagnosis and self.chronic_diagnosis != 'Не выявлено' else ''

        return ''.join([patient_info, territorial, disability, health, diagnosis])

    def __repr__(self):
        return super().__repr__()
