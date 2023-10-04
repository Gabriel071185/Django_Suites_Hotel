from django.shortcuts import render
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta




def index(request):
    context = {
        "date": datetime.now(),
        "active": "index",
    }
    return render(request, "reservas/inicio.html", context)

def rooms(request):
    rooms = [
        {
        "id": 1,
        "name": "Habitación Individual", 
         "capacity": 1, 
         "num_beds": "1 cama simple", 
         "view": "Frente", 
         "AC": "Si",
         "TV": "Si",
         "price_low": 30_000, 
         "price_med": 40_000, 
         "price_high": 50_000, 
         "imgs": ["individual1.webp", "individual2.webp", "individual3.webp", "individual4.webp"],
         "range": range(0,4),
         },

         {"id": 2,
          "name": "Habitación Doble Clásica", 
         "capacity": 2, 
         "num_beds": "2 camas simples", 
         "view": "Playa",
         "AC": "Si",
         "TV": "Si",
         "price_low": 40_000, 
         "price_med": 50_000, 
         "price_high": 60_000, 
         "imgs": ["doble1.webp", "doble2.webp", "doble3.webp"],
         "range": range(0,3),
         },

         {"id": 3,
        "name": "Habitación Matrimonial", 
         "capacity": 2, 
         "num_beds": "1 cama doble", 
         "view": "Ambas", 
         "AC": "Si",
         "TV": "Si",
         "price_low": 30_000, 
         "price_med": 40_000, 
         "price_high": 50_000, 
         "imgs": ["matrimonial1.webp", "matrimonial2.webp", "matrimonial3.webp"],
         "range": range(0,3),
         },

         {"id": 4,
        "name": "Habitación Triple",
         "capacity": 3, 
         "num_beds": "3 camas simples", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 40_000, 
         "price_med": 50_000, 
         "price_high": 60_000, 
         "imgs": ["triple1.webp", "triple2.webp", "triple3.webp"],
         "range": range(0,3),
         },

         {"id": 5,
        "name": "Habitación Familiar", 
         "capacity": 4, 
         "num_beds": "1 cama doble - 2 camas simples", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 50_000, 
         "price_med": 60_000, 
         "price_high": 70_000, 
         "imgs": ["familiar1.webp", "familiar2.webp", "familiar3.webp", "familiar4.webp"],
         "range": range(0,4),
         },

         {"id": 6,
        "name": "Suite", 
         "capacity": 3, 
         "num_beds": "1 cama doble - 1 sillón cama", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 60_000, 
         "price_med": 70_000, 
         "price_high": 80_000, 
         "imgs": ["suite1.webp", "suite2.webp", "suite3.webp", "suite4.webp"],
         "range": range(0,4),
         },
         
         ]
    context = {
            "date": datetime.now(),
            "active": "rooms",
            "rooms_list": rooms,
        }
    return render(request, 'reservas/habitaciones.html', context)

def facilities(request):
    context = {
        "hero":{"title":"DSH","content":"Queremos que tu estancia en nuestro exuberante hotel sea realmente inolvidable. Por eso prestamos especial atención a todas tus necesidades para que podamos asegurarte una experiencia única. habitaciones exquisitamente diseñadas, piscina y jacuzzi, un restaurante que celebra sabores auténticos, y servicios personalizados, en Django Hotel Suites creamos experiencias inolvidables. Únete a nosotros y sumérgete en un mundo donde la elegancia y la comodidad danzan en armonía."},
        "date": datetime.now(),
        "active": "facilities",
        "imagenes": [
            {"img":"img/facilities/instalacion_general.jpg"},
            {"img":"img/facilities/instalaciones_01.webp"},
            {"img":"img/facilities/instalaciones_02.webp"},
            {"img":"img/facilities/instalaciones_03.webp"},
            {"img":"img/facilities/instalaciones_04.webp"},
            {"img":"img/facilities/instalaciones_05.webp"},
            {"img":"img/facilities/instalaciones_06.webp"},
            ],
        "cards":[
            {"title":"Habitaciones","img":"img/facilities/instalaciones_05.webp","comentario":"Sumérgete en la opulencia y el confort con nuestras Habitaciones de Lujo. Cada detalle ha sido diseñado con elegancia para brindarte una experiencia de alojamiento excepcional. Disfruta de una estancia inolvidable en un entorno de lujo y comodidad incomparables."},
            {"title":"Restaurantes & bares","img":"img/facilities/instalaciones_RESTAURANTE&BAR.webp","comentario":"Explora una deliciosa variedad de sabores en nuestros exclusivos restaurantes y bares. Desde la cocina gourmet hasta cócteles artesanales, te invitamos a saborear una experiencia culinaria excepcional en un entorno encantador. Descubre un festín para tus sentidos en nuestro hotel."},
            {"title":"YATES","img":"img/facilities/instalaciones_YATES.webp","comentario":"¡Explora las maravillas del mar con nuestra gama de servicios náuticos! Desde emocionantes paseos en motos acuáticas hasta relajantes viajes en lancha y barco, tenemos todo lo que necesitas para una experiencia inolvidable en el agua. ¡Prepárate para navegar hacia la diversión y la aventura!"},
            {"title":"SPA","img":"img/facilities/instalaciones_ESPA.webp","comentario":"Descubre la tranquilidad y el encanto de nuestro oasis ESPA. Un lugar donde el bienestar y la relajación te esperan en cada rincón. ¡Sumérgete en una experiencia rejuvenecedora que te dejará renovado y revitalizado!"},
            {"title":"Ambientes Climatizados","img":"img/facilities/instalaciones_05.webp","comentario":"Relájate y sumérgete en la comodidad de nuestros Ambientes Climatizados, donde disfrutarás de la frescura y la relajación constante de una piscina cerrada. Un refugio perfecto para escapar del calor y disfrutar de un ambiente agradable en cualquier época del año. ¡Tu oasis personal de serenidad!"},
            {"title":"GYM","img":"img/facilities/instalaciones_GYM.webp","comentario":"Encuentra el equilibrio perfecto entre relajación y actividad en nuestro moderno gimnasio. Mantén tu rutina de ejercicios, disfruta de equipos de primera calidad y mantente en forma durante tu estancia. En nuestro hotel, el bienestar es una prioridad, incluso cuando estás de viaje."},
            {"title":"Playa privada","img":"img/facilities/instalaciones_PLAYAPRIVADA.webp","comentario":"Disfruta de la serenidad y la exclusividad en nuestro paraíso junto al mar. Nuestra playa privada te ofrece un rincón de tranquilidad y belleza donde puedes relajarte, tomar el sol y sumergirte en las aguas cristalinas. ¡Tu escape perfecto a la orilla del mar te espera!"},
        ]
    }
    return render(request, "reservas/facilities.html", context)

def contact(request):
    context = {
        "date": datetime.now(),
        "active": "contact",
        }
    return render(request, "reservas/contacto.html", context)

def reservation(request, id_hab):
    rooms = [
        {
        "id": 1,
        "name": "Habitación Individual", 
         "capacity": 1, 
         "num_beds": "1 cama simple", 
         "view": "Frente", 
         "AC": "Si",
         "TV": "Si",
         "price_low": 30_000, 
         "price_med": 40_000, 
         "price_high": 50_000, 
         "imgs": ["individual1.webp", "individual2.webp", "individual3.webp", "individual4.webp"],
         "range": range(0,4),
         },

         {"id": 2,
          "name": "Habitación Doble Clásica", 
         "capacity": 2, 
         "num_beds": "2 camas simples", 
         "view": "Playa",
         "AC": "Si",
         "TV": "Si",
         "price_low": 40_000, 
         "price_med": 50_000, 
         "price_high": 60_000, 
         "imgs": ["doble1.webp", "doble2.webp", "doble3.webp"],
         "range": range(0,3),
         },

         {"id": 3,
        "name": "Habitación Matrimonial", 
         "capacity": 2, 
         "num_beds": "1 cama doble", 
         "view": "Ambas", 
         "AC": "Si",
         "TV": "Si",
         "price_low": 30_000, 
         "price_med": 40_000, 
         "price_high": 50_000, 
         "imgs": ["matrimonial1.webp", "matrimonial2.webp", "matrimonial3.webp"],
         "range": range(0,3),
         },

         {"id": 4,
        "name": "Habitación Triple",
         "capacity": 3, 
         "num_beds": "3 camas simples", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 40_000, 
         "price_med": 50_000, 
         "price_high": 60_000, 
         "imgs": ["triple1.webp", "triple2.webp", "triple3.webp"],
         "range": range(0,3),
         },

         {"id": 5,
        "name": "Habitación Familiar", 
         "capacity": 4, 
         "num_beds": "1 cama doble - 2 camas simples", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 50_000, 
         "price_med": 60_000, 
         "price_high": 70_000, 
         "imgs": ["familiar1.webp", "familiar2.webp", "familiar3.webp", "familiar4.webp"],
         "range": range(0,4),
         },

         {"id": 6,
        "name": "Suite", 
         "capacity": 3, 
         "num_beds": "1 cama doble - 1 sillón cama", 
         "view": "Ambas",
         "AC": "Si",
         "TV": "Si",
         "price_low": 60_000, 
         "price_med": 70_000, 
         "price_high": 80_000, 
         "imgs": ["suite1.webp", "suite2.webp", "suite3.webp", "suite4.webp"],
         "range": range(0,4),
         },
         
         ]
    if request.method == "GET":
        room = list(filter(lambda room: room["id"] == id_hab, rooms))[0]
        context = {
            "date": datetime.now(),
            "min_date_check_in": datetime.now() + timedelta(days=1),
            "max_date_check_in": datetime.now() + relativedelta(years=1),
            "date_check_out": datetime.now() + relativedelta(months=2),
            "room": room,
            "available": False,
        }
    if request.method == "POST":
        name = request.POST.getlist("room_type")[0]
        num_people = request.POST["num_people"]
        room_view = request.POST.getlist("room_view")[0]
        date_in = request.POST["date_in"].split("-")
        date_in = date_in[2] + "/" + date_in[1] + "/" + date_in[0]
        date_out = request.POST["date_out"].split("-")
        date_out = date_out[2] + "/" + date_out[1] + "/" + date_out[0]
        comment = request.POST["comment"]
        form = {"name": name, "num_people": num_people, "room_view": room_view, "date_in": date_in, "date_out": date_out, "comment": comment}

        context = {
            "date": datetime.now(),
            "min_date_check_in": datetime.now() + timedelta(days=1),
            "max_date_check_in": datetime.now() + relativedelta(years=1),
            "date_check_out": datetime.now() + relativedelta(months=2),
            "available": True,
            "form": form,
        }
    
    return render(request, "reservas/reserva.html", context)

