// A3Sol2.js
// 1. Count total number of subjects
print(">Q1) db.Subject.aggregate([{ $count: \"totalSubjects\" }])");
db.Subject.aggregate([
  { $count: "totalSubjects" }
]).forEach(doc => printjson(doc));

// 2. Count subjects with no prerequisites
print("\n>Q2) db.Subject.aggregate([ { $match: { \"subject.prerequisite\": { $exists: false } } }, { $count: \"noPrereqSubjects\" } ])");
db.Subject.aggregate([
  { $match: { "subject.prerequisite": { $exists: false } } },
  { $count: "noPrereqSubjects" }
]).forEach(doc => printjson(doc));

// 3. Count subjects worth more than 3 credit points
print("\n>Q3) db.Subject.aggregate([ { $match: { \"subject.credit\": { $gt: 3 } } }, { $count: \"moreThan3Credits\" } ])");
db.Subject.aggregate([
  { $match: { "subject.credit": { $gt: 3 } } },
  { $count: "moreThan3Credits" }
]).forEach(doc => printjson(doc));

// 4. Find subject title, type & credit of the subject with the highest credit
print("\n>Q4) db.Subject.aggregate([ { $sort: { \"subject.credit\": -1 } }, { $limit: 1 }, { $project: { _id:0, title:\"$subject.subTitle\", type:\"$subject.type\", credit:\"$subject.credit\" } } ])");
db.Subject.aggregate([
  { $sort: { "subject.credit": -1 } },
  { $limit: 1 },
  { $project: { _id: 0, title: "$subject.subTitle", type: "$subject.type", credit: "$subject.credit" } }
]).forEach(doc => printjson(doc));

// 5. List subject title, type, credit where credit = 3, sorted by title ascending
print("\n>Q5) db.Subject.aggregate([ { $match: { \"subject.credit\": 3 } }, { $project: { _id:0, title:\"$subject.subTitle\", type:\"$subject.type\", credit:\"$subject.credit\" } }, { $sort: { title:1 } } ])");
db.Subject.aggregate([
  { $match: { "subject.credit": 3 } },
  { $project: { _id: 0, title: "$subject.subTitle", type: "$subject.type", credit: "$subject.credit" } },
  { $sort: { title: 1 } }
]).forEach(doc => printjson(doc));

// 6. For each subject type, count total number of subjects
print("\n>Q6) db.Subject.aggregate([ { $group: { _id:\"$subject.type\", count:{ $sum:1 } } }, { $project:{ _id:0, type:\"$_id\", count:1 } } ])");
db.Subject.aggregate([
  { $group: { _id: "$subject.type", count: { $sum: 1 } } },
  { $project: { _id: 0, type: "$_id", count: 1 } }
]).forEach(doc => printjson(doc));

// 7. Find ISBN and title of books published in 2012
print("\n>Q7) db.Subject.aggregate([ { $unwind:\"$subject.book\" }, { $match:{ \"subject.book.yearPub\":2012 } }, { $project:{ _id:0, ISBN:\"$subject.book.ISBN\", title:\"$subject.book.bookTitle\" } } ])");
db.Subject.aggregate([
  { $unwind: "$subject.book" },
  { $match: { "subject.book.yearPub": 2012 } },
  { $project: { _id: 0, ISBN: "$subject.book.ISBN", title: "$subject.book.bookTitle" } }
]).forEach(doc => printjson(doc));

// 8. Find title, author & type of books used in CSCI235
print("\n>Q8) db.Subject.aggregate([ { $match:{ \"subject.subCode\":\"CSCI235\" } }, { $unwind:\"$subject.book\" }, { $project:{ _id:0, title:\"$subject.book.bookTitle\", author:\"$subject.book.author\", type:\"$subject.book.bookType\" } } ])");
db.Subject.aggregate([
  { $match: { "subject.subCode": "CSCI235" } },
  { $unwind: "$subject.book" },
  { $project: { _id: 0, title: "$subject.book.bookTitle", author: "$subject.book.author", type: "$subject.book.bookType" } }
]).forEach(doc => printjson(doc));

// 9. Find ISBN, title, and publisher of books with 2 to 3 authors
print("\n>Q9) db.Subject.aggregate([ { $unwind:\"$subject.book\" }, { $addFields:{ authorCount:{ $size:\"$subject.book.author\" } } }, { $match:{ authorCount:{ $gte:2,$lte:3 } } }, { $project:{ _id:0, ISBN:\"$subject.book.ISBN\", title:\"$subject.book.bookTitle\", publisher:\"$subject.book.publisher\" } } ])");
db.Subject.aggregate([
  { $unwind: "$subject.book" },
  { $addFields: { authorCount: { $size: "$subject.book.author" } } },
  { $match: { authorCount: { $gte: 2, $lte: 3 } } },
  { $project: { _id: 0, ISBN: "$subject.book.ISBN", title: "$subject.book.bookTitle", publisher: "$subject.book.publisher" } }
]).forEach(doc => printjson(doc));

// 10. List subject code, title of book & publisher, sorted by subject code ASC, publisher DESC
print("\n>Q10) db.Subject.aggregate([ { $unwind:\"$subject.book\" }, { $project:{ _id:0, subCode:\"$subject.subCode\", bookTitle:\"$subject.book.bookTitle\", publisher:\"$subject.book.publisher\" } }, { $sort:{ subCode:1, publisher:-1 } } ])");
db.Subject.aggregate([
  { $unwind: "$subject.book" },
  { $project: { _id: 0, subCode: "$subject.subCode", bookTitle: "$subject.book.bookTitle", publisher: "$subject.book.publisher" } },
  { $sort: { subCode: 1, publisher: -1 } }
]).forEach(doc => printjson(doc));
