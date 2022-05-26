import http.server
import socketserver
import termcolor
import pathlib
import urllib.parse as u
import jinja2 as j
from seq1 import Seq
import http.client
import json
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
HTML_FOLDER = "./html/"
SERVER = 'rest.ensembl.org'
ARGUMENT = "?content-type=application/json"
def make_ensembl_request(url):
    conn = http.client.HTTPConnection(SERVER)
    parameters = "?content-type=application/json"
    try:
        conn.request("GET", url + parameters)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the server")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    return data1

def read_html_file(filename):
    contents = pathlib.Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received! Request line:")
        termcolor.cprint("  " + self.requestline, 'green')
        url_path = u.urlparse(self.path)
        path = url_path.path
        arguments = u.parse_qs(url_path.query)
        print("  Command: " + self.command)
        print("  Path: " + self.path)

        if self.path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/favicon.ico":
            contents = read_html_file("index.html").read_text()

        elif path == "/listSpecies":
            try:
                limit_species = int(arguments["limit_species"][0])
                # print("limit species ", limit_species)
                dictionary_info = make_ensembl_request("info/species")
                # print("dictionary_info",dictionary_info)
                species_info_list = dictionary_info["species"]
                # print( "species_info_list......................................................",species_info_list)
                list_spcs = []
                for i in species_info_list:
                    list_spcs.append(i["common_name"])
                   #print("---------------------------------------------------------",list_spcs)
                #esto es porque se repiten las especies hay(36 especies son las que se repiten)
                final_list_spcs = []
                for i in list_spcs:
                    if i not in final_list_spcs:
                        final_list_spcs.append(i)
                    else:
                        pass
                num_species = len(final_list_spcs)
                if limit_species <= num_species:
                    species_html = "<br><br>"
                    for n in final_list_spcs[0:limit_species]:
                        species_html += "<ul>" + "<li>" + " " + n + "<br>" + "</li>" + "</ul>"
                    contents = read_html_file("listSpecies.html").render(context={"species": species_html,"total_species": num_species,"limit_species":limit_species})
                else:
                    contents = pathlib.Path("html/error.html").read_text()
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/karyotype":
            try:
                species = arguments["specie"][0]
                dict_info_karyotype = make_ensembl_request("info/species")
                #print(dict_info_karyotype)
                species_info_list = dict_info_karyotype["species"]
                #print("-------------------------------------------------------------",species_info_list)
                species_name = []
                for i in species_info_list:
                    species_name.append(i["common_name"])
                dic_specie = make_ensembl_request("info/assembly/" + species)
                karyotype = dic_specie["karyotype"]
                karyotype_html = "<br><br>"
                for n in karyotype:
                    karyotype_html += " " + n + "<br>"
                contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype_html})
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()


        elif path == "/chromosomeLength":
            try:
                species = arguments["specie"][0]
                chromosome = arguments["chromo"][0]
                dic_specie = make_ensembl_request("info/assembly/" + species)
                list_specie = dic_specie["top_level_region"]
                length = ""
                for i in list_specie:
                    if i["name"] == chromosome:
                        length = i["length"]
                contents = read_html_file("chromosomeLength.html").render(context={"length": length})
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneSeq":
            try:
                gene = arguments["gene"][0]
                dic_specie_gene = make_ensembl_request("lookup/symbol/homo_sapiens/"+gene)
                try:
                    id_gene = dic_specie_gene["id"]
                    dic_gene = make_ensembl_request("sequence/id/" + id_gene)
                    sequence_gene = dic_gene["seq"]

                    if l_json == 0:
                        correct_sequence_gene = ""
                        n = 0
                        for i in sequence_gene:
                            correct_sequence_gene += i
                            n += 1
                            if n == 100:
                                correct_sequence_gene += "<br>"
                                n = 0
                        contents = read_html_file("gene.html").render(context={"gene": correct_sequence_gene})
                    elif l_json == 1:
                        sequence_gene = list(sequence_gene)
                        contents = json.dumps(sequence_gene)
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()



        else:
            contents = pathlib.Path("html/error.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()