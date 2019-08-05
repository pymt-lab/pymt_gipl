"""An example of running GIPL through its Python-wrapped BMI."""

import numpy as np
from pymt_gipl import GIPL


# Instantiate a model and get its name.
m = GIPL()
print(m.get_component_name())

# List input and output variable names.
print('Input variable names:')
for name in m.get_input_var_names():
    print(' - {}'.format(name))
print('Output variable names:')
for name in m.get_output_var_names():
    print(' - {}'.format(name))

# Initialize the model with a config file pointing to local files.
m.initialize('gipl_config.cfg')

# Get time information from the model.
print('Start time:', m.get_start_time())
print('End time:', m.get_end_time())
print('Current time:', m.get_current_time())
print('Time step:', m.get_time_step())
print('Time units:', m.get_time_units())

# Get the grid_id for the soil__temperature variable.
var_name = 'soil__temperature'
print('Variable: {}'.format(var_name))
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)

# Get grid and variable info for soil__temperature.
print(' - grid type:', m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(' - rank:', grid_rank)
grid_shape = np.empty(grid_rank, dtype=np.int32)
m.get_grid_shape(grid_id, grid_shape)
print(' - shape:', grid_shape)
grid_size = m.get_grid_size(grid_id)
print(' - size:', grid_size)
print(' - spacing: n/a for a {} grid'.format(m.get_grid_type(grid_id)))
grid_origin = np.empty(grid_rank, dtype=np.float64)
m.get_grid_origin(grid_id, grid_origin)
print(' - origin:', grid_origin)
grid_x = np.empty(grid_shape[1], dtype=np.float64)
m.get_grid_x(grid_id, grid_x)
print(' - x nodes:', grid_x)
grid_y = np.empty(grid_shape[0], dtype=np.float64)
m.get_grid_y(grid_id, grid_y)
print(' - y nodes:', grid_y)
grid_z = np.empty(grid_shape[2], dtype=np.float64)
m.get_grid_z(grid_id, grid_z)
print(' - z nodes:', grid_z)
print(' - variable type:', m.get_var_type(var_name))
print(' - units:', m.get_var_units(var_name))
print(' - itemsize:', m.get_var_itemsize(var_name))
print(' - nbytes:', m.get_var_nbytes(var_name))

# Advance the model by one time step.
print('Updating model...')
m.update()
print(' - current time:', m.get_current_time())

# Advance the model by a fractional time step.
print('Updating model...')
m.update_frac(0.75)
print(' - current time:', m.get_current_time())

# Advance the model until a later time.
print('Updating model...')
m.update_until(15.0)
print(' - current time:', m.get_current_time())

# Get the soil__temperature values.
print('Get values for {}:'.format(var_name))
val = np.empty(grid_shape[2], dtype=np.float32)
m.get_value(var_name, val)
print(' - values (streamwise):')
print(val)

# The get_value_ptr method isn't implemented.

# Set new soil__temperature values.
print('Set new values for {}:'.format(var_name))
new = np.arange(grid_shape[2], dtype=np.float32)
print(' - new values (streamwise):')
print(new)
m.set_value(var_name, new)
check = np.empty(grid_size, dtype=np.float32)
m.get_value(var_name, check)
print(' - check new values (set/get, streamwise):')
print(check)
print(' - are new and check the same? (True)', np.array_equal(new, check))

# Finalize the model.
m.finalize()
print('Done.')
