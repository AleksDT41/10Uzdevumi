from collections import Counter
import string

# Ievades teksts
teksts = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. 
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

# 1. Tīra tekstu no pieturzīmēm un pārvērš visus burtus mazajos
teksts = teksts.lower().translate(str.maketrans("", "", string.punctuation))

# 2. Pārvērš tekstu par vārdu sarakstu
vardi = teksts.split()

# 3. Nosaka vārdu biežumu
vardu_biezums = Counter(vardi)

# 4. Izvada rezultātu
print("Vārdu biežuma analīze:")
for vards, skaits in vardu_biezums.items():
    print(f"{vards}: {skaits}")

