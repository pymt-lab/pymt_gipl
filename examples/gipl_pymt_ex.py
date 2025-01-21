"""An example of running the GIPL model through PyMT."""

from pymt.models import GIPL


# Instantiate the model and get its name.
m = GIPL()
print(m.name)

# List input and output variable names.
print("Input variable names:")
for name in m.input_var_names:
    print(" - {}".format(name))
print("Output variable names:")
for name in m.output_var_names:
    print(" - {}".format(name))

# Call setup to get default config and data files.
defaults = m.setup(".")
print("Setup:")
for item in defaults:
    print(" - {}".format(item))

# Initialize the model with the defaults.
m.initialize(*defaults)

# Display the start, end, and current model time.
print("Start time: {}".format(m.start_time))
print("End time: {}".format(m.end_time))
print("Current time: {}".format(m.time))

# Update the model state.
print("Update the model state...")
m.update()
print("Current time: {}".format(m.time))

# Get the soil temperature at this time.
soilt = m.var["soil__temperature"].data
units = m.var["soil__temperature"].units
print("Soil temperature: {} {}".format(soilt, units))

# Advance the model to the end.
print("Run the model to the end...")
m.update_until(m.end_time)
print("Current time: {}".format(m.time))

# Get the final soil temperature distribution.
soilt = m.var["soil__temperature"].data
print("Soil temperature: {} {}".format(soilt, units))

# Finalize the model.
m.finalize()
print("Done.")
