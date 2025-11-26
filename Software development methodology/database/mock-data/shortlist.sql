CREATE TABLE shortlist (
    shortlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,  -- CSR user who shortlisted
    request_id INTEGER NOT NULL,  -- The PIN request they saved
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (request_id) REFERENCES request(request_id),
    UNIQUE(user_id, request_id)  -- Prevent duplicate shortlists
);

-- CSR user 3 shortlisted these open requests
insert into shortlist (shortlist_id, user_id, request_id) values (1, 3, 1);
insert into shortlist (shortlist_id, user_id, request_id) values (2, 3, 7);
insert into shortlist (shortlist_id, user_id, request_id) values (3, 3, 15);

-- CSR user 5 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (4, 5, 2);
insert into shortlist (shortlist_id, user_id, request_id) values (5, 5, 11);
insert into shortlist (shortlist_id, user_id, request_id) values (6, 5, 23);

-- CSR user 8 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (7, 8, 3);
insert into shortlist (shortlist_id, user_id, request_id) values (8, 8, 12);
insert into shortlist (shortlist_id, user_id, request_id) values (9, 8, 25);

-- CSR user 12 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (10, 12, 5);
insert into shortlist (shortlist_id, user_id, request_id) values (11, 12, 17);
insert into shortlist (shortlist_id, user_id, request_id) values (12, 12, 29);

-- CSR user 15 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (13, 15, 7);
insert into shortlist (shortlist_id, user_id, request_id) values (14, 15, 21);
insert into shortlist (shortlist_id, user_id, request_id) values (15, 15, 31);

-- CSR user 18 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (16, 18, 22);
insert into shortlist (shortlist_id, user_id, request_id) values (17, 18, 24);
insert into shortlist (shortlist_id, user_id, request_id) values (18, 18, 32);

-- CSR user 22 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (19, 22, 15);
insert into shortlist (shortlist_id, user_id, request_id) values (20, 22, 36);
insert into shortlist (shortlist_id, user_id, request_id) values (21, 22, 40);

-- CSR user 25 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (22, 25, 45);
insert into shortlist (shortlist_id, user_id, request_id) values (23, 25, 46);
insert into shortlist (shortlist_id, user_id, request_id) values (24, 25, 47);

-- CSR user 30 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (25, 30, 52);
insert into shortlist (shortlist_id, user_id, request_id) values (26, 30, 54);
insert into shortlist (shortlist_id, user_id, request_id) values (27, 30, 55);

-- CSR user 33 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (28, 33, 58);
insert into shortlist (shortlist_id, user_id, request_id) values (29, 33, 59);
insert into shortlist (shortlist_id, user_id, request_id) values (30, 33, 61);