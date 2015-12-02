# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

# Get the keys from a specific url and then use them to connect to AWS Service 
x = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
keys = x.read();
keyset = keys.split(":")

access_key_id = keyset[0]
secret_access_key = keyset[1]

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Get a list of the queues that exists and then print the list out
#rs = conn.get_all_queues()
#for q in rs:
#	print q.id


# 4. Creating a new queue
#rs = conn.create_queue(sys.argv[1])
#qname = rs.name

#print ("> queue " + qname + " is now created")



# 6. Write a message to the queue
#queue = conn.get_queue(sys.argv[1])
#conn.send_message(queue, sys.argv[2])
#print ("Message" + sys.argv[2] + "written to the queue")


#7. Count number of messages on the queue

x = conn.get_queue(sys.argv[1]).count()
print ("Number of messages in the queue = " + x)




