# builder is used for the registering and application of rules for specific widgets.
from kivy.lang import Builder

# the properties classes are used when you create an eventdispatcher
from kivy.properties import StringProperty, ListProperty

# to change the kivy default setting we use config
from kivy.config import Config
Config.set('graphics','width','550')
Config.set('graphics','height','550')

# this module contains MDApp class that is inherited from app
from kivymd.app import MDApp

# import theming to use them ,color and hover options
from kivymd.theming import ThemableBehavior

# boxlayout arranges children in a vertical or horizontal box
from kivymd.uix.boxlayout import MDBoxLayout

# onelinelistitem will create a list that expands as items are added to it
from kivymd.uix.list import OneLineIconListItem, MDList

# creating the kv file.you can write it also in a separate .kv file
KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: .5, None
            size: "75dp", "75dp"
            source: "img.png"

    MDLabel:
        text: "sam codehub channel"
        font_style: "Button"
        adaptive_height: True

    MDLabel:
        text: "samcodehub@gmail.com"
        font_style: "Caption"
        adaptive_height: True

    ScrollView:

        DrawerList:
            id: md_list



MDScreen:

    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


# create a class to use mdboxlayout for the navigation content
class ContentNavigationDrawer(MDBoxLayout):
    pass

# create another class and specifying icon and text colors
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))
    
# create a drawerlist class for theming the item list
class DrawerList(ThemableBehavior, MDList):
    # called when tap on menu item
    def set_color_item(self, instance_item):
        # set the color of the icon and text for the menu items
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

# load the kv file and declaring items with icons
class NavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
            
# run the app
NavigationDrawer().run()