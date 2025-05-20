from patient import Patient


class HospitalPatient(Patient):
    """
        Class describes a hospital patient, inheriting from the Patient class, with additional medical details.
    """
    def __init__(self, full_name, gender, birthday,
                 place_birth, married, passport,
                 residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study,
                 blood_type, rhesus_affiliation, allergic_reactions,
                 medical_department, room_number, clinical_diagnosis):
        super().__init__(full_name, gender, birthday,
                         place_birth, married, passport,
                         residence_address, level_education, phone_number,
                         medical_policy, status, place_work_study,
                         blood_type, rhesus_affiliation, allergic_reactions)

        self.medical_department = medical_department
        self.room_number = room_number
        self.clinical_diagnosis = clinical_diagnosis

    def __str__(self):
        patient_info = super().__str__()
        department = f'Медицинский отдел: {self.medical_department}\n' if self.medical_department else ''
        room = f'Номер палаты: {self.room_number}\n' if self.room_number else ''
        diagnosis = (f'Диагноз: {self.clinical_diagnosis}\n'
                     if self.clinical_diagnosis and self.clinical_diagnosis != 'Диагноз не выявлен' else '')

        return ''.join([patient_info, department, room, diagnosis])

    def __repr__(self):
        return super().__repr__()
