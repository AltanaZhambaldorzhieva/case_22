from employee import Employee

class Doctor(Employee):
    """
        Class describes a doctor, inheriting from the Employee class, with additional details.
    """

    AVAILABLE_CATEGORIES = ['высшая', 'первая', 'вторая']

    def __init__(self, full_name, gender, birthday, place_birth, married, passport,
                 residence_address, level_education, phone_number,
                 know_foreign_language, education_document, year_graduation, qualification,
                 specialty, profession, work_experience,
                 academic_degree, academic_rank, category,
                 trainings, medical_errors, diagnosis_patients,
                 treatment_patients, rehabilitation_patients):
        super().__init__(full_name, gender, birthday, place_birth, married, passport, residence_address,
                         level_education, phone_number, know_foreign_language,
                         education_document, year_graduation, qualification,
                         specialty, profession, work_experience)

        self.academic_degree = academic_degree if isinstance(academic_degree, bool) else None
        self.academic_rank = academic_rank if isinstance(academic_rank, bool) else None
        self.category = category
        self.trainings = trainings if isinstance(trainings, bool) else None
        self.medical_errors = medical_errors if isinstance(medical_errors, bool) else None
        self.diagnosis_patients = diagnosis_patients if isinstance(diagnosis_patients, bool) else None
        self.treatment_patients = treatment_patients if isinstance(treatment_patients, bool) else None
        self.rehabilitation_patients = rehabilitation_patients if isinstance(rehabilitation_patients, bool) else None

    @property
    def category(self):
        """
            Returns a category of a doctor.
        """
        return self.__category

    @category.setter
    def category(self, value):
        """
            Sets a category of a doctor.
        """
        if isinstance(value, str) and value in Doctor.AVAILABLE_CATEGORIES:
            self.__category = value
        else:
            self.__category = None

    def __str__(self):
        employee_info = super().__str__()

        degree = f'Ученая степень: {"да" if self.academic_degree == True else "нет" if self.academic_degree == False else ""}\n'
        rank = f'Ученое звание: {"да" if self.academic_rank == True else "нет" if self.academic_rank == False else ""}\n'
        category = f'Категория: {self.category}\n' if self.category else ''
        train = f'Обучение: {"да" if self.trainings == True else "нет" if self.trainings == False else ""}\n'
        errors = f'Медицинские ошибки: {self.medical_errors}\n' if self.medical_errors else ''
        diagnosis = f'Диагнозы пациентов: {"да" if self.diagnosis_patients == True else "нет" if self.diagnosis_patients == False else ""}\n'
        treatment = f'Лечение пациентов: {"да" if self.treatment_patients == True else "нет" if self.treatment_patients == False else ""}\n'
        rehab = f'Пациенты на реабилитации: {"да" if self.rehabilitation_patients == True else "нет" if self.rehabilitation_patients == False else ""}\n'

        return ''.join([employee_info, degree, rank, category, train, errors, diagnosis, treatment, rehab])

    def __repr__(self):
        return super().__repr__()
