from employee import Employee

class Nurse(Employee):
    """
        Class representing a nurse, inheriting from the Employee class.
    """
    def __init__(self, full_name, gender, birthday, place_birth, married, passport,
                 residence_address, level_education, phone_number,
                 know_foreign_language, education_document, year_graduation, qualification,
                 specialty, profession, work_experience,
                 sanitary_service, patient_care, medical_procedures):
        super().__init__(full_name, gender, birthday, place_birth, married, passport, residence_address,
                         level_education, phone_number, know_foreign_language,
                         education_document, year_graduation, qualification,
                         specialty, profession, work_experience)
        self.sanitary_service = sanitary_service if isinstance(sanitary_service, bool) else None
        self.patient_care = patient_care if isinstance(patient_care, bool) else None
        self.medical_procedures = medical_procedures if isinstance(medical_procedures, bool) else None

    def __str__(self):
        employee_info = super().__str__()
        sanitary = f'Санитарная служба: {"да" if self.sanitary_service == True
        else "нет" if self.sanitary_service == False else ""}\n'
        care = f'Уход за пациентами: {"да" if self.patient_care == True
        else "нет" if self.patient_care == False else ""}\n'
        procedures = f'Медицинские процедуры: {"да" if self.medical_procedures == True
        else "нет" if self.medical_procedures == False else ""}\n'

        return ''.join([employee_info, sanitary, care, procedures])

    def __repr__(self):
        return super().__repr__()
