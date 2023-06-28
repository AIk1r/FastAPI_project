# Добавляем middleware для работы с базой данных
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "hello world"}

# Создаем книгу
@app.post('/book/', response_model=SchemaBook)
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

# Получаем список всех книг
@app.get('/book/')
async def book():
    book = db.session.query(ModelBook).all()
    return book

# Редактируем книгу
@app.patch("/book/{book_id}")
async def edit_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    book_query = db.query(ModelBook).filter(ModelBook.id == book_id).first()
    if not book_query:
        raise HTTPException(status_code=404, detail="Book not found")
    book_query.title = book.title
    book_query.rating = book.rating
    book_query.author_id = book.author_id
    db.commit()
    return book_query

# Удаляем книгу
@app.delete('/book/{book_id}')
def delete_post(book_id: int, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    book = book_query.first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No book with this id: {id} found')
    book_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Создаем автора
@app.post('/author/', response_model=SchemaAuthor)
async def author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author

# Получаем список всех авторов
@app.get('/author/')
async def author():
    author = db.session.query(ModelAuthor).all()
    return author

# Запускаем приложение
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
