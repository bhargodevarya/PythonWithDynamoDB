from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)


class Thread(Model):
    class Meta:
        table_name = 'Thread'
        region = 'us-east-1'

    forum_name = UnicodeAttribute(hash_key=True)
    subject = UnicodeAttribute(range_key=True)
    views = NumberAttribute(default=0)
    replies = NumberAttribute(default=0)
    answered = NumberAttribute(default=0)
    tags = UnicodeSetAttribute()
    last_post_datetime = UTCDateTimeAttribute(null=True)

if not Thread.exists(): 
        Thread.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        print("Table created")

#print(Thread.describe_table())

forums = [
    #Thread('Javascript', 'ui'),
    #Thread('Java', 'server'),
    Thread('Python', 'scripting', replies=9)]

# for f in forums:
#     #f.delete()
#     f.save()

# for th in Thread.query(Thread.replies==9):
#     print(th)

# for item in Thread.scan():
#     print(item.subject)