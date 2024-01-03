import matplotlib.pyplot as plt
import pandas as pd 


df = pd.DataFrame({'Country':['Finland', 'Denmark', 
                              'Estonia', 'Sweden', 'Ireland', 
                              'Switzerland', 'Netherlands',
                              'Iceland', 'Belgium', 'Germany',
                              'Portugal', 'UK', 'Austria',
                              'Czech Rep.', 'Spain', 'France',
                              'Latvia', 'Lithuania', 
                              'Poland', 'Slovakia', 'Italy', 'Croatia', 
                              'Malta', 'Hungary', 'Cyprus', 'Greece',
                              'Ukraine', 'Serbia', 'Moldova', 'Montenegro',
                              'Bulgaria', 'Turkey', 
                              'Bosnia', 'Albania',
                              'N. Macedonia', 'Georgia'],
                   
                   
                   
                  'Index':[74, 73, 71, 71, 70, 67, 64, 
                           62, 61, 61, 60, 60, 59, 58, 58, 57, 55,
                           54, 53, 48, 47, 45, 45, 41, 39, 38,
                           38, 33, 32, 32, 31, 29, 24, 23, 22, 20]})


reversed_df = df.iloc[::-1]


fig, ax = plt.subplots(figsize=(9,5)) 

ax.hlines(reversed_df['Country'], xmin=0, xmax=reversed_df['Index'],
          alpha=0.7)


plt.tick_params(
    which='both',      
    labelleft=True,
    bottom=False,      
    left = False,
    top=False,         
    labelbottom=False) 

plt.yticks(fontsize=6)

ax.text(74.7, 34.7, '74', fontsize=6)
ax.text(71.0, 30.5, '70', fontsize=6)
ax.text(61.0, 24.5, '60', fontsize=6)
ax.text(49.5, 15.8, '50', fontsize=6)
ax.text(40.0, 10.5, '40', fontsize=6)
ax.text(32.5, 4.5, '30', fontsize=6)
ax.text(21.5, -0.3, '20', fontsize=6)



plt.title("Media Literacy in Europe: \n Index on how resilient a country's population is to fake news", fontsize=10)

plt.text(56, -4, "Source: Open Society Institute – Sofia", 
         size='x-small', color='black', fontweight='light')

plt.savefig('media.png', dpi=300)
plt.show()


