from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.clock import Clock
import json
import random

class QuizScreen(Screen):
    question = StringProperty("")
    options = ListProperty([])
    correct = StringProperty("")
    score = NumericProperty(0)
    q_index = NumericProperty(0)
    data = []

    def on_pre_enter(self):
        with open("data/questions.json", "r") as f:
            self.data = json.load(f)
        random.shuffle(self.data)
        self.load_question()

    def load_question(self):
        if self.q_index >= len(self.data):
            self.manager.current = "result"
            self.manager.get_screen("result").final_score = self.score
            return

        q = self.data[self.q_index]
        self.question = q["question"]
        self.options = q["options"]
        self.correct = q["answer"]

    def check_answer(self, option):
        if option == self.correct:
            self.score += 1
        self.q_index += 1
        Clock.schedule_once(lambda x: self.load_question(), 0.2)


class ResultScreen(Screen):
    final_score = NumericProperty(0)


class MainApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(QuizScreen(name="quiz"))
        sm.add_widget(ResultScreen(name="result"))
        return sm


if __name__ == "__main__":
    MainApp().run()
s