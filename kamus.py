meme_dict = {
            'LOL': 'tanggapan terhadap sesuatu yang lucu',
            'CRINGE': 'sesuatu yang aneh atau memalukan',
            'ROFL': 'tanggapan terhadap lelucon',
            'SHEESH': 'sedikit ketidaksetujuan',
            'CREEPY': 'menakutkan, tidak menyenangkan',
            'AGGRO': 'untuk menjadi agresif/marah',
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print('ARTINYA')
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('MAAF KATA TIDAK TERSEDIA')
