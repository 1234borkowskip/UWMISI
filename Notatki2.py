Wykres kołowy

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('olympics.csv')
labels = 'Great Britain (GBR) [GBR] [Z]', 'Greece (GRE) [Z]', 'Canada (CAN)', 'Germany (GER) [GER] [Z]', 'China (CHN) [CHN]'
sizes = [806, 111, 459, 782, 526]
explode = (0, 0.1, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
wykres kołowy
tylko nie mam danych pokazanych skąd wziąłem ale są z tej tabelki

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('biostats.csv', delimiter=';', encoding='windows-1250')
x = data.iloc[3:, 0]
y = data.iloc[3:, 4]

y_pos = np.arange(len(x))
plt.bar(y_pos, y)
plt.xticks(y_pos, x)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('biostats.csv', delimiter=';', encoding='windows-1250')
x = data.iloc[3:, 0]
y = data.iloc[3:, 4]

y_pos = np.arange(len(x))
plt.bar(y_pos, y)
plt.xticks(y_pos, x)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("mtcars.csv")
df = pd.DataFrame(data)
df.sort_values('cyl')
df.columns = ['marka','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
mniejDisp = (data[data['disp']<255])
cyl4 = mniejDisp[mniejDisp['cyl'] ==4]
cyl6 = mniejDisp[mniejDisp['cyl'] ==6]
avg4 = np.average(cyl4['mpg'])
avg6 = np.average(cyl6['mpg'])
plt.bar(4,avg4, label='4 cylindry')
plt.bar(6,avg6, label='6 cylindrów')
plt.xlabel('Ilość cylindrów')
plt.ylabel('Spalanie (mpg)')
plt.legend()
plt.title('Spalanie dla danej ilości cylindrów')
plt.savefig("spalanie.png", dpi=72)
plt.show()




import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 8, 100)
plt.subplot(3, 1, 1) # 1-ilosc rys. 2-
plt.plot(x, np.power(x, 2)+3*x-5, 'b', label="y=x^2+3*x-4")
plt.xlim(-2, 6) #os x
#plt.ylim(-25, 25)
plt.title('Wykres pierwszej funkcji')
plt.grid(True)
plt.legend()



plt.subplot(3, 1, 2)
plt.plot(x, (25*(np.cos(x))), '.y', label="25*cos(x)")
plt.legend()
plt.grid(True)
plt.title('Wykres drugiej funkcji')



plt.subplot(3, 1, 3)
plt.plot(x, (x**2)+(3*x-5), 'b', label="y=x^2+3*x+4")
plt.plot(x, 25*(np.cos(x)), '.y', label="25*cos(x)")
plt.grid(True)
plt.xlim(-2, 4)

plt.title('Jedna funkcja na drugiej')
plt.legend()
plt.savefig("fig3.png", dpi=72)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.subplot(1, 4, 1) # 1-ilosc rys. 2-
plt.plot(x, (x**2)+(3*x+4), 'b')
plt.grid(True)
plt.xlim(0, 10) #os x
plt.subplot(1, 4, 2)

plt.plot(x, 25*np.sin(x), '.g')
plt.grid(True)
plt.xlim(0, 10)
plt.subplot(1, 4, 3)

plt.plot(x, x**2+3*x+4, 'b', x, 25*np.sin(x), '.g')
plt.grid(True)
plt.xlim(0, 10)
plt.savefig("fig3.png", dpi=72)
plt.show()




import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
plt.subplot(1, 4, 1) # 1-ilosc rys. 2-
plt.plot(x, (x**2)+(3*x+4), 'b')
plt.grid(True)
plt.title('Wykres pierwszej funkcji')
plt.xlim(0, 10) #os x
plt.ylim(-10, 50)
plt.subplot(1, 4, 2)

plt.plot(x, 25*np.sin(x), '.g')
plt.grid(True)
plt.title('Wykres drugiej funkcji')
plt.xlim(0, 10)
plt.subplot(1, 4, 3)

plt.plot(x, x**2+3*x+4, 'b', x, 25*np.sin(x), '.g')
plt.grid(True)
plt.title('Jedna funkcja na drugiej')
plt.xlim(0, 10)
plt.ylim(-30, 40)
plt.savefig("fig3.png", dpi=72)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
plt.subplot(1, 4, 1) # 1-ilosc rys. 2-
plt.plot(x, (x**2)+(3*x+4), 'b', label="y=x^2+3*x+4")
plt.grid(True)
plt.title('Wykres pierwszej funkcji')
plt.legend()
plt.xlim(0, 10) #os x
plt.ylim(-10, 50)
plt.subplot(1, 4, 2)

plt.plot(x, 25*np.sin(x), '.g', label="25*sin(x)")
plt.grid(True)
plt.title('Wykres drugiej funkcji')
plt.legend()
plt.xlim(0, 10)

plt.subplot(1, 4, 3)

plt.plot(x, x**2+3*x+4, 'b', label="y=x^2+3*x+4")
plt.plot(x, 25*np.sin(x), '.g', label="25*sin(x)")        
plt.grid(True)
plt.title('Jedna funkcja na drugiej')
plt.legend()
plt.xlim(0, 10)
plt.ylim(-30, 40)
plt.savefig("fig3.png", dpi=72)
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,7,0.1)

plt.plot(x, np.sin(x)+5*pow(4,x)+np.sqrt(x**2+4*x+4), 'b')
plt.grid(True)


plt.xlim(1, 7)
plt.ylim(0, 30)
plt.show()
