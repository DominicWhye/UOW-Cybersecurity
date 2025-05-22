db.studentSeminar.insert(
{"seminar": { "seminarID": "sem001",
              "seminarDescription": "Security in Databases.",
              "seminarDate": "25-April-2025",
              "prerequisite": "Year 3 standing",
              "creditPoint": 3,
              "seminarEnrolment": [ 
                      {"studentID": "std001",
                       "enrolmentDate": "14-April-2025"},
                      {"studentID": "std009",
                       "enrolmentDate": "18-April-2025"} ] },
 "student": [ { "studentID": "std001",
                 "studentName": "Richard Davis",
                 "address": "Block 140, Bukit Batok",
                 "telephone": [ 
                      {"handphone": "92378888",
                       "officephone": "64283333" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem001",
                       "markReceived": 78 } ] },
               { "studentID": "std009",
                 "studentName": "Sharon Smith",
                 "address": "10 Bukit Timah Road",
                 "telephone": [ 
                      {"handphone": "81881234",
                       "residentphone": "64123456" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem001",
                       "markReceived": 80 } ] } ]
} );

db.studentSeminar.insert(
{"seminar": { "seminarID": "sem002",
              "seminarDescription": "Concurrency in Distributed Database.",

              "seminarDate": "5-May-2025",
              "creditPoint": 2,
              "seminarEnrolment": [ 
                      {"studentID": "std006",
                       "enrolmentDate": "30-April-2025"},
                      {"studentID": "std009",
                       "enrolmentDate": "18-April-2025"} ] },
 "student": [ { "studentID": "std006",
                 "studentName": "Ofelia Ashley",
                 "address": "123, Bukit Timah",
                 "telephone": [ 
                      {"handphone": "93858134",
                       "residentphone": "64352893" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem002",
                       "markReceived": 79 } ] },
               { "studentID": "std009",
                 "studentName": "Sharon Smith",
                 "address": "10 Bukit Timah Road",
                 "telephone": [ 
                      {"handphone": "81881234",
                       "residentphone": "64123456" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem002",
                       "markReceived": 82 } ] } ]
} );

db.studentSeminar.insert(
{"seminar": { "seminarID": "sem003",
              "seminarDescription": "Unstructured Database.",
              "seminarDate": "12-May-2025",
              "prerequisite": "Year 2 standing",
              "creditPoint": 3,
              "seminarEnrolment": [ 
                      {"studentID": "std010",
                       "enrolmentDate": "10-April-2025"},
                      {"studentID": "std005",
                       "enrolmentDate": "18-April-2025"} ] },
 "student": [ { "studentID": "std010",
                 "studentName": "Wendy Graham",
                 "address": "23, Lornie Hill",
                 "telephone": [ 
                      {"handphone": "93858134",
                       "residentphone": "64352893" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem003",
                       "markReceived": 74} ] },
               { "studentID": "std005",
                 "studentName": "Deann Larson",
                 "address": "17 Bukit Panjang",
                 "telephone": [ 
                      {"handphone": "91867237",
                       "residentphone": "62783256" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem003",
                       "markReceived": 62 } ] } ]
} );

db.studentSeminar.insert(
{"seminar": { "seminarID": "sem004",
              "seminarDescription": "In-memory Database.",
              "seminarDate": "2-May-2025",
              "creditPoint": 3,
              "seminarEnrolment": [ 
                      {"studentID": "std004",
                       "enrolmentDate": "20-April-2025"},
                      {"studentID": "std002",
                       "enrolmentDate": "10-April-2025"} ] },
 "student": [ { "studentID": "std004",
                 "studentName": "Klein Acevedo",
                 "address": "Block 23, Toa Payoh",
                 "telephone": [ 
                      {"handphone1": "93589248",
                       "handphone2": "82354723" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem004",
                       "markReceived": 64} ] },
               { "studentID": "std002",
                 "studentName": "Selma Hobbs",
                 "address": "87 Pearl Hill",
                 "telephone": [ 
                      {"handphone": "91647249",
                       "residentphone": "62691355" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem004",
                       "markReceived": 89 } ] } ]
} );

db.studentSeminar.insert(
{"seminar": { "seminarID": "sem005",
              "seminarDescription": "Network Security.",
              "seminarDate": "6-May-2025",
              "creditPoint": 0,
              "seminarEnrolment": [ 
                      {"studentID": "std004",
                       "enrolmentDate": "10-April-2025"},
                      {"studentID": "std005",
                       "enrolmentDate": "10-April-2025"},
                      {"studentID": "std003",
                       "enrolmentDate": "12-April-2025"}] },
 "student": [ { "studentID": "std004",
                 "studentName": "Janie Hinton",
                 "address": "Block 1824, Sembawang Loop",
                 "telephone": [ 
                      {"handphone1": "91793263",
                       "residentphone": "65478223" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem005",
                       "markReceived": 76} ] },
               { "studentID": "std003",
                 "studentName": "Marcy Collier",
                 "address": "Block 384, Jurong West",
                 "telephone": [ 
                      {"handphone1": "87396264",
                       "residentphone": "69398059" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem005",
                       "markReceived": 69} ] },
               { "studentID": "std005",
                 "studentName": "Deann Larson",
                 "address": "17 Bukit Panjang",
                 "telephone": [ 
                      {"handphone": "91867237",
                       "residentphone": "62783256" } ],
                 "enrolTo": [ 
                      {"seminarID": "sem005",
                       "markReceived": 92 } ] } ]
} );
