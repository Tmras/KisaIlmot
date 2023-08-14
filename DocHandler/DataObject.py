class DataObjectFencing:
    def __init__(self, date, contest):
        self.date = date
        self.contest = contest

    def get_date(self):
        return self.date

    def get_contest(self):
        return self.contest
