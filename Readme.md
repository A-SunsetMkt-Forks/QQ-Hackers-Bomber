# QQ Hackers Bomber

QQ盗号骗子炸弹，让骗子原地爆炸。

Write for <http://nuiyyz.cn/Ru_op> within a few minutes. 

For a better communication experience, I write this `README.md` in English. `README-zh_CN.md` is provided. <README-zh_CN.md>

## Why not multithreading? 

In my stress test, server crashes after a minute in the speed of 500 milliseconds per POST request, approximately a hundred requests. 

![Potato server](images/img1.jpg)

This server is too weak so I give up supporting multithreading. 

For injecting as much garbage data as possible, interval between each request is set to approximately 5 seconds. 

Benefits are obvious; The hacker's server can get enough rest, and I can do my own work. After running in background, it iakes up less than 1% CPU resources and nearly no network usage. 

Only one night, I generated three thousands of garbage and upload to this server. 

## Why write so much code to generate the "RANDOM" password? 

Because of love and peace. 

![Love & peace](images/img1.jpg)

Generating a lifelike random password can protect innocent people who provide their real password to hacker. 

I assume that 1/20 of people use password with randomly assigned letters and numbers because of the existence of significant level and the theory of small probability. Then I doubled the 0.05 significant level twice. 

Details are in my code. 

## How to use? 

In your command-line interface, keys `pip install -r requirements.txt`. 

Edit `bomber.py`, line 71, modify your upload value. Progress Telerik Fiddler is recommended to web debugging. 

Then `python bomber.py`. 

Enjoy your life. 

June 25, 2019
