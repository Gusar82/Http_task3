import requests
import datetime
from pprint import pprint


def get_unix_time(diff_days):
    data_diff = datetime.datetime.today() - datetime.timedelta(days=diff_days)
    return int(data_diff.timestamp())


def unix_in_date(unix_time):
    return datetime.datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d')


def request_questions(tag,diff_days):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {"site": "ru.stackoverflow",
              "sort": "week",
              "order": "desc",
              "tagged": tag,
              "fromdate": get_unix_time(diff_days)}
    response = requests.get(url, params=params)
    return response.json()


def get_questions(tag, diff_days):
    for id_question in request_questions(tag, diff_days)['items']:
        print (f"{unix_in_date(id_question['creation_date'])} - {id_question['title']}")

# # url = "https://api.stackexchange.com/2.2/sites"


get_questions("Python", 2)
