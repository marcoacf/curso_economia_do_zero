from pyhtml2pdf import converter

converter.convert('C:\\Users\\usuario\\Dropbox (Real Investor)\\Felipe\\Python\\Lâminas comparativas\\quantstats-tearsheet.html',
                  'sample.pdf',
                  print_options={"scale": 0.95}
                  )