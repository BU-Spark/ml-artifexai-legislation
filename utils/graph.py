class Node:
    def __init__(self, id, url):
        self.id = id
        self.url = url


class BillNode(Node):
    def __init__(self, id, bill_number, bill_url, bill_title, bill_text, bill_sponsor, bill_sponsor_url, bill_view_text_url, bill_download_pdf_url, bill_is_home_rule, bill_municipality, bill_num_cosponsors, bill_cosponsors, bill_history, bill_path, topic_id  ):
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
        self.topic_id = topic_id

class LegislatorNode(Node):
    def __init__(self, id, url, first, last, district, party, committee_ids):
        super().__init__(id, url)
        self.first = first
        self.last = last
        self.district = district
        self.party = party
        self.committee_ids = committee_ids

class TopicNode():
    def __init__(self, id, topic_id, topic_name):
        self.id = id
        self.topic_id = topic_id
        self.topic_name = topic_name


class CustomGraph:
    def __init__(self):
        self.bill_nodes = {}         # bill_id -> BillNode
        self.legislator_nodes = {}   # legislator_id -> LegislatorNode
        self.topic_nodes = {}        # topic_id -> TopicNode
        self.edges = []              # list of (src_id, dst_id, relation_type)

    def add_bill(self, bill: BillNode):
        self.bill_nodes[bill.id] = bill

    def add_legislator(self, legislator: LegislatorNode):
        self.legislator_nodes[legislator.id] = legislator

    def add_topic(self, topic: TopicNode):
        self.topic_nodes[topic.id] = topic

    def add_edge(self, src_id, dst_id, relation_type):
        self.edges.append((src_id, dst_id, relation_type))

    def get_bill(self, billID):
        return self.bill_nodes[billID]
    
    def get_legislator(self, legID):
        return self.legislator_nodes[legID]
    
    def get_topic(self, topicID):
        return self.topic_nodes[topicID]
        




    

