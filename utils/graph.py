class Node:
    def __init__(self, id, url):
        self.id = id
        self.url = url


class BillNode(Node):
    def __init__(self, id, bill_number, bill_url, bill_title, bill_text, bill_sponsor, bill_sponsor_url, bill_view_text_url, bill_download_pdf_url, bill_is_home_rule, bill_municipality, bill_num_cosponsors, bill_cosponsors, bill_history, bill_path  ):
        super().__init__(id, bill_url)
        self.number = bill_number
        self.title = bill_title
        self.text = bill_text
        self.sponsor = bill_sponsor
        self.sponsor_url = bill_sponsor_url
        self.view_text_url = bill_view_text_url
        self.download_pdf_url = bill_download_pdf_url
        self.is_home_rule = bill_is_home_rule
        self.municipality = bill_municipality
        self.num_cosponsors = bill_num_cosponsors
        self.cosponsors = bill_cosponsors
        self.history = bill_history
        self.path = bill_path

class LegislatorNode(Node):
    def __init__(self, id, url, first, last, district, party, committee_ids):
        super().__init__(id, url)
        self.first = first
        self.last = last
        self.district = district
        self.party = party
        self.committee_ids = committee_ids

class CustomGraph:
    def __init__(self):
        self.bill_nodes = {}         # bill_id -> BillNode
        self.legislator_nodes = {}   # legislator_name -> LegislatorNode
        self.edges = []              # list of (src_id, dst_id, relation_type)

    def add_bill(self, bill: BillNode):
        self.bill_nodes[bill.id] = bill

    def add_legislator(self, legislator: LegislatorNode):
        self.legislator_nodes[legislator.id] = legislator

    def add_edge(self, src_id, dst_id, relation_type):
        self.edges.append((src_id, dst_id, relation_type))




    

