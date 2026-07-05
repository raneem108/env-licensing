from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    doc_type = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime)
    approved_at = Column(DateTime)
    size = Column(Integer)

    user = relationship("User", back_populates="documents")
    processes = relationship("Process", back_populates="document")