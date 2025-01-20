import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./tourism_data.csv')

    country = input('Type Country: ')
    result = utils.receipts_by_country(data, country)

    if len(result) > 0:
        country_data = result
        labels, values = utils.get_receipts_per_year(country_data, start_year=2010, end_year=2020)
        charts.generate_bar_chart(country, labels, values)
        print(f'Charts generate for {country}.')
    else:
        print(f'No data found for country: {country}.')

if __name__ == '__main__':
    run()