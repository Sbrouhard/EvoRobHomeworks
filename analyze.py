import numpy as np
import matplotlib.pyplot


frontSensorData = np.load("data/frontTouchSensorData.npy")
backSensorData = np.load("data/backTouchSensorData.npy")

matplotlib.pyplot.plot(frontSensorData, linewidth=4)
matplotlib.pyplot.plot(backSensorData, linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

