import re
from string import join

def kelime2bin(kelime):
	return "".join([str(int(unlu_mu(h))) for h in kelime])
	
def unlu_mu(harf):
	return harf in "aeiou"

def kural1(kelime, basl=0):
	"""\
	iki unlu arasinda bir unsuzun bulundugu ardisillikta 
	unsuzun indisini dondurur.

    Algoritma:
	1. gelen kelimeyi 1 ('unlu'), 0 ('unsuz') dizisine cevir
	2. bu dizide '101' ('unlu - unsuz - unlu') paternini ara
	3. eger yoksa '-1' varsa unsuzun indisini dondur

	>>> kural1('ankara')
	4
	>>> kural1("samsunspor")
	-1
	"""

	kelime = kelime[basl:]

	kb = kelime2bin(kelime)
	ind = kb.find("101")
	if ind > -1:
		ind += basl + 1

	return ind

def kural2(kelime, basl=0):
	"""\
	en az bir unluyu takip eden iki veya daha fazla unsuzden
	sonuncusunun indisini dondurur.

	Algoritma
	1. gelen kelimeyi 1 ('unlu'), 0 ('unsuz') dizisine cevir
	2. "1+0{2,0}" duzenli ifadesiyle tarama yap
	3. bulamazsan "-1" dondur

	>>> kural2("ussssu")
	4
	>>> kural2("usssu")
	3
	>>> kural2("ussu")
	2
	>>> kural2("usu")
	-1
	>>> kural2("tren")
	-1
	"""

	kelime = kelime[basl:]

	kb = kelime2bin(kelime)
	m = re.search("1+0{2,}", kb)
	if m == None:
		return -1
	else:
		return basl + m.end() - 1

# main
while True:	
	kelime = raw_input("kelime girin (sonlandirmak icin 'son' yazin): ")
	if kelime == "son" or kelime == "":
		exit()

	print kelime
	heceler = []
	
	while True:
		k1 = kural1(kelime)
		k2 = kural2(kelime)
		
		if k1 == -1 and k2 == -1:
			heceler.append(kelime)
			break
		elif k1 != -1 and k2 != -1:
			k = min(k1, k2)
		else:
			k = max(k1, k2)
		
		hece = kelime[:k]
		heceler.append(hece)
		
		kelime = kelime[k:]
	
	print join(heceler, " - ")
	
