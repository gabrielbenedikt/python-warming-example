from warming.data.summary import Summary
from warming.plot.maps import World

def main():
    summary = Summary()
    world = World()
    world.show(summary.co2(), "CO2C")
    world.show(summary.n2o(), "N2OC")

if __name__ == "__main__":
    main()