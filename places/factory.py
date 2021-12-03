import factory
from places.models import Place


class PlaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Place

    name = factory.Sequence(lambda n: f"Karoche Name of place number {n}")
    location = factory.Sequence(lambda n: f"Location - {n}")
    description = factory.Sequence(lambda n: f"description - {n}")

