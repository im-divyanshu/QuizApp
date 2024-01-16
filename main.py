from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
import requests
import random
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager,Screen

class FirstWindow(Screen):
    quiz_json=requests.get('https://the-trivia-api.com/api/questions').json()
    count=0
    question=StringProperty(quiz_json[0]['question'])
    print(question)
    options=quiz_json[0]['incorrectAnswers']
    options.append(quiz_json[0]['correctAnswer'])
    print(quiz_json[0]['correctAnswer'])
    random.shuffle(options)
    b0text=StringProperty(options[0])
    b1text=StringProperty(options[1])
    b2text=StringProperty(options[2])
    b3text=StringProperty(options[3])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def update(self,widget):

        if(widget.text==self.quiz_json[self.count]['correctAnswer']):
            self.count+=1
            self.question=self.quiz_json[self.count]['question']
            options=self.quiz_json[self.count]['incorrectAnswers']
            options.append(self.quiz_json[self.count]['correctAnswer'])
            print(self.quiz_json[self.count]['correctAnswer'])
            random.shuffle(options)
            self.b0text=options[0]
            self.b1text=options[1]
            self.b2text=options[2]
            self.b3text=options[3]
            print(self.count)
        if self.count==9:
            self.count=0
            self.quiz_json=requests.get('https://the-trivia-api.com/api/questions').json()

class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

# class MainWidget(Widget):
#     quiz_json=requests.get('https://the-trivia-api.com/api/questions').json()
#     count=0
#     question=StringProperty(quiz_json[0]['question'])
#     print(question)
#     options=quiz_json[0]['incorrectAnswers']
#     options.append(quiz_json[0]['correctAnswer'])
#     print(quiz_json[0]['correctAnswer'])
#     random.shuffle(options)
#     b0text=StringProperty(options[0])
#     b1text=StringProperty(options[1])
#     b2text=StringProperty(options[2])
#     b3text=StringProperty(options[3])

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#     def update(self,widget):

#         if(widget.text==self.quiz_json[self.count]['correctAnswer']):
#             self.count+=1
#             self.question=self.quiz_json[self.count]['question']
#             options=self.quiz_json[self.count]['incorrectAnswers']
#             options.append(self.quiz_json[self.count]['correctAnswer'])
#             print(self.quiz_json[self.count]['correctAnswer'])
#             random.shuffle(options)
#             self.b0text=options[0]
#             self.b1text=options[1]
#             self.b2text=options[2]
#             self.b3text=options[3]
#         if self.count==9:
#             self.count=0
#             self.quiz_json=requests.get('https://the-trivia-api.com/api/questions').json()

kv=Builder.load_file("app.kv")

class QuizApp(App):
    def build(self):
        return kv

QuizApp().run()