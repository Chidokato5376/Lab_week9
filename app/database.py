import os
from sqlmodel import create_engine, Session
from fastapi import Depends
from typing import Annotated

# 1. Đọc DATABASE_URL từ môi trường, fallback về SQLite nếu không thấy
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./app.db")

# 2. Tạo engine với echo=True để in ra các câu lệnh SQL
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

# 3. Viết yield-dependency get_session và type alias SessionDep
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]