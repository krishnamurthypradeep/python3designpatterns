import json
from pathlib import Path
import xml.etree.ElementTree as ET

class JSONDataExtractor:
    def __init__(self,filepath: Path) -> None:
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)
    
    @property
    def parsed_data(self):
        return self.data        
    

class XMLDataExtractor:
    def __init__(self,filepath: Path) -> None:
        self.tree = ET.parse(filepath)
        
    
    @property
    def parsed_data(self):
        return self.tree

def extract_factory(filepath: Path):
    ext = filepath.name.split(".")[-1] 
    if ext == "json":
        return JSONDataExtractor(filepath)
    elif ext == "xml":
        return XMLDataExtractor(filepath)
    else:
        raise ValueError("cannot extract data")

def extract(case: str):
    dir_path = Path(__file__).parent
    if case == "json":
        path = dir_path/Path("products.json")
        factory = extract_factory(path)
        data = factory.parsed_data
        for product in data:
            print(f"- {product['name']}")
    elif case == "xml":
        path = dir_path/Path("products.xml")
        factory = extract_factory(path)
        data = factory.parsed_data
        search_xpath = ".//products"
        products = data.findall(search_xpath)
        for product in products:
            name = product.find("name").text
            print(f"Name {name}")

if __name__ == "__main__":
    extract(case="json")
    extract(case="xml")    

# if case == 'json':
#     path = dir_path/
#     data = JSONDataExtractor(path).parsed_data
            
                    
# Small To Medium
# Enterprise business
# Government Agencies

# Build a Library For easy Access to classes 
# for all the types of customers       
             
        