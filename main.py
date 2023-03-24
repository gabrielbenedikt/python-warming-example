from warming.data.summary import Summary
from warming.plot.maps import World
from warming.plot.maps import Europe


def main():
    summary = Summary()
    world = World()
    world.show(summary.co2(), "CO2C")
    europe = Europe()
    europe.show(summary.co2(), "CO2C")

if __name__ == "__main__":
    main()