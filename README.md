# DDoS
StressTestPro
StressTestPro is an advanced, asynchronous stress testing tool designed for evaluating the resilience of web servers under high load conditions. It is intended for use by server administrators and security professionals to test their own systems or those they have explicit permission to assess.
Features

Asynchronous HTTP requests using aiohttp for high performance.
Support for SOCKS5 and HTTP proxies to distribute requests and avoid IP blocking.
Configurable concurrency and test duration.
Real-time metrics including requests per second (RPS), latency percentiles (P50, P95, P99), and success rates.
Automatic proxy testing and filtering to ensure only active proxies are used.
Ethical use guidelines and legal notices.

Installation
To use StressTestPro, you need Python 3.8 or higher. Install the required dependencies using pip:
pip install aiohttp aiohttp_socks numpy

Usage

Clone the repository:

git clone https://github.com/yourusername/StressTestPro.git
cd StressTestPro


Prepare a list of target URLs and, optionally, a list of proxies in a text file (e.g., socks5.txt).

Run the tool:


python StressTestPro.py

Follow the prompts to enter target URLs, concurrency level, test duration, and proxy list file.
Configuration

Target URLs: Enter one or more URLs separated by commas (e.g., `[invalid url, do not cite]).
Concurrency: Number of simultaneous tasks (50-1000).
Duration: Test duration in seconds (60-3600).
Proxy List: Path to a text file containing proxies, one per line, in the format socks5://ip:port or [invalid url, do not cite] (e.g., socks5://192.252.214.20:15864`).

Ethics and Legal Notice
This tool is provided for educational and testing purposes only. It must only be used on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
License
This project is licensed under the MIT License. See the LICENSE file for details.
فارسی


StressTestPro
StressTestPro یک ابزار تست استرس پیشرفته و ناهمزمان است که برای ارزیابی مقاومت سرورهای وب در شرایط بار بالا طراحی شده است. این ابزار برای استفاده توسط مدیران سرور و متخصصان امنیت به منظور تست سیستم‌های خود یا سیستم‌هایی که صراحتاً اجازه ارزیابی آن‌ها را دارند، در نظر گرفته شده است.
ویژگی‌ها

درخواست‌های HTTP ناهمزمان با استفاده از aiohttp برای عملکرد بالا.
پشتیبانی از پروکسی‌های SOCKS5 و HTTP برای توزیع درخواست‌ها و جلوگیری از مسدود شدن IP.
قابلیت تنظیم همزمانی و مدت زمان تست.
معیارهای زمان واقعی شامل درخواست در ثانیه (RPS)، صدک‌های تأخیر (P50، P95، P99) و نرخ موفقیت.
تست و فیلتر خودکار پروکسی‌ها برای اطمینان از استفاده از پروکسی‌های فعال.
دستورالعمل‌های استفاده اخلاقی و اطلاعیه‌های قانونی.

نصب
برای استفاده از StressTestPro، به Python 3.8 یا بالاتر نیاز دارید. وابستگی‌های مورد نیاز را با استفاده از pip نصب کنید:
pip install aiohttp aiohttp_socks numpy

استفاده

مخزن را کلون کنید:

git clone https://github.com/yourusername/StressTestPro.git
cd StressTestPro


لیستی از URLهای هدف و، در صورت تمایل، لیستی از پروکسی‌ها را در یک فایل متنی (مثل socks5.txt) آماده کنید.

ابزار را اجرا کنید:


python StressTestPro.py

دستورات را دنبال کنید تا URLهای هدف، سطح همزمانی، مدت زمان تست و فایل لیست پروکسی را وارد کنید.
پیکربندی

URLهای هدف: یک یا چند URL را با کاما جدا کنید (مثل `[invalid url, do not cite]).
همزمانی: تعداد وظایف همزمان (50-1000).
مدت زمان: مدت زمان تست به ثانیه (60-3600).
لیست پروکسی: مسیر فایل متنی حاوی پروکسی‌ها، هر پروکسی در یک خط، با فرمت socks5://ip:port یا [invalid url, do not cite] (مثل socks5://192.252.214.20:15864`).

