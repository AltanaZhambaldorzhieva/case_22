from person import Person

class Patient(Person):
    """
        Class describes a patient with personal and medical details.
    """

    AVAILABLE_STATUS = ['рабочий', 'служащий', 'обучающийся']
    AVAILABLE_BLOOD_TYPES = ['1', '2', '3', '4']
    AVAILABLE_RHESUS_AFFILIATION = ['-', '+']

    def __init__(self, full_name, gender, birthday,
                 place_birth, married, passport,
                 residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study,
                 blood_type, rhesus_affiliation, allergic_reactions):
        super().__init__(full_name, gender, birthday,
                         place_birth, married, passport,
                         residence_address, level_education, phone_number)

        self.medical_policy = medical_policy
        self.status = status
        self.place_work_study = place_work_study
        self.blood_type = blood_type
        self.rhesus_affiliation = rhesus_affiliation
        self.allergic_reactions = allergic_reactions

    @property
    def status(self):
        """
            Returns a status.
        """
        return self.__status

    @property
    def blood_type(self):
        """
            Returns a blood type of human.
        """
        return self.__blood_type

    @property
    def rhesus_affiliation(self):
        """
            Returns a blood rhesus.
        """
        return self.__rhesus_affiliation

    @status.setter
    def status(self, value):
        """
            Sets the patient's status, ensuring it's one of the available options.
        """
        self.__status = value if value in Patient.AVAILABLE_STATUS else None

    @blood_type.setter
    def blood_type(self, value):
        """
            Sets the patient's blood type, ensuring it's one of the available types.
        """
        self.__blood_type = value if value in Patient.AVAILABLE_BLOOD_TYPES else None

    @rhesus_affiliation.setter
    def rhesus_affiliation(self, value):
        """
            Sets the patient's rhesus affiliation, ensuring it's one of the available options.
        """
        self.__rhesus_affiliation = value if value in Patient.AVAILABLE_RHESUS_AFFILIATION else None

    def __str__(self):
        person = super().__str__()
        blood = (f'Группа крови: {self.blood_type} ({self.rhesus_affiliation})\n'
                 if self.blood_type and self.rhesus_affiliation else
                 f'Группа крови: {self.blood_type}\n' if self.blood_type else '')
        status = f'Статус: {self.status}\n' if self.status else ''
        policy = f'Медицинский полис: {self.medical_policy}\n' if self.medical_policy else ''
        place = f'Место работы: {self.place_work_study}\n' if self.place_work_study else ''
        react = f'Аллергические реакции: {self.allergic_reactions}\n' if self.allergic_reactions else ''

        return ''.join([person, policy, status, place, blood, react])

    def __repr__(self):
        return super().__repr__()
