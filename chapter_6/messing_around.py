glossary_dict = {
    'dns' : 'domain name service',
    'ospf' : 'open shortest path first',
    'vlan' : 'virtual local area network',
    'eigrp' : 'enhanced interior gateway routing protocol',
    'mpls' : 'multi protocol label service',
};

def glossary(dict):
    # print(f"{dict.items()}");
    for key in dict.keys():
        print(key.upper());
    for key, value in dict.items():
        print(f"Key: {key}");
        print(f"Value: {value}");
    

glossary(glossary_dict);