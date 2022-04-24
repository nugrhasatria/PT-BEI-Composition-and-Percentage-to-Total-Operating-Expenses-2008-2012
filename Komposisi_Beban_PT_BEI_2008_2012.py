import matplotlib.pyplot as plt

                    # Pie Chart for Composition of Operating Expense
                                  # PT BEI 2008-2012

# YOY 2008
        # Nama Akun
labels8 = 'Gaji\ndan Tunjangan', 'Pengembangan\nPerdagangan', 'Penyusutan', 'Umum\ndan Administrasi', 'Sewa'
        # Nilai Akun
values8 = [49.15, 16.82, 5.78, 19.15, 9.22]
        # Warna Akun
colors8 = ['BurlyWood', 'teal', 'sienna', 'tomato', 'LightSalmon']
        # Explode 
explode8 = (0, 0.1, 0.0, 0, 0)

        # Figure
fig, ax = plt.subplots()
ax.pie(values8, labels = labels8,
          colors = colors8, 
          autopct='%.0f%%', 
          explode = explode8, 
          shadow = False)

        # Checkout Plot    
ax.set_title('Komposisi Beban Usaha PT BEI \n Tahun 2008')
plt.show()

# YOY 2009
        # Nama Akun
labels9 = 'Gaji\ndan Tunjangan', 'Pengembangan\nPerdagangan', 'Penyusutan', 'Umum\ndan Administrasi', 'Sewa'
        # Nilai Akun
values9 = [47.11, 16.82, 8.07, 19.56, 8.43]
        # Warna Akun
colors9 = ['BurlyWood', 'teal', 'sienna', 'tomato', 'LightSalmon']
        # Explode 
explode9 = (0, 0.1, 0.0, 0, 0)

        # Figure
fig, ax = plt.subplots()
ax.pie(values9, labels = labels9, 
          colors = colors9, 
          autopct='%.0f%%', 
          explode = explode9, 
          shadow = False)

        # Checkout Plot    
ax.set_title('Komposisi Beban Usaha PT BEI \n Tahun 2009')
plt.show()

# YOY 2010
        # Nama Akun
labels10 = 'Gaji\ndan Tunjangan', 'Pengembangan\nPerdagangan', 'Penyusutan', 'Umum\ndan Administrasi', 'Sewa', 'Perbaikan\ndan Pemeliharaan', 'Transportasi\ndan Telekomunikasi', 'Konsultan'
        # Nilai Akun
values10 = [51.20, 14.81, 9.29, 8.67, 6.15, 4.55, 2.63, 2.71]
        # Warna Akun
colors10 = ['BurlyWood', 'teal', 'sienna', 'tomato', 'LightSalmon', 'tan', 'Olive', 'oliveDrab']
        # Explode 
explode10 = (0, 0.1, 0.0, 0, 0, 0, 0, 0)

        # Figure
fig, ax = plt.subplots()
ax.pie(values10, labels = labels10, 
          colors = colors10, 
          autopct='%.0f%%', 
          explode = explode10, 
          shadow = False)

        # Checkout Plot
ax.set_title('Komposisi Beban Usaha PT BEI \n Tahun 2010')
plt.show()

# YOY 2011
        # Nama Akun
labels11 = 'Gaji\ndan Tunjangan', 'Pengembangan\nPerdagangan', 'Penyusutan', 'Umum\ndan Administrasi', 'Sewa', 'Perbaikan\ndan Pemeliharaan', 'Transportasi\ndan Telekomunikasi', 'Konsultan', 'Lain-lain'
        # Nilai Akun
values11 = [46.72, 16.35, 11.89, 10.13, 4.82, 3.41, 3.40, 2.83, 0.45]
        # Warna Akun
colors11 = ['BurlyWood', 'teal', 'sienna', 'tomato', 'LightSalmon', 'tan', 'Olive', 'oliveDrab', 'PapayaWhip']
        # Explode 
explode11 = (0, 0.1, 0.0, 0, 0, 0, 0, 0 ,0)

        # Figure
fig, ax = plt.subplots()
ax.pie(values11, labels = labels11, 
          colors = colors11, 
          autopct='%.0f%%', 
          explode = explode11, 
          shadow = False)

        # Checkout Plot    
ax.set_title('Komposisi Beban Usaha PT BEI \n Tahun 2011')
plt.show()

# YOY 2012
        # Nama Akun
labels12 = 'Gaji\ndan Tunjangan', 'Pengembangan\nPerdagangan', 'Penyusutan', 'Umum\ndan Administrasi', 'Sewa', 'Perbaikan\ndan Pemeliharaan', 'Transportasi\ndan Telekomunikasi', 'Konsultan', 'Lain-lain'
        # Nilai Akun
values12 = [44.20, 14.57, 16.59, 8.16, 4.48, 6.40, 2.88, 2.31, 0.41]
        # Warna Akun
colors12 = ['BurlyWood', 'teal', 'sienna', 'tomato', 'LightSalmon', 'tan', 'Olive', 'oliveDrab', 'PapayaWhip']
        # Explode 
explode12 = (0, 0.1, 0.0, 0, 0, 0, 0, 0 ,0)

        # Figure
fig, ax = plt.subplots()
ax.pie(values12, labels = labels12, 
          colors = colors12, 
          autopct='%.0f%%', 
          explode = explode12, 
          shadow = False)

        # Checkout Plot    
ax.set_title('Komposisi Beban Usaha PT BEI \n Tahun 2012')
plt.show()