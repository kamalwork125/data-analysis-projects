-- TABLE 1: Members
CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    name TEXT,
    join_date TEXT
);

INSERT INTO members VALUES (1, 'Kamal', '2024-01-01');
INSERT INTO members VALUES (2, 'Simran', '2024-02-15');
INSERT INTO members VALUES (3, 'Aman', '2024-03-10');

-- TABLE 2: Books
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    category TEXT
);

INSERT INTO books VALUES (1, 'Python Basics', 'John Doe', 'Programming');
INSERT INTO books VALUES (2, 'DBMS Concepts', 'Navathe', 'Database');
INSERT INTO books VALUES (3, 'C++ Mastery', 'Bjarne Stroustrup', 'Programming');

-- TABLE 3: Issued Books
CREATE TABLE issued_books (
    issue_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    book_id INTEGER,
    issue_date TEXT,
    return_date TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO issued_books VALUES (1, 1, 2, '2024-07-10', '2024-07-20');
INSERT INTO issued_books VALUES (2, 2, 1, '2024-07-12', NULL);
INSERT INTO issued_books VALUES (3, 3, 3, '2024-07-15', NULL);
