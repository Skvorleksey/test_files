file = open('links.txt', 'r')
file = file.read()

ip_adresses = []
counts_of_ip = {}
top5 = []

spsk = (file.split("\t", -1))

for i in spsk[1:: 2]:
    ip_adresses.append(i)
    if i not in counts_of_ip:
        counts_of_ip[i] = 1
    if i in counts_of_ip:
        counts_of_ip[i] += 1

pares_list = list(counts_of_ip.items())
pares_list.sort(key=lambda a: a[1])
pares_list = pares_list[len(pares_list) - 5: len(pares_list)]
for i in pares_list:
    top5.append(i[0])

print(f"Наиболее часто встречаются эти IP-адреса: {top5}")
