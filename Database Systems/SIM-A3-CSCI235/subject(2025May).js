db.Subject.insertOne(
{
"_id":ObjectId(),
"subject": {
		"subCode":"CSCI103",
		"subTitle":"Algorithm and Problem Solving",
		"credit":3,
		"type":"Core",
		"assessments": [
				{ "assessNum": 1,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Problem Solving and Invariant" },
				{ "assessNum": 2,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Assignment 1 - Sorting and Seaarching, Linked Lists, and Stack and Queues" },
				{ "assessNum": 3,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Assignment 2 - Recursion, Trees, and Algorithmic Strategies" },
				{ "assessNum": 4,
				  "weight":10,
				  "assessType":"Test/Quiz",
				  "description":"Closed-book Class Test" },
				{ "assessNum": 5,
				  "weight":60,
				  "assessType":"Examination",
				  "description": "Closed-book Final Examination" }
			],
		"book": [
				{ "ISBN":"13:978-0-13-231681-1",
				  "bookType":"textbook",
				  "bookTitle":"Introduction to the Design and Analysis of Algorithms",
				  "edition":3,
				  "yearPub":2012,
				  "publisher":"Pearson",
				  "author": [ "Anany Levitin" ] },
				{ "ISBN":"13:978-0-13-231681-1",
				  "bookType":"reference",
				  "edition":3,
				  "yearPub":2005,
				  "publisher":"Pearson",
				  "author": [ "B A Forouzan", "D S Malik", "M K Sen Thomson" ] }

			]
		}
}
)

db.Subject.insertOne(
{
"_id":ObjectId(),
"subject": {
		"subCode":"CSCI114",
		"subTitle":"Procedural Programming",
		"credit":3,
		"type":"Core",
		"assessments": [
				{ "assessNum": 1,
				  "weight":5,
				  "assessType":"Assignment",
				  "description":"Assignment 1 - Basic Concepts: Sequential Designs" },
				{ "assignNum": 2,
				  "weight":5,
				  "assessType":"Assignment",
				  "description":"Assignment 2 - Control structures: Selection Designs" },
				{ "assessNum": 3,
				  "weight":5,
				  "assessType":"Assignment",
				  "description":"Assignment 3 - Repetition Designs and Functions I" },
				{ "assessNum": 4,
				  "weight":15,
				  "assessType":"Test/Quiz",
				  "description":"Closed-book Class Test" },
				{ "assessNum": 5,
				  "weight": 10,
				  "assessType":"Test/Quiz",
				  "description":"Laboratory Test" },
				{ "assessNum": 6,
				  "weight": 10,
				  "assessType":"Test/Quiz",
				  "description": "Closed-book Class Test" },
				{ "assessNum": 7,
				  "weight":50,
				  "assessType":"Examination",
				  "description": "Closed-book Final Examination" }
			],
		"book": [
				{ "ISBN":"13:978-1-133-52635-3",
				  "bookType":"reference",
				  "bookTitle":"C++ Programming - Program design including data structure",
				  "edition":6,
				  "yearPub":2013,
				  "publisher":"CENGAGE Learning",
				  "author": [ "Malik D S" ] },
				{ "ISBN":"13:978-0-273-75983-6",
				  "bookType":"reference",
                    "bookTitle":"Starting Out With C++: From Control Structures through Objects",
				  "edition":7,
				  "yearPub":2012,
				  "publisher":"Addison-Wesley",
				  "author": [ "Tony Gaddis" ] },

			]
		}
}
)

db.Subject.insertOne(
{
"_id":ObjectId(),
"subject": {
		"subCode":"CSCI124",
		"subTitle":"Applied Programming",
		"credit":3,
		"type":"Core",
		"prerequisite": ["csci114"],
		"assessments": [
				{ "assessNum": 1,
				  "weight":12,
				  "assessType":"Assignment",
				  "description":"Assignment 1 - Application on binary file processing" },
				{ "assignNum": 2,
				  "weight":12,
				  "assessType":"Assignment",
				  "description":"Assignment 2 - Application on pointers" },
				{ "assessNum": 3,
				  "weight":12,
				  "assessType":"Assignment",
				  "description":"Assignment 3 - Application on classes and objects and dynamic data structures" },
				{ "assessNum": 4,
				  "weight":14,
				  "assessType":"Laboratory",
				  "description":"Laboraory/Implementation Tasks" },
				{ "assessNum": 5,
				  "weight": 50,
				  "assessType":"Examination",
				  "description":"Closed-book Final Examination" }
			],
		"book": [
				{ "ISBN":"10:1-4390-4023-0",
				  "bookType":"textbook",
				  "bookTitle":"Data Structures Using C++",
				  "edition":2,
				  "yearPub":2010,
				  "publisher":"CENGAGE Learning",
				  "author": [ "Malik D S" ] },
				{ "ISBN":"13:978-1-133-52635-3",
				  "bookType":"reference",
                    "bookTitle":"C++ Programming - Program design including data structure",
				  "edition":6,
				  "yearPub":2013,
				  "publisher":"CENGAGE Learning",
				  "author": [ "Malik D S" ] },
				{ "ISBN":"13:978-0-273-75983-6",
				  "bookType":"reference",
                    "bookTitle":"Starting Out With C++: From Control Structures through Objects",
				  "edition":7,
				  "yearPub":2012,
				  "publisher":"Addison-Wesley",
				  "author": [ "Tony Gaddis" ] }
			]
		}
}
)

db.Subject.insertOne(
{ 
	"_id":ObjectId(),
	"subject":{ 
		"subCode":"CSCI235",
		"subTitle":"Database Systems",
		"credit":3,
		"type":"Core",
		"prerequisite": ["csci124","csci103"],
		"assessments": [
				{ "assessNum": 1,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Assignment 1 - Normalization and Indexing" },
				{ "assignNum": 2,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Assignment 2 - PL/SQL programming and Concurrency Control" },
				{ "assessNum": 3,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Assignment 3 - JSON/BSON and MongoDB" },
				{ "assessNum": 4,
				  "weight":10,
				  "assessType":"Laboratory",
				  "description":"Laboraory/Implementation Tasks" },
				{ "assessNum": 5,
				  "weight": 60,
				  "assessType":"Examination",
				  "description":"Closed-book Final Examination" }
			],
		"book": [
				{ "ISBN":"13:978-0-136-08620-8",
				  "bookType":"textbook",
				  "bookTitle":"Fundamentals of Database Systems",
				  "edition":6,
				  "yearPub":2010,
				  "publisher":"Addison-Wesley",
				  "author": [ "Ramez Elmasri", "Shamkant B Navathe" ] },
				{ "ISBN":"0-07-246563-8",
				  "bookType":"reference",
                    "bookTitle":"Database Management Systems",
				  "edition":3,
				  "yearPub":2003,
				  "publisher":"McGraw-Hill",
				  "author": [ "Raghur Ramakrishnan", "Johannes Gehrke" ] } ]
  }
}
)

db.Subject.insertOne(
{ 
	"_id":ObjectId(),
	"subject":{ 
		"subCode":"CSCI203",
		"subTitle":"Algorithm and Data Structures",
		"credit":3,
		"type":"Core",
		"prerequisite": ["csci103"],
		"assessments": [
				{ "assessNum": 1,
				  "weight":10,
				  "assessType":"Assignment",
				  "description":"Assignment 1 - Mathematic Concepts and Algorithm Complexity" },
				{ "assignNum": 2,
				  "weight":15,
				  "assessType":"Assignment",
				  "description":"Assignment 2 - Linear and Non-linear Data Structure" },
				{ "assessNum": 3,
				  "weight":15,
				  "assessType":"Assignment",
				  "description":"Assignment 3 - Greedy Algorithm and Branch-and-Bound" },
				{ "assessNum": 4,
				  "weight": 60,
				  "assessType":"Examination",
				  "description":"Closed-book Final Examination" }
			],
		"book": [
				{ "ISBN":"13:978-0-13-231681-1",
				  "bookType":"textbook",
				  "bookTitle":"Introduction to the Design and Analysis of Algorithms",
				  "edition":3,
				  "yearPub":2012,
				  "publisher":"Pearson",
				  "author": [ "Levitin" ] },
				{ "ISBN":"978-0-262-53305-8",
				  "bookType":"reference",
                    "bookTitle":"Introduction to Algorithms",
				  "edition":3,
				  "yearPub":2013,
				  "publisher":"The MIT Press",
				  "author": [ "Thomas H Cormen", "Charles E Leiserson", "Ronald L Riverst", "Clifford Stein" ] } ]
  }
}
)

db.Subject.insertOne(
{ 
	"_id":ObjectId(),
	"subject":{ 
		"subCode":"IACT201",
		"subTitle":"Professional Practice and Ethics",
		"credit":3,
		"type":"Elective",
		"assessments": [
				{ "assessNum": 1,
				  "weight":35,
				  "assessType":"Assignment",
				  "description":"Assignment 1 - Ethical Dilemma Case Study" },
				{ "assignNum": 2,
				  "weight":25,
				  "assessType":"Presentation",
				  "description":"Presentation of Case Study" },
				{ "assessNum": 3,
				  "weight": 40,
				  "assessType":"Examination",
				  "description":"Closed-book Final Examination" }
			]
  }
}
)

db.Subject.insertOne(
{ 
	"_id":ObjectId(),
	"subject":{ 
		"subCode":"CSCI321",
		"subTitle":"Final Year Project",
		"credit":6,
		"type":"Core",
		"assessments": [
				{ "assessNum": 1,
				  "weight":30,
				  "assessType":"Presentation",
				  "description":"Prototype demonstration" },
				{ "assignNum": 2,
				  "weight":70,
				  "assessType":"Implementation and Presentation",
				  "description":"Final product Presentation and assessment of product implementation by panel of project supervisors" }
			]
  }
}
)
