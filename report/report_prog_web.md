---
# pandoc report_prog_web.md -o pdf/report_prog_web.pdf --from markdown --template eisvogel.tex --listings --pdf-engine=xelatex --toc --number-sections

papersize: a4
lang: en-US
# geometry:
#     - top=30mm
#     - left=20mm
#     - right=20mm
#     - heightrounded
mainfont: "Helvetica"
sansfont: "Helvetica"
monofont: "Helvetica"
documentclass: article
title: Web programming project report
# author: LAI Khang Duy - Lylia DJALI
author: \textbf{LAI Khang Duy} \newline
        \textbf{Zilu YANG} \newline
        \textbf{KLIMINA Mariia} \newline
        \textbf{Nadia KACEM CHAOUCHE} \newline
        \newline
        \newline
        \textit{Université de Paris} \newline 
        \textit{UFR des Sciences Fondamentales et Biomédicales}
footer-left: Université de Paris
date: 28-03-2022
titlepage: true
toc-own-page: true
# lof: true
titlepage-logo: assets/images/uparis.png
header-includes: 
      - |
        ``` {=latex}
        \let\originAlParaGraph\paragraph
        \renewcommand{\paragraph}[1]{\originAlParaGraph{#1} \hfill}
        ```
...


# Introduction 
As the final project for this course, we created a web application for visualizing existing datasets, exploratory data analysis and training of different models. It was done using the Streamlit framework. Streamlit is an open-source app framework for Machine Learning and Data Science teams and is a very powerful python library. 

In this report there are five parts: Introduction, Application Architecture, Implementation, Problems encountered, Demonstrations and Conclusion.

# Application Architecture
Overall, the web application is divided into five parts: Side Bar, Data Visualization, Data pre-processing, Models, and Evaluation. They are distinct from each other but at the same time interconnected. To give you a clearer picture of our applications, we will show you the architecture of the web application here: