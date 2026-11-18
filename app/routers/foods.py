from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/foods", tags=["foods"])


@router.get("/", response_model=list[schemas.FoodResponse])
def list_foods(db: Session = Depends(get_db)):
    return db.query(models.Food).all()


@router.get("/{food_id}", response_model=schemas.FoodResponse)
def get_food(food_id: int, db: Session = Depends(get_db)):
    food = db.get(models.Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food


@router.post("/", response_model=schemas.FoodResponse, status_code=201)
def create_food(data: schemas.FoodCreate, db: Session = Depends(get_db)):
    food = models.Food(**data.model_dump())
    db.add(food)
    db.commit()
    db.refresh(food)
    return food


@router.put("/{food_id}", response_model=schemas.FoodResponse)
def update_food(food_id: int, data: schemas.FoodCreate, db: Session = Depends(get_db)):
    food = db.get(models.Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    for key, value in data.model_dump().items():
        setattr(food, key, value)
    db.commit()
    db.refresh(food)
    return food


@router.delete("/{food_id}", status_code=204)
def delete_food(food_id: int, db: Session = Depends(get_db)):
    food = db.get(models.Food, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    db.delete(food)
    db.commit()