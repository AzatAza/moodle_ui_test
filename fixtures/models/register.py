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


class RegisterInvalidLogin:
    def __init__(self,
                 login_1=None,
                 login_2=None,
                 login_3=None,
                 login_4=None,
                 login_5=None,
                 login_6=None):
        self.login_1 = login_1
        self.login_2 = login_2
        self.login_3 = login_3
        self.login_4 = login_4
        self.login_5 = login_5
        self.login_6 = login_6

    @staticmethod
    def random_login():
        login_1 = fake.lexify(text='?', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        login_2 = fake.lexify(text='?????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        login_3 = fake.lexify(text='??????????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        login_4 = fake.lexify(text='?', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ') + \
            fake.lexify(text='?', letters='abcdefghijklmnopqrstuvwxyz')
        login_5 = fake.lexify(text='?????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ') + \
            fake.lexify(text='?????', letters='abcdefghijklmnopqrstuvwxyz')
        login_6 = fake.lexify(text='??????????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ') + \
            fake.lexify(text='??????????', letters='abcdefghijklmnopqrstuvwxyz')
        return RegisterInvalidLogin(login_1=login_1,
                                    login_2=login_2,
                                    login_3=login_3,
                                    login_4=login_4,
                                    login_5=login_5,
                                    login_6=login_6
                                    )


class RegisterInvalidPassword():
    def __init__(self,
                 password_1=None,
                 password_2=None,
                 password_3=None,
                 password_4=None,
                 password_5=None
                 ):
        self.password_1 = password_1
        self.password_2 = password_2
        self.password_3 = password_3
        self.password_4 = password_4
        self.password_5 = password_5

    @staticmethod
    def random_password():
        password_1 = fake.password(length=7, special_chars=True, digits=True, upper_case=True, lower_case=True)
        password_2 = fake.password(length=8, special_chars=True, digits=False, upper_case=True, lower_case=True)
        password_3 = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=False)
        password_4 = fake.password(length=8, special_chars=True, digits=True, upper_case=False, lower_case=True)
        password_5 = fake.password(length=8, special_chars=False, digits=True, upper_case=True, lower_case=True)
        return RegisterInvalidPassword(password_1=password_1,
                                       password_2=password_2,
                                       password_3=password_3,
                                       password_4=password_4,
                                       password_5=password_5
                                       )
