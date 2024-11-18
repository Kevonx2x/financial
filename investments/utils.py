def get_investment_type_name(type_id):
    investment_types = {
        '1': 'Stocks',
        '2': 'Precious Metals',
        '3': 'Bonds',
        '4': 'Real Estate'
    }
    return investment_types.get(type_id, '')
