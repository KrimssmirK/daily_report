from django.db import models
from datetime import timedelta

# Create your models here.

# fields
# time stamp
# visa
# pax
# report_by (visa coordinator)

# The first element in each tuple is the actual value to be set on the model, 
# and the second element is the human-readable name.
visa = (
    ("TOURISM", "TOURISM"),
    ("PACKAGE TOUR", "PACKAGE TOUR"),
    ("BUSINESS, CONFERENCE OR CULTURAL EXCHANGE, etc.", "BUSINESS, CONFERENCE OR CULTURAL EXCHANGE, etc."),
    ("VISITING RELATIVES", "VISITING RELATIVES"),
    ("VISITING FRIENDS OR DISTANT RELATIVES", "VISITING FRIENDS OR DISTANT RELATIVES"),
    ("VISITING US MILITARY PERSONNEL", "VISITING US MILITARY PERSONNEL"),
    ("SPOUSE OR CHILDD OF JAPANESE NATIONAL RESIDING IN THE PHILIPPINES", "SPOUSE OR CHILD OF JAPANESE NATIONAL RESIDING IN THE PHILIPPINES"),
    ("TRANSIT", "TRANSIT"),
    ("DIPLOMAT/OFFICIAL", "DIPLOMAT/OFFICIAL"),
    ("HOUSEKEEPER OF DIPLOMAT/OFFICIAL", "HOUSEKEEPER OF DIPLOMAT/OFFICIAL"),
    ("NIKKEI-JIN (JAPANESE DESCENDANT)", "NIKKEI-JIN (JAPANESE DESCENDANT)"),
    ("FILIPINO PARENTS TRAVELLING TO JAPAN WITH JAPANESE-FILIPINO CHILDREN", "FILIPINO PARENTS TRAVELLING TO JAPAN WITH JAPANESE-FILIPINO CHILDREN"),
    ("COE", "COE")
)

# need to add
visa_coordinators = (
    ("RV", "RV"),
    ("PAUL", "PAUL"),
    ("JOEVIL", "JOEVIL"),
    ("AIMEE", "AIMEE"),
    ("ARJANE", "ARJANE")
)

class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now=True) # datetime.datetime instance
    visa = models.CharField(max_length=100, choices=visa, default="Tourist")
    pax = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)))
    report_by = models.CharField(max_length=100, default="select", choices=visa_coordinators)
    
    # for readability
    def __str__(self):
        # add 8 hours to timestamp (datetime.datetime object) and convert it to mm-dd-yyyy hh:mm
        ph_time = self.timestamp + timedelta(hours=8)
        return ph_time.strftime("%x %X") + "-" + self.visa + "-" + str(self.pax) + "-" + str(self.report_by)
    