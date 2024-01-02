# Load all importance packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("military-personnel-relative-to-total-population.csv")

print(df.isnull().sum())

df.drop(columns='Code', inplace=True)


# Loop over dataframe 

for i in df['Entity'].unique():
    print(i + " = df[df['Entity'] == '" + i +"'] ")
    print("sns.lineplot(x = 'Year', y= 'military_personnel_share', data = " + i + ", color='darkorange', alpha=0.1)\n")


# Plotting 

fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim([1950, 2012])
ax.set_ylim([-0.5, 10])
sns.set(style="white")


Afghanistan = df[df['Entity'] == 'Afghanistan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Afghanistan, color='darkorange', alpha=0.1)

Albania = df[df['Entity'] == 'Albania'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Albania, color='darkorange', alpha=0.1)

Algeria = df[df['Entity'] == 'Algeria'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Algeria, color='darkorange', alpha=0.1)

Andorra = df[df['Entity'] == 'Andorra'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Andorra, color='darkorange', alpha=0.1)

Angola = df[df['Entity'] == 'Angola'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Angola, color='darkorange', alpha=0.1)

Antigua_Barbuda = df[df['Entity'] == 'Antigua and Barbuda'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Antigua_Barbuda, color='darkorange', alpha=0.1)

Argentina = df[df['Entity'] == 'Argentina'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Argentina, color='darkorange', alpha=0.1)

Armenia = df[df['Entity'] == 'Armenia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Armenia, color='darkorange', alpha=0.1)

Australia = df[df['Entity'] == 'Australia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Australia, color='darkorange', alpha=0.1)

Austria = df[df['Entity'] == 'Austria'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Austria, color='darkorange', alpha=0.1)

Austria_Hungary = df[df['Entity'] == 'Austria-Hungary'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Austria_Hungary, color='darkorange', alpha=0.1)

Azerbaijan = df[df['Entity'] == 'Azerbaijan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Azerbaijan, color='darkorange', alpha=0.1)

Baden = df[df['Entity'] == 'Baden'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Baden, color='darkorange', alpha=0.1)

Bahamas = df[df['Entity'] == 'Bahamas'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bahamas, color='darkorange', alpha=0.1)

Bahrain = df[df['Entity'] == 'Bahrain'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bahrain, color='darkorange', alpha=0.1)

Bangladesh = df[df['Entity'] == 'Bangladesh'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bangladesh, color='darkorange', alpha=0.1)

Barbados = df[df['Entity'] == 'Barbados'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Barbados, color='darkorange', alpha=0.1)

Bavaria = df[df['Entity'] == 'Bavaria'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bavaria, color='darkorange', alpha=0.1)

Belarus = df[df['Entity'] == 'Belarus'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Belarus, color='darkorange', alpha=0.1)

Belgium = df[df['Entity'] == 'Belgium'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Belgium, color='darkorange', alpha=0.1)

Belize = df[df['Entity'] == 'Belize'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Belize, color='darkorange', alpha=0.1)

Benin = df[df['Entity'] == 'Benin'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Benin, color='darkorange', alpha=0.1)

Bhutan = df[df['Entity'] == 'Bhutan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bhutan, color='darkorange', alpha=0.1)

Bolivia = df[df['Entity'] == 'Bolivia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bolivia, color='darkorange', alpha=0.1)

Bosnia_Herzegovina = df[df['Entity'] == 'Bosnia and Herzegovina'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bosnia_Herzegovina, color='darkorange', alpha=0.1)

Botswana = df[df['Entity'] == 'Botswana'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Botswana, color='darkorange', alpha=0.1)

Brazil = df[df['Entity'] == 'Brazil'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Brazil, color='darkorange', alpha=0.1)

Brunei = df[df['Entity'] == 'Brunei'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Brunei, color='darkorange', alpha=0.1)

Bulgaria = df[df['Entity'] == 'Bulgaria'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Bulgaria, color='darkorange', alpha=0.1)

Burkina_Faso = df[df['Entity'] == 'Burkina Faso'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Burkina_Faso, color='darkorange', alpha=0.1)

Burundi = df[df['Entity'] == 'Burundi'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Burundi, color='darkorange', alpha=0.1)

Cambodia = df[df['Entity'] == 'Cambodia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Cambodia, color='darkorange', alpha=0.1)

Cameroon = df[df['Entity'] == 'Cameroon'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Cameroon, color='darkorange', alpha=0.1)

Canada = df[df['Entity'] == 'Canada'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Canada, color='darkorange', alpha=0.1)

Cape_Verde = df[df['Entity'] == 'Cape Verde'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Cape_Verde, color='darkorange', alpha=0.1)

CAR = df[df['Entity'] == 'Central African Republic'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = CAR, color='darkorange', alpha=0.1)

Chad = df[df['Entity'] == 'Chad'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Chad, color='darkorange', alpha=0.1)

Chile = df[df['Entity'] == 'Chile'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Chile, color='darkorange', alpha=0.1)

China = df[df['Entity'] == 'China'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = China, color='darkorange', alpha=0.1)

Colombia = df[df['Entity'] == 'Colombia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Colombia, color='darkorange', alpha=0.1)

Comoros = df[df['Entity'] == 'Comoros'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Comoros, color='darkorange', alpha=0.1)

Congo = df[df['Entity'] == 'Congo'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Congo, color='darkorange', alpha=0.1)

Costa_Rica = df[df['Entity'] == 'Costa Rica'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Costa_Rica, color='darkorange', alpha=0.1)

Cote_d_Ivoire = df[df['Entity'] == "Cote d'Ivoire"] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Cote_d_Ivoire, color='darkorange', alpha=0.1)

Croatia = df[df['Entity'] == 'Croatia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Croatia, color='darkorange', alpha=0.1)

Cuba = df[df['Entity'] == 'Cuba'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Cuba, color='darkorange', alpha=0.1)

Cyprus = df[df['Entity'] == 'Cyprus'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Cyprus, color='darkorange', alpha=0.1)

Czechia = df[df['Entity'] == 'Czechia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Czechia, color='darkorange', alpha=0.1)

Czechoslovakia = df[df['Entity'] == 'Czechoslovakia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Czechoslovakia, color='darkorange', alpha=0.1)

DRC = df[df['Entity'] == 'Democratic Republic of Congo'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = DRC, color='darkorange', alpha=0.1)

Denmark = df[df['Entity'] == 'Denmark'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Denmark, color='darkorange', alpha=0.1)

Djibouti = df[df['Entity'] == 'Djibouti'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Djibouti, color='darkorange', alpha=0.1)

Dominica = df[df['Entity'] == 'Dominica'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Dominica, color='darkorange', alpha=0.1)

Dominican_Republic = df[df['Entity'] == 'Dominican Republic'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Dominican_Republic, color='darkorange', alpha=0.1)

East_Germany = df[df['Entity'] == 'East Germany'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = East_Germany, color='darkorange', alpha=0.1)

East_Timor = df[df['Entity'] == 'East Timor'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = East_Timor, color='darkorange', alpha=0.1)

Ecuador = df[df['Entity'] == 'Ecuador'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Ecuador, color='darkorange', alpha=0.1)

Egypt = df[df['Entity'] == 'Egypt'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Egypt, color='darkorange', alpha=0.1)

Salvador = df[df['Entity'] == 'El Salvador'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Salvador, color='darkorange', alpha=0.1)

Equatorial_Guinea = df[df['Entity'] == 'Equatorial Guinea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Equatorial_Guinea, color='darkorange', alpha=0.1)

Eritrea = df[df['Entity'] == 'Eritrea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Eritrea, color='darkorange', alpha=0.1)

Estonia = df[df['Entity'] == 'Estonia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Estonia, color='darkorange', alpha=0.1)

Eswatini = df[df['Entity'] == 'Eswatini'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Eswatini, color='darkorange', alpha=0.1)

Ethiopia = df[df['Entity'] == 'Ethiopia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Ethiopia, color='darkorange', alpha=0.1)

Fiji = df[df['Entity'] == 'Fiji'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Fiji, color='darkorange', alpha=0.1)

Finland = df[df['Entity'] == 'Finland'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Finland, color='darkorange', alpha=0.1)

France = df[df['Entity'] == 'France'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = France, color='darkorange', alpha=0.1)

Gabon = df[df['Entity'] == 'Gabon'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Gabon, color='darkorange', alpha=0.1)

Gambia = df[df['Entity'] == 'Gambia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Gambia, color='darkorange', alpha=0.1)

Georgia = df[df['Entity'] == 'Georgia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Georgia, color='darkorange', alpha=0.1)

Germany = df[df['Entity'] == 'Germany'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Germany, color='darkorange', alpha=0.1)

Ghana = df[df['Entity'] == 'Ghana'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Ghana, color='darkorange', alpha=0.1)

Greece = df[df['Entity'] == 'Greece'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Greece, color='darkorange', alpha=0.1)

Grenada = df[df['Entity'] == 'Grenada'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Grenada, color='darkorange', alpha=0.1)

Guatemala = df[df['Entity'] == 'Guatemala'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Guatemala, color='darkorange', alpha=0.1)

Guinea = df[df['Entity'] == 'Guinea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Guinea, color='darkorange', alpha=0.1)

Guinea_Bissau = df[df['Entity'] == 'Guinea-Bissau'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Guinea_Bissau, color='darkorange', alpha=0.1)

Guyana = df[df['Entity'] == 'Guyana'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Guyana, color='darkorange', alpha=0.1)

Haiti = df[df['Entity'] == 'Haiti'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Haiti, color='darkorange', alpha=0.1)

Hanover = df[df['Entity'] == 'Hanover'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Hanover, color='darkorange', alpha=0.1)

Hesse_Electoral = df[df['Entity'] == 'Hesse Electoral'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Hesse_Electoral, color='darkorange', alpha=0.1)

Hesse_Grand_Ducal = df[df['Entity'] == 'Hesse Grand Ducal'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Hesse_Grand_Ducal, color='darkorange', alpha=0.1)

Honduras = df[df['Entity'] == 'Honduras'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Honduras, color='darkorange', alpha=0.1)

Hungary = df[df['Entity'] == 'Hungary'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Hungary, color='darkorange', alpha=0.1)

Iceland = df[df['Entity'] == 'Iceland'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Iceland, color='darkorange', alpha=0.1)

India = df[df['Entity'] == 'India'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = India, color='darkorange', alpha=0.1)

Indonesia = df[df['Entity'] == 'Indonesia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Indonesia, color='darkorange', alpha=0.1)

Iran = df[df['Entity'] == 'Iran'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Iran, color='darkorange', alpha=0.1)

Iraq = df[df['Entity'] == 'Iraq'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Iraq, color='red', alpha=0.5)

Ireland = df[df['Entity'] == 'Ireland'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Ireland, color='darkorange', alpha=0.1)

Israel = df[df['Entity'] == 'Israel']
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Israel, color='blue', alpha=0.5)

Italy = df[df['Entity'] == 'Italy'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Italy, color='darkorange', alpha=0.1)

Jamaica = df[df['Entity'] == 'Jamaica'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Jamaica, color='darkorange', alpha=0.1)

Japan = df[df['Entity'] == 'Japan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Japan, color='darkorange', alpha=0.1)

Jordan = df[df['Entity'] == 'Jordan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Jordan, color='darkorange', alpha=0.1)

Kazakhstan = df[df['Entity'] == 'Kazakhstan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Kazakhstan, color='darkorange', alpha=0.1)

Kenya = df[df['Entity'] == 'Kenya'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Kenya, color='darkorange', alpha=0.1)

Kiribati = df[df['Entity'] == 'Kiribati'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Kiribati, color='darkorange', alpha=0.1)

Korea = df[df['Entity'] == 'Korea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Korea, color='darkorange', alpha=0.1)

Kosovo = df[df['Entity'] == 'Kosovo'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Kosovo, color='darkorange', alpha=0.1)

Kuwait = df[df['Entity'] == 'Kuwait'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Kuwait, color='darkorange', alpha=0.1)

Kyrgyzstan = df[df['Entity'] == 'Kyrgyzstan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Kyrgyzstan, color='darkorange', alpha=0.1)

Laos = df[df['Entity'] == 'Laos'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Laos, color='darkorange', alpha=0.1)

Latvia = df[df['Entity'] == 'Latvia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Latvia, color='darkorange', alpha=0.1)

Lebanon = df[df['Entity'] == 'Lebanon'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Lebanon, color='darkorange', alpha=0.1)

Lesotho = df[df['Entity'] == 'Lesotho'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Lesotho, color='darkorange', alpha=0.1)

Liberia = df[df['Entity'] == 'Liberia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Liberia, color='darkorange', alpha=0.1)

Libya = df[df['Entity'] == 'Libya'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Libya, color='darkorange', alpha=0.1)

Liechtenstein = df[df['Entity'] == 'Liechtenstein'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Liechtenstein, color='darkorange', alpha=0.1)

Lithuania = df[df['Entity'] == 'Lithuania'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Lithuania, color='darkorange', alpha=0.1)

Luxembourg = df[df['Entity'] == 'Luxembourg'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Luxembourg, color='darkorange', alpha=0.1)

Madagascar = df[df['Entity'] == 'Madagascar'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Madagascar, color='darkorange', alpha=0.1)

Malawi = df[df['Entity'] == 'Malawi'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Malawi, color='darkorange', alpha=0.1)

Malaysia = df[df['Entity'] == 'Malaysia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Malaysia, color='darkorange', alpha=0.1)

Maldives = df[df['Entity'] == 'Maldives'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Maldives, color='darkorange', alpha=0.1)

Mali = df[df['Entity'] == 'Mali'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mali, color='darkorange', alpha=0.1)

Malta = df[df['Entity'] == 'Malta'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Malta, color='darkorange', alpha=0.1)

Marshall_Islands = df[df['Entity'] == 'Marshall Islands'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Marshall_Islands, color='darkorange', alpha=0.1)

Mauritania = df[df['Entity'] == 'Mauritania'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mauritania, color='darkorange', alpha=0.1)

Mauritius = df[df['Entity'] == 'Mauritius'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mauritius, color='darkorange', alpha=0.1)

Mecklenburg_Schwerin = df[df['Entity'] == 'Mecklenburg Schwerin'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mecklenburg_Schwerin, color='darkorange', alpha=0.1)

Mexico = df[df['Entity'] == 'Mexico'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mexico, color='darkorange', alpha=0.1)

Micronesia = df[df['Entity'] == 'Micronesia (country)'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Micronesia, color='darkorange', alpha=0.1)

Modena = df[df['Entity'] == 'Modena'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Modena, color='darkorange', alpha=0.1)

Moldova = df[df['Entity'] == 'Moldova'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Moldova, color='darkorange', alpha=0.1)

Monaco = df[df['Entity'] == 'Monaco'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Monaco, color='darkorange', alpha=0.1)

Mongolia = df[df['Entity'] == 'Mongolia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mongolia, color='darkorange', alpha=0.1)

Montenegro = df[df['Entity'] == 'Montenegro'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Montenegro, color='darkorange', alpha=0.1)

Morocco = df[df['Entity'] == 'Morocco'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Morocco, color='darkorange', alpha=0.1)

Mozambique = df[df['Entity'] == 'Mozambique'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Mozambique, color='darkorange', alpha=0.1)

Myanmar = df[df['Entity'] == 'Myanmar'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Myanmar, color='darkorange', alpha=0.1)

Namibia = df[df['Entity'] == 'Namibia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Namibia, color='darkorange', alpha=0.1)

Nauru = df[df['Entity'] == 'Nauru'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Nauru, color='darkorange', alpha=0.1)

Nepal = df[df['Entity'] == 'Nepal'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Nepal, color='darkorange', alpha=0.1)

Netherlands = df[df['Entity'] == 'Netherlands'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Netherlands, color='darkorange', alpha=0.1)

New_Zealand = df[df['Entity'] == 'New Zealand'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = New_Zealand, color='darkorange', alpha=0.1)

Nicaragua = df[df['Entity'] == 'Nicaragua'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Nicaragua, color='darkorange', alpha=0.1)

Niger = df[df['Entity'] == 'Niger'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Niger, color='darkorange', alpha=0.1)

Nigeria = df[df['Entity'] == 'Nigeria'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Nigeria, color='darkorange', alpha=0.1)

North_Korea = df[df['Entity'] == 'North Korea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = North_Korea, color='gold', alpha=0.5)

North_Macedonia = df[df['Entity'] == 'North Macedonia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = North_Macedonia, color='darkorange', alpha=0.1)

Norway = df[df['Entity'] == 'Norway'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Norway, color='darkorange', alpha=0.1)

Oman = df[df['Entity'] == 'Oman'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Oman, color='darkorange', alpha=0.1)

Pakistan = df[df['Entity'] == 'Pakistan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Pakistan, color='darkorange', alpha=0.1)

Palau = df[df['Entity'] == 'Palau'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Palau, color='darkorange', alpha=0.1)

Panama = df[df['Entity'] == 'Panama'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Panama, color='darkorange', alpha=0.1)

Papua_New_Guinea = df[df['Entity'] == 'Papua New Guinea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Papua_New_Guinea, color='darkorange', alpha=0.1)

Paraguay = df[df['Entity'] == 'Paraguay'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Paraguay, color='darkorange', alpha=0.1)

Parma = df[df['Entity'] == 'Parma'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Parma, color='darkorange', alpha=0.1)

Peru = df[df['Entity'] == 'Peru'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Peru, color='darkorange', alpha=0.1)

Philippines = df[df['Entity'] == 'Philippines'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Philippines, color='darkorange', alpha=0.1)

Poland = df[df['Entity'] == 'Poland'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Poland, color='darkorange', alpha=0.1)

Portugal = df[df['Entity'] == 'Portugal'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Portugal, color='darkorange', alpha=0.1)

Qatar = df[df['Entity'] == 'Qatar'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Qatar, color='darkorange', alpha=0.1)

Vietnam = df[df['Entity'] == 'Republic of Vietnam'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Vietnam, color='darkorange', alpha=0.1)

Romania = df[df['Entity'] == 'Romania'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Romania, color='darkorange', alpha=0.1)

Russia = df[df['Entity'] == 'Russia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Russia, color='green', alpha=0.5)

Rwanda = df[df['Entity'] == 'Rwanda'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Rwanda, color='darkorange', alpha=0.1)

Saint_Kitts_Nevis = df[df['Entity'] == 'Saint Kitts and Nevis'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Saint_Kitts_Nevis, color='darkorange', alpha=0.1)

Saint_Lucia = df[df['Entity'] == 'Saint Lucia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Saint_Lucia, color='darkorange', alpha=0.1)

Saint_Vincent_the_Grenadines = df[df['Entity'] == 'Saint Vincent and the Grenadines'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Saint_Vincent_the_Grenadines, color='darkorange', alpha=0.1)

Samoa = df[df['Entity'] == 'Samoa'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Samoa, color='darkorange', alpha=0.1)

San_Marino = df[df['Entity'] == 'San Marino'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = San_Marino, color='darkorange', alpha=0.1)

Sao_Tome_Principe = df[df['Entity'] == 'Sao Tome and Principe'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Sao_Tome_Principe, color='darkorange', alpha=0.1)

KSA = df[df['Entity'] == 'Saudi Arabia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = KSA, color='darkorange', alpha=0.1)

Saxony = df[df['Entity'] == 'Saxony'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Saxony, color='darkorange', alpha=0.1)

Senegal = df[df['Entity'] == 'Senegal'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Senegal, color='darkorange', alpha=0.1)

Serbia = df[df['Entity'] == 'Serbia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Serbia, color='darkorange', alpha=0.1)

Seychelles = df[df['Entity'] == 'Seychelles'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Seychelles, color='darkorange', alpha=0.1)

Sierra_Leone = df[df['Entity'] == 'Sierra Leone'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Sierra_Leone, color='darkorange', alpha=0.1)

Singapore = df[df['Entity'] == 'Singapore'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Singapore, color='darkorange', alpha=0.1)

Slovakia = df[df['Entity'] == 'Slovakia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Slovakia, color='darkorange', alpha=0.1)

Slovenia = df[df['Entity'] == 'Slovenia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Slovenia, color='darkorange', alpha=0.1)

Solomon_Islands = df[df['Entity'] == 'Solomon Islands'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Solomon_Islands, color='darkorange', alpha=0.1)

Somalia = df[df['Entity'] == 'Somalia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Somalia, color='darkorange', alpha=0.1)

South_Africa = df[df['Entity'] == 'South Africa'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = South_Africa, color='darkorange', alpha=0.1)

South_Korea = df[df['Entity'] == 'South Korea'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = South_Korea, color='darkorange', alpha=0.1)

South_Sudan = df[df['Entity'] == 'South Sudan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = South_Sudan, color='darkorange', alpha=0.1)

Spain = df[df['Entity'] == 'Spain'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Spain, color='darkorange', alpha=0.1)

Sri_Lanka = df[df['Entity'] == 'Sri Lanka'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Sri_Lanka, color='darkorange', alpha=0.1)

Sudan = df[df['Entity'] == 'Sudan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Sudan, color='darkorange', alpha=0.1)

Suriname = df[df['Entity'] == 'Suriname'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Suriname, color='darkorange', alpha=0.1)

Sweden = df[df['Entity'] == 'Sweden'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Sweden, color='darkorange', alpha=0.1)

Switzerland = df[df['Entity'] == 'Switzerland'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Switzerland, color='darkorange', alpha=0.1)

Syria = df[df['Entity'] == 'Syria'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Syria, color='darkorange', alpha=0.1)

Taiwan = df[df['Entity'] == 'Taiwan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Taiwan, color='darkorange', alpha=0.1)

Tajikistan = df[df['Entity'] == 'Tajikistan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Tajikistan, color='darkorange', alpha=0.1)

Tanzania = df[df['Entity'] == 'Tanzania'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Tanzania, color='darkorange', alpha=0.1)

Thailand = df[df['Entity'] == 'Thailand'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Thailand, color='darkorange', alpha=0.1)

Togo = df[df['Entity'] == 'Togo'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Togo, color='darkorange', alpha=0.1)

Tonga = df[df['Entity'] == 'Tonga'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Tonga, color='darkorange', alpha=0.1)

Trinidad_Tobago = df[df['Entity'] == 'Trinidad and Tobago'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Trinidad_Tobago, color='darkorange', alpha=0.1)

Tunisia = df[df['Entity'] == 'Tunisia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Tunisia, color='darkorange', alpha=0.1)

Turkey = df[df['Entity'] == 'Turkey'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Turkey, color='darkorange', alpha=0.1)

Turkmenistan = df[df['Entity'] == 'Turkmenistan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Turkmenistan, color='darkorange', alpha=0.1)

Tuscany = df[df['Entity'] == 'Tuscany'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Tuscany, color='darkorange', alpha=0.1)

Tuvalu = df[df['Entity'] == 'Tuvalu'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Tuvalu, color='darkorange', alpha=0.1)

Two_Sicilies = df[df['Entity'] == 'Two Sicilies'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Two_Sicilies, color='darkorange', alpha=0.1)

Uganda = df[df['Entity'] == 'Uganda'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Uganda, color='darkorange', alpha=0.1)

Ukraine = df[df['Entity'] == 'Ukraine'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Ukraine, color='darkorange', alpha=0.1)

UAE = df[df['Entity'] == 'United Arab Emirates'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = UAE, color='darkorange', alpha=0.1)

UK = df[df['Entity'] == 'United Kingdom'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = UK, color='darkorange', alpha=0.1)

US = df[df['Entity'] == 'United States'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = US, color='purple', alpha=0.5)

Uruguay = df[df['Entity'] == 'Uruguay'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Uruguay, color='darkorange', alpha=0.1)

Uzbekistan = df[df['Entity'] == 'Uzbekistan'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Uzbekistan, color='darkorange', alpha=0.1)

Vanuatu = df[df['Entity'] == 'Vanuatu'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Vanuatu, color='darkorange', alpha=0.1)

Vatican = df[df['Entity'] == 'Vatican'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Vatican, color='darkorange', alpha=0.1)

Venezuela = df[df['Entity'] == 'Venezuela'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Venezuela, color='darkorange', alpha=0.1)

Vietnam = df[df['Entity'] == 'Vietnam'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Vietnam, color='darkorange', alpha=0.1)

West_Germany = df[df['Entity'] == 'West Germany'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = West_Germany, color='darkorange', alpha=0.1)

Wuerttemburg = df[df['Entity'] == 'Wuerttemburg'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Wuerttemburg, color='darkorange', alpha=0.1)

Yemen = df[df['Entity'] == 'Yemen'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Yemen, color='darkorange', alpha=0.1)

YAR = df[df['Entity'] == 'Yemen Arab Republic'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = YAR, color='darkorange', alpha=0.1)

YPR = df[df['Entity'] == "Yemen People's Republic"] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = YPR, color='darkorange', alpha=0.1)

Zambia = df[df['Entity'] == 'Zambia'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Zambia, color='darkorange', alpha=0.1)

Zanzibar = df[df['Entity'] == 'Zanzibar'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Zanzibar, color='darkorange', alpha=0.1)

Zimbabwe = df[df['Entity'] == 'Zimbabwe'] 
sns.lineplot(x = 'Year', y= 'military_personnel_share', data = Zimbabwe, color='darkorange', alpha=0.1)


# Extracting relevant info from the dataset to plot

max_is = Israel['military_personnel_share'].where(df['Year'] >= 1950).max()
max_ir = Iraq['military_personnel_share'].where(df['Year'] >= 1950).max()
last_value_N_korea = North_Korea['military_personnel_share'].iloc[-1]
max_ru = Russia['military_personnel_share'].where(df['Year'] >= 1950).max()
max_us = US['military_personnel_share'].where(df['Year'] >= 1950).max()

print("The maximum value of Israel is", np.round(max_is,1))
print("The maximum value of Iraq is", np.round(max_ir,1))
print("The last value of N. Korea is", np.round(last_value_N_korea,1))
print("The maximum value of Russia is", np.round(max_ru,1))
print("The maximum value of USA is", np.round(max_us,1))


# Customizing the plot

plt.text(1951, 6.2, "Israel 6.2%", size='medium', color='blue', fontweight='light')
plt.text(1991, 7.7, "Iraq 7.7%", size='medium', color='red', alpha=0.7, fontweight='light')
plt.text(2006, 4.9, "N. Korea 4.7%", size='medium', color='gold', alpha=0.8, fontweight='light')
plt.text(1951, 3.2, "Russia 3.1%", size='medium', color='green', alpha=0.8, fontweight='light')
plt.text(1951, 2.4, "US 2.3%", size='medium', color='purple', alpha=0.8, fontweight='light')

plt.xlabel("Year", fontsize=15)
plt.ylabel("Soldiers as % of population", fontsize=15)
plt.title("Military as a % of total population", fontsize=18)

plt.text(2003, -1.5, "Source: Our World in Data", size='small', color='black', fontweight='light')


plt.savefig('military.pdf')
plt.show()