from faker import Faker

fake = Faker("Ru-ru")


class RegisterData:
    def __init__(self,
                 login=None,
                 password=None,
                 email=None,
                 email2=None,
                 name=None,
                 surname=None,
                 city=None
                 ):
        self.login = login
        self.password = password
        self.email = email
        self.email2 = email2
        self.name = name
        self.surname = surname
        self.city = city

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        email = fake.email()
        email2 = email
        name = fake.first_name_male()
        surname = fake.last_name_male()
        city = fake.city()
        return RegisterData(login=login,
                            password=password,
                            email=email,
                            email2=email2,
                            name=name,
                            surname=surname,
                            city=city
                            )
