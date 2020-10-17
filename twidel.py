import twitter
import csv

api = twitter.Api( # !! please write !!
    consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret=''
)

csvReader = csv.reader(open('tweets.csv',encoding='utf-8'))
next(csvReader)

for row in csvReader:
    try:
        print(row[1]+' → del')  # Time stamp 
        api.DestroyStatus(row[0])
    except twitter.error.TwitterError: #skip deleted data 
        print('-----------deleted data')
    except IndexError: #skip empty
        continue
        