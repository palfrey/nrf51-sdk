Import("pio_lib_builder")

# skip built-in ARM mbed NRF51 SDK, place library's includes before
pio_lib_builder.env.Prepend(CPPPATH=pio_lib_builder.get_include_dirs())
