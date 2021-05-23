from pynamodb import models
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)

from datetime import datetime
import pytz

class Progress(models.Model):
    class Meta:
        table_name = 'Progress'
        region = 'us-east-1'
    
    update = UnicodeAttribute()
    madeOn = UnicodeAttribute()
    challenge = UnicodeAttribute(range_key=True)
    of = UnicodeAttribute(hash_key=True)

    def __str__(self) -> str:
        return f'{self.update} was made on {self.madeOn} for challenge {self.challenge}'

if not Progress.exists():
    Progress.create_table(wait=True, read_capacity_units=1, write_capacity_units=1)
    print('Table created')

progress_1 = Progress(update='Started with PynamoDB', madeOn=str(datetime.now(pytz.timezone('Asia/Kolkata'))), 
                    challenge='Learn DynamoDB', of='May/21')

#progress_1.save()

print(next(Progress.query(hash_key='May/21')))
    
