import accounts as accounts
import summary as summary
import sys
import config_accountdata as config

fileName = config.SCRATCH + config.INPUTS_loc + '/data.csv'

accFile = accounts.AccountsFile(fileName)
accFile.stats()


class Printer(object):
    def __init__(self, where):
        self._where = where
        pass

    def write(self, msg):
        self._where.write(msg + '\n')


output_meta = {
    'outlocs': {
        'summary-debit': config.SCRATCH + config.OUTPUTS_loc + 'summary-debit.csv',
        'summary-credit': config.SCRATCH + config.OUTPUTS_loc + 'summary-credit.csv',
    }
}

summary = summary.SummariseByDescription(
    Printer(sys.stdout), accFile._accounts)
summary.create_summariesSave(output_meta['outlocs'])
summary.save_summaryOverview(
    filename=config.SCRATCH + config.OUTPUTS_loc + 'overview.csv')
