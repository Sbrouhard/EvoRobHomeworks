import numpy as np
import matplotlib.pyplot


frontSensorData = np.load("data/frontTouchSensorData.npy")
backSensorData = np.load("data/backTouchSensorData.npy")
flsinvalues = np.load("data/frontLegSinvalues.npy")
blsinvalues = np.load("data/backLegSinvalues.npy")


# matplotlib.pyplot.plot(frontSensorData, linewidth=4)
# matplotlib.pyplot.plot(backSensorData, linewidth=2)
matplotlib.pyplot.plot(flsinvalues, linewidth=5)
matplotlib.pyplot.plot(blsinvalues, linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

