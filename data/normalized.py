users = {
    1: {"name": "John Doe", "email": "johndoe@email.com", "phone": "555-1234"},
    2: {"name": "Jane Smith", "email": "janesmith@email.com", "phone": "555-5678"},
    3: {"name": "Bob Johnson", "email": "bobjohnson@email.com", "phone": "555-9876"},
    4: {"name": "Alice Brown", "email": "alicebrown@email.com", "phone": "555-4321"},
    5: {"name": "Charlie Davis", "email": "charlie@email.com", "phone": "555-8765"},
    6: {"name": "Eva Wilson", "email": "eva@email.com", "phone": "555-2468"},
    7: {"name": "Frank Miller", "email": "frank@email.com", "phone": "555-1357"},
    8: {"name": "Grace Lee", "email": "grace@email.com", "phone": "555-3690"},
    9: {"name": "Henry Taylor", "email": "henry@email.com", "phone": "555-1592"},
    10: {"name": "Ivy Chen", "email": "ivy@email.com", "phone": "555-7531"}
}

movies = {
    101: {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999},
    102: {"title": "Jurassic Park", "genre": "Adventure", "year": 1993},
    103: {"title": "Titanic", "genre": "Romance", "year": 1997},
    104: {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},
    105: {"title": "Forrest Gump", "genre": "Drama", "year": 1994},
    106: {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
    107: {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    108: {"title": "The Dark Knight", "genre": "Action", "year": 2008},
    109: {"title": "Avatar", "genre": "Sci-Fi", "year": 2009},
    110: {"title": "Goodfellas", "genre": "Crime", "year": 1990},
    111: {"title": "The Godfather", "genre": "Crime", "year": 1972},
    112: {"title": "Schindler's List", "genre": "Drama", "year": 1993},
    113: {"title": "The Lord of the Rings", "genre": "Fantasy", "year": 2001},
    114: {"title": "Fight Club", "genre": "Drama", "year": 1999},
    115: {"title": "Star Wars: A New Hope", "genre": "Sci-Fi", "year": 1977}
}

stores = {
    501: {"name": "Blockbuster Main St", "address": "123 Main St", "city": "Anytown", "state": "CA"},
    502: {"name": "Blockbuster Oak Ave", "address": "456 Oak Ave", "city": "Springfield", "state": "IL"},
    503: {"name": "Blockbuster Pine St", "address": "789 Pine St", "city": "Lakeside", "state": "NY"},
    504: {"name": "Blockbuster Elm St", "address": "321 Elm St", "city": "River City", "state": "TX"},
    505: {"name": "Blockbuster Maple Rd", "address": "654 Maple Rd", "city": "Hill Valley", "state": "CA"}
}

rentals = [
    {"rental_id": 1, "user_id": 1, "movie_id": 101, "store_id": 501, "rental_date": "2023-09-15", "return_date": "2023-09-18", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 2, "user_id": 1, "movie_id": 102, "store_id": 501, "rental_date": "2023-09-15", "return_date": "2023-09-18", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 3, "user_id": 2, "movie_id": 103, "store_id": 502, "rental_date": "2023-09-16", "return_date": "2023-09-20", "rental_fee": 3.99, "late_fee": 1.99},
    {"rental_id": 4, "user_id": 3, "movie_id": 101, "store_id": 503, "rental_date": "2023-09-17", "return_date": "2023-09-19", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 5, "user_id": 2, "movie_id": 104, "store_id": 502, "rental_date": "2023-09-18", "return_date": "2023-09-21", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 6, "user_id": 4, "movie_id": 105, "store_id": 501, "rental_date": "2023-09-19", "return_date": "2023-09-23", "rental_fee": 3.99, "late_fee": 1.99},
    {"rental_id": 7, "user_id": 3, "movie_id": 106, "store_id": 503, "rental_date": "2023-09-20", "return_date": "2023-09-22", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 8, "user_id": 4, "movie_id": 107, "store_id": 501, "rental_date": "2023-09-21", "return_date": "2023-09-24", "rental_fee": 4.99, "late_fee": 0.00},
    {"rental_id": 9, "user_id": 1, "movie_id": 108, "store_id": 501, "rental_date": "2023-09-22", "return_date": "2023-09-25", "rental_fee": 4.99, "late_fee": 0.00},
    {"rental_id": 10, "user_id": 2, "movie_id": 109, "store_id": 502, "rental_date": "2023-09-23", "return_date": "2023-09-27", "rental_fee": 4.99, "late_fee": 1.99},
    {"rental_id": 11, "user_id": 5, "movie_id": 110, "store_id": 504, "rental_date": "2023-09-24", "return_date": "2023-09-26", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 12, "user_id": 6, "movie_id": 111, "store_id": 505, "rental_date": "2023-09-25", "return_date": "2023-09-28", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 13, "user_id": 7, "movie_id": 112, "store_id": 503, "rental_date": "2023-09-26", "return_date": "2023-09-29", "rental_fee": 4.99, "late_fee": 0.00},
    {"rental_id": 14, "user_id": 8, "movie_id": 113, "store_id": 502, "rental_date": "2023-09-27", "return_date": "2023-09-30", "rental_fee": 4.99, "late_fee": 0.00},
    {"rental_id": 15, "user_id": 9, "movie_id": 114, "store_id": 501, "rental_date": "2023-09-28", "return_date": "2023-10-01", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 16, "user_id": 10, "movie_id": 115, "store_id": 505, "rental_date": "2023-09-29", "return_date": "2023-10-02", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 17, "user_id": 5, "movie_id": 101, "store_id": 504, "rental_date": "2023-09-30", "return_date": "2023-10-03", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 18, "user_id": 6, "movie_id": 103, "store_id": 503, "rental_date": "2023-10-01", "return_date": "2023-10-04", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 19, "user_id": 7, "movie_id": 105, "store_id": 502, "rental_date": "2023-10-02", "return_date": "2023-10-05", "rental_fee": 3.99, "late_fee": 0.00},
    {"rental_id": 20, "user_id": 8, "movie_id": 107, "store_id": 501, "rental_date": "2023-10-03", "return_date": "2023-10-06", "rental_fee": 4.99, "late_fee": 0.00}
]