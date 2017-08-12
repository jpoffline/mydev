import accounts as accounts
import summary as summary
import sys
import config_accountdata as config
import json

mappings = open(config.SCRATCH + config.CONFIG_loc + config.MAPPINGS_file).read()
mappings = json.loads(mappings)
fileName = config.SCRATCH + config.INPUTS_loc + '/data.csv'

accFile = accounts.AccountsFile(fileName, mappings)
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
        'summary-html': config.SCRATCH + config.HTMLOUT_loc + config.HTML_report_file

    }
}

summary = summary.SummariseByDescription(
    Printer(sys.stdout), accFile._accounts)
summary.create_summariesSave(output_meta['outlocs'])
summary.save_summaryOverview(
    filename=config.SCRATCH + config.OUTPUTS_loc + 'overview.csv')