**Zadání:** <br>
Napište program, který načte historická data o průměrných denních průtocích a spočítá roční a sedmidení průměry. 

Bonusové úkoly:
* program bude vypisovat do konzole minimální a maximální průtok
* program zkontroluje, zda se v datech objeví nulový nebo záporný průtok a nebo zda nějaký den v záznamu chybí.
* odevzdejte úkol přes GitHub.

**Vypracování:**<br>
Program nejprve načte data a definuje základní operace a základní proměnné. Poté prochází všechny řádky v souboru a pro každý řádek je definováno datum a průměrný průtok. V případě, že průtok není kladný, program na to uživatele upozorní. Následně jsou vypočítány sedmidenní průměry průtoků a výsledek je spolu s datem prvního dne průběžně zapisován do souboru 'vystup_7dni.csv'. Je taktéž počítán průměrný průtok pro daný rok. V případě, že daný rok skončí (tj. rok v datumu je o 1 větší), program spočítá celkový průměrný průtok a spolu s datem prvního záznamu v onom roce jej průběžně zapisuje do souboru 'vystup_rok.csv'. Dále je zjišťován minimální a maximální průtok a také dny, kdy byly naměřeny. Na závěr jsou tyto údaje vypsány do konzole. 

Pozn.: U vstupních dat je použit experimentální vzorek pojmenovaný jako 'vstup_test.csv'. Spolu s touto testovací sadou je na GitHubu umístěná také původní sada 'vstup.csv'. 