import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("model_devi.out", names=True)
for name in ["max_devi_f"]:
    plt.plot(data['step'], data[name], label=name)
plt.legend()
plt.xlabel('Step')
plt.ylabel('Devi')
plt.grid()
plt.savefig('max_devi_f.pdf', bbox_inches='tight')
plt.show()
