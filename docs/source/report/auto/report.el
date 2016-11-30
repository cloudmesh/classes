(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("styles/osajnl" "9pt" "twocolumn" "twoside")))
   (TeX-run-style-hooks
    "latex2e"
    "styles/osajnl"
    "styles/osajnl10"
    "fancyvrb")
   (LaTeX-add-labels
    "sec:examples"
    "fig:false-color"
    "tab:shape-functions"
    "eq:refname1"
    "alg:euclid"
    "euclidendwhile"
    "alg:python")
   (LaTeX-add-bibliographies
    "references")))

