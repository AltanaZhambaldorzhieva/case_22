import inspect
from hospital_patient import HospitalPatient
from ambulatory_patient import AmbulatoryPatient
from nurse import Nurse
from doctor import Doctor


class Loader:
    """
        Class responsible for loading data from files and creating instances of different classes.
    """

    def __init__(self):
        self.doctors = []
        self.nurses = []
        self.hospital_patients = []
        self.ambulatory_patients = []

    def load_doctors(self, file):
        """
            Loads doctor data from the specified file and stores it in the `doctors` list.
        """
        self.doctors = Loader.loader(file, Doctor)

    def load_nurses(self, file):
        """
            Loads nurse data from the specified file and stores it in the `nurses` list.
        """
        self.nurses = Loader.loader(file, Nurse)

    def load_hospital_patients(self, file):
        """
            Loads hospital patient data from the specified file and stores it in the `hospital_patients` list.
        """
        self.hospital_patients = Loader.loader(file, HospitalPatient)

    def load_ambulatory_patients(self, file):
        """
            Loads ambulatory patient data from the specified file and stores it in the `ambulatory_patients` list.
        """
        self.ambulatory_patients = Loader.loader(file, AmbulatoryPatient)

    @staticmethod
    def loader(file, cls):
        """
            A static method that loads data from a file and creates instances of the specified class.
        """
        objects = []
        try:
            with open(file, 'r', encoding='utf-8') as data:
                for raw in data.readlines():
                    args = raw.strip().split(';')
                    if args[-1] == '':
                        args = args[:-1]

                    args = [True if arg.lower() == 'true' or arg.lower() == 'да' else False
                    if arg.lower() == 'false' or arg.lower() == 'нет' else arg for arg in args]

                    need_args = len(inspect.signature(cls.__init__).parameters) - 1

                    if len(args) != need_args:
                        print(f"Ошибка: некорректное количество данных для {cls.__name__}: {len(args)}")
                        continue

                    patient = cls(*args)
                    objects.append(patient)

            return objects

        except FileNotFoundError:
            print(f"Ошибка: файл не найден.")
            return []

    def print_doctors(self):
        for doctor in self.doctors:
            print(doctor)

    def print_nurses(self):
        for nurse in self.nurses:
            print(nurse)

    def print_hospital_patients(self):
        for patient in self.hospital_patients:
            print(patient)

    def print_ambulatory_patients(self):
        for patient in self.ambulatory_patients:
            print(patient)
