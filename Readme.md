# Distirbution Generator

## Ne Yapıyor:

- Verilmiş olan verisetini öncelikle standardize ediyor.

- Standardize edilmiş verisetini daha önceden verilmiş olsaılık dağılımları ile fit ediyor. Böylelikle fit edilen olasılık dağılım ile verinin sıfıra göre 1. momentini ve ortalamaya göre 2. momentini , ayrıca eğer varsa hiperparametreleri için en olası değeri buluyor. Fit ederken maximum likelihood ile optimize ediliyor.

- Bulunan olası en iyi dağılım parametreleri ile oluşturulan olasılık dağılımın CDF i için Kolmogrov-Smirnov testi ile o fit edilen dağılıma uygunluğu test ediliyor. 

- H0: verilerin dağılımı,teorik dağılımdan anlamlı bir şekilde fark yoktur.

  H1: verilerin dağılımı , teorik dağılımdan anlamlı bir şekilde farklıdır.

- Bütün dağılımlar için Kolmogrov-Smirnov testini uyguladıktan sonra en yüksek P-value değerine sahip dağılımı alarak istenilen sayıda o dağılıma uyan veri üretiyor.

- Veri ürettikten sonra Standardize çıktıları inverse ediyor ve çıktı olarak üretilen dataları veriyor.

- Eğer istenirse integer sayı , çıktı verilmesi ve en iyi fit eden dağılımların gösterilmesi gibi opsiyonlar argüman olarak eklenebilir.



## Parametreler:

- data = dağılımının tespit edileceği veriseti ( numpy array) 
- size = dağılımdan üretilicek veri sayısı (integer)
- dist_list = sınanmak istenen dağılımların listesi (list)
- verbose = fit ederken alınacak log çıktı (default False)
- print_limit = en iyi fit eden dağılımlar ve çıktıları (default 10) (integer)
- int_type = dağılımdan üretilecek verinin tamsayı olması(default False)



## Uyarı:

- 1000 veriden sonra KS testi için , KS hesaplanmış değerleri yetersizliğinden dolayı H0 hipotezi red ediliyor.

