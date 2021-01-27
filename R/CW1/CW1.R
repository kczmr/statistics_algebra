# Zad 1
data <- read.csv('napoje_po_reklamie.csv', fileEncoding = 'UTF-8-BOM', sep=';')
data

print(min(data['pepsi']))
print(max(data['fanta']))
print(mean(data$okocim))

# Zad 2

pepsi <- as.vector(data$pepsi)
fanta <- as.vector(data$fanta)

print(min(pepsi))
print(max(fanta))
print(mean(pepsi))

# Zad 3
wzrost = read.csv('Wzrost.csv', header= FALSE, sep = ',')
wzrost
print(min(wzrost))
print(max(wzrost))
print(mean(wzrost))

