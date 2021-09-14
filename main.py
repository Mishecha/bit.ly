import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(headers, payload):
  shorten_url = 'https://api-ssl.bitly.com/v4/shorten'
  response = requests.post(shorten_url, headers=headers, json=payload)
  response.raise_for_status()
  return response.json()['id']


def count_clicks(headers, netloc_and_path):
  clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc_and_path}/clicks/summary'
  response = requests.get(clicks_url, headers=headers)
  response.raise_for_status()
  return response.json()['total_clicks']


def is_bitlink(headers, netloc_and_path):
  check_url = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc_and_path}'
  response = requests.get(check_url, headers=headers)
  return response.ok


def get_parsed_user_link(user_link):
  parsed_link = urlparse(user_link)
  netloc = parsed_link.netloc
  path = parsed_link.path
  return '{}{}'.format(path ,netloc)


if __name__ == '__main__':
  load_dotenv()


  parser = argparse.ArgumentParser(
    description='Сокращение ссылок'
  )
  parser.add_argument('user_link', help='')
  user_link = parser.parse_args().user_link


  bitly_token = os.environ['BITLY_TOKEN']
  netloc_and_path = get_parsed_user_link(user_link)
  

  headers = {
    'Authorization': f'Bearer {bitly_token}'
  }


  payload = {
    'long_url': user_link
  }


  try:
    if is_bitlink(headers, netloc_and_path):
      print('{}{}'.format('количество кликов: ', count_clicks(headers, netloc_and_path)))
    else:
      print(shorten_link(headers, payload))
  except requests.exceptions.HTTPError:
    print('Неправильная ссылка')
