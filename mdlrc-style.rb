all
# Extend line length
rule 'MD013', :line_length => 99999

# Use "1. 2. 3."-style numbered lists instead of "1. 1. 1."
rule 'MD029', :style => :ordered

# Allow in-line HTML
exclude_rule 'MD033'

exclude_rule 'MD034'

exclude_rule 'MD041'



# False positives, see: https://github.com/markdownlint/markdownlint/issues/374
exclude_rule 'MD005'

# False positives, see: https://github.com/markdownlint/markdownlint/issues/313
exclude_rule 'MD007'
