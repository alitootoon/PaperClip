from .models import Histogram, Data


def core():
    c = pro.a
    b = Histogram.image_id.get(histogram=c)
    file = Data.objects.filter(fk=b)

    return file


def pro(image):
    a = image
    return a
