# Market Sentiment for SkinCare Product

## Intro
Dalam membuat keputusan untuk merilis produk baru, perusahaan akan mempertimbangkan strategi untuk itu. 
Salah satunya yaitu memiliki penjadwalan yang matang dan mencari titik lemah dari kategori produk yang diproduksi sebelumnya*.
<br>
Dari permasalahan tersebut, dalam project ini akan menjawab penjadwalan dan menemukan titik lemah tersebut. Atau bisa disimpulkan sebagai berikut.
1. Menemukan sentimen pasar terhadap produk skincare sebelumnya yang kemudian bisa menjadi pertimbangan apakah produk yang akan dirilis bisa segera diluncurkan/ditahan.
2. Memunculkan word frequency dari sentimen positif/negatif terhadap produk lalu yang kemudian bisa menjadi pertimbangan untuk improvisasi produk kedepannya.

*Pada project ini, kategori skincare difokuskan pada kategori night cream (krim malam).

## Dataset
Dataset yang digunakan adalah hasil scraping yang diambil dari website femaledaily.com pada kategori skincare dari berbagai macam produk sebanyak 7875 baris pada 18 September 2020. <br>
Feature yang diambil adalah sebagai berikut.
1. **Username** - Nama pengguna
2. **SkinCond_Age** - Kondisi wajah & umur pengguna
4. **Recommend** - Apakah pengguna merekomendasikan produk/tidak
5. **PostDate** - Tanggal ulasan diunggah oleh pengguna
6. **Review** - Isi ulasan dari produk
7. **Rating** - Rating produk yang diberikan oleh pengguna, yang kemudian akan dijadikan sebagai target sentimen (1-2: Negatif; 3: Neutral; 4-5: Positive)

![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/dataset.JPG?raw=true)

## Exploratory Data
![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/visdat1.png?raw=true)

**Insight:** Dari dataset produk yang banyak diulas yaitu dari brand Wardah dan diikuti oleh brand The Body Shop

![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/visdat3.png?raw=true)

**Insight:** Dari grafik menunjukkan bahwa kebanyakan pengulas berada di umur 19-24. Atau bisa disimpulkan bahwa pengguna krim malam terbanyak berada di umur 19-24 dan diikuti oleh range umur 25-29.

![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/visdat4.png?raw=true)

**Insight:** Disimpulkan bahwa dataset timpang karena data tidak seimbang antara ulasan positif-netral-negatif.

## Text Preprocessing
Pada text preprocessing, salah satu langkah yang dilakukan yaitu text cleaning. Berikut hasil text cleaning yang dimunculkan oleh wordcloud.
![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/negative_review.png?raw=true)
![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/positive_review.png?raw=true)

## Modelling
Model final yang digunakan adalah logistic regression dengan pengurangan feature dari 3000+ menjadi 100 feature.
Dengan nilai f1 negatif: 37%, netral: 22%, positif: 83% <br>
![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/model_score.png?raw=true)<br>
![alt text](https://github.com/fdhanh/Sentiment_Analysis_SkinCare_Product/blob/main/img/metric.png?raw=true)

Model bisa dikatakan bias karena data timpang (lebih banyak di sentimen positif, jadi banyak false positive yang masuk ke sentimen positif) <br>
Untuk treatment selanjutnya akan digunakan deep learning untuk memperbaiki akurasi dari model.
