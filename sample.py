from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

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
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Welcome to Water Tracker')
        button = Button(text='Go to Dynamic Cards', on_press=self.go_to_cards)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_cards(self, instance):
        self.manager.current = 'cards'

class DynamicCardsPage(Screen):
    def __init__(self, **kwargs):
        super(DynamicCardsPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=1, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        for i in range(10):
            card = Button(text=f'Card {i+1}', size_hint_y=None, height=100, on_press=self.go_to_card)
            grid_layout.add_widget(card)

        scroll_view.add_widget(grid_layout)
        layout.add_widget(scroll_view)
        self.add_widget(layout)

    def go_to_card(self, instance):
        self.manager.current = 'card'
        self.manager.get_screen('card').update_card(instance.text)

class CardPage(Screen):
    def __init__(self, **kwargs):
        super(CardPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Card Details')
        self.layout.add_widget(self.label)
        self.add_widget(self.layout)

    def update_card(self, card_name):
        self.label.text = f'Details of {card_name}'

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
