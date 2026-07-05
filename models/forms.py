from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Form(Base):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    status = Column(String, default="pending")
    user_id = Column(Integer, ForeignKey('users.id'))
    submitted_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship("User", back_populates="forms")

