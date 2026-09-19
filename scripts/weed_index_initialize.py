from data_loader import load_locality_data
import matplotlib.pyplot as plt
import numpy as np


def weed_index_initialize(density, pressure_coef, w_min=0.05, w_max=1):
    if w_max < w_min:
        raise ValueError('Max index must greater then min index')
    
    weed_index = w_min + (w_max - w_min) * np.exp(-density*pressure_coef)
    return weed_index


if __name__ == "__main__":

    localities = load_locality_data()

    metro = localities[
        localities["postcode"].astype(int).between(6000,6199)
    ].copy()

    metro['weed_index'] = weed_index_initialize(density=metro['population_density_km2'],
                                                pressure_coef=0.05,
                                                w_min=0.05,
                                                w_max=1)


    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 10))

    metro.plot(
        column="weed_index",
        cmap="YlGn",
        legend=True,
        ax=ax,
        edgecolor="none"
    )

    ax.set_title("Initial Weed Density Index")
    ax.set_axis_off()

    plt.tight_layout()
    plt.show()
        