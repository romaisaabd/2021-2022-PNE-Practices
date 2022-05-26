import http.server
import socketserver
import termcolor
import pathlib
import urllib.parse as u
import jinja2 as j
from Seq1 import Seq
import http.client
import json

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
HTML_FOLDER = "./html/"
SERVER = 'rest.ensembl.org'
ARGUMENT = "?content-type=application/json"

genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"
              }


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

        param_json = 0
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                param_json = 1

        print("  Command: " + self.command)
        print("  Path: " + self.path)

        if self.path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/listSpecies":
            try:
                species_info_list = make_ensembl_request("info/species")["species"]
                list_spcs = []
                for i in species_info_list:
                    list_spcs.append(i["common_name"])

                total_species = len(list_spcs)
                limit_species = int(arguments["limit_species"][0])
                if 0 <= limit_species <= len(list_spcs):
                    species_list_result = list_spcs[0:limit_species]
                    if param_json == 0:
                        contents = read_html_file("listSpecies.html").render(
                            context={"species": species_list_result, "total_species": total_species,
                                     "limit_species": limit_species})
                    elif param_json == 1:
                        species_json = '{"Species": ' + json.dumps(species_list_result) + "}"
                        contents = species_json

                else:
                    contents = pathlib.Path("html/error.html").read_text()

            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()

         # elif path == "/listSpecies":
            # try:
                # limit_species = int(arguments["limit_species"][0])
                # print("limit species ", limit_species)
                # dictionary_info = make_ensembl_request("info/species")
                # print("dictionary_info",dictionary_info)
                # species_info_list = dictionary_info["species"]
                # print( "species_info_list......................................................",species_info_list)
                #  list_spcs = []
                # for i in species_info_list:
                #   list_spcs.append(i["common_name"])
                   #print("---------------------------------------------------------",list_spcs)
                #esto es porque se repiten las especies hay(36 especies son las que se repiten)
                # final_list_spcs = []
                # for i in list_spcs:
                #  if i not in final_list_spcs:
                #  final_list_spcs.append(i)
                # else:
                #  pass
                # num_species = len(final_list_spcs)
                # if limit_species <= num_species:
                #  species_html = "<br><br>"
                    # for n in final_list_spcs[0:limit_species]:
                #  species_html += "<ul>" + "<li>" + " " + n + "<br>" + "</li>" + "</ul>"
                #  contents = read_html_file("listSpecies.html").render(context={"species": species_html,"total_species": num_species,"limit_species":limit_species})
                #  else:
            #   contents = pathlib.Path("html/error.html").read_text()
            # except ValueError:
                # contents = pathlib.Path("html/error.html").read_text()


        elif path == "/karyotype":
            try:
                species = arguments["specie"][0].lower()
                if species.find(" ") != -1:
                    species = species.replace(" ", "_")
                species_info_list = make_ensembl_request("info/species")["species"]
                list_species = []
                for i in species_info_list:
                    list_species.append((i["name"]))
                    print(list_species)

                karyotype = make_ensembl_request("info/assembly/" + species)["karyotype"]
                if not len(karyotype) == 0:
                    if param_json == 0:
                        contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype})
                    elif param_json == 1:
                        karyotype_json = '{"karyotype": ' + json.dumps(karyotype) + "}"
                        contents = karyotype_json
                else:
                    contents = pathlib.Path("html/error.html").read_text()

            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/chromosomeLength":
            try:
                species = arguments["specie"][0]
                chromosome = arguments["chromo"][0]
                species = species.lower()
                if species.find(" ") != -1:
                    species = species.replace(" ", "_")
                try:
                    list_specie = make_ensembl_request("info/assembly/" + species)["top_level_region"]
                    length = ""
                    for i in list_specie:
                        if i["name"] == chromosome:
                            length = i["length"]
                        else:
                            print("ERROR MESSAGE!!!")
                    if param_json == 0:
                        contents = read_html_file("chromosomeLength.html").render(context={"length": length})
                    elif param_json == 1:
                        length_chromo_json = '{"length_chromosome": ' + json.dumps(length) + "}"
                        contents = length_chromo_json
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneSeq":
            try:
                gene_name = arguments["gene"][0].upper()
                # print(gene_name)
                # dic_gene_name = make_ensembl_request("lookup/symbol/homo_sapiens/" + gene_name)
                # print( "--------------------",dic_specie_gene)
                try:
                    gene_id = make_ensembl_request("lookup/symbol/homo_sapiens/" + gene_name)["id"]
                    # print("ID GENE",gene_id)
                    dic_sequence = make_ensembl_request("sequence/id/" + gene_id)
                    # print(dic_sequence)
                    sequence = dic_sequence["seq"]
                    # print(sequence)
                    if param_json == 0:
                        contents = read_html_file("seqgene.html").render(context={"gene": sequence})
                        # print("para json igual a 0", contents) # lo que hace es imprimirte el seqgene con la
                        # secuencia en concreto
                    elif param_json == 1:
                        sequence = list(sequence)
                        contents = '{"geneSeq": ' + json.dumps(sequence) + "}"
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneInfo":
            try:
                # dictionary_info = make_ensembl_request("info/species")
                gene_name = arguments["gene"][0].upper()
                dict_answer = make_ensembl_request("lookup/symbol/homo_sapiens/" + gene_name)
                try:
                    start_gene = int(dict_answer["start"])
                    end_gene = int(dict_answer["end"])
                    id_gene = dict_answer["id"]
                    genelength = end_gene - start_gene
                    print(genelength)

                    chromosome_name = dict_answer["seq_region_name"]

                    """gene_info = dict_answer["desc"].split(":")
                    #print(gene_info)
                    start_gene = int(gene_info[3])
                    #print(start_gene)
                    end_gene = int(gene_info[4])
                    #print(end_gene)
                    id_gene = int(gene_info[2])
                    #print(id_gene)
                    genelength = end_gene - start_gene
                    #print(genelength)
                    chromosome_name = gene_info[1]
                    #print(chromosome_name)"""

                    if param_json == 0:
                        contents = read_html_file("infogene.html").render(
                            context={"length": genelength, "start": start_gene, "end": end_gene, "id_gene": id_gene,
                                     "chromosome": chromosome_name})
                    elif param_json == 1:
                        dict_keys = ["length", "start", "end", "id_gene", "chromosome"]
                        info = [genelength, start_gene, end_gene, id_gene, chromosome_name]
                        contents = json.dumps(dict(zip(dict_keys, info)))

                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()

        elif path == "/geneCalc":
            try:
                gene = arguments["gene"][0]
                try:
                    id_gene = genes_dict[gene.upper()]
                    dict_gene = make_ensembl_request("sequence/id/" + id_gene)
                    sequence = dict_gene["seq"]
                    seq = Seq()
                    operation = seq.info_operation(sequence)

                    if param_json == 0:
                        contents = read_html_file("calcbases.html").render(
                            context={"gene": gene, "oper_bases": operation})
                    elif param_json == 1:
                        contents = json.dumps(operation)
                except KeyError:
                    contents = pathlib.Path("html/error.html").read_text()
            except KeyError:
                contents = pathlib.Path("html/error.html").read_text()
        elif path == "/geneList":
            try:
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]
                list_genes = make_ensembl_request("/phenotype/region/homo_sapiens/" + chromo + ":" + start + "-" + end)
                name_genes = []
                for l in list_genes:
                    try:
                        for n in l["phenotype_associations"]:
                            if "attributes" in n.keys():
                                if "associated_gene" in n["attributes"]:
                                    name_genes.append(n["attributes"]["associated_gene"])
                    except TypeError:
                        contents = pathlib.Path("html/error.html").read_text()

                if not len(list_genes) == 0:
                    try:
                        if len(name_genes) != 0:
                            if param_json == 0:
                                contents = read_html_file("gencromo.html").render(
                                    context={"chromo": chromo, "start": start, "end": end, "name_genes": name_genes})
                            elif param_json == 1:
                                contents = '{"genes": ' + json.dumps(name_genes) + "}"
                        else:
                            name_genes = []
                            contents = read_html_file("gencromo.html").render(
                                context={"chromo": chromo, "start": start, "end": end, "name_genes": name_genes})
                    except KeyError:
                        contents = pathlib.Path("html/error.html").read_text()
                    except TypeError:
                        contents = pathlib.Path("html/error.html").read_text()
                else:
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
