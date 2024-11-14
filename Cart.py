from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.scrollview import ScrollView

import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('7510/GroupProject/24450782.json')
firebase_admin.initialize_app(cred_obj, {
'databaseURL':'https://comp7510-99695-default-rtdb.asia-southeast1.firebasedatabase.app/',
'storageBucket': 'gs://comp7510-99695.appspot.com'
})

class Cart(Screen):
    def ScrollViewBox(self):
        self.cart_layout = Screen()

        self.update_cart()

        scroll = ScrollView()
        scroll.add_widget(self.cart_layout)
        self.add_widget(scroll)

    def update_cart(self):
        self.cart_layout = Screen()
        self.cart_layout.clear_widgets()
        all_data = db.reference('/student').get()
        usernames = list(all_data.keys())#get username key
        print(usernames)
        
class MyApp(MDApp):
    def build(self):
        Builder.load_file("Cart.kv")
        self.title = 'Sign Up'
        screen = Cart()
        return screen

if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import platform
    if platform in ('win', 'macosx'):
        Window.size = (320,540)

MyApp().run()