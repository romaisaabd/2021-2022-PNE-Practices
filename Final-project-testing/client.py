import http.client
import socketserver

PORT = 8080
SERVER = '127.0.0.1'

conn = http.client.HTTPConnection(SERVER, PORT)
socketserver.TCPServer.allow_reuse_address = True

try:
    conn.request("GET", "/listSpecies?limit=5&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data_1 = r1.read().decode("utf-8")
print(data_1)
try:
    conn.request("GET", "/karyotype?specie=human&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r2 = conn.getresponse()
print(f"Response received!: {r2.status} {r2.reason}\n")
data_2 = r2.read().decode("utf-8")
print(data_2)
try:
    conn.request("GET", "/chromosomeLength?specie=mouse&chromo=1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r3 = conn.getresponse()
print(f"Response received!: {r3.status} {r3.reason}\n")
data_3 = r3.read().decode("utf-8")
print(data_3)
try:
    conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r4 = conn.getresponse()
print(f"Response received!: {r4.status} {r4.reason}\n")
data_4 = r4.read().decode("utf-8")
print(data_4)
try:
    conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r5 = conn.getresponse()
print(f"Response received!: {r5.status} {r5.reason}\n")
data_5 = r5.read().decode("utf-8")
print(data_5)
try:
    conn.request("GET", "/geneCalc?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r6 = conn.getresponse()
print(f"Response received!: {r6.status} {r6.reason}\n")
data_6 = r6.read().decode("utf-8")
print(data_6)
try:
    conn.request("GET", "/geneList?chromo=9&start=22125500&end=22136000&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
r7 = conn.getresponse()
print(f"Response received!: {r7.status} {r7.reason}\n")
data_7 = r7.read().decode("utf-8")
print(data_7)