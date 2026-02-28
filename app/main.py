from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = []
    for customer in customers:
        new_custumer = Customer(customer["name"], customer["food"])
        customer_instances.append(new_custumer)
        CinemaBar.sell_product(product=new_custumer.food,
                               customer=new_custumer)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(movie_name=movie, customer=customer_instances,
                       cleaning_staff=cleaning_staff)
