"""An example of running GIPL through its Python-wrapped BMI."""

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

# Finalize the model.
m.finalize()
print('Done.')
