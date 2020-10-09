from .selector import Selector

from random import choices as rand_choices

from ...models import Individual

from typing import List, Tuple, Dict

from random import uniform


class RouletteSelector(Selector):
    def __init__(self):
        super().__init__()

    def make_selection(self, population: List[Individual], selection_amount: int = -1) -> List[Tuple[Individual, Individual]]:
        selection_amount = selection_amount if selection_amount > 0 else int(len(population) / 2)

        selection: List[Tuple[Individual, Individual]] = []

        return selection

