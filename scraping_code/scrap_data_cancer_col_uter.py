from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

# Configurer Selenium
driver = webdriver.Chrome()  # Assure-toi d'avoir installé chromedriver

# Ouvrir la page avec le tableau
url = "https://gco.iarc.fr/today/en/dataviz/tables?mode=population&cancers=23&sexes=2&key=crude_rate&age_end=17&multiple_cancers=0&populations=100_104_108_112_116_12_120_124_132_140_144_148_152_160_170_174_178_180_188_191_192_196_203_204_208_214_218_222_226_231_232_233_24_242_246_250_254_258_262_266_268_270_275_276_288_300_31_312_316_32_320_324_328_332_340_348_352_356_36_360_364_368_372_376_380_384_388_392_398_4_40_400_404_408_410_414_417_418_422_426_428_430_434_44_440_442_450_454_458_462_466_470_474_478_48_480_484_496_498_499_50_504_508_51_512_516_52_524_528_540_548_554_558_56_562_566_578_586_591_598_600_604_608_616_620_624_626_630_634_638_64_642_643_646_662_678_68_682_686_688_694_70_702_703_704_705_706_710_716_72_724_728_729_740_748_752_756_76_760_762_764_768_780_784_788_792_795_8_800_804_807_818_826_834_84_840_854_858_860_862_882_887_894_90_96"
driver.get(url)

# Attendre le chargement de la page
time.sleep(5)

# Localiser le tableau
table = driver.find_element(By.TAG_NAME, "table")

# Récupérer les en-têtes (noms des colonnes)
headers = table.find_elements(By.TAG_NAME, "th")
column_names = [header.text for header in headers]  # Extraire le texte des colonnes

# Récupérer les lignes du tableau (hors en-têtes)
rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Sauter la première ligne car elle contient les en-têtes

# Extraire les données
data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data.append([col.text for col in cols])

# Transformer en DataFrame avec les colonnes
df = pd.DataFrame(data, columns=column_names)

# Afficher les données
print(df)  # Affiche le tableau dans la console

# Sauvegarder dans un fichier CSV avec les colonnes
df.to_csv("data_cancer_cil_uter.csv", index=False)

# Afficher le chemin complet du fichier
print("Fichier enregistré à :", os.path.abspath("data_cancer_cil_uter.csv"))

# Fermer le navigateur
driver.quit()
