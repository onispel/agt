from typing import Iterable
import tabulate, json

def format_table(response: list[dict], exclude:list[str]|None=None, fmt:str = 'simple') -> str:
    """Format vaults in human readable table format"""
    if isinstance(response, dict):
        response = [response]
    if response:
        headers = list(response[0].keys())
        if exclude:
            for header in exclude:
                headers.remove(header)
    data = []
    for data_set in response:
        row = []
        for header in headers:
            row_item = (data_set.get(header, ''))
            if isinstance(row_item, Iterable):
                row_item = "..."
            row.append(row_item)
        data.append(row)
    if data:
        return tabulate.tabulate(data, headers=headers, tablefmt=fmt)
    else:
        return 'nothing found'
    
def format_list_item(response: dict, exclude:list[str]|None=None, fmt:str = 'simple') -> str:
    """Format vaults in list format"""
    if response:
        if exclude:
            for header in exclude:
                del response[header]

        data = []
        for key, value in response.items():
            data.append([key, value])
        return tabulate.tabulate(data, tablefmt=fmt)
    else:
        return 'nothing found'
    
def format_list(response: dict|Iterable[dict], exclude:list[str]|None=None, fmt:str = 'simple') -> str:
    """Format vaults in list format"""
    items = []
    if isinstance(response, dict) and len(response) > 0:
        items = [response]
    else:
        items = tuple(response)
    if items:
        out = ''
        for item in items:
            if out: out += '\n'
            out += format_list_item(item, exclude, fmt)
        return out
    else:
        return 'nothing found'    

def format_json(response: dict, exclude:list[str]|None=None) -> str:
    """Format vaults in tabbed json format"""
    if exclude:
        for vault in response:
            for header in exclude:
                del vault[header]
    if response:
        return json.dumps(response, indent=4)
    else:
        return 'nothing found'