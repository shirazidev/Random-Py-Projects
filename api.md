
1. آب‌وهوا‌نما

هدف: دریافت اطلاعات آب‌وهوا برای یک شهر.
```
import requests

def get_weather(city_name):
    api_key = "YOUR_API_KEY"  # کلید API خود را از OpenWeatherMap دریافت کنید
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "fa"  # زبان فارسی برای توضیحات
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"آب‌وهوا: {weather}")
        print(f"دما: {temp}°C")
        print(f"رطوبت: {humidity}%")
        print(f"سرعت باد: {wind_speed} m/s")
    else:
        print("خطا در دریافت اطلاعات. لطفاً نام شهر را بررسی کنید.")

city = input("نام شهر را وارد کنید: ")
get_weather(city)
```

2. ترجمه‌گر متون

هدف: ترجمه متن به زبان مقصد.
```

import requests

def translate_text(text, target_language):
    url = "https://libretranslate.de/translate"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "q": text,
        "source": "auto",  # شناسایی خودکار زبان متن
        "target": target_language
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        translation = response.json()["translatedText"]
        print(f"متن ترجمه‌شده: {translation}")
    else:
        print("خطایی در ترجمه رخ داده است.")

text = input("متن مورد نظر برای ترجمه: ")
language = input("کد زبان مقصد (مانند 'en' برای انگلیسی): ")
translate_text(text, language)
```

3. ارسال ایمیل با Mailgun

هدف: ارسال ایمیل با استفاده از Mailgun API.
```
import requests

def send_email(api_key, domain, recipient, subject, message):
    url = f"https://api.mailgun.net/v3/{domain}/messages"
    auth = ("api", api_key)
    data = {
        "from": f"Your Name <mailgun@{domain}>",
        "to": [recipient],
        "subject": subject,
        "text": message
    }

    response = requests.post(url, auth=auth, data=data)

    if response.status_code == 200:
        print("ایمیل با موفقیت ارسال شد!")
    else:
        print(f"خطا: {response.status_code}, {response.text}")

api_key = "YOUR_MAILGUN_API_KEY"
domain = "YOUR_MAILGUN_DOMAIN"
recipient = input("ایمیل گیرنده: ")
subject = input("موضوع ایمیل: ")
message = input("متن ایمیل: ")

send_email(api_key, domain, recipient, subject, message)
```

4. مدیریت TODOها

هدف: ایجاد، مشاهده و مدیریت وظایف.
```
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

def list_todos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        todos = response.json()
        for todo in todos[:10]:  # نمایش 10 وظیفه اول
            print(f"{todo['id']}: {todo['title']} (وضعیت: {'انجام شده' if todo['completed'] else 'در حال انجام'})")
    else:
        print("خطا در دریافت وظایف.")

def create_todo(title):
    data = {"title": title, "completed": False}
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("وظیفه با موفقیت اضافه شد!")
    else:
        print("خطا در ایجاد وظیفه.")

print("1. مشاهده وظایف\n2. افزودن وظیفه")
choice = int(input("انتخاب شما: "))
if choice == 1:
    list_todos()
elif choice == 2:
    title = input("عنوان وظیفه: ")
    create_todo(title)
```

5. سرچ فیلم و سریال

هدف: جستجوی اطلاعات فیلم یا سریال.
```
import requests

def search_movie(title):
    api_key = "YOUR_OMDB_API_KEY"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["Response"] == "True":
            print(f"عنوان: {data['Title']}")
            print(f"سال انتشار: {data['Year']}")
            print(f"ژانر: {data['Genre']}")
            print(f"امتیاز IMDb: {data['imdbRating']}")
            print(f"خلاصه: {data['Plot']}")
        else:
            print("فیلمی با این عنوان پیدا نشد.")
    else:
        print("خطا در اتصال به API.")

movie_title = input("نام فیلم یا سریال: ")
search_movie(movie_title)
```

6. نمایش نرخ ارز

هدف: دریافت نرخ تبدیل ارز.

```
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        print(f"نرخ تبدیل {base_currency} به {target_currency}: {rate}")
    else:
        print("خطا در دریافت نرخ تبدیل.")

base = input("ارز مبدا (مانند USD): ")
target = input("ارز مقصد (مانند EUR): ")
get_exchange_rate(base, target)
```

7. پایش قیمت ارز دیجیتال

هدف: دریافت قیمت لحظه‌ای ارزهای دیجیتال.
```
import requests

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data.get(crypto, {}).get("usd")
        if price:
            print(f"قیمت لحظه‌ای {crypto}: ${price}")
        else:
            print("ارز دیجیتال مورد نظر پیدا نشد.")
    else:
        print("خطا در دریافت اطلاعات.")

crypto = input("نام ارز دیجیتال (مانند bitcoin): ").lower()
get_crypto_price(crypto)
```

8. ربات جستجوی کتاب

هدف: جستجوی کتاب با استفاده از Google Books API.
```
import requests

def search_book(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        books = data.get("items", [])
        for book in books[:5]:
            info = book["volumeInfo"]
            title = info.get("title", "عنوان موجود نیست")
            authors = ", ".join(info.get("authors", ["نویسنده نامشخص"]))
            print(f"عنوان: {title}")
            print(f"نویسنده: {authors}")
            print("-" * 30)
    else:
        print("خطا در جستجوی کتاب.")

query = input("عبارت جستجو: ")
search_book(query)
```

9. تحلیل اخبار

هدف: دریافت آخرین اخبار.
```
import requests

def get_news(query):
    api_key = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        for article in articles[:5]:
            print(f"عنوان: {article['title']}")
            print(f"منبع: {article['source']['name']}")
            print(f"لینک: {article['url']}")
            print("-" * 50)
    else:
        print("خطا در دریافت اخبار.")

query = input("موضوع جستجوی اخبار: ")
get_news(query)
```
10.  دستیار یادآور

هدف: ارسال یادآوری به تلگرام.
```
import requests
import time

def send_reminder(bot_token, chat_id, message, delay):
    print(f"یادآور ارسال خواهد شد در {delay} ثانیه...")
    time.sleep(delay)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("یادآور ارسال شد!")
    else:
        print("خطا در ارسال یادآور.")
bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
message = input("پیام یادآور: ")
delay = int(input("مدت زمان تأخیر (ثانیه): "))
send_reminder(bot_token, chat_id, message, delay)
```

11. دریافت نرخ تتر از نوبیتکس
```
import requests

data = requests.get("https://api.nobitex.ir/market/stats?srcCurrency=usdt&dstCurrency=rls")

data = data.json()

price = data['stats']['usdt-rls']['bestBuy']

print(price)
```
