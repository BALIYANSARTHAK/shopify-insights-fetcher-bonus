from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    url = Column(String(512), unique=True)
    about = Column(Text)

    products = relationship("Product", back_populates="brand")
    social_links = relationship("SocialLink", back_populates="brand")
    contact_infos = relationship("ContactInfo", back_populates="brand")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    brand_id = Column(Integer, ForeignKey("brands.id"))

    brand = relationship("Brand", back_populates="products")

class SocialLink(Base):
    __tablename__ = "social_links"
    id = Column(Integer, primary_key=True)
    platform = Column(String(100))
    url = Column(String(512))
    brand_id = Column(Integer, ForeignKey("brands.id"))

    brand = relationship("Brand", back_populates="social_links")

class ContactInfo(Base):
    __tablename__ = "contact_infos"
    id = Column(Integer, primary_key=True)
    type = Column(String(100))  # email or phone
    value = Column(String(255))
    brand_id = Column(Integer, ForeignKey("brands.id"))

    brand = relationship("Brand", back_populates="contact_infos")