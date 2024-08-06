from pyhtml2pdf import converter

converter.convert("C:\\Users\\felip\\Desktop\\Economia do Zero\\Relatório PDF\\Relatório.html",
                  "RelatórioPython.pdf",
                  print_options={"scale": 0.95}
                  )