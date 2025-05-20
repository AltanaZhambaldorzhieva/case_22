import re

class Loader:
    def __init__(self):
        self.hospital_patients = []
        self.ambulatory_patients = []
        self.nurses = []
        self.doctors = []

    def load_hospital_patients(self, file_path):
        with open(file_path, "r", encoding="utf=8") as file:
            for row in file:
                parts = row.strip().split(";")
                if len(parts) != 19:
                    continue
                self.hospital_patients.append(
                    HospitalPatient(
                        medical_department=parts[15],
                        room_number=parts[16],
                        clinical_diagnosis=parts[17],
                        full_name=parts[0], gender=parts[1], birthday=parts[2], place_birth=parts[3],
                        married=parts[4], passport=parts[5], residence_address=parts[6],
                        level_education=parts[7], phone_number=parts[8], medical_policy=parts[9],
                        status=parts[10], place_work_study=parts[11], blood_type=parts[12],
                        rhesus_affiliation=parts[13], allergic_reactions=parts[14]
                    )
                )

    def load_ambulatory_patients(self, file_path):
        with open(file_path, "r", encoding="utf=8") as file:
            for row in file:
                parts = row.strip().split(";")
                if len(parts) != 20:
                    continue
                self.ambulatory_patients.append(
                    AmbulatoryPatient(
                        territorial_number=parts[15],
                        disability=parts[16],
                        health_group=parts[17],
                        chronic_diagnosis=parts[18],
                        full_name=parts[0], gender=parts[1], birthday=parts[2], place_birth=parts[3],
                        married=parts[4], passport=parts[5], residence_address=parts[6],
                        level_education=parts[7], phone_number=parts[8], medical_policy=parts[9],
                        status=parts[10], place_work_study=parts[11], blood_type=parts[12],
                        rhesus_affiliation=parts[13], allergic_reactions=parts[14]
                    )
                )

    def load_nurses(self, file_path):
        with open(file_path, "r", encoding="utf=8") as file:
            for row in file:
                parts = row.strip().split(";")
                if len(parts) != 20:
                    continue
                self.nurses.append(
                    Nurse(
                        sanitary_service=parts[16],
                        patient_care=parts[17],
                        medical_procedures=parts[18],
                        know_foreign=parts[9],
                        education_doc=parts[10],
                        year_grad=parts[11],
                        qual=parts[12],
                        specialty=parts[13],
                        profession=parts[14],
                        work_ex=parts[15],
                        full_name=parts[0], gender=parts[1], birthday=parts[2], place_birth=parts[3],
                        married=parts[4], passport=parts[5], residence_address=parts[6],
                        level_education=parts[7], phone_number=parts[8]
                    )
                )

    def load_doctors(self, file_path):
        with open(file_path, "r", encoding="utf=8") as file:
            for row in file:
                parts = row.strip().split(";")
                if len(parts) != 25:
                    continue
                self.doctors.append(
                    Doctor(
                        academic_degree=parts[16],
                        academic_rank=parts[17],
                        category=parts[18],
                        trainings=parts[19],
                        medical_errors=parts[20],
                        diagnosis_patients=parts[21],
                        treatment_patients=parts[22],
                        rehabilitation_patients=parts[23],
                        know_foreign=parts[9],
                        education_doc=parts[10],
                        year_grad=parts[11],
                        qual=parts[12],
                        specialty=parts[13],
                        profession=parts[14],
                        work_ex=parts[15],
                        full_name=parts[0], gender=parts[1], birthday=parts[2], place_birth=parts[3],
                        married=parts[4], passport=parts[5], residence_address=parts[6],
                        level_education=parts[7], phone_number=parts[8]
                    )
                )

class Person:
    _id = 1

    def __init__(self, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number):
        self._id = Person._id
        Person._id += 1
        self.__full_name = self._cut(full_name, 25)
        self.__gender = self._validate_gender(gender)
        self._birthday = self._validate_birthday(birthday)
        self.place_birth = self._as_str(place_birth)
        self.married = self._as_bool(married)
        self.__passport = self._validate_passport(passport)
        self.residence_address = self._as_str(residence_address)
        self.__level_education = self._validate_education(level_education)
        self.__phone_number = self._validate_phone(phone_number)

    @staticmethod
    def _cut(value, length):
        return value[:length] if isinstance(value, str) and len(value) > length else value

    @staticmethod
    def _as_str(value):
        return value if isinstance(value, str) and value else None

    @staticmethod
    def _as_bool(value):
        if value == "True":
            return True
        if value == "False":
            return False
        return None

    @staticmethod
    def _as_int(value):
        try:
            return int(value)
        except Exception:
            return None

    @staticmethod
    def _validate_gender(value):
        genders = ["муж.", "жен."]
        return value if value in genders else None

    @staticmethod
    def _validate_birthday(value):
        if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", value or ""):
            return value
        return None

    @staticmethod
    def _validate_passport(value):
        if re.fullmatch(r"\d{4} \d{6} \d{2}\.\d{2}\.\d{4}", value or ""):
            return value
        return None

    @staticmethod
    def _validate_education(value):
        educations = ["высшее", "ср.спец", "среднее"]
        return value.lower() if value and value.lower() in educations else None

    @staticmethod
    def _validate_phone(value):
        if re.fullmatch(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", value or ""):
            return value
        return None

    @property
    def birthday(self):
        return self._birthday

    def __repr__(self):
        return f"{self._id}. {self.__full_name}"

    def __str__(self):
        fields = [
            f"Номер: {self._id}",
            f"ФИО: {self.__full_name}" if self.__full_name else "",
            f"Пол: {self.__gender}" if self.__gender else "",
            f"Дата рождения: {self._birthday}" if self._birthday else "",
            f"Место рождения: {self.place_birth}" if self.place_birth else "",
            f"В браке: {'да' if self.married else 'нет'}" if self.married is not None else "",
            f"Паспорт: {self.__passport}" if self.__passport else "",
            f"Адрес регистрации: {self.residence_address}" if self.residence_address else "",
            f"Уровень образования: {self.__level_education}" if self.__level_education else "",
            f"Телефон: {self.__phone_number}" if self.__phone_number else "",
        ]
        return "\n".join(filter(None, fields))

class Employee(Person):
    def __init__(self, know_foreign, education_doc, year_grad, qual, specialty, profession, work_ex,
                 full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number):
        super().__init__(full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number)
        self.know_foreign_language = self._as_bool(know_foreign)
        self.education_document = self._as_str(education_doc)
        self.__year_graduation = self._validate_year(year_grad)
        self.qualification = self._as_str(qual)
        self.specialty = self._as_str(specialty)
        self.__profession = self._validate_profession(profession)
        self.__work_experience = self._validate_experience(work_ex)

    @staticmethod
    def _validate_year(value):
        v = Person._as_int(value)
        return v if v and 1950 <= v <= 2030 else None

    @staticmethod
    def _validate_profession(value):
        professions = ["врач", "медицинская сестра"]
        return value.lower() if value and value.lower() in professions else None

    @staticmethod
    def _validate_experience(value):
        v = Person._as_int(value)
        return v if v is not None and 0 <= v <= 60 else None

    @property
    def year_graduation(self):
        return self.__year_graduation

    @property
    def profession(self):
        return self.__profession

    @property
    def work_experience(self):
        return self.__work_experience

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        fields = [
            super().__str__(),
            f"Знает иностранный язык: {'да' if self.know_foreign_language else 'нет'}" if self.know_foreign_language is not None else "",
            f"Документ об образовании: {self.education_document}" if self.education_document else "",
            f"Год окончания: {self.__year_graduation}" if self.__year_graduation else "",
            f"Квалификация: {self.qualification}" if self.qualification else "",
            f"Специализация: {self.specialty}" if self.specialty else "",
            f"Профессия: {self.__profession}" if self.__profession else "",
            f"Стаж: {self.__work_experience}" if self.__work_experience is not None else "",
        ]
        return "\n".join(filter(None, fields))

class Nurse(Employee):
    def __init__(self, sanitary_service, patient_care, medical_procedures,
                 know_foreign, education_doc, year_grad, qual, specialty, profession, work_ex,
                 full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number):
        super().__init__(know_foreign, education_doc, year_grad, qual, specialty, profession, work_ex,
                         full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number)
        self.sanitary_service = self._as_bool(sanitary_service)
        self.patient_care = self._as_bool(patient_care)
        self.medical_procedures = self._as_bool(medical_procedures)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        fields = [
            super().__str__(),
            f"Санитарная обработка помещений: {'да' if self.sanitary_service else 'нет'}" if self.sanitary_service is not None else "",
            f"Уход за больными: {'да' if self.patient_care else 'нет'}" if self.patient_care is not None else "",
            f"Выполнение медицинских процедур: {'да' if self.medical_procedures else 'нет'}" if self.medical_procedures is not None else ""
        ]
        return "\n".join(filter(None, fields)) + "\n"

class Doctor(Employee):
    def __init__(self, academic_degree, academic_rank, category, trainings, medical_errors, diagnosis_patients,
                 treatment_patients, rehabilitation_patients,
                 know_foreign, education_doc, year_grad, qual, specialty, profession, work_ex,
                 full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number):
        super().__init__(know_foreign, education_doc, year_grad, qual, specialty, profession, work_ex,
                         full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number)
        self.academic_degree = self._as_bool(academic_degree)
        self.academic_rank = self._as_bool(academic_rank)
        self.__category = self._validate_category(category)
        self.trainings = self._as_bool(trainings)
        self.medical_errors = self._as_str(medical_errors)
        self.diagnosis_patients = self._as_bool(diagnosis_patients)
        self.treatment_patients = self._as_bool(treatment_patients)
        self.rehabilitation_patients = self._as_bool(rehabilitation_patients)

    @staticmethod
    def _validate_category(value):
        values = ["высшая", "первая", "вторая"]
        return value.lower() if value and value.lower() in values else None

    @property
    def category(self):
        return self.__category

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        fields = [
            super().__str__(),
            f"Ученая степень: {'да' if self.academic_degree else 'нет'}" if self.academic_degree is not None else "",
            f"Ученое звание: {'да' if self.academic_rank else 'нет'}" if self.academic_rank is not None else "",
            f"Категория: {self.__category}" if self.__category else "",
            f"Повышение квалификации: {'да' if self.trainings else 'нет'}" if self.trainings is not None else "",
            f"Медицинские ошибки: {self.medical_errors}" if self.medical_errors else "",
            f"Выполнение диагностики заболеваний: {'да' if self.diagnosis_patients else 'нет'}" if self.diagnosis_patients is not None else "",
            f"Лечебная практика: {'да' if self.treatment_patients else 'нет'}" if self.treatment_patients is not None else "",
            f"Реабилитация больных: {'да' if self.rehabilitation_patients else 'нет'}" if self.rehabilitation_patients is not None else ""
        ]
        return "\n".join(filter(None, fields)) + "\n"

class Patient(Person):
    def __init__(self, medical_policy, status, place_work_study, blood_type,
                 rhesus_affiliation, allergic_reactions,
                 full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number):
        super().__init__(full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number)
        self.medical_policy = self._as_str(medical_policy)
        self.__status = self._validate_status(status)
        self.place_work_study = self._as_str(place_work_study)
        self.__blood_type = self._validate_blood_type(blood_type)
        self.__rhesus_affiliation = self._validate_rhesus(rhesus_affiliation)
        self.allergic_reactions = self._as_str(allergic_reactions)

    @staticmethod
    def _validate_status(value):
        statuses = ["рабочий", "служащий", "обучающийся"]
        return value if value in statuses else None

    @staticmethod
    def _validate_blood_type(value):
        v = Person._as_int(value)
        return v if v and 1 <= v <= 4 else None

    @staticmethod
    def _validate_rhesus(value):
        rhesuses = ["+", "-"]
        return value if value in rhesuses else None

    @property
    def status(self):
        return self.__status

    @property
    def blood_type(self):
        return self.__blood_type

    @property
    def rhesus_affiliation(self):
        return self.__rhesus_affiliation

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        fields = [
            super().__str__(),
            f"Медицинский полис: {self.medical_policy}" if self.medical_policy else "",
            f"Cтатус: {self.__status}" if self.__status else "",
            f"Место работы (учёбы): {self.place_work_study}" if self.place_work_study else ""
        ]
        if self.__blood_type:
            blood = f"Группа крови: {self.__blood_type}"
            if self.__rhesus_affiliation:
                blood += f"({self.__rhesus_affiliation})"
            fields.append(blood)
        if self.allergic_reactions:
            fields.append(f"Аллергические реакции: {self.allergic_reactions}")
        return "\n".join(filter(None, fields))

class HospitalPatient(Patient):
    def __init__(self, medical_department, room_number, clinical_diagnosis,
                 full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study, blood_type, rhesus_affiliation, allergic_reactions):
        super().__init__(medical_policy, status, place_work_study, blood_type, rhesus_affiliation, allergic_reactions,
                         full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number)
        self.medical_department = self._as_str(medical_department)
        self.room_number = self._as_int(room_number)
        self.clinical_diagnosis = self._as_str(clinical_diagnosis)

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        fields = [
            super().__str__(),
            f"Отделение: {self.medical_department}" if self.medical_department else "",
            f"Палата: {self.room_number}" if self.room_number is not None else "",
            f"Клинический диагноз: {self.clinical_diagnosis}" if self.clinical_diagnosis else ""
        ]
        return "\n".join(filter(None, fields)) + "\n"

class AmbulatoryPatient(Patient):
    def __init__(self, territorial_number, disability, health_group, chronic_diagnosis,
                 full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study, blood_type, rhesus_affiliation, allergic_reactions):
        super().__init__(medical_policy, status, place_work_study, blood_type, rhesus_affiliation, allergic_reactions,
                         full_name, gender, birthday, place_birth, married, passport, residence_address, level_education, phone_number)
        self.__territorial_number = self._validate_territorial_number(territorial_number)
        self.__disability = self._validate_disability(disability)
        self.__health_group = self._validate_health_group(health_group)
        self.chronic_diagnosis = self._as_str(chronic_diagnosis)

    @staticmethod
    def _validate_territorial_number(value):
        v = Person._as_int(value)
        return v if v and 1 <= v <= 20 else None

    @staticmethod
    def _validate_disability(value):
        v = Person._as_int(value)
        return v if v is not None and 0 <= v <= 3 else None

    @staticmethod
    def _validate_health_group(value):
        groups = ["I", "II", "III"]
        return value.upper() if value and value.upper() in groups else None

    @property
    def territorial_number(self):
        return self.__territorial_number

    @property
    def disability(self):
        return self.__disability

    @property
    def health_group(self):
        return self.__health_group

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        fields = [
            super().__str__(),
            f"Участок: {self.__territorial_number}" if self.__territorial_number else "",
            f"Группа инвалидности: {self.__disability} группа" if self.__disability else "",
            f"Группа здоровья: {self.__health_group}" if self.__health_group else "",
            f"Хронический диагноз: {self.chronic_diagnosis}" if self.chronic_diagnosis and self.chronic_diagnosis != "Не выявлено" else ""
        ]
        return "\n".join(filter(None, fields)) + "\n"
