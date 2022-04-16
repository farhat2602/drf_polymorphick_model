from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField
from polymorphic.models import PolymorphicModel

User = get_user_model()


class Post(PolymorphicModel):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    city_choice = Choices('Aşgabat', 'Lebap welaýaty', 'Darganata', 'Farap', 'Gazojak', 'Dänew', 'Garabekewül',
                         'Türkmenabat', 'Dostluk', 'Hojambaz', 'Köýtendag', 'Kerki', 'Magdanly', 'Sakar', 'Saýat',
                         'Seýdi', 'Çärjew', 'Halaç', 'Ahal welaýaty', 'Ýaşlyk', 'Ak bugdaý etraby', 'Bäherden',
                         'Babadaýhan', 'Gökdepe', 'Kaka', 'Änew', 'Tejen', 'Sarahs', 'Balkan welaýaty', 'Magtymguly',
                         'Bereket', 'Etrek', 'Esenguly', 'Gumdag', 'Balkanabat', 'Garabogaz', 'Hazar', 'Serdar',
                         'Türkmenbaşy', 'Jebel', 'Mary welaýaty', 'Ýolöten', 'Mary', 'Murgap', 'Sakarçäge',
                         'Serhetabat ', 'Tagtabazar', 'Türkmengala', 'Oguz han', 'Baýramaly', 'Şatlyk', 'Wekilbazar',
                         'Garagum etraby', 'Daşoguz welaýaty', 'Akdepe', 'Gurbansoltan Eje', 'Boldumsaz', 'Daşoguz',
                         'Gubadag', 'Görogly(Tagta)', 'Türkmenbaşy etraby', 'Ruhubelent etraby', 'Köneürgenç',
                         'S.A. Nyýazow etr',)
    city = StatusField(choices_name='city_choice')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])
    currency_choice = Choices('TMT', 'USD')
    currency_type = StatusField(choices_name='currency_choice')
    phone_num = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])
    extra_phone_num = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)], null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
