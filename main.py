from physics.absorption import (
    sample_absorption_distance
)

for i in range(10):

    distance = (
        sample_absorption_distance(
            10
        )
    )

    print(distance)