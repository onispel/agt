import tabulate, json

def format_vaults_table(response: dict, exclude:list[str]|None=None, fmt:str = 'simple') -> str:
    """Format vaults in human readable table format"""
    if len(response) > 0:
        headers = list(response[0].keys())
        if exclude:
            for header in exclude:
                headers.remove(header)
    data = []
    for vault in response:
        row = []
        for header in headers:
            row.append(vault[header])
        data.append(row)
    if data:
        return tabulate.tabulate(data, headers=headers, tablefmt=fmt)
    else:
        return 'nothing found'
    
def format_vaults_json(response: dict, exclude:list[str]|None=None) -> str:
    """Format vaults in tabbed json format"""
    if exclude:
        for vault in response:
            for header in exclude:
                del vault[header]
    if response:
        return json.dumps(response, indent=4)
    else:
        return 'nothing found'