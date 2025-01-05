from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import pandas as pd

class MainApp(App):
    def build(self):
        self.title = 'Analisis Tingkat Kebisingan'
        self.file_path = None
        self.spreadsheet = None

        layout = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        file_chooser.bind(selection=self.on_file_selected)
        layout.add_widget(file_chooser)

        return layout

    def load_file(self, path):
        self.file_path = path
        self.spreadsheet = pd.read_excel(self.file_path, sheet_name='Amplitudes')
        self.calculate_average()

    def on_file_selected(self, instance, path):
        if path and len(path) > 0:
            self.load_file(path[0])

    def calculate_average(self):
        if self.spreadsheet is not None:
            column = 'Sound pressure level (dB)'
            start_row = 3
            data = self.spreadsheet[column].tolist()[start_row:]
            total = sum(data)
            count = len(data)
            average = total / count
            self.show_result_popup(average)

    def show_result_popup(self, average):
        result = self.categorize_average(average)
        popup = Popup(title='Rata-Rata Tingkat Kebisingan',
                      content=Label(text=result),
                      size_hint=(None, None), size=(600, 200))
        popup.open()

    def categorize_average(self, average):
        if average < 30:
            return 'Suara yang tenang, dapat membantu relaksasi dan mengurangi stres.'
        elif average >= 31 and average <= 50:
            return 'Kebisingan sedang, dapat mengganggu konsentrasi saat bekerja atau belajar'
        elif average >= 51 and average <= 70:
            return 'Kebisingan tinggi, dapat mengganggu tidur, menyebabkan stres'
        elif average >= 71 and average <= 90:
            return 'Kebisingan sangat tinggi, dapat merusak pendengaran dan menyebabkan tuli permanen.'
        else:
            return 'Tidak Dikategorikan'

if __name__ == '__main__':
    MainApp().run()
