// IT3Task2.js
// Make sure you run with: mongosh "mongodb://localhost:27017/myDB" --file IT3Task2.js

// 2(i): seminars with description "In-memory Database."
print(">2(i) db.studentSeminar.find({ \"seminar.seminarDescription\": \"In-memory Database.\" }).forEach(doc => printjson(doc))");
db.studentSeminar
  .find({ "seminar.seminarDescription": "In-memory Database." })
  .forEach(doc => printjson(doc));

// 2(ii): count of seminars student std009 has enrolled in
print("\n>2(ii) db.studentSeminar.countDocuments({ \"seminar.seminarEnrolment.studentID\": \"std009\" })");
let cnt = db.studentSeminar.countDocuments(
  { "seminar.seminarEnrolment.studentID": "std009" }
);
print(cnt);

// 2(iii): seminars where any student’s markReceived > 80
print("\n>2(iii) db.studentSeminar.find({ \"student.enrolTo.markReceived\": { $gt: 80 } }).forEach(doc => printjson(doc))");
db.studentSeminar
  .find({ "student.enrolTo.markReceived": { $gt: 80 } })
  .forEach(doc => printjson(doc));

// 2(iv): all 3-credit seminars attended by Sharon Smith
print("\n>2(iv) db.studentSeminar.find({ \"seminar.creditPoint\": 3, \"student.studentName\": \"Sharon Smith\" }).forEach(doc => printjson(doc))");
db.studentSeminar
  .find({
    "seminar.creditPoint": 3,
    "student.studentName": "Sharon Smith"
  })
  .forEach(doc => printjson(doc));

// 2(v): insert new seminar sem006
print("\n>2(v) db.studentSeminar.insertOne({ seminar: { seminarID: \"sem006\", seminarDescription: \"Attending Online Course\", seminarDate: \"12-May-2025\", creditPoint: 2 } })");
let resV = db.studentSeminar.insertOne({
  seminar: {
    seminarID: "sem006",
    seminarDescription: "Attending Online Course",
    seminarDate: "12-May-2025",
    creditPoint: 2
  }
});
printjson(resV);

// 2(vi): update sem006 date to 18-May-2025
print("\n>2(vi) db.studentSeminar.updateOne({ \"seminar.seminarID\": \"sem006\" }, { $set: { \"seminar.seminarDate\": \"18-May-2025\" } })");
let resVI = db.studentSeminar.updateOne(
  { "seminar.seminarID": "sem006" },
  { $set: { "seminar.seminarDate": "18-May-2025" } }
);
printjson(resVI);

// 2(vii): add new student enrolment under sem006
print("\n>2(vii) db.studentSeminar.updateOne({ \"seminar.seminarID\": \"sem006\" }, { $push: { student: { studentID: \"std006\", studentName: \"Ofelia Ashley\", address: \"123, Bukit Timah\", telephone: [{ handphone: \"93858134\", residentphone: \"64352893\" }], enrolTo: [{ seminarID: \"sem006\", markReceived: 0 }], enrolmentDate: \"12-May-2025\" } } })");
let resVII = db.studentSeminar.updateOne(
  { "seminar.seminarID": "sem006" },
  {
    $push: {
      student: {
        studentID: "std006",
        studentName: "Ofelia Ashley",
        address: "123, Bukit Timah",
        telephone: [
          { handphone: "93858134", residentphone: "64352893" }
        ],
        enrolTo: [
          { seminarID: "sem006", markReceived: 0 }
        ],
        enrolmentDate: "12-May-2025"
      }
    }
  }
);
printjson(resVII);

