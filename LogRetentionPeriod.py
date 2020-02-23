#!/usr/bin/python3
import boto3
import sys

client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
print("Here is the list of regions")
print(regions)
print("\n")
print("=================")

print("Enter the region")
region=input()

if region in regions:
    client = boto3.client('logs',region_name=region)
elif region not in regions:
    print("not a valid region")
    sys.exit()


response = client.describe_log_groups(
    limit=50
)

names=[]
retention=[]
response=response.get("logGroups")
for i in range(0,len(response)):
        names.append(response[i].get("logGroupName"))
        
print("=================")
print("Following are the log groups")
for i in names:
    print(i)

if(len(names)==0):
    print("No Log Groups found")

if(len(names)==0):
    sys.exit()

print("=================")

print("Enter the retnetion  period you wish to set on the Log Groups")
num=int(input())
for i in names:
        response = client.put_retention_policy(
          logGroupName=i,
          retentionInDays=num
          )

print("=================")

print("Done")





