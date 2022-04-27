# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
from seq1 import Seq

genes_dict = {"SRCAP": "ENSG00000080603",
            "FRAT1": "ENSG00000165879",
            "ADA":"ENSG00000196839",
            "FXN":"ENSG00000165060",
            "RNU6_269P":"ENSG00000212379",
            "MIR633":"ENSG00000207552",
            "TTTY4C":"ENSG00000228296",
            "RBMY2YP":"ENSG00000227633",
            "FGFR3":"ENSG00000068078",
            "KDR":"ENSG00000128052",
            "ANK2":"ENSG00000145362"
}
gene_name = input("Write the gene name: ")
SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + genes_dict[gene_name] + PARAMS
print(f"\nServer: {SERVER}\n")
print(f"\nURL: {URL}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + genes_dict[gene_name] + PARAMS)  # -- WE DONT PUT THE SERVER HERE

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)

    print(f" Gene: {gene_name}\n", f"Description : {data1['desc']}")
    bases = Seq(data1['seq'])
    print("Total length: ",  bases.info_operation(bases))


except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
