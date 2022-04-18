from college import College
class AppliedScience(College):

    def validateAs(self):
        if self.sessionStart == self.year.year:
            return "You are A valid Student"
        else:
            return "You are not A Student of Applied Science "



    def semesterResult(self):

        if self.fee == True:
            return "Your Semester Result are on Erp"
        else:
            return "Please Submit the Fee"

s_applied = AppliedScience("Kanishk",1232,2021,2025)
print(s_applied.validate())
print(s_applied.semesterResult())