from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from post.models import Post
from electronic.models import (Smartphone, DialPhone, Desktop, Laptop, Monitor, Camera, Speaker,
                               Headphone, GameConsole, Printer)
from electronic.serializers import (SmartphoneSerializer, DialPhoneSerializer, DesktopSerializer,
                                    LaptopSerializer, MonitorSerializer, CameraSerializer,
                                    SpeakerSerializer, HeadphoneSerializer, GameConsoleSerializer,
                                    PrinterSerializer)
from estate.models import Apartment, Office, CottageHouse, LandPlot, WorkPlace
from estate.serializers import (ApartmentSerializer, OfficeSerializer, CottageHouseSerializer,
                                LandPlotSerializer, WorkPlaceSerializer)
from job.models import Vacancy, Resume
from job.serializers import VacancySerializer, ResumeSerializer
from transport.models import Car, Motorcycle, Truck
from transport.serializers import CarSerializer, MotorcycleSerializer, TruckSerializer
from fashion.models import (ManClothes, WomanClothes, ChildClothes, Watch, Shoes, Underwear,
                            Bag, Cosmetic, Accessories, Textile)
from fashion.serializers import (ManClothesSerializer, WomanClothesSerializer, ChildClothesSerializer,
                                 WatchSerializer, ShoesSerializer, UnderwearSerializer, BagSerializer,
                                 CosmeticSerializer, AccessoriesSerializer, TextileSerializer)
from home_garden.serializers import (CarpetSerializer, ConsumerElectronicSerializer, FurnitureSerializer,
                                     PlantSerializer, DishesAppliancesSerializer)
from home_garden.models import (Carpet, ConsumerElectronic, Furniture, Plant, DishesAppliances)
from services.models import Service
from services.serializers import ServiceSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostPolymorphicSerializer(PolymorphicSerializer):

   model_serializer_mapping = {
       Post: PostSerializer,
       Smartphone: SmartphoneSerializer,
       DialPhone: DialPhoneSerializer,
       Desktop: DesktopSerializer,
       Laptop: LaptopSerializer,
       Monitor: MonitorSerializer,
       Camera: CameraSerializer,
       Speaker: SpeakerSerializer,
       Headphone: HeadphoneSerializer,
       GameConsole: GameConsoleSerializer,
       Printer: PrinterSerializer,
       Apartment: ApartmentSerializer,
       Office: OfficeSerializer,
       CottageHouse: CottageHouseSerializer,
       LandPlot: LandPlotSerializer,
       WorkPlace: WorkPlaceSerializer,
       Vacancy: VacancySerializer,
       Resume: ResumeSerializer,
       Car: CarSerializer,
       Motorcycle: MotorcycleSerializer,
       Truck: TruckSerializer,
       ManClothes: ManClothesSerializer,
       WomanClothes: WomanClothesSerializer,
       ChildClothes: ChildClothesSerializer,
       Watch: WatchSerializer,
       Shoes: ShoesSerializer,
       Underwear: UnderwearSerializer,
       Bag: BagSerializer,
       Cosmetic: CosmeticSerializer,
       Accessories: AccessoriesSerializer,
       Textile: TextileSerializer,
       Carpet: CarpetSerializer,
       ConsumerElectronic: ConsumerElectronicSerializer,
       Furniture: FurnitureSerializer,
       Plant: PlantSerializer,
       DishesAppliances: DishesAppliancesSerializer,
       Service: ServiceSerializer,
   }
