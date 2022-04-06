class Spartan:
    def __init__(self, s_id, s_first_name, s_last_name, s_birth_day, s_birth_month, s_birth_year, s_course, s_stream):
        self.sparta_id = s_id
        self.first_name = s_first_name
        self.last_name = s_last_name
        self.birth_day = s_birth_day
        self.birth_month = s_birth_month
        self.birth_year = s_birth_year
        self.course = s_course
        self.stream = s_stream

    def __str__(self):
        return vars(self).__str__()

    def get_sparta_id(self):
        return self.sparta_id

    def set_sparta_id(self, s_id):
        self.sparta_id = s_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, s_first_name):
        self.first_name = s_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, s_last_name):
        self.last_name = s_last_name

    def get_birth_day(self):
        return self.birth_day

    def set_birth_day(self, s_birth_day):
        self.birth_day = s_birth_day

    def get_birth_month(self):
        return self.birth_month

    def set_birth_month(self, s_birth_month):
        self.birth_month = s_birth_month

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, s_birth_year):
        self.birth_year = s_birth_year

    def get_course(self):
        return self.course

    def set_course(self, s_course):
        self.course = s_course

    def get_stream(self):
        return self.stream

    def set_stream(self, s_stream):
        self.stream = s_stream
