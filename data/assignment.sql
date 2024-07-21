-- -------------------------------------------------------------
-- TablePlus 6.1.2(568)
--
-- https://tableplus.com/
--
-- Database: assignment
-- Generation Time: 2024-07-21 20:44:38.5160
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."books";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS books_id_seq;

-- Table Definition
CREATE TABLE "public"."books" (
    "id" int8 NOT NULL DEFAULT nextval('books_id_seq'::regclass),
    "title" varchar(255) NOT NULL,
    "author" varchar(255) NOT NULL,
    "genre" varchar(255) NOT NULL,
    "year_published" int8 NOT NULL,
    "summary" text,
    PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "public"."reviews";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS reviews_id_seq;

-- Table Definition
CREATE TABLE "public"."reviews" (
    "id" int4 NOT NULL DEFAULT nextval('reviews_id_seq'::regclass),
    "book_id" int4 NOT NULL,
    "user_id" int4 NOT NULL,
    "review_text" text NOT NULL,
    "rating" int4 CHECK ((rating >= 1) AND (rating <= 5)),
    PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "public"."users";
-- This script only contains the table creation statements and does not fully represent the table in the database. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS users_id_seq;

-- Table Definition
CREATE TABLE "public"."users" (
    "id" int4 NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    "username" varchar(50) NOT NULL,
    "email" varchar(255) NOT NULL,
    "created_at" timestamp DEFAULT CURRENT_TIMESTAMP,
    "hashed_password" varchar NOT NULL,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."books" ("id", "title", "author", "genre", "year_published", "summary") VALUES
(1, 'Updated Book', 'F. Scott Fitzgerald', 'Fiction', 1925, 'A story about the Jazz Age in the United States.'),
(2, 'Updated Book', 'Harper Lee', 'Fiction', 1960, 'A novel about the serious issues of rape and racial inequality.'),
(3, '1984', 'George Orwell', 'Dystopian', 1949, 'A dystopian social science fiction novel and cautionary tale.'),
(4, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 'A romantic novel that charts the emotional development of the protagonist.'),
(5, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 'A story about teenage rebellion and angst.'),
(6, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 'A fantasy novel and children’s book by English author J.R.R. Tolkien.'),
(7, 'Moby-Dick', 'Herman Melville', 'Adventure', 1851, 'A novel about the voyage of the whaling ship Pequod.'),
(8, 'War and Peace', 'Leo Tolstoy', 'Historical', 1869, 'A novel that chronicles the history of the French invasion of Russia.'),
(9, 'The Odyssey', 'Homer', 'Epic', 1959, 'An ancient Greek epic poem attributed to Homer.'),
(10, 'Ulysses', 'James Joyce', 'Modernist', 1922, 'A modernist novel by Irish writer James Joyce.'),
(11, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932, 'A dystopian novel set in a futuristic World State.'),
(12, 'The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 1954, 'An epic high-fantasy novel written by English author J.R.R. Tolkien.'),
(13, 'Animal Farm', 'George Orwell', 'Political Satire', 1945, 'A satirical allegorical novella that reflects events leading up to the Russian Revolution.'),
(14, 'Jane Eyre', 'Charlotte Bronte', 'Romance', 1847, 'A novel that follows the experiences of its eponymous heroine.'),
(15, 'The Grapes of Wrath', 'John Steinbeck', 'Historical', 1939, 'A novel about the Great Depression.'),
(16, 'The Chronicles of Narnia', 'C.S. Lewis', 'Fantasy', 1950, 'A series of seven fantasy novels for children.'),
(17, 'The Hitchhikers Guide to the Galaxy', 'Douglas Adams', 'Science Fiction', 1979, 'A comic science fiction series created by Douglas Adams.'),
(18, 'Crime and Punishment', 'Fyodor Dostoevsky', 'Philosophical', 1866, 'A novel about the mental anguish and moral dilemmas of an impoverished ex-student.'),
(19, 'The Adventures of Huckleberry Finn', 'Mark Twain', 'Adventure', 1884, 'A novel about a young boy’s adventures.'),
(20, 'Wuthering Heights', 'Emily Bronte', 'Gothic', 1847, 'A novel about the intense, almost demonic love between Catherine Earnshaw and Heathcliff.'),
(49, 'New Book', 'Author', 'Fiction', 2022, 'Summary of the new book');

INSERT INTO "public"."reviews" ("id", "book_id", "user_id", "review_text", "rating") VALUES
(1, 1, 1, 'An amazing story with deep characters.', 5),
(2, 2, 2, 'A powerful narrative on social issues.', 5),
(3, 3, 3, 'A thought-provoking dystopian novel.', 4),
(4, 4, 4, 'A timeless romance.', 5),
(5, 5, 5, 'A captivating and emotional read.', 4),
(6, 6, 6, 'A fantastic adventure tale.', 5),
(7, 7, 7, 'A challenging but rewarding read.', 3),
(8, 8, 8, 'A monumental piece of literature.', 5),
(9, 9, 9, 'A fascinating journey through ancient Greece.', 4),
(10, 10, 10, 'A complex and intriguing novel.', 4),
(11, 11, 1, 'A must-read classic.', 5),
(12, 12, 2, 'Highly recommended.', 4),
(13, 13, 3, 'Very impactful.', 5),
(14, 14, 4, 'Beautifully written.', 5),
(15, 15, 5, 'Engaging and thought-provoking.', 4),
(16, 16, 6, 'A wonderful tale.', 5),
(17, 17, 7, 'Difficult but worth it.', 3),
(18, 18, 8, 'An epic story.', 5),
(19, 19, 9, 'Incredibly interesting.', 4),
(20, 20, 10, 'A dense but rewarding read.', 4),
(25, 1, 1, 'Great book!', 5);

INSERT INTO "public"."users" ("id", "username", "email", "created_at", "hashed_password") VALUES
(1, 'john_doe', 'john_doe@example.com', '2024-01-01 10:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(2, 'jane_smith', 'jane_smith@example.com', '2024-01-02 11:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(3, 'alice_jones', 'alice_jones@example.com', '2024-01-03 12:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(4, 'bob_brown', 'bob_brown@example.com', '2024-01-04 13:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(5, 'charlie_black', 'charlie_black@example.com', '2024-01-05 14:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(6, 'dave_white', 'dave_white@example.com', '2024-01-06 15:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(7, 'eve_green', 'eve_green@example.com', '2024-01-07 16:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(8, 'frank_gray', 'frank_gray@example.com', '2024-01-08 17:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(9, 'grace_blue', 'grace_blue@example.com', '2024-01-09 18:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(10, 'henry_yellow', 'henry_yellow@example.com', '2024-01-10 19:00:00', '$2b$12$eisn1cVLj02W4tqrkzG2cONIzaF2ejiT2vwxptMN7X3zUJSuVHomG'),
(12, 'debasmita', 'debasmita@example.com', '2024-07-19 20:51:13.852174', '$2b$12$mmfran0tKIppnrHWp4H8tehnZXnWNeAwlScbOO5uAmwedf1fQqCX6'),
(15, 'rahul', 'rahul@example.com', '2024-07-20 20:27:49.57727', '$2b$12$ndAyw2Skx5b5ZiYs2zZbkOgntNwF37neStLeKqWx9sIhouSVpkVQG'),
(21, 'newuser', 'newuser@example.com', '2024-07-20 23:07:44.342145', '$2b$12$czIWN5kwup7cB7nlCDC4geYBz2A5RbMATMUEIsiTnYBWUclLTtKe2');



-- Indices
CREATE UNIQUE INDEX "Books_pkey" ON public.books USING btree (id);
ALTER TABLE "public"."reviews" ADD FOREIGN KEY ("user_id") REFERENCES "public"."users"("id");
ALTER TABLE "public"."reviews" ADD FOREIGN KEY ("book_id") REFERENCES "public"."books"("id");


-- Indices
CREATE UNIQUE INDEX users_username_key ON public.users USING btree (username);
CREATE UNIQUE INDEX users_email_key ON public.users USING btree (email);
