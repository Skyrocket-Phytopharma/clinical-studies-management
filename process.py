from classes.processor import Processor


neuropad_args = ("Neuropad", 11, "", 1914)
monofilament_args = ("Neuropad", 11, "", 1914)

# Neuropad
processor = Processor(
    realms="Neuropad",
    priority=1,
    languages="English",
    earliest=2010,
    max=160,
    prefix="neuropad",
)
processor.process()
processor.export()

# Monofilament
processor = Processor(
    realms="Monofilament",
    priority=10,
    languages="",
    earliest=1914,
    max=100,
    prefix="monofilament",
)
processor.process()
processor.export()
