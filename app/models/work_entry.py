from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.db import Base

class WorkEntry(Base):
    __tablename__ = "work_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.worker_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.item_id"), nullable=False)
    date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    worker = relationship("Worker")
    item = relationship("Item")


class Earning(Base):
    __tablename__ = "earnings"

    earning_id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.worker_id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    period = Column(String, nullable=False)
    entry_id = Column(Integer, ForeignKey("work_entries.entry_id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    worker = relationship("Worker")
    work_entry = relationship("WorkEntry")


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    entry_id = Column(Integer, ForeignKey("work_entries.entry_id"), nullable=False)
    admin_id = Column(Integer, ForeignKey("admins.admin_id"), nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
    work_entry = relationship("WorkEntry")
    admin = relationship("Admin")
