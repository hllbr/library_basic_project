import sqlite3

con =sqlite3.connect("kütüphane.db")

cursor =con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def veri_ekleme():
 	cursor.execute("INSERT INTO kitaplık Values('İstanbul Hatırası','Ahmet Ümit','EVEREST YAYINCILIK',561)")
 	con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
	cursor.execute("INSERT INTO kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
	con.commit()
#input("isim : ")
#yazar=input("yazar : ")
#yayınevi =input("yayınevi : ")
#sayfa_sayısı=int(input("sayfa sayısı : "))
def verileri_al():
	cursor.execute("SELECT * FROM  kitaplık")
	liste =cursor.fetchall()
	print("kitaplık tablosunun bilgileri .... ")
	for i in liste:
	    print(i)    
def verileri_al2():
	cursor.execute("SELECT İsim,Yazar FROM kitaplık")
	liste = cursor.fetchall()
	for i in liste:
		print(i)
def  verileri_al3(yayınevi):
	cursor.execute("SELECT * FROM kitaplık WHERE Yayınevi = ?",(yayınevi,))
	liste = cursor.fetchall()
	print("kitaplık tablosunun bilgileri ....")
	for i in liste:
		print(i)
def verileri_güncelle(eski_yayınevi,yeni_yayınevi):
	cursor.execute("UPDATE kitaplık SET Yayınevi = ? WHERE Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
	con.commit()
def verileri_sil(yazar):
	cursor.execute("DELETE FROM kitaplık WHERE Yazar = ?",(yazar,))
	con.commit()

verileri_sil("Ahmet Ümit")
verileri_al()


con.close()
