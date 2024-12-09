from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import matplotlib.pyplot as plt
import tempfile

class FlashPage(Screen):
    def __init__(self, **kwargs):
        super(FlashPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        logo = Image(source='logo.png')
        layout.add_widget(logo)
        self.add_widget(layout)

class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        label = Label(text='Welcome to Water Tracker', font_size='24sp', bold=True)
        button = Button(text='Get every day stats', size_hint=(1, 0.2),font_size = 20 ,on_press=self.go_to_cards, background_color=(0.1, 0.5, 0.8, 1))

        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_cards(self, instance):
        self.manager.current = 'cards'

class DynamicCardsPage(Screen):
    def __init__(self, **kwargs):
        super(DynamicCardsPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=2, size_hint_y=None, spacing=10 )
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
        
        for i in days:
            card = Button(text=f'{i}', size_hint_y=None, height=200, font_size = 22 ,on_press=self.go_to_card, background_color=(0.2, 0.6, 0.9, 1))
            grid_layout.add_widget(card)

        scroll_view.add_widget(grid_layout)
        layout.add_widget(scroll_view)

        self.back_button = Button(text='Back', size_hint=(1, 0.1), on_press=self.go_back, background_color=(0.8, 0.1, 0.1, 1))
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def go_to_card(self, instance):
        self.manager.current = 'card'
        self.manager.get_screen('card').update_card(instance.text)

    def go_back(self, instance):
        self.manager.current = 'home'

class CardPage(Screen):
    def __init__(self, **kwargs):
        super(CardPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text='Get more details', font_size='24sp', bold=True)
        self.back_button = Button(text='Back', size_hint=(1, 0.1), on_press=self.go_back, background_color=(0.8, 0.1, 0.1, 1))

        self.layout.add_widget(self.label)
        x = [n for n in range(0,150)]
        y = [n for n in range(100,250)]

        # Create a simple plot
        plt.plot(x, y)
        # plt.figure(figsize=(100,100))
        plt.title('Sample Graph')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # Save the plot to a temporary image
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_path = temp_file.name
            plt.savefig(temp_path)
            print(f"Graph saved to temporary file: {temp_path}")

        # Close the plot to free memory
        plt.close()
        
        self.layout.add_widget(Image(source=temp_path))
        self.layout.add_widget(self.back_button)
        self.add_widget(self.layout)
    

    def update_card(self, card_name):
        self.label.text = f'Details of {card_name}'

    def go_back(self, instance):
        self.manager.current = 'cards'

class WaterTrackerApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(FlashPage(name='flash'))
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(DynamicCardsPage(name='cards'))
        sm.add_widget(CardPage(name='card'))

        # Set the initial screen to flash
        sm.current = 'flash'

        # Automatically switch to home after 2 seconds
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: setattr(sm, 'current', 'home'), 2)

        return sm

if __name__ == '__main__':
    WaterTrackerApp().run()
