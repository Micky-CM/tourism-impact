def get_receipts_per_year(tourism_dict, start_year=2010, end_year=2020):
    receipts_dict = {}
    for item in tourism_dict:
        year = int(item['year'])
        if start_year <= year <= end_year:
            receipts = float(item['tourism_receipts']) if item['tourism_receipts'] else 0
            receipts_dict[year] = receipts

    sorted_years = sorted(receipts_dict.keys())
    labels = [str(year) for year in sorted_years]
    values = [receipts_dict[year] for year in sorted_years]
    return labels, values

def receipts_by_country(data, country):
    result = list(filter(lambda item: item['country'] == country, data))
    return result