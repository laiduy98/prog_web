---
# pandoc report_prog_web.md -o pdf/report_prog_web.pdf --from markdown --template eisvogel.tex --listings --pdf-engine=xelatex --toc --number-sections

papersize: a4
lang: fr-FR
# geometry:
#     - top=30mm
#     - left=20mm
#     - right=20mm
#     - heightrounded
# mainfont: "NewComputerModern"
# sansfont: "NewComputerModern"
# monofont: "JetBrains Mono"
documentclass: article
title: Rapport projet du module Programmation web
# author: LAI Khang Duy - Lylia DJALI
author: \textbf{LAI Khang Duy} \newline
        \textbf{Lylia DJALI} \newline
        \newline
        \newline
        \textit{Université de Paris} \newline 
        \textit{UFR des Sciences Fondamentales et Biomédicales}
footer-left: Université de Paris
date: 29-01-2022
titlepage: true
toc-own-page: true
lof: true
titlepage-logo: assets/images/uparis.png
header-includes: 
      - |
        ``` {=latex}
        \let\originAlParaGraph\paragraph
        \renewcommand{\paragraph}[1]{\originAlParaGraph{#1} \hfill}
        ```
...


# Overview