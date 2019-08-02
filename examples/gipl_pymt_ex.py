"""An example of running the GIPL model through PyMT."""

from pymt.models import GIPL


# Instantiate the model and get its name.
m = GIPL()
print(m.name)

# List input and output variable names.
print('Input variable names:')
for name in m.input_var_names:
    print(' - {}'.format(name))
print('Output variable names:')
for name in m.output_var_names:
    print(' - {}'.format(name))

# Call setup to get default config and data files.
defaults = m.setup('.')
print('Setup:')
for item in defaults:
    print(' - {}'.format(item))

# Initialize the model with the defaults.
# m.initialize(*defaults)

# Finalize the model.
# m.finalize()
print('Done.')
