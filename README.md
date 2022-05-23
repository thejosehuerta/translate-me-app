# TranslateMe
TranslateMe is a website capable of translating words and phrases, and utilizes an existing microservice to produce different charts comparing the hours it would take to learn different languages. It also offers an API endpoint that an extrernal application can use to translate words and phrases of their own.

# Website
To visit this website, go to http://thejosehuerta.pythonanywhere.com/

# Overview
This website was a final project for Software Engineeering I (CS 361) at Oregon State University. The objective of this project was to create a wesbsite with the fundamentals of **microservices** in mind. This includes making this project both provide and use a service. <p>
  
## Translating
Using the [Googletrans API](https://py-googletrans.readthedocs.io/en/latest/), translating words and phrases to other languages is a single click away. Similar to other translating services on the web, just enter your phrase in one textbox, select a language, and expect your translation in another textbox.
  
| ![image](https://user-images.githubusercontent.com/44957830/169717511-1cb84b81-ec4b-4af9-b5aa-dfbd1d8d49bf.png "Translator") |
|:--:| 
| *Language translator* | 

## API Endpoint
With the power of Flask and HTTP communication, this website provides an API endpoint that can be used to return a
translated phrase in JSON which can then be utilized by any extrernal application.

| ![image](https://user-images.githubusercontent.com/44957830/169720564-251cb7ea-c19f-4844-9cd1-c05f66a161b8.png "API Endpoint") | 
|:--:| 
| *API endpoint showing returned JSON* |
  
## Chart
By calling an [extrenal chart creation service](https://github.com/thejosehuerta/chart-me-app), this website generates a chart of chosen languages. Each language will be a unique color and their size will represent the hours it would take to learn them.
  
| ![image](https://user-images.githubusercontent.com/44957830/169720874-12e10dfd-0abf-4e34-b3f6-61330baef29c.png "Different Languages Chart") |
|:--:|
| *Different languages chart with Italian selected* |

The hours it would take to learn each language was provided by [Effective Language Learning](https://effectivelanguagelearning.com/language-guide/language-difficulty/).

# Tutorial
Below is the video tutorial on how to use this website, along with a timestamp description. 
  
https://user-images.githubusercontent.com/44957830/169876625-da2252fd-c280-4c63-a282-2dac9d5f7491.mp4

<details><summary>Timestamps</summary>
  
| Time | Description | 
|:--|:--| 
| 00:00 | Introduction |
| 00:18 | Language translator section |
| 00:57 | API endpoint |
| 01:30 | Language charter |
  
</details>
