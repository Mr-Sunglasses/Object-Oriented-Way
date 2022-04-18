from datetime import date

class College:

    year = date.today()

    fee = False

    def __init__(self, Name , ID , StartSession , EndSession):

        self.name = Name
        self.id = ID
        self.sessionStart = StartSession
        self.sessionEnd = EndSession



    def SubmitFee(self,p=True):

        self.fee = p
        if self.fee == True:
            return f"Fee is Submitted"
        else:
            return f"Fee is not Submitted"

    def validate(self):
        if self.sessionEnd < self.year.year:
            return "You are No Longer the Student of Our College"
        else:
            return "You are a Valid Student"



