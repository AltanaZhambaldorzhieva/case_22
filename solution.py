import re
class Loader:
    """A class for loading patient and employee data from files.
        Attributes:
            hospital_patients (list): List of hospitalized patients
            ambulatory_patients (list): List of outpatients
            nurses (list): List of nurses
            doctors (list): List of doctors
        """
    def __init__(self):
        self.hospital_patients = []
        self.ambulatory_patients = []
        self.nurses = []
        self.doctors = []
    def load_hospital_patients(self, inp):
        with open(inp, "r", encoding="utf=8") as f:
            for pat in f:
                data = pat.split(";")
                if len(data) != 19:
                    continue
                self.hospital_patients.append(HospitalPatient(data[15], data[16], data[17],
                                            full_name=data[0], gender=data[1], birthday=data[2], place_birth=data[3],
                                            married=data[4], passport=data[5], residence_address=data[6],
                                            level_education=data[7], phone_number = data[8], medical_policy=data[9],
                                            status=data[10], place_work_study=data[11], blood_type=data[12],
                                            rhesus_affiliation=data[13], allergic_reactions=data[14]))
    def load_ambulatory_patients(self, inp):
        with open(inp, "r", encoding="utf=8") as f:
            for pat in f:
                data = pat.split(";")
                if len(data) != 20:
                    continue
                self.ambulatory_patients.append(AmbulatoryPatient(data[15], data[16], data[17], data[18],
                                            full_name=data[0], gender=data[1], birthday=data[2], place_birth=data[3],
                                            married=data[4], passport=data[5], residence_address=data[6],
                                            level_education=data[7], phone_number = data[8], medical_policy=data[9],
                                            status=data[10], place_work_study=data[11], blood_type=data[12],
                                            rhesus_affiliation=data[13], allergic_reactions=data[14]))
    def load_nurses(self, inp):
        with open(inp, "r", encoding="utf=8") as f:
            for emp in f:
                data = emp.split(";")
                if len(data) != 20:
                    continue
                self.nurses.append(Nurse(data[16], data[17], data[18],
                                            full_name=data[0], gender=data[1], birthday=data[2], place_birth=data[3],
                                            married=data[4], passport=data[5], residence_address=data[6],
                                            level_education=data[7], phone_number = data[8], know_foreign=data[9],
                                            education_doc=data[10], year_grad=data[11], qual=data[12],
                                            specialty=data[13], profession=data[14], work_ex=data[15]))
    def load_doctors(self, inp):
        with open(inp, "r", encoding="utf=8") as f:
            for emp in f:
                data = emp.split(";")
                if len(data) != 25:
                    continue
                self.doctors.append(Doctor(data[16], data[17], data[18], data[19], data[20], data[21], data[22],
                                           data[23], full_name=data[0], gender=data[1], birthday=data[2],
                                           place_birth=data[3], married=data[4], passport=data[5],
                                           residence_address=data[6], level_education=data[7], phone_number = data[8],
                                           know_foreign=data[9], education_doc=data[10], year_grad=data[11],
                                           qual=data[12], specialty=data[13], profession=data[14], work_ex=data[15]))
class Person:
    """Base class representing a person with personal information.
        Attributes:
            _id_pers (int): Class variable for auto-incrementing IDs
            genders (list): Possible gender values
            educations (list): Possible education levels
        Instance Attributes:
            __id (int): Unique identifier
            __full_name (str): Full name (max 25 chars)
            __gender (str): Gender from allowed values
            __birthday (str): Birth date in DD.MM.YYYY format
            place_birth (str): Place of birth
            married (bool): Marital status
            __passport (str): Passport info in specific format
            residence_address (str): Registered address
            __level_education (str): Education level from allowed values
            __phone_number (str): Phone in +7(XXX)XXX-XX-XX format
        """
    _id_pers = 1
    genders = ["муж.", "жен."]
    educations = ["высшее", "ср.спец","среднее"]
    def __init__(self, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number):
        self.__id = Person._id_pers
        self.__full_name = self.set_name(full_name)
        self.__gender = self.set_gender(gender)
        self.__birthday = self.set_birthday(birthday)
        self.place_birth = self.check_str(place_birth)
        self.married = self.check_bool(married)
        self.__passport = self.set_passport(passport)
        self.residence_address = self.check_str(residence_address)
        self.__level_education = self.set_education(level_education)
        self.__phone_number = self.set_phone(phone_number)
        Person._id_pers += 1
    @staticmethod
    def check_int(value):
        try:
            return int(value)
        except ValueError:
            return None
    @staticmethod
    def check_str(value):
        if isinstance(value, str):
            return value
        return None
    @staticmethod
    def check_bool(value):
        if value == "True":
            return True
        elif value == "False":
            return False
        return None
    def get_name(self):
        return self.__full_name
    def get_gender(self):
        return self.__gender
    def get_birthday(self):
        return self.__birthday
    def get_educations(self):
        return self.__level_education
    def get_phone(self):
        return self.__phone_number
    def set_name(self, value):
        value = self.check_str(value)
        if value and len(value) > 25:
            return value[:25]
        return value
    def set_gender(self, value):
        value = self.check_str(value)
        if value and value in self.genders:
            return value
        return None
    def set_birthday(self, value):
        value = self.check_str(value)
        if (value and len(value) == 10
                and re.fullmatch(r"^\d{2}\.\d{2}\.\d{4}$", value)):
            return value
        return None
    def set_passport(self, value):
        value = self.check_str(value)
        if (value and len(value) == 22
                and re.fullmatch(r"^\d{4} \d{6} \d{2}\.\d{2}\.\d{4}$", value)):
            return value
        return None
    def set_education(self, value):
        value = self.check_str(value)
        if value and value.lower() in self.educations:
            return value.lower()
        return None
    def set_phone(self, value):
        value = self.check_str(value)
        if (value and len(value) == 16
                and re.fullmatch(r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$", value)):
            return value
        return None
    def __repr__(self):
        return f"{self.__id}. {self.__full_name}"
    def __str__(self):
        parts = []
        parts.append(f"Номер: {self.__id}")
        if self.__full_name:
            parts.append(f"ФИО: {self.__full_name}")
        if self.__gender:
            parts.append(f"Пол: {self.__gender}")
        if self.__birthday:
            parts.append(f"Дата рождения: {self.__birthday}")
        if self.place_birth:
            parts.append(f"Место рождения: {self.place_birth}")
        if self.married is not None:
            parts.append(f"В браке: {'да' if self.married else 'нет'}")
        if self.__passport:
            parts.append(f"Паспорт: {self.__passport}")
        if self.residence_address:
            parts.append(f"Адрес регистрации: {self.residence_address}")
        if self.__level_education:
            parts.append(f"Уровень образования: {self.__level_education}")
        if self.__phone_number:
            parts.append(f"Телефон: {self.__phone_number}")
        return '\n'.join(parts)
class Employee(Person):
    """Class representing an employee, inherits from Person.
        Additional Attributes:
            professions (list): Possible profession values
        Instance Attributes:
            know_foreign_language (bool): Foreign language knowledge
            education_document (str): Education document info
            __year_graduation (int): Graduation year (1950-2030)
            qualification (str): Employee qualification
            specialty (str): Employee specialty
            __profession (str): Profession from allowed values
            __work_experience (int): Years of experience (0-60)
        """
    professions = ["врач", "медицинская сестра"]
    def __init__(self, know_foreign, education_doc, year_grad, qual, specialty, profession, work_ex, **kwargs):
        super().__init__(**kwargs)
        self.know_foreign_language = self.check_bool(know_foreign)
        self.education_document = self.check_str(education_doc)
        self.__year_graduation = self.set_graduation(year_grad)
        self.qualification = self.check_str(qual)
        self.specialty = self.check_str(specialty)
        self.__profession = self.set_profession(profession)
        self.__work_experience = self.set_ex(work_ex)
    def get_graduation(self):
        return self.__year_graduation
    def get_profession(self):
        return self.__profession
    def get_ex(self):
        return self.__work_experience
    def set_graduation(self, value):
        value = self.check_int(value)
        if value and 1950 <= int(value) <= 2030:
            return value
        return None
    def set_profession(self, value):
        value = self.check_str(value)
        if value and value.lower() in self.professions:
            return value.lower()
        return None
    def set_ex(self, value):
        value = self.check_int(value)
        if value and (0 <= value <= 60):
            return int(value)
        return None
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        parts = [super().__str__()]
        if self.know_foreign_language is not None:
            parts.append(f"Знает иностранный язык: {'да' if self.know_foreign_language else 'нет'}")
        if self.education_document:
            parts.append(f"Документ об образовании: {self.education_document}")
        if self.__year_graduation:
            parts.append(f"Год окончания: {self.__year_graduation}")
        if self.qualification:
            parts.append(f"Квалификация: {self.qualification}")
        if self.specialty:
            parts.append(f"Специализация: {self.specialty}")
        if self.__profession:
            parts.append(f"Профессия: {self.__profession}")
        if self.__work_experience is not None:
            parts.append(f"Стаж: {self.__work_experience}")
        return '\n'.join(parts)
class Nurse(Employee):
    """Class representing a nurse, inherits from Employee.
       Additional Attributes:
           sanitary_service (bool): Performs sanitary services
           patient_care (bool): Provides patient care
           medical_procedures (bool): Performs medical procedures
       """
    def __init__(self, sanitary_service, patient_care, medical_procedures, **kwargs):
        super().__init__(**kwargs)
        self.sanitary_service = self.check_bool(sanitary_service)
        self.patient_care = self.check_bool(patient_care)
        self.medical_procedures = self.check_bool(medical_procedures)
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        parts = [super().__str__()]
        if self.sanitary_service is not None:
            parts.append(f"Санитарная обработка помещений: {'да' if self.sanitary_service else 'нет'}")
        if self.patient_care is not None:
            parts.append(f"Уход за больными: {'да' if self.patient_care else 'нет'}")
        if self.medical_procedures is not None:
            parts.append(f"Выполнение медицинских процедур: {'да' if self.medical_procedures else 'нет'}")
        return '\n'.join(parts) + "\n"
class Doctor(Employee):
    """Class representing a doctor, inherits from Employee.
        Additional Attributes:
            categories (list): Possible qualification categories
        Instance Attributes:
            academic_degree (bool): Has academic degree
            academic_rank (bool): Has academic rank
            __category (str): Qualification category
            trainings (bool): Completed additional trainings
            medical_errors (str): Information about medical errors
            diagnosis_patients (bool): Performs diagnostics
            treatment_patients (bool): Provides treatment
            rehabilitation_patient (bool): Provides rehabilitation
        """
    categories = ["высшая", "первая", "вторая"]
    def __init__(self, academic_degree, academic_rank, category, trainings, medical_errors, diagnosis_patients,
                 treatment_patients, rehabilitation_patient, **kwargs):
        super().__init__(**kwargs)
        self.academic_degree = self.check_bool(academic_degree)
        self.academic_rank = self.check_bool(academic_rank)
        self.__category = self.set_category(category)
        self.trainings = self.check_bool(trainings)
        self.medical_errors = self.check_str(medical_errors)
        self.diagnosis_patients = self.check_bool(diagnosis_patients)
        self.treatment_patients = self.check_bool(treatment_patients)
        self.rehabilitation_patient = self.check_bool(rehabilitation_patient)
    def get_category(self):
        return self.__category
    def set_category(self, category):
        category = self.check_str(category)
        if category and category.lower() in self.categories:
           return category.lower()
        return None
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        parts = [super().__str__()]
        if self.academic_degree is not None:
            parts.append(f"Ученая степень: {'да' if self.academic_degree else 'нет'}")
        if self.academic_rank is not None:
            parts.append(f"Ученое звание: {'да' if self.academic_rank else 'нет'}")
        if self.__category:
            parts.append(f"Категория: {self.__category}")
        if self.trainings is not None:
            parts.append(f"Повышение квалификации: {'да' if self.trainings else 'нет'}")
        if self.medical_errors:
            parts.append(f"Медицинские ошибки: {self.medical_errors}")
        if self.diagnosis_patients is not None:
            parts.append(f"Выполнение диагностики заболеваний: {'да' if self.diagnosis_patients else 'нет'}")
        if self.treatment_patients is not None:
            parts.append(f"Лечебная практика: {'да' if self.treatment_patients else 'нет'}")
        if self.rehabilitation_patient is not None:
            parts.append(f"Реабилитация больных: {'да' if self.rehabilitation_patient else 'нет'}")
        return '\n'.join(parts) + "\n"
class Patient(Person):
    """Base class representing a patient, inherits from Person.
        Additional Attributes:
            statuses (list): Possible social status values
            rhesuses (list): Possible Rh factor values
        Instance Attributes:
            medical_policy (str): Insurance policy number
            __status (str): Social status from allowed values
            place_work_study (str): Workplace/educational institution
            __blood_type (int): Blood type (1-4)
            __rhesus_affiliation (str): Rh factor (+/-)
            allergic_reactions (str): Allergy information
        """
    statuses = ["рабочий", "служащий", "обучающийся"]
    rhesuses = ["+", "-"]
    def __init__(self, medical_policy, status, place_work_study, blood_type,
                 rhesus_affiliation, allergic_reactions, **kwargs):
        super().__init__(**kwargs)
        self.medical_policy = self.check_str(medical_policy)
        self.__status = self.set_status(status)
        self.place_work_study = self.check_str(place_work_study)
        self.__blood_type = self.set_blood_type(blood_type)
        self.__rhesus_affiliation = self.set_rhesus_affiliation(rhesus_affiliation)
        self.allergic_reactions = self.check_str(allergic_reactions)
    def get_status(self):
        return self.__status
    def get_blood_type(self):
        return self.__blood_type
    def get_rhesus_affiliation(self):
        return self.__rhesus_affiliation
    def set_status(self, value):
        value = self.check_str(value)
        if value and value in self.statuses:
            return value
        return None
    def set_blood_type(self, value):
        value = self.check_int(value)
        if value and 1 <= int(value) <= 4:
            return int(value)
    def set_rhesus_affiliation(self, value):
        value = self.check_str(value)
        if value and value in self.rhesuses:
            return value
        return None
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        parts = [super().__str__()]
        if self.medical_policy:
            parts.append(f"Медицинский полис: {self.medical_policy}")
        if self.get_status():
            parts.append(f"Cтатус: {self.get_status()}")
        if self.place_work_study:
            parts.append(f"Место работы (учёбы): {self.place_work_study}")
        if self.get_blood_type():
            part = f"Группа крови: {self.get_blood_type()}"
            if self.get_rhesus_affiliation():
                part += f"({self.get_rhesus_affiliation()})"
            parts.append(part)
        if self.allergic_reactions:
            parts.append(f"Аллергические реакции: {self.allergic_reactions}")
        return '\n'.join(parts)
class HospitalPatient(Patient):
    """Class representing a hospitalized patient, inherits from Patient.
       Additional Attributes:
           medical_department (str): Hospital department
           room_number (int): Room number
           clinical_diagnosis (str): Primary diagnosis
       """
    def __init__(self, medical_department, room_number, clinical_diagnosis, **kwargs):
        super().__init__(**kwargs)
        self.medical_department = self.check_str(medical_department)
        self.room_number = self.check_int(room_number)
        self.clinical_diagnosis = self.check_str(clinical_diagnosis)
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        parts = [super().__str__()]
        if self.medical_department:
            parts.append(f"Отделение: {self.medical_department}")
        if self.room_number is not None:
            parts.append(f"Палата: {self.room_number}")
        if self.clinical_diagnosis:
            parts.append(f"Клинический диагноз: {self.clinical_diagnosis}")
        return '\n'.join(parts) + "\n"
class AmbulatoryPatient(Patient):
    """Class representing an outpatient, inherits from Patient.
        Additional Attributes:
            groups (list): Possible health group values
        Instance Attributes:
            __territorial_number (int): Territorial clinic number (1-20)
            __disability (int): Disability group (0-3)
            __health_group (str): Health group from allowed values
            chronic_diagnosis (str): Chronic conditions
        """
    groups = ["I", "II", "III"]
    def __init__(self, territorial_number, disability, health_group, chronic_diagnosis, **kwargs):
        super().__init__(**kwargs)
        self.__territorial_number = self.set_ternum(territorial_number)
        self.__disability = self.set_disability(disability)
        self.__health_group = self.set_group(health_group)
        self.chronic_diagnosis = self.check_str(chronic_diagnosis)
    def get_ternum(self):
        return self.__territorial_number
    def get_disability(self):
        return self.__disability
    def get_group(self):
        return self.__health_group
    def set_ternum(self, value):
        value = self.check_int(value)
        if value and 1 <= value <= 20:
            return value
        return None
    def set_disability(self, value):
        value = self.check_int(value)
        if value and 0 <= value <= 3:
            return value
        return None
    def set_group(self, value):
        value = self.check_str(value)
        if value and value.upper() in self.groups:
            return value.upper()
        return None
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        parts = [super().__str__()]
        if self.get_ternum():
            parts.append(f"Участок: {self.get_ternum()}")
        if self.get_disability():
            parts.append(f"Группа инвалидности: {self.get_disability()} группа")
        if self.get_group():
            parts.append(f"Группа здоровья: {self.get_group()}")
        if self.chronic_diagnosis and self.chronic_diagnosis != "Не выявлено":
            parts.append(f"Хронический диагноз: {self.chronic_diagnosis}")
        return '\n'.join(parts) + "\n"
