(C) Copyright Mikhail Soutchanski, 2016
This work is licensed under a Creative Commons Attribution, NonCommercial,
ShareAlike 3.0 Unported License. Please read details at 
	https://creativecommons.org/licenses/by-nc-sa/3.0/us/

This set of challenging planning problems in PDDL has been created to stimulate
research and progress in AI planning. Planning Domain Definition Language (PDDL) 
is a standard input computer language to encode planning domains and problems. 
All AI systems competing at the  International Planning Competitions read PDDL.
Each benchmark problem requires solving an organic synthesis problem similar to
the problems encountered by the undergraduate students at the Chemistry exams.

The file  domain.pddl  includes PDDL code of all reactions that are used to
solve the 20 benchmark problems. Each folder includes a planning problem in 
PDDL and the corresponding images of the molecules obtained after every step. 
The solutions have been verified using the software VAL responsible for plan 
validation. All information and the computer files here are provided without 
any guaranty, warranty, or representation as to quality or suitability for 
any particular purpose.  Use at your own risk.

If you would like to write a paper related to this research, please cite 
the following publications:
	Arman Masoumi, Megan Antoniazzi and Mikhail Soutchanski
	Modeling Organic Chemistry and Planning Organic Synthesis.
	Proceedings of the 1st Global Conference on Artificial Intelligence 
	(GCAI 2015): Tbilisi, Georgia, October 16-19, 2015. This paper was 
	published in the EasyChair Proceedings in Computing: 
	Volume 36, pages 176-195, 2015 (issn 2040-557X). 

	Rami Matloob and Mikhail Soutchanski
	Exploring Organic Synthesis With State-of-the-Art Planners. 
	Proceedings of Scheduling and Planning Applications woRKshop (SPARK), 
	pages 52-61, held on June 13, 2016 in conjunction with the 26th 
	Intern. Conference on Automated Planning and Scheduling, London, UK.

Both papers are available at
	http://www.cs.ryerson.ca/~mes/publications/

		Provenance.
This set of 20 planning problems has been translated to PDDL from the benchmark 
developed by Abraham Heifets. It is available at
	http://www.cs.toronto.edu/~aheifets/ChemicalPlanning/

All 19 benchmark problems are derived from the images of the publicly available 
solutions to the MIT 5.13 Organic Chemistry 2 exams. They are available at
http://ocw.mit.edu/courses/chemistry/5-13-organic-chemistry-ii-fall-2006/exams/
The copies of all questions are collected into the PDF file  allMITproblems.pdf

The enclosed document matches reactions developed by Heifets in SMARTS format  
with reactions developed at Ryerson in RXN. The names of RXN reactions 
can be different from the names of SMARTS reactions.

		Acknowledgements.
This benchmark has been developed by a group of undergraduate and graduate
students from the Computer Science Department at the Ryerson University,
Toronto, Ontario, Canada.  The significant contributions have been provided by 
the following students (in the chronological order, most recent are listed last):
	Arman Masoumi
	Megan Antoniazzi
	Vitaliy Batusov
	Alden Ozburn
	Nick Salerni
	Rami Matloob 
	Hadi Qovaizi

Dr. Anne Johnson from the Department of Chemistry and Biology at the Ryerson 
University provided consultations and verified the chemical correctness of 
the reactions. Several faculty members from the Department of Chemistry
and Biology at Ryerson provided stimulating discussions and comments at
the various stages of this project (in the chronological order):
	Dr. Andrew McWilliams
	Dr. Bryan Koivisto
	Dr. Sharonna Greenberg
	Dr. Anne Johnson
	Dr. Russell Viirre
