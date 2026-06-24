import math
import random


def sample_absorption_distance(
    mu_abs
):

    if mu_abs <= 0:

        return float("inf")

    return (
        -math.log(
            random.random()
        )
        /
        mu_abs
    )