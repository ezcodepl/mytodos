from domain import Athlete
def get_all():
    result=[]
    a1 = Athlete(1, 'Andrzej', 'Klusiewicz', 1.76, 73)
    a2 = Athlete(2, 'Muniek', 'Staszczyk', 1.58, 82)
    a3 = Athlete(3, 'Czesław', 'Mozil', 1.89, 92)
    result.append(a1)
    result.append(a2)
    result.append(a3)
    return result