from models.users import User 


class Repo:
    def create(db,user):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


    def login(db, email, password):
        return db.query(User).filter(User.email==email).filter()