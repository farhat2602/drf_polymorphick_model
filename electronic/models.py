from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from post.models import Post

User = get_user_model()


class Electronic(Post):

    state_choice = Choices('New', '2Hand')
    state_type = StatusField(choices_name='state_choice')

    def __str__(self):
        return self.state_type


class Phone(Electronic):

    phone_choice = Choices('Smartphone', 'DialPhone')
    phone_type = StatusField(choices_name='phone_choice')

    def __str__(self):
        return self.phone_type


class Smartphone(Phone):

    brand_choice = Choices('Samsung', 'Apple', 'Xiaomi', 'Nokia', 'Reeder', 'General Mobile', 'Oppo',
                           'Realme', 'LG', 'Huawei', 'BlackBerry', 'POCO', 'Casper', 'TCL', 'VESTEL',
                           'LENOVO', 'Alcatel', 'Htc', 'ZTE', 'Motorola', 'OnePlus', 'Meizu', 'Honor',
                           'Panasonic', 'Turkcell', 'Turk Telekom', 'Syrox', 'Asus')
    brand_type = StatusField(choices_name='brand_choice')
    memory_choice = Choices('8GB','16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB')
    memory_type = StatusField(choices_name='memory_choice')
    ram_memory_choice = Choices('1GB', '2GB', '3GB', '4GB', '6GB', '8GB', '16GB', '32GB')
    ram_memory_type = StatusField(choices_name='ram_memory_choice')
    dual_sim = models.BooleanField(default=False)
    nfc = models.BooleanField(default=False)
    face_id = models.BooleanField(default=False)
    network_choice = Choices('2G', '3G', '4G', '4.5G', '5G')
    network = StatusField(choices_name='network_choice')
    guaranty = models.CharField(max_length=124, null=True, blank=True)
    change = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_type


class SmartphoneImage(models.Model):

    smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE, related_name='smartphone_images')
    images = models.ImageField(upload_to='electronic/smartphone_images/', null=True, blank=True)

class DialPhone(Phone):

    brand_choice = Choices('Samsung', 'Nokia', 'LG', 'BlackBerry', 'TCL', 'VESTEL', 'LENOVO',
                           'Alcatel', 'Motorola', 'Panasonic', 'other')
    brand_type = StatusField(choices_name='brand_choice')
    have_camera = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_type


class DialPhoneImage(models.Model):

    dial_phone = models.ForeignKey(DialPhone, on_delete=models.CASCADE, related_name='dial_phone_images')
    images = models.ImageField(upload_to='electronic/dial_phone_images/', null=True, blank=True)


class Tablet(Electronic):

    brand_choice = Choices('Apple', 'Asus', 'Beko', 'Google', 'Huawei', 'Honor',
                           'Lenovo', 'LG', 'Microsoft', 'Motorola', 'Nokia', 'Oppo', 'Redmi',
                           'Samsung', 'Sony', 'Xiaomi', 'ZTE', 'Other')
    brand_type = StatusField(choices_name='brand_choice')
    memory_choice = Choices('16Gb', '32Gb', '64Gb', '128Gb', '256Gb', '512Gb', '1TB')
    memory_type = StatusField(choices_name='memory_choice')
    ram_memory_choice = Choices('1Gb', '2Gb', '3Gb', '4Gb', '6Gb', '8Gb', '16GB', '32GB')
    ram_memory_type = StatusField(choices_name='ram_memory_choice')
    sim = models.BooleanField(default=False)
    network_choice = Choices('2G', '3G', '4G', '4.5G', '5G')
    network = StatusField(choices_name='network_choice')
    nfc = models.BooleanField(default=False)
    face_id = models.BooleanField(default=False)
    guaranty = models.CharField(max_length=124, null=True, blank=True)
    change = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_type


class TabletImage(models.Model):

    tablet = models.ForeignKey(Tablet, on_delete=models.CASCADE, related_name='tablet_images')
    images = models.ImageField(upload_to='electronic/tablet_images/', null=True, blank=True)


class Desktop(Electronic):

    brand_choice = Choices('Apple', 'Acer', 'Asus', 'Beko', 'Casper', 'Dell', 'HP', 'Lenovo', 'LG',
                           'Microsoft', 'Msi', 'Monster', 'Samsung', 'Toshiba', 'Xiaomi', 'Other')
    brand_type = StatusField(choices_name='brand_choice')
    ram_memory_choice = Choices('1Gb', '2Gb', '3Gb', '4Gb', '6Gb', '8Gb', '16GB', '32GB', '64GB')
    ram_memory_type = StatusField(choices_name='ram_memory_choice')
    memory_choice = Choices('16Gb', '32Gb', '64Gb', '128Gb', '256Gb', '512Gb', '1TB', '2TB', '4TB')
    memory_type = StatusField(choices_name='memory_choice')
    disk_choice = Choices('SSD', 'HDD')
    disk_type = StatusField(choices_name='disk_choice')
    guaranty = models.CharField(max_length=124, null=True, blank=True)
    change = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_type


class DesktopImage(models.Model):

    desktop = models.ForeignKey(Desktop, on_delete=models.CASCADE, related_name='desktop_images')
    images = models.ImageField(upload_to='electronic/desktop_images/', null=True, blank=True)


class Laptop(Electronic):

    brand_choice = Choices('Apple', 'Acer', 'Asus', 'BlackBerry', 'Casper', 'Dell', 'Google',
                           'Huawei', 'Honor', 'HomeTech', 'HP', 'Lenovo', 'LG', 'Microsoft',
                           'Msi', 'Monster', 'Redmi', 'Samsung', 'Sony', 'Toshiba',
                           'Xiaomi', 'Other')
    brand_type = StatusField(choices_name='brand_choice')
    screen_diagonal_choice = Choices('10', '13', '13.3', '14', '15', '15.6', '16', '16.1', '17.3')
    screen_diagonal_type = StatusField(choices_name='screen_diagonal_choice')
    discrete_video_card = models.BooleanField(default=False)
    graphic_card_choice = Choices('1Gb', '2Gb', '3Gb', '4Gb', '6Gb', '8Gb', '16GB', '32GB')
    graphic_card_type = StatusField(choices_name='graphic_card_choice')

    def __str__(self):
        return self.brand_type


class LaptopImage(models.Model):

    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='laptop_images')
    images = models.ImageField(upload_to='electronic/laptop_images/', null=True, blank=True)


class Monitor(Electronic):

    brand_choice = Choices('ASUS', 'LENOVO', 'HP', 'ACER', 'Huawei', 'Monster', 'Casper', 'DELL',
                           'MSI', 'FUJITSU', 'Microsoft', 'TOSHIBA', 'Honor', 'RAZER', 'VESTEL',
                           'Intel', 'Samsung', 'other')
    brand_type = StatusField(choices_name='brand_choice')
    wfi = models.BooleanField(default=False)
    hdmi = models.BooleanField(default=False)
    vga = models.BooleanField(default=False)
    screen_diagonal_choice = Choices('7', '10', '14', '15', '15.6', '17', '18.5', '19', '19.5', '20', '20.7', '21', '22', '23', '23.5',
                      '24', '25', '27', '28', '29', '31', '32', '34', '35', '49' '55')
    screen_diagonal_type = StatusField(choices_name='screen_diagonal_choice')
    hz_choice = Choices('60', '72', '75', '83', '100', '120', '144', '165', '200', '240')
    hz_type = StatusField(choices_name='hz_choice')

    def __str__(self):
        return self.brand_type


class MonitorImage(models.Model):

    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, related_name='monitor_images')
    images = models.ImageField(upload_to='electronic/monitor_images/', null=True, blank=True)


class Camera(Electronic):

    brand_choice = Choices('Fujifilm', 'Canon', 'Xiaomi', 'Sony', 'Kodak', 'Heider', 'Nikon', 'Dijimedia', 'BLUE İNTER',
                        'EKEN', 'Samsung', 'Skygo', 'DJI', 'Everest', 'OEM', 'Retro', 'Zore', 'Panasonic', 'Baseus',
                        'KAISER', 'Enshall', 'Sandisk', 'Dahua', 'Olympus', 'Platoon', 'Benks', 'Polaroid', 'Chermik',
                        'Tucano', 'Duracell', 'Addison', 'logitech', 'HP', 'Vision', 'Zoom', 'Beta', 'Oppo', 'Apple',
                        'Kingston', 'KAYAMU', 'LG', 'Toshiba', 'NEVO', 'other')
    brand_type = StatusField(choices_name='brand_choice')

    def __str__(self):
        return self.brand_type


class CameraImage(models.Model):

    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name='camera_images')
    images = models.ImageField(upload_to='electronic/camera_images/')


class Speaker(Electronic):

    brand_choice = Choices('Polygold', 'JBL', 'Xiaomi', 'Pioneer', 'logitech', 'Snopy', 'Harman Kardon', 'Sony', 'Piranha',
                        'Sunix', 'Torima', 'LG', 'Samsung', 'Mikado', 'HP', 'Philips', 'LENOVO', 'Havana', 'other')
    brand_type = StatusField(choices_name='brand_choice')

    def __str__(self):
        return self.brand_type


class SpeakerImage(models.Model):

    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name='speaker_images')
    images = models.ImageField(upload_to='electronic/speaker_images/')


class Headphone(Electronic):

    type_choice = Choices('Bluetooth', '3.5mm')
    type = StatusField(choices_name='type_choice')
    brand = models.CharField(max_length=24)

    def __str__(self):
        return self.type


class HeadphoneImage(models.Model):

    headphone = models.ForeignKey(Headphone, on_delete=models.CASCADE, related_name='headphone_images')
    images = models.ImageField(upload_to='electronic/headphone_images/')


class GameConsole(Electronic):

    game_choice = Choices('Playstation', 'Xbox')
    game_type = StatusField(choices_name='game_choice')
    brand_choice = Choices('Sony', 'GoldMaster', 'gamam', '2K Games', 'Ubisoft', 'logitech', 'RockStar Games', 'Polygold')
    brand_type = StatusField(choices_name='brand_choice')
    memory_choice = Choices('160 GB', '320 GB', '500 GB', '825 GB', '1 TB', '2 TB')
    memory_type = StatusField(choices_name='memory_choice')

    def __str__(self):
        return self.brand_type


class GameConsoleImage(models.Model):

    game = models.ForeignKey(GameConsole, on_delete=models.CASCADE, related_name='game_console_images')
    images = models.ImageField(upload_to='electronic/game_console_images/')


class Printer(Electronic):

    printer_choice = Choices('Printer', 'Copy', 'Scanner')
    printer_type = StatusField(choices_name='printer_choice')
    brand = models.CharField(max_length=55)

    def __str__(self):
        return self.printer_type


class PrinterImage(models.Model):

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, related_name='printer_images')
    images = models.ImageField(upload_to='electronic/printer_images/')
