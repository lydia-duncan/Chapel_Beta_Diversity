import betaDiversity

import xarray as xr
import netCDF4
import matplotlib.pyplot as plt

# set up Chapel library
betaDiversity.chpl_setup()

# run Chapel library
result = betaDiversity.beta_diversity(in_name="Utila", map_type="geomorphic",
                                      window_size=12732)

# visually display the result
file = xr.open_dataset(result)
file['beta_diversity'].plot()
plt.show()

betaDiversity.chpl_cleanup()
