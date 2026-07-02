from core.vector import Vector

from geometry.rectangular_film import (
    RectangularFilm
)

from materials.material import (
    Material
)

from sources.point_source import (
    PointSource
)

from simulation.simulation import (
    Simulation
)

from tracking.summary_observer import (
    SummaryObserver
)

from tracking.track_observer import (
    TrackObserver
)

from tracking.event_observer import (
    EventObserver
)

from tracking.composite_observer import (
    CompositeObserver
)

from config.simulation_config import (
    SimulationConfig
)

from config.physics_config import (
    PhysicsConfig
)


# ==========================================
# Geometry
# ==========================================

film = RectangularFilm(

    width=0.210,

    length=0.297,

    thickness=0.0004,

    refractive_index=1.49
)


# ==========================================
# Material
# ==========================================

material = Material(

    refractive_index=1.49,

    mu_abs=1000,

    mu_scat=0
)

# ==========================================
# Physics Configuration
# ==========================================

physics = PhysicsConfig(

    absorption=True,

    scattering=False,

    fluorescence=False,

    boundary_model="mirror",

    scattering_model="isotropic"
)



# ==========================================
# Output Configuration
# ==========================================



config = SimulationConfig(

    store_summary=True,

    store_photon=True,

    store_events=True
)


# ==========================================
# Build Observers
# ==========================================

summary_observer = SummaryObserver()

track_observer = TrackObserver()

event_observer = EventObserver()

observers = []

if config.store_summary:

    observers.append(
        summary_observer
    )

if config.store_photon:

    observers.append(
        track_observer
    )

if config.store_events:

    observers.append(
        event_observer
    )

observer = CompositeObserver(
    *observers
)


# ==========================================
# Light Source
# ==========================================

source = PointSource(

    position=Vector(
        0.100,
        0.100,
        0.0002
    ),

    direction=Vector(
        1,
        0,
        1
    ),

    wavelength=450
)


# ==========================================
# Simulation
# ==========================================

simulation = Simulation(

    source=source,

    film=film,

    material=material,

    observer=observer
)

simulation.run(

    n_photons=10
)


# ==========================================
# Print Photon Results
# ==========================================

if config.store_photon:

    print("\nPhoton Results\n")

    for photon_result in track_observer.results:

        print(photon_result)


# ==========================================
# Print Photon History
# ==========================================

if config.store_events:

    print("\nPhoton History\n")

    for event in event_observer.histories[0]:

        print(event)


# ==========================================
# Print Summary
# ==========================================

if config.store_summary:

    print("\nSummary\n")

    print(
        "Total photons:",
        summary_observer.total
    )

    print(
        "Absorbed:",
        summary_observer.absorbed
    )

    print(
        "Top exit:",
        summary_observer.top_exit
    )

    print(
        "Bottom exit:",
        summary_observer.bottom_exit
    )

    print(
        "Edge exit:",
        summary_observer.edge_exit
    )