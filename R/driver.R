cat("Checking code coverage\n")

#install.packages("devtools",repos='https://cran.ma.imperial.ac.uk/')
#install.packages("testthat",repos='https://cran.ma.imperial.ac.uk/')
#install.packages("covr",repos='https://cran.ma.imperial.ac.uk/')
#install.packages("DT",repos='https://cran.ma.imperial.ac.uk/')
#install.packages("shiny",repos='https://cran.ma.imperial.ac.uk/')

suppressWarnings(suppressMessages(library(devtools)))
suppressWarnings(suppressMessages(library(testthat)))

#test("examplepkg")

library(covr)
cov <- package_coverage("examplepkg")
print(cov)

report(cov, file = paste0("examplepkg", "-report.html"), browse = interactive())