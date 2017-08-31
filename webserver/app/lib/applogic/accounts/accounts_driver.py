import accounts as accounts
import summary as summary
import sys
import config_accountdata as config
import json
import html_landing as htmllanding

mappings = open(config.SCRATCH + config.CONFIG_loc +
                config.MAPPINGS_file).read()
mappings = json.loads(mappings)

acc_type = 'current'

months = ['may', 'june','july']

outhtml_fileName_suffix = acc_type + '-may-july'

input_AccountsFile_names = [
    config.SCRATCH + config.INPUTS_loc + '/' + acc_type + '-may' + '.csv',
    config.SCRATCH + config.INPUTS_loc + '/' + acc_type + '-june' + '.csv',
    config.SCRATCH + config.INPUTS_loc + '/' + acc_type + '-july' + '.csv']

link_pages = [
    {
        'title': 'Current',
        'short': '2017',
        'body': 'May -> July',
        'link': 'current-may-july.php'
    },
    {
        'title': 'Savings',
        'short': '2017',
        'body': 'May -> July',
        'link': 'savings-may-july.php'
    }
]


accFile = accounts.AccountsFile(input_AccountsFile_names, mappings, multi=True)
accFile.stats()


class Printer(object):
    def __init__(self, where):
        self._where = where
        pass

    def write(self, msg):
        self._where.write(msg + '\n')


output_meta = {
    'outlocs': {
        'summary-debit': config.SCRATCH + config.OUTPUTS_loc + 'debit-summary.csv',
        'summary-credit': config.SCRATCH + config.OUTPUTS_loc + 'credit-summary.csv',
        'summary-regular-debit': config.SCRATCH + config.OUTPUTS_loc + 'debit-summary-regular.csv',
        'summary-regular-credit': config.SCRATCH + config.OUTPUTS_loc + 'credit-summary-regular.csv',
        'summary-oneoff-debit': config.SCRATCH + config.OUTPUTS_loc + 'debit-summary-oneoff.csv',
        'summary-oneoff-credit': config.SCRATCH + config.OUTPUTS_loc + 'credit-summary-oneoff.csv',
        'summary-html': config.HTMLOUT_loc + outhtml_fileName_suffix + '.php',
        'link_pages': link_pages
    }
}

summary = summary.SummariseByDescription(
    Printer(sys.stdout), accFile._accounts,
    meta={
        'description': outhtml_fileName_suffix
    })

summary.create_summariesSave(output_meta['outlocs'])
summary.save_overview(
    filename=config.SCRATCH + config.OUTPUTS_loc + 'overview.csv')


htmllanding.htmllanding().to_file(config.HTMLOUT_loc + 'index2.html')
