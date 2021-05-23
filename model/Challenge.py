from pynamodb import models
import pynamodb
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)

from datetime import datetime
import pytz

ist_tz = pytz.timezone('Asia/Kolkata')

class Challenge(models.Model):
    class Meta:
        table_name = 'Challenge'
        region = 'us-east-1'
    
    Forr = UnicodeAttribute(hash_key=True)
    Status = UnicodeAttribute(range_key=True)
    Title = UnicodeAttribute()
    DeferredReason = UnicodeAttribute(null=True)
    DeferredOn = UnicodeAttribute(null=True)
    Completed = UnicodeAttribute(null=True, default_for_new='False')
    AddedOn = UTCDateTimeAttribute(default=datetime.now(ist_tz))

    def __str__(self) -> str:
        return f'For the month of {self.Forr}, the challenge is {self.Title} and was added on {self.AddedOn}'

if not Challenge.exists():
    Challenge.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    print('Table created')

#first_challenge = Challenge(Forr='May/21', Title='Learn DynamoDB', Status='Created')

#first_challenge.save()

result = Challenge.scan()

for item in result:
    print(item)