'''Home work for the lesson 33'''

'''Task 1 - Robots.txt:
Download and save to file robots.txt from wikipedia, twitter websites etc'''

import requests

url_wiki = 'https://en.wikipedia.org/robots.txt'
url_twitter = 'https://twitter.com/robots.txt'

try:
    response_wiki = requests.get(url_wiki)
    response_twitter = requests.get(url_twitter)

    if response_wiki.status_code == 200 and response_twitter.status_code == 200:
        print('Response codes from Wiki and Twitter are both "200"')
        
        response_wiki_content = response_wiki.text
        response_twitter_content = response_twitter.text

        robots_txt_file_path = "Python_for_web/robots_content.txt"
        with open(robots_txt_file_path, 'a', encoding='utf-8') as file:
            file.write(response_wiki_content)
            file.write(response_twitter_content)

        print('Writing is done!')
    else:
        print("Failed to retrieve robots.txt. One of the URLs is unavailable")

except requests.RequestException as e:
    print("An error occurred during the request:", e)

except IOError as e:
    print("An error occurred while writing to the file:", e)

'''Task 2 - Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file.'''

# !!! This task should be skipped !!!


'''Task 3 - The Weather app:
Write a console application which takes as an input a city name and returns current 
weather in the format of your choice. For the current task, you can choose 
any weather API or website or use openweathermap.org '''

import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"Weather in {city_name}: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        return f"Error: {data['message']}"

def main():
    api_key = "1c9cec2114c1405d50d5c6e8ed462105"
    city_name = input("Enter a city name: ")
    weather_info = get_weather(city_name, api_key)
    print(weather_info)

if __name__ == "__main__":
    main()
